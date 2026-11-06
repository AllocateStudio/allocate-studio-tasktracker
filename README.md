# Task Tracker · Allocate Studio

Open index.html in your browser. Keep the other files and assets in the same folder.

- Tasks: create, edit, delete, complete, search, and filter by status or priority.
- Calendar: browse months; select a day to add a task or a task to edit it.
- Settings: choose Sunday/Monday, add optional examples, export/import a JSON backup.

Data is stored locally in the browser, separately from Budget Planner and Bill Calendar. Back up before moving files or clearing browser data. There is no cross-device sync.

Design assets, fonts, palette, and month picker are copied from the existing Allocate Studio projects. The source projects were not modified.

Verification: JavaScript syntax and a mocked-DOM smoke test covering rendering, sample creation, persistence, completion, search, calendar, and editing. Visual/browser verification was blocked by the preview browser's file URL policy.

## Change log

This folder is a git repository. Run `git log` and `git diff HEAD~1` to see each change in detail.

### 2026-11-05: Style matched to Bill Calendar (edited in Claude Code)

- Month / Week switch on the Calendar view now uses Bill Calendar's segmented control: classes `mode-switch` and `mode-pill` (app.js, in `calendar()`), an ink outline with a shadow, and the active pill in pink `var(--blush)`. On phones (700px and narrower) it fills the full width. Styles are at the end of tracker.css. The old `.calendar-switch` rules in tracker.css are no longer used.
- Summary cards at the top (Total tasks, In progress, Completed, Overdue) now match Bill Calendar's size and type: label in DM Sans 14px, value in Plus Jakarta Sans 800 at `clamp(1.3rem,2.6vw,2rem)`, padding 18px 20px, radius 16px, gap 14px. On phones (650px and narrower): padding 14px, value 1.6rem. This replaced the "Compact summary cards" block in tracker.css.
- Week view on the Calendar is now a top-to-bottom list of seven day rows, like Bill Calendar, instead of seven columns. New function `weekList()` in app.js; `calendar()` calls it when `calendarMode==='Week'`. Each row (`.week-row`) shows the day name ("Thursday, Nov 5") with a ＋, then the tasks as full-width cards (`.week-task`: title, then project · priority · status), or "No tasks due". Today's row has a lime inner ring. Clicking a row adds a task on that day; clicking a task opens it for editing. Styles are at the end of tracker.css. The old `.week-grid` rules in tracker.css are no longer used.
- All changes were checked in a browser at desktop and phone widths.
