# Task Tracker · Allocate Studio

Open index.html in your browser. Keep the other files and assets in the same folder.

- Tasks: create, edit, delete, complete, search, and filter by status or priority. A Today card at the top lists what is due today and overdue.
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
- Today card on the Tasks view, between the summary cards and "Your tasks". It is the app's reminder: no browser notifications, by decision. New function `todayCard()` in app.js. It lists every unfinished task that is overdue (any month, oldest first) and then those due today (High priority first), with the count on the right and a summary line ("Thursday, Nov 5 · 1 due today · 1 overdue"). The checkbox completes a task and the task opens for editing on click. Overdue items are pink with red meta text. Empty state: "Nothing due today. Enjoy the calm." Styled like Bill Calendar's "Due in the next 7 days" card; styles at the end of tracker.css.
- All changes were checked in a browser at desktop and phone widths.

### 2026-11-05: Codex review of Claude changes

- Preserved the Today card, vertical Week view, pink Month/Week control, and revised card styling.
- Fixed the save indicator: a failed browser-storage write now remains visible after rendering or changing views; a successful retry clears it.
- Simplified the Today empty-state text, keeping decorative captions removed.
- Verified JavaScript syntax and mocked-DOM behavior for overdue tasks across months, Today priority ordering, completed/future task exclusion, completion, seven-day Week view, week navigation, task dialogs, storage failure, and recovery. No new visual browser verification was performed in this review.

### 2026-11-05: Month view on phones (edited in Claude Code)

- On screens 700px and narrower, the Month calendar shows each task as a short chip inside the day: title wrapped to two lines with an ellipsis, at most two chips per day, then "+N" (`.cal-more`). Chip colour shows status: blue to do, pink overdue (`.cal-task.late`), green and struck through when done (the ✓ is hidden on phones via `.cal-check`). Cells are taller (96px) with tighter padding so more text fits.
- Tapping a task chip opens it. Tapping elsewhere in a day selects that day (pink date, ink border) and shows all of its tasks below the calendar in a day panel (`dayPanel()` in app.js, `selectedDay` state, ＋ Add button). On load the selected day is today, or the 1st if another month is shown.
- Desktop Month view is unchanged: titles in cells, clicking a day adds a task. The phone check is `phone()` (matchMedia max-width 700px) in the click handler.
- Checked in a browser at phone and desktop widths.


### 2026-11-05: Smaller summary cards (edited in Claude Code)

- The summary cards felt too large at Bill Calendar's size, so they are now compact with the same fonts: label 13px, value 22px, padding 12px 16px (about 68px tall instead of 103px). On phones all four sit in one row: label 11px, value 20px, padding 8px 9px, about 60px tall. The rule is the last block in tracker.css and overrides the earlier "Summary cards, matching Bill Calendar" block.
