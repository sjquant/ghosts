# 168h Design

## Direction

A personal weekly planner for people who need to place tasks within a finite 168-hour week. The main screen keeps all seven 24-hour days visible alongside a computed allocation ledger and unscheduled tasks. Use warm paper and terracotta to make repeated planning comfortable, with the colored blocks and explicit totals needed to judge capacity. The generated preview establishes mood and composition; its depicted times are illustrative.

[Selected preview](assets/selected-direction-v2.png)

## Visual rules

| Area | Roles and values or source | Usage rules |
| --- | --- | --- |
| Typography | Georgia 32/1.1 for the `168h` wordmark and week heading; system sans 14/1.4 for controls and tasks; system sans 12/1.3 for time labels | Keep task labels readable within short blocks; truncate only when duration is under one hour. |
| Color | Background `#f6f2ec`; surface `#fffdf9`; text `#28221e`; muted `#766f67`; terracotta `#ba654b`; sleep `#777287`; work `#c77b63`; life `#91a98b`; focus `#a79aca`; free `#e8dfd3` | Use text labels with color; never rely on color alone for category meaning. |
| Spacing | 4px base, with 8, 12, 16, 24, and 32px steps | Calendar columns need tight spacing; cards and summary get larger padding. |
| Layout | Seven equal day columns, a 44px time ruler, and a 292px right rail at wide widths | Give the calendar the primary width. Keep the 168-hour ledger and backlog visible beside it. |
| Shape and elevation | 12px panels, 7px event blocks, subtle 1px borders, no heavy shadows | Borders distinguish dense schedule regions without adding visual weight. |

## Flow and components

The user scans the 168-hour ledger, finds free slots across seven days, then adds a scheduled task or places an unscheduled task. The ledger derives category totals and free hours from the schedule. Each day is exactly 24 hours; the week is exactly 168. A scheduled block cannot overlap another block or cross midnight. Native form controls and a native dialog handle task creation, editing, and completion. An invalid slot stays in the form with a clear error. A task may remain in the backlog until scheduled. Clicking a block or backlog row opens editing and deletion; changes persist locally per week. Completed tasks keep their allocated hours.

## Responsive behavior and accessibility

Responsive behavior: At widths below 1180px, the ledger and backlog move below the calendar. Below 760px, the seven-day calendar scrolls horizontally with day columns at least 154px wide; the time ruler remains at its start. The full 24-hour scale and all seven days remain available.

Accessibility: All actions are buttons or labeled native form controls. The dialog supports Escape and focus return. Blocks show category text as well as color. Focus rings remain visible. Motion is minimal and reduced-motion preference is respected.

## Open decisions

None for this evaluation build.
