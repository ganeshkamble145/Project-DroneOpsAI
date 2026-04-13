#!/usr/bin/env python3
"""
DroneOps AI - Production Intelligence System
Sample Database Utility & Analyzer
================================================
This script loads the DroneOps AI sample JSON database and provides:
  - Summary statistics of all 10 production events
  - Vendor scorecard analysis
  - KPI snapshot display
  - Filtered views by persona, severity, and status
  - Export of filtered records to CSV

Usage:
    python droneops_ai_analyzer.py
    python droneops_ai_analyzer.py --severity HIGH
    python droneops_ai_analyzer.py --persona "Operations Manager"
    python droneops_ai_analyzer.py --status PENDING
    python droneops_ai_analyzer.py --export filtered_events.csv --severity HIGH

Requirements: Python 3.8+  |  Standard library only (json, csv, argparse, os)
"""

import json
import csv
import argparse
import os
import sys
from datetime import datetime
from typing import List, Dict, Optional

# ─────────────────────────────────────────────────────────────────────────────
# Configuration
# ─────────────────────────────────────────────────────────────────────────────
DEFAULT_DB_PATH = "droneops_ai_database.json"

SEVERITY_ORDER = {"HIGH": 1, "MEDIUM": 2, "LOW": 3}
STATUS_COLORS = {
    "IN_PROGRESS": "\033[93m",  # Yellow
    "PENDING":     "\033[91m",  # Red
    "RESOLVED":    "\033[92m",  # Green
}
SEVERITY_COLORS = {
    "HIGH":   "\033[91m",
    "MEDIUM": "\033[93m",
    "LOW":    "\033[92m",
}
RESET = "\033[0m"
BOLD  = "\033[1m"
CYAN  = "\033[96m"
BLUE  = "\033[94m"


# ─────────────────────────────────────────────────────────────────────────────
# Helpers
# ─────────────────────────────────────────────────────────────────────────────
def color(text: str, code: str) -> str:
    """Wrap text with an ANSI color code (resets at end)."""
    return f"{code}{text}{RESET}"


def load_database(path: str) -> Dict:
    """Load and parse the JSON database file."""
    if not os.path.exists(path):
        print(f"\n[ERROR] Database file not found: {path}")
        print("Make sure 'droneops_ai_database.json' is in the same directory.")
        sys.exit(1)
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)["droneops_ai_database"]


def fmt_inr(amount: int) -> str:
    """Format a number as Indian Rupees (₹)."""
    if amount >= 100000:
        return f"₹{amount / 100000:.2f}L"
    if amount >= 1000:
        return f"₹{amount / 1000:.1f}K"
    return f"₹{amount}"


def fmt_ts(ts_str: str) -> str:
    """Pretty-print an ISO timestamp."""
    try:
        dt = datetime.fromisoformat(ts_str.replace("Z", "+00:00"))
        return dt.strftime("%d %b %Y  %H:%M UTC")
    except ValueError:
        return ts_str


def separator(char: str = "─", width: int = 72) -> str:
    return char * width


# ─────────────────────────────────────────────────────────────────────────────
# Display Functions
# ─────────────────────────────────────────────────────────────────────────────
def print_header(db: Dict) -> None:
    meta = db["metadata"]
    print("\n" + separator("═"))
    print(color(f"  {BOLD}DroneOps AI — Production Intelligence System", BOLD + CYAN))
    print(f"  {meta['description']}")
    print(f"  Plant: {meta['plant']}   |   DB Version: {meta['version']}   |   Generated: {meta['generated_date']}")
    print(separator("═"))


def print_kpi_snapshot(db: Dict) -> None:
    kpi = db["kpi_snapshot"]
    print(f"\n{color('  KPI SNAPSHOT', BOLD + BLUE)}")
    print(separator())
    metrics = [
        ("Overall Equipment Effectiveness (OEE)", f"{kpi['overall_equipment_effectiveness_pct']}%"),
        ("Throughput Rate",                        f"{kpi['throughput_rate_pct']}%"),
        ("Yield Rate",                             f"{kpi['yield_rate_pct']}%"),
        ("Defect Count Today",                     str(kpi['defect_count_today'])),
        ("Quality Score",                          str(kpi['quality_score'])),
        ("Unplanned Downtime This Week",           f"{kpi['unplanned_downtime_hrs_this_week']} hrs"),
        ("AI Auto-Rescheduled Batches",            f"{kpi['ai_auto_rescheduled_batches_pct']}%"),
        ("On-Time Delivery",                       f"{kpi['on_time_delivery_pct']}%"),
    ]
    for label, value in metrics:
        print(f"  {label:<42} {color(value, BOLD)}")
    print()


def print_vendor_scorecards(db: Dict) -> None:
    vendors = db["vendor_scorecards"]
    print(f"{color('  VENDOR SCORECARDS', BOLD + BLUE)}")
    print(separator())
    header = f"  {'Vendor':<28} {'Reliability':>11} {'Defect Rate':>12} {'Lead Time':>10} {'Status':>10}"
    print(color(header, BOLD))
    print(separator("─"))
    for v in vendors:
        status_col = STATUS_COLORS.get("IN_PROGRESS", "") if v["status"] not in STATUS_COLORS else STATUS_COLORS.get(v["status"], "")
        # Map vendor status to a simple display color
        if v["status"] == "CRITICAL":
            sc = SEVERITY_COLORS["HIGH"]
        elif v["status"] == "WARNING":
            sc = SEVERITY_COLORS["MEDIUM"]
        else:
            sc = SEVERITY_COLORS["LOW"]
        row = (
            f"  {v['name']:<28} "
            f"{v['reliability_pct']:>10}% "
            f"{v['defect_rate_pct']:>11}% "
            f"{v['lead_time_days']:>8} days "
            f"{color(v['status'], sc):>10}"
        )
        print(row)
    print()


def print_events(events: List[Dict], title: str = "PRODUCTION EVENTS") -> None:
    print(f"{color(f'  {title}', BOLD + BLUE)}  ({len(events)} record(s))")
    print(separator())
    for evt in events:
        alert = evt["alert"]
        impact = evt["kpi_impact"]
        sev_color = SEVERITY_COLORS.get(alert["severity"], "")
        sta_color = STATUS_COLORS.get(alert["status"], "")

        print(f"\n  {color(evt['id'], BOLD)}  |  {fmt_ts(evt['timestamp'])}")
        print(f"  Type       : {evt['type'].replace('_', ' ').title()}")
        print(f"  Persona    : {evt['persona']}")
        print(f"  Machine    : {evt['machine']['name']}  (Station: {evt['machine']['station']})")
        print(f"  Severity   : {color(alert['severity'], sev_color)}   |   Status: {color(alert['status'], sta_color)}")
        print(f"  Category   : {alert['category']}")
        print(f"  Description: {alert['description']}")
        print(f"  AI Rec.    : {alert['ai_recommendation']}")
        print(f"  Confidence : {alert['confidence_score'] * 100:.0f}%")
        print(f"  Action     : {alert['action_taken']}")
        print(f"  Est. Downtime : {impact['estimated_downtime_mins']} min   |   Cost Impact: {fmt_inr(impact['cost_impact_inr'])}")
        print(f"  Batches    : {', '.join(impact['affected_batches']) if impact['affected_batches'] else 'N/A'}")
        print(separator("·"))


def print_summary(events: List[Dict]) -> None:
    total = len(events)
    by_severity: Dict[str, int] = {}
    by_status: Dict[str, int] = {}
    by_persona: Dict[str, int] = {}
    by_type: Dict[str, int] = {}
    total_downtime = 0
    total_cost = 0
    auto_rescheduled = 0

    for evt in events:
        sev = evt["alert"]["severity"]
        sta = evt["alert"]["status"]
        persona = evt["persona"]
        etype = evt["type"].replace("_", " ").title()

        by_severity[sev] = by_severity.get(sev, 0) + 1
        by_status[sta] = by_status.get(sta, 0) + 1
        by_persona[persona] = by_persona.get(persona, 0) + 1
        by_type[etype] = by_type.get(etype, 0) + 1
        total_downtime += evt["kpi_impact"]["estimated_downtime_mins"]
        total_cost += evt["kpi_impact"]["cost_impact_inr"]
        if evt["alert"]["auto_rescheduled"]:
            auto_rescheduled += 1

    print(f"\n{color('  SUMMARY STATISTICS', BOLD + BLUE)}")
    print(separator())
    print(f"  Total Events        : {total}")
    print(f"  Total Est. Downtime : {total_downtime} minutes ({total_downtime / 60:.1f} hours)")
    print(f"  Total Cost Impact   : {fmt_inr(total_cost)}")
    print(f"  Auto-Rescheduled    : {auto_rescheduled} events ({auto_rescheduled / total * 100:.0f}%)")

    print(f"\n  By Severity:")
    for sev in ["HIGH", "MEDIUM", "LOW"]:
        count = by_severity.get(sev, 0)
        bar = "█" * count
        print(f"    {color(sev, SEVERITY_COLORS.get(sev,'')):<30} {bar} ({count})")

    print(f"\n  By Status:")
    for sta, count in sorted(by_status.items()):
        print(f"    {color(sta, STATUS_COLORS.get(sta,'')):<30} {count}")

    print(f"\n  By Persona:")
    for p, count in sorted(by_persona.items()):
        print(f"    {p:<40} {count}")

    print(f"\n  By Event Type:")
    for t, count in sorted(by_type.items()):
        print(f"    {t:<40} {count}")
    print()


# ─────────────────────────────────────────────────────────────────────────────
# Filter Function
# ─────────────────────────────────────────────────────────────────────────────
def filter_events(
    events: List[Dict],
    severity: Optional[str] = None,
    persona: Optional[str] = None,
    status: Optional[str] = None,
) -> List[Dict]:
    result = events
    if severity:
        result = [e for e in result if e["alert"]["severity"].upper() == severity.upper()]
    if persona:
        result = [e for e in result if persona.lower() in e["persona"].lower()]
    if status:
        result = [e for e in result if e["alert"]["status"].upper() == status.upper()]
    return sorted(result, key=lambda e: SEVERITY_ORDER.get(e["alert"]["severity"], 99))


# ─────────────────────────────────────────────────────────────────────────────
# CSV Export
# ─────────────────────────────────────────────────────────────────────────────
def export_to_csv(events: List[Dict], path: str) -> None:
    fieldnames = [
        "id", "timestamp", "type", "persona",
        "machine_id", "machine_name", "line", "station",
        "severity", "category", "description",
        "ai_recommendation", "confidence_score", "action_taken",
        "status", "auto_rescheduled",
        "estimated_downtime_mins", "cost_impact_inr", "affected_batches",
    ]
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for evt in events:
            alert = evt["alert"]
            impact = evt["kpi_impact"]
            writer.writerow({
                "id":                      evt["id"],
                "timestamp":               evt["timestamp"],
                "type":                    evt["type"],
                "persona":                 evt["persona"],
                "machine_id":              evt["machine"]["id"],
                "machine_name":            evt["machine"]["name"],
                "line":                    evt["machine"]["line"],
                "station":                 evt["machine"]["station"],
                "severity":                alert["severity"],
                "category":                alert["category"],
                "description":             alert["description"],
                "ai_recommendation":       alert["ai_recommendation"],
                "confidence_score":        alert["confidence_score"],
                "action_taken":            alert["action_taken"],
                "status":                  alert["status"],
                "auto_rescheduled":        alert["auto_rescheduled"],
                "estimated_downtime_mins": impact["estimated_downtime_mins"],
                "cost_impact_inr":         impact["cost_impact_inr"],
                "affected_batches":        "; ".join(impact["affected_batches"]),
            })
    print(color(f"\n  [✓] Exported {len(events)} record(s) to: {path}\n", "\033[92m"))


# ─────────────────────────────────────────────────────────────────────────────
# Main
# ─────────────────────────────────────────────────────────────────────────────
def main() -> None:
    parser = argparse.ArgumentParser(
        description="DroneOps AI — Database Analyzer",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python droneops_ai_analyzer.py
  python droneops_ai_analyzer.py --severity HIGH
  python droneops_ai_analyzer.py --persona "Supply Chain Manager"
  python droneops_ai_analyzer.py --status PENDING --export pending_events.csv
  python droneops_ai_analyzer.py --db /path/to/droneops_ai_database.json
        """,
    )
    parser.add_argument("--db",       default=DEFAULT_DB_PATH,
                        help="Path to JSON database file (default: droneops_ai_database.json)")
    parser.add_argument("--severity", choices=["HIGH", "MEDIUM", "LOW"],
                        help="Filter events by severity")
    parser.add_argument("--persona",  help="Filter events by persona substring (e.g. 'Operations')")
    parser.add_argument("--status",   choices=["IN_PROGRESS", "PENDING", "RESOLVED"],
                        help="Filter events by status")
    parser.add_argument("--export",   metavar="FILE.csv",
                        help="Export filtered results to a CSV file")
    parser.add_argument("--no-events", action="store_true",
                        help="Skip printing individual event details (show summary only)")
    args = parser.parse_args()

    # Load
    db = load_database(args.db)

    # Print header + KPIs + vendors (always)
    print_header(db)
    print_kpi_snapshot(db)
    print_vendor_scorecards(db)

    # Filter events
    all_events: List[Dict] = db["production_events"]
    filtered = filter_events(all_events, args.severity, args.persona, args.status)

    # Build filter label
    active_filters = []
    if args.severity: active_filters.append(f"severity={args.severity}")
    if args.persona:  active_filters.append(f"persona='{args.persona}'")
    if args.status:   active_filters.append(f"status={args.status}")
    filter_label = "  Filters: " + ", ".join(active_filters) if active_filters else "  No filters applied — showing all events"
    print(color(filter_label, CYAN))

    # Summary
    print_summary(filtered)

    # Events detail
    if not args.no_events:
        title = "FILTERED PRODUCTION EVENTS" if active_filters else "ALL PRODUCTION EVENTS"
        print_events(filtered, title)

    # Export
    if args.export:
        export_to_csv(filtered, args.export)

    if not filtered:
        print(color("  [!] No events match the specified filters.\n", SEVERITY_COLORS["MEDIUM"]))


if __name__ == "__main__":
    main()
