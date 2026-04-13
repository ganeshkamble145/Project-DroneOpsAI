# DroneOps AI — Production Intelligence System

> *Predict disruptions. Self-adjust operations. Keep humans in control.*

DroneOps AI is an agentic AI platform for **drone electronics manufacturing** that eliminates reactive firefighting by predicting machine failures, quality defects, inventory shortfalls, and vendor delays — and dynamically adjusting production decisions in real time.

---

## Table of Contents

- [Overview](#overview)
- [Key Features](#key-features)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [Using the Dashboard](#using-the-dashboard)
- [Python Analyzer CLI](#python-analyzer-cli)
- [AI Agents](#ai-agents)
- [Tech Stack](#tech-stack)
- [Success Metrics](#success-metrics)
- [Team](#team)

---

## Overview

| Attribute        | Detail                                              |
|------------------|-----------------------------------------------------|
| **Product Name** | DroneOps AI                                         |
| **Type**         | Agentic AI / Production Intelligence Platform       |
| **Industry**     | Drone Electronics Manufacturing                     |
| **Deployment**   | SaaS, Pilot-led, Subscription                       |
| **Primary Users**| Operations Manager · Supply Chain Manager · Line Supervisor |

DroneOps AI covers the full manufacturing lifecycle for three drone types — **MultiRotor**, **Fixed-Wing**, and **Single-Rotor** — across frame fabrication, main assembly, quality control, and packaging.

---

## Key Features

### 🔵 Operations Intelligence Dashboard
- Real-time assembly line status with efficiency metrics
- Predictive downtime event tracking with AI confidence scores
- AI-generated operations recommendations with **human-in-the-loop** Accept / Reject controls
- Context-aware alternative suggestions when a recommendation is rejected

### 🟣 Supply Chain Console
- Vendor scorecards with reliability, defect rate, and lead time tracking
- Critical stock-level alerts with emergency PO recommendations
- AI-driven vendor switching recommendations with alternative suggestions
- Component inventory forecast with days-in-stock visualisation

### 🟢 Line Supervisor App
- Live alert feed (Critical / Warning / Update) with approve/reject actions
- Shift task queue with drag-and-reassign AI suggestions
- Defect log with per-defect severity and rework authorisation controls
- KPI strip: Critical Alerts · Active Tasks · High-Severity Defects

---

## Project Structure

```
Project DroneOpsAI/
├── index.html                        # Single-file web application (dashboard UI + logic)
├── data.js                           # Production sample data (window.droneOpsDB)
├── droneops_ai_database.json         # Full structured JSON database (10 production events)
├── droneops_ai_analyzer.py           # Python CLI analyzer & CSV exporter
├── events_export.csv                 # Sample exported events (CSV)
├── DroneOps_AI_Solution_Documentation.md  # Full product documentation
├── DroneOps AI wireframes.pdf        # UI wireframes
└── DroneOpsAI PRD Final_ver1.0.pdf   # Product Requirements Document
```

---

## Getting Started

### Prerequisites
- A modern web browser (Chrome, Firefox, Edge)
- Python 3.8+ (for the CLI analyzer only)

### Running the Web Dashboard

1. Clone or download this repository.
2. Open `index.html` directly in your browser — **no build step or server required**.
3. `data.js` must be in the same directory as `index.html` (it is, by default).

```bash
# Quick launch (Windows)
start index.html

# Quick launch (macOS / Linux)
open index.html
```

> **Note:** If you open via `file://` and see a blank screen, use a local dev server (e.g. VS Code Live Server or `python -m http.server 8080`) to avoid CORS restrictions.

---

## Using the Dashboard

The application dashboard contains 8 comprehensive Agentic AI views:

### Operations Manager
1. **Ops Manager Dashboard:** Plant 1 status, Bottleneck Heatmap, AI Predictor, KPI summary
2. **Downtime Alert Detail:** Sensor telemetry, maintenance AI options & impact
3. **QC Vision Inspection:** Live feed simulation, defect report, confidence scores, defect trend

### Line Supervisor Mobile
4. **AI Chat Assistant:** Conversational AI alerts, worker fatigue, quick actions
5. **Shift Planner:** Shift roster, AI rotation suggestions, fatigue flags

### Supply Chain
6. **Vendor & Inventory Console:** Supplier KPI, inventory forecast, cost simulation, AI vendor recommendations
7. **Procurement Confirmation:** Generated PO approval and ERP integration toggle

### Analytics
8. **Team & Roles:** Live personnel roster

### Human-in-the-Loop Controls
Every AI recommendation in the dashboard includes an enforced review checkpoint:
- ✅ **Approve / Accept** — Approves the AI action; Agent receives execution clearance to push via integrating loops (e.g. ERP).
- ❌ **Reject / Override** — Dismisses the recommendation and forces the Agent to surface a context-aware **Alternative Strategy**.

---

## Python Analyzer CLI

`droneops_ai_analyzer.py` loads `droneops_ai_database.json` and provides summary statistics, vendor scorecards, KPI snapshots, filtered event views, and CSV export.

### Basic Usage

```bash
# Show all events with full summary
python droneops_ai_analyzer.py

# Filter by severity
python droneops_ai_analyzer.py --severity HIGH

# Filter by persona
python droneops_ai_analyzer.py --persona "Operations Manager"

# Filter by status
python droneops_ai_analyzer.py --status PENDING

# Export filtered results to CSV
python droneops_ai_analyzer.py --severity HIGH --export high_severity_events.csv

# Show summary only (skip individual event details)
python droneops_ai_analyzer.py --no-events

# Use a custom database path
python droneops_ai_analyzer.py --db /path/to/droneops_ai_database.json
```

### CLI Arguments

| Argument | Values | Description |
|----------|--------|-------------|
| `--severity` | `HIGH` `MEDIUM` `LOW` | Filter events by severity |
| `--persona` | substring string | Filter by persona (e.g. `"Supply Chain"`) |
| `--status` | `IN_PROGRESS` `PENDING` `RESOLVED` | Filter by event status |
| `--export` | `filename.csv` | Export filtered records to CSV |
| `--no-events` | flag | Show summary statistics only |
| `--db` | filepath | Custom JSON database path |

> **Requirements:** Python 3.8+ · Standard library only (`json`, `csv`, `argparse`, `os`)

---

## AI Agents

DroneOps AI uses a **Cross-Persona Multi-Agent Orchestration** framework:

| Agent | Role | Trigger |
|-------|------|---------|
| **Maintenance Agent** | Predictive analytics, equipment health monitoring | Sensor data crosses failure thresholds |
| **Quality Agent** | Computer vision defect detection, process compliance | Defect rate exceeds defined limits |
| **Vendor Risk Agent** | Real-time supplier monitoring | Vendor KPI degradation |
| **Inventory Optimization Agent** | Demand forecasting, auto-PO triggers | Stock falls below safety threshold |
| **Smart Task Allocation Agent** | Workforce distribution, shift optimization | Urgent orders or worker imbalance |

### AI Performance Targets

| Metric | Target |
|--------|--------|
| Prediction accuracy | ≥ 85% |
| False positive/negative rate | < 10% combined |
| Recommendation acceptance rate | ≥ 70% |
| Alert latency (event → alert) | ≤ 60 seconds |
| System uptime | ≥ 99.9% |

---

## Tech Stack

| Layer | Technologies |
|-------|-------------|
| **Dashboard** | HTML5, Vanilla CSS (glassmorphism dark theme), Vanilla JS |
| **Data Layer** | JSON (structured sample DB), JavaScript module |
| **CLI Utility** | Python 3.8+, standard library |
| **AI & Data** | Python, TensorFlow / PyTorch, OpenCV *(production)* |
| **Backend** | Node.js / Python APIs, Kafka / MQTT *(production)* |
| **Frontend** | React web dashboards *(production)* |
| **Infrastructure** | AWS / Azure, Docker, Kubernetes *(production)* |
| **Integration** | ERP/MES connectors — REST, OPC UA, MQTT *(production)* |

---

## Success Metrics

### Operational Targets (90-day pilot)

| Metric | Target |
|--------|--------|
| Unplanned downtime reduction | ≥ 30% |
| AI-driven auto-rescheduling | ≥ 40% of batches |
| Defect & rework reduction | ≥ 25% |
| On-time component availability | ≥ 20% improvement |

### Current Dashboard KPIs (Sample Data)

| KPI | Value |
|-----|-------|
| Overall Equipment Effectiveness | 82.4% |
| Throughput Rate | 94.7% |
| Yield Rate | 90.8% |

---

## Ethical AI Commitments

- **Human-in-the-loop:** All critical decisions require explicit human approval
- **Transparency:** Every AI insight includes a confidence score and rationale
- **Data Privacy:** Privacy-by-design; encrypted at rest and in transit; role-based access
- **Bias & Fairness:** Workforce scheduling models continuously monitored for bias
- **Safety Compliance:** Constrained by DGCA, ISO, and IPC standards

---

## Team

**DroneOps AI PRD v1.0 · January 2026**

| Name | Role |
|------|------|
| Ganesh Prabhakar Kamble | Product & AI Lead |
| Vardhan Patil | Engineering Lead |
| Alok Asthana | UX & Operations Lead |

---

*For full product documentation, see [`DroneOps_AI_Solution_Documentation.md`](./DroneOps_AI_Solution_Documentation.md).*  
*For UI wireframes, see [`DroneOps AI wireframes.pdf`](./DroneOps%20AI%20wireframes.pdf).*
