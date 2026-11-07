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

### 2026-11-06: Sky "due today" pill (edited in Claude Code)

- The "N due today" pill in the Today card is now sky blue (`var(--sky)`, the To do colour) instead of lime, so all three counts match the task colours: sky due today, pink overdue, mint done. tracker.css `.today-count.is-due`.

### 2026-11-06: Black ticked checkbox in Today (edited in Claude Code)

- A ticked checkbox in the Today card is a black square (`var(--ink)`) with a white ✓ (`.today-item.done .check`). The task list below keeps its pink ticked box. Last tracker.css block.

### 2026-11-06: Completed tasks stay in Today (edited in Claude Code)

- Ticking a task in the Today card no longer makes it disappear. It moves to the bottom of the list, turns mint (`.today-item.done`), is struck through, shows a ticked box and the meta "Completed · Due today" or "Completed · Was due Nov 4". Unticking puts it back in its place.
- New task field `doneOn` (YYYY-MM-DD): set when a task becomes Done via the checkbox or the edit form, removed when reopened. Today shows Done tasks whose `date` or `doneOn` is today. Tasks completed before this change have no `doneOn`, so they only appear if they are due today.
- A mint "N done" pill joins the Today counts when there is at least one.
- app.js: `todayCard()`, the `data-toggle` click handler, and the editor submit. Styles in the last tracker.css block. Backup: `work/app-before-today-done.js`.

### 2026-11-06: Centred checkbox tick (edited in Claude Code)

- The tick in a completed task's checkbox is the original "✓" glyph, now centred in the square: `.check` uses `display:grid;place-items:center` plus padding `1.3px 0.6px 0 0`: vertically centred, and 1px right of the exact centre at the owner's request (optical balance). A CSS-drawn tick was tried first and reverted at the owner's request. Styles in the last tracker.css block.

### 2026-11-06: Today card head redesign (edited in Claude Code)

- Today card head: the line "Friday, Nov 6 · 3 due today · 7 overdue" and the big total number are replaced by the date next to the "Today" title plus two outlined pills: lime "N due today" and pink "N overdue" (the overdue pill is hidden when there are none). app.js `todayCard()`, classes `today-date`, `today-counts`, `today-count is-due/is-late`; styles in the last tracker.css block. On phones the pills sit under the title.

### 2026-11-06: Readable overdue chips (edited in Claude Code)

- 2026-11-06: Overdue chips in Month, Week and Today now use dark ink text on the pink background. The generic red `.late` colour was hard to read there (tracker.css, last block).

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

- On desktop the summary cards felt too large at Bill Calendar's size, so on screens wider than 700px they are compact with the same fonts: label 13px, value 22px, padding 12px 16px (about 77px tall instead of 103px). Phones keep Bill Calendar's 2x2 cards exactly (label 14px, value 1.6rem, padding 14px, about 93px tall). The compact rule is the last block in tracker.css, wrapped in `@media(min-width:701px)`.

### 2026-11-06: Column headings in the task list (edited in Claude Code)

- "Your tasks" now has a heading row (`.task-head`) above the rows: Task, Priority, Due date, Status. It uses the same grid columns as `.task-row`, so each heading sits exactly over its column. It is added in `list()` only when there are tasks, and hidden on phones (700px and narrower), where rows show only the checkbox, title and menu.

### 2026-11-06: One font for text and numbers (edited in Claude Code)

- styles.css (copied from the budget app) sets body text to `'Budget Digits', 'DM Sans'`. "Budget Digits" is Plus Jakarta limited to numerals, so dates like "Nov 1" mixed two fonts. tracker.css now sets `body` to plain DM Sans, like Bill Calendar. Headings and summary-card numbers still use Plus Jakarta explicitly.
- In task rows, priority badge, due date and status are all 13px (date weight 500, badge 600).

### 2026-11-06: Status colours match the summary cards (edited in Claude Code)

- Task chips are coloured by status with the same tokens as the summary cards: to do `--sky`, in progress `--butter` (new class `is-progress`; not `progress`, which is the progress-bar class in styles.css), completed `--mint` (struck through), overdue `--blush` (overdue wins over in progress). Applies to month cells (`.cal-task`), week rows and the phone day panel (`.week-task`), and the Today card (`.today-item`). Previously done tasks were pink and in-progress tasks looked like to-do ones.
- A colour key (`.status-legend`: To do, In progress, Completed, Overdue) sits under the month grid and the week list, like Bill Calendar's legend. On phones it fits on one line.
