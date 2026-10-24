# 168h Design

## Direction

A personal weekly planner for people who need to place tasks within a finite 168-hour week. The desktop screen keeps all seven 24-hour days visible alongside a computed allocation ledger and unscheduled tasks. Mobile keeps a seven-day capacity overview visible while showing one selected day's timeline. Use warm paper and terracotta to make repeated planning comfortable, with colored blocks and explicit totals needed to judge capacity. The selected generated desktop preview establishes mood; its depicted times are illustrative. The mobile previews show the verified working flow.

[Selected preview](assets/selected-direction-v2.png)
[Mobile week](assets/mobile-week-verified.png) · [Task scheduling](assets/mobile-schedule-verified.png) · [Conflict recovery](assets/mobile-conflict-verified.png) · [Scheduled result](assets/mobile-recovered-verified.png)

## Visual rules

| Area | Roles and values or source | Usage rules |
| --- | --- | --- |
| Typography | Georgia 32/1.1 for the `168h` wordmark and week heading; system sans 14/1.4 for controls and tasks; system sans 12/1.3 for time labels | Keep task labels readable within short blocks; truncate only when duration is under one hour. |
| Color | Background `#f6f2ec`; surface `#fffdf9`; text `#28221e`; muted `#766f67`; terracotta `#ba654b`; sleep `#777287`; work `#c77b63`; life `#91a98b`; focus `#a79aca`; free `#e8dfd3` | Use text labels with color; never rely on color alone for category meaning. |
| Spacing | 4px base, with 8, 12, 16, 24, and 32px steps | Calendar columns need tight spacing; cards and summary get larger padding. |
| Layout | Seven equal day columns, a 44px time ruler, and a 292px right rail at wide widths | Give the calendar the primary width. Keep the 168-hour ledger and backlog visible beside it. |
| Shape and elevation | 12px panels, 7px event blocks, subtle 1px borders, no heavy shadows | Borders distinguish dense schedule regions without adding visual weight. |

## Flow and components

The user scans weekly capacity, selects a day, then taps a free slot or a backlog task. A bottom sheet on mobile offers computed open slots; a conflict names the overlapping block and offers alternatives plus a direct "Keep in backlog" action. The user can schedule the task or leave it in the backlog. The ledger derives category totals and free hours from the schedule. Each day is exactly 24 hours; the week is exactly 168. A scheduled block cannot overlap another block or cross midnight. Native form controls and a native dialog handle task creation, editing, and completion. Clicking a block or backlog row opens editing and deletion; changes persist locally per week. Completed tasks keep their allocated hours.

## Responsive behavior and accessibility

Responsive behavior: At widths below 1180px, the ledger and backlog move below the desktop calendar. At 800px and below, replace seven dense columns with a seven-day capacity strip and one selected day's task timeline; the compact 168-hour summary stays above them and the backlog follows below. Tapping a day changes the timeline without losing week context. The task dialog becomes a bottom sheet. All seven days remain directly selectable.

Accessibility: All actions are buttons or labeled native form controls. The dialog supports Escape and focus return. Blocks show category text as well as color. Focus rings remain visible. Motion is minimal and reduced-motion preference is respected.

## Open decisions

None for this evaluation build.
