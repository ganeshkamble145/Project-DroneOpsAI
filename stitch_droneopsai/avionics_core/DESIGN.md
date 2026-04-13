# Design System Specification: Industrial Precision & Cognitive Flow

## 1. Overview & Creative North Star: "The Sentinel Aesthetic"
This design system moves beyond the standard SaaS "dashboard" look to embrace **The Sentinel Aesthetic**. In the context of Indian drone manufacturing—where hardware meets high-level AI—the UI must feel like a precision instrument: authoritative, calm, and hyper-legible.

We achieve a high-end editorial feel by rejecting "standard" containerization. Instead of trapping data in boxes with heavy borders, we use **Tonal Architecture**. The interface should feel like a sophisticated flight deck: layered surfaces, intentional asymmetry in data visualization, and a "breathable" hierarchy that mimics the openness of the sky while maintaining the grounded stability of an industrial facility.

---

## 2. Colors: Tonal Architecture
The palette transitions from the deep shadows of the `primary` navy to the expansive light of `surface`. We treat color as "environmental light" rather than just a fill.

### The "No-Line" Rule
**Borders are a failure of hierarchy.** Designers are strictly prohibited from using 1px solid lines to separate sections. Structure must be defined through:
- **Background Shifts:** Placing a `surface-container-lowest` card on a `surface-container-low` background.
- **Negative Space:** Using the spacing scale to create mental groupings.

### Surface Hierarchy & Nesting
Treat the UI as physical layers of frosted glass and machined aluminum. 
- **Layer 0 (Canvas):** `surface` (#f8f9fb) – The base ground.
- **Layer 1 (Main UI Blocks):** `surface-container-low` (#f3f4f6) – For large content areas.
- **Layer 2 (Interactive Cards):** `surface-container-lowest` (#ffffff) – To create a natural "pop" against the canvas.
- **Layer 3 (Modals/Overlays):** `surface-bright` with 80% opacity + 20px Backdrop Blur (Glassmorphism).

### Signature Textures
Main Action Buttons and Hero Metrics must use a **Cognitive Gradient**: A subtle linear transition from `primary` (#091426) to `primary_container` (#1e293b) at a 135-degree angle. This adds "soul" and depth to the AI-driven elements.

---

## 3. Typography: Editorial Authority
By pairing the technical precision of **Inter** with the architectural personality of **Space Grotesk**, we create an "Industrial-Editorial" rhythm.

- **Display (Space Grotesk):** Large-scale metrics and page titles. Use `display-md` (2.75rem) for hero drone health percentages.
- **Headlines (Space Grotesk):** Used for section headers. The wider aperture of Space Grotesk adds a modern, high-tech feel.
- **Body & Labels (Inter):** All functional data, navigation, and telemetry logs use Inter. 
  - **Body-sm (0.75rem):** Our workhorse for industrial data tables.
  - **Label-md (0.75rem):** High-contrast caps for drone status tags.

**Hierarchy Note:** Always pair a `display` metric with a `label-sm` in `on_surface_variant` (#45474c) to anchor the data.

---

## 4. Elevation & Depth: The Layering Principle
We do not "drop shadows" on everything. We "lift surfaces" using light.

- **Tonal Layering:** The primary method of elevation. A `surface-container-highest` element will naturally feel "closer" to the user than a `surface-container-low` element.
- **Ambient Shadows:** Only used for floating elements (e.g., flight path controls). Use the color `primary` at 6% opacity with a 32px blur and 8px Y-offset. This mimics a soft shadow cast by a hovering drone.
- **The Ghost Border Fallback:** If a border is required for high-density data accessibility, use `outline_variant` (#c5c6cd) at **15% opacity**. It should be felt, not seen.
- **Glassmorphism:** Use `surface_container_low` at 70% opacity with a `blur(12px)` for the sidebar and top navigation. This allows the movement of drone telemetry to "bleed" through the UI, maintaining a sense of constant motion.

---

## 5. Components: Machined Primitives

### Cards & Telemetry Blocks
*   **Style:** No borders. `8px` to `12px` (md) corner radius.
*   **Separation:** Forbid dividers. Use 24px of vertical white space to separate flight logs.
*   **Accent:** Use a 4px vertical strip of `tertiary_container` (#481b00) on the left edge to indicate an active AI-monitored card.

### Buttons (The "Actuator" Style)
*   **Primary:** Cognitive Gradient (Primary to Primary Container), white text, `8px` radius.
*   **Secondary:** `surface_container_high` background with `on_surface` text. No border.
*   **AI Action:** Use `tertiary_container` (#481b00) with `on_tertiary_container` (#eb6905) for all AI-triggered operations.

### Input Fields
*   **Default:** `surface_container_highest` background, no border.
*   **Focus:** A "Ghost Border" of `primary` at 40% opacity and a subtle `0.25rem` outer glow.

### Additional Industrial Components
*   **Status Orbs:** Pulsing `tertiary` (#280c00) or `on_tertiary_container` (#eb6905) dots to represent live AI processing.
*   **Metric Strips:** A horizontal bar for battery/signal levels using a background of `surface_container_high` and a fill of `on_tertiary_container`.

---

## 6. Do’s and Don'ts

### Do:
*   **Do** use asymmetrical layouts. A metric card on the left can be wider than the status list on the right to create an editorial feel.
*   **Do** use "White Space as a Divider." If it looks cluttered, add 8px more padding before considering a line.
*   **Do** use the `tertiary_fixed` (#ffdbca) color for "Warning" states—it feels more sophisticated than standard bright amber.

### Don’t:
*   **Don't** use 100% black. Use `primary` (#091426) for your darkest tones to maintain the "Navy/Steel" brand identity.
*   **Don't** use standard 1px borders on cards. This makes the UI look like a template.
*   **Don't** use heavy shadows. If the shadow is clearly visible, it's too dark. It should feel like "ambient occlusion," not a drop shadow.
*   **Don't** center-align data. Industrial UI is for scanning; keep telemetry left-aligned or tabular.