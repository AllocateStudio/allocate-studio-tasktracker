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

### 2026-11-06: Month view hides the per-day ＋ (edited in Claude Code)

- Month view on desktop showed a faint ＋ in every day cell (the earlier hide rule only applied on phones). Now it is hidden and appears only on the hovered day with a mouse, same as Week. Phones never show it. Clicking the day number still adds a task on that date. Last tracker.css block.

### 2026-11-06: Week range looks like the month picker (edited in Claude Code)

- Week view: the separate ‹ / range / › buttons are replaced by one outlined control with the calendar icon, using the existing `.week-nav-picker` + `.mp-step` / `.mp-trigger` styles from styles.css (same look as the Month picker). The range label is not clickable; the arrows still use `data-week-step`. Today stays a separate button. On phones the picker fills the width and Today + Add task sit side by side below it. app.js `weekControls()`; last tracker.css block. Backup: `work/app-before-week-picker.js`.

### 2026-11-06: Quieter add buttons in Week (edited in Claude Code)

- Week view: the ＋ next to each day name is hidden on devices with a mouse and appears when hovering the day row or focusing it with the keyboard (`@media(hover:hover)`). On touch screens it stays, fainter (opacity .3). Clicking a day still opens a new task for that date, as before. Month view and the phone day panel are unchanged. Last tracker.css block.

### 2026-11-06: Status pills in Your tasks (edited in Claude Code)

- Priority column is now plain text (no coloured badge). The Status column is an oval pill coloured by status, with darker text in the same hue: To do sky / #2f5aa8, In progress butter / #8a6100, Done mint / #3b7524. app.js `row()` adds `st-todo|st-progress|st-done` to `.task-status`; styles in the last tracker.css block. Overdue is still shown in the Due date column. Backup: `work/app-before-status-pills.js`.

### 2026-11-06: Sky "due today" pill (edited in Claude Code)

- The "N due today" pill in the Today card is now sky blue (`var(--sky)`, the To do colour) instead of lime, so all three counts match the task colours: sky due today, pink overdue, mint done. tracker.css `.today-count.is-due`.
- Then split diagonally: sky on the left, butter on the right (`linear-gradient(115deg,var(--sky) 50%,var(--butter) 50%)`), because tasks due today can be To do (sky) or In progress (butter).

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


### 2026-11-07: Task planning features

- Inbox stores tasks without a date. Unscheduled tasks are excluded from overdue counts and calendar views.
- The task editor supports Daily, Weekdays, Weekly, and Monthly repeats. Completing an occurrence creates one next occurrence; repeating an old completion does not create a duplicate. Missed dates are skipped to the next future occurrence. Monthly repeats keep their original day, clamping to the last day of shorter months. Deleting an occurrence does not delete other occurrences.
- ~~Subtasks~~: removed by the owner on purpose. There is no subtask UI in the editor or the task list. app.js still accepts an optional `subtasks` array in saved data and backups (for compatibility), but nothing shows or edits it. Do not add subtasks back unless asked.
- Tomorrow, Next week, and No date / Inbox buttons fill the editor date; Save task applies the change. The date field supports any specific date.
- Projects are created by entering a new project name in the editor. Existing projects appear as suggestions and in the project filter.
- Select tasks enables bulk completion, scheduling, and deletion with confirmation. Select visible respects current filters; changing filters clears selection.
- Search includes titles, project names and notes within the selected month (Inbox was removed later, see below).
- Existing browser data and JSON backups remain compatible. Syntax and mocked-DOM tests passed, including recurrence boundaries, leap years, duplication prevention, bulk operations, and editor compatibility. Visual verification was not available.

### 2026-11-07: Inbox removed (edited in Claude Code)

- At the owner's request the Inbox tab is gone: navigation is Tasks, Calendar, Settings. The editor's due date is required again ("Due date", `required`), and the "No date / Inbox" quick button is removed (Tomorrow and Next week stay).
- Safety net: any task that still has no date (from an older backup or browser data) is listed at the top of Your tasks, so it is never hidden. Overdue counts still ignore undated tasks.
- Leftover `view==='Inbox'` branches in app.js are now unreachable and harmless. Backup: `work/app-before-remove-inbox.js`.

### 2026-11-07: Reschedule as an icon with a small menu (edited in Claude Code)

- The "▸ Reschedule" row under every task (Today, Week, Your tasks) is replaced by a small icon button at the right of each open task: Lucide `calendar-clock` (ISC licence, inlined as SVG in app.js `reschedIcon`). Clicking it opens a menu: → Tomorrow, → Next week, Pick a date. Outside click or Escape closes it.
- With a mouse the icon appears only on hover/focus; on touch screens it is always visible but faint (opacity .55). Done tasks have no icon.
- app.js: `quickMove()` now renders `.resched` (button `.resched-btn` + `.resched-menu`); `closeResched()` and an Escape key handler were added; the click handler toggles the menu. The existing `data-move` / `data-move-date` actions are unchanged. List rows wrap the title cell in `.task-main`. Styles in the last tracker.css block; `.task-reschedule` is now unused. index.html CSS version bumped to `20261107-resched-icon`. Backup: `work/app-before-resched-icon.js`.

### 2026-11-07: Lucide icon in the Week picker (edited in Claude Code)

- The Week range control (`weekControls()` in app.js) now uses Lucide `calendar-range` (ISC) instead of the hand-drawn calendar, matching the reschedule icon's style (class `lucide-ico`: stroke 1.8, round caps). The Month picker icon (from month-picker.js, shared with other products) is unchanged. index.html CSS version `20261107-week-icon`.

### 2026-11-07: Owner's calendar-days icon in both pickers (edited in Claude Code)

- The owner chose Lucide `calendar-days` (her variant: top ticks `v3`, rect at y=3, divider at y=9, two rows of dots). It replaces `calendar-range` in the Week picker (app.js `weekControls()`) and the old hand-drawn icon in the Month picker (`month-picker.js`, this product's copy only; Bill Calendar's copy is unchanged). Both use class `lucide-ico`. index.html CSS version `20261107-days-icon`.

### 2026-11-07: Bare reschedule icon in Today (edited in Claude Code)

- In the Today card the reschedule button has no frame or fill: just the black calendar-clock icon (19px) on the row color. The owner tried a black square first and did not like it. When the menu is open it turns into a black square with a white icon. The Week list and Your tasks keep the white framed button. Still hover-only on desktop. index.html CSS version `20261107-today-resched-bare`.

### 2026-11-07: Bare reschedule icon in Calendar Week too (edited in Claude Code)

- The Calendar Week list (`.week-task-body`) now uses the same bare black reschedule icon as Today (no frame, 19px, black square only while the menu is open). Your tasks keeps the white framed button. index.html CSS version `20261107-week-resched-bare`.

### 2026-11-07: Clicking outside the reschedule menu only closes it (edited in Claude Code)

- Before, closing the open reschedule menu by clicking elsewhere also triggered whatever was under the click (often opening another task's editor). Now, while a menu is open, a click outside it only closes the menu (`preventDefault`, then stop). The next click works as usual. Clicking another task's reschedule icon still switches straight to that menu. Change is at the start of the delegated click handler in app.js. Backup: `work/app-before-resched-outside-click.js`.

### 2026-11-07: Your tasks rows open the editor; full month names (edited in Claude Code)

- The whole row in Your tasks now opens the editor (`.task-row[data-edit]`, role=button, tabindex=0; Enter or Space works too), same as Today and Week. The three-dots `.edit` button is removed and so is its empty header column. The checkbox and the reschedule icon still do their own thing and do not open the editor. On desktop the title underlines on hover.
- The Due date column shows the full month ("November 7" instead of "Nov 7"); the column is 130px wide now.
- Grid is `30px 1fr 100px 130px 115px` (phone `26px 1fr`). Backup: `work/app-before-row-click.js`. index.html CSS version `20261107-row-click`.

### 2026-11-07: No hover underline in Your tasks (edited in Claude Code)

- The owner did not like the title underline on row hover, so it is removed. Rows still show a pointer cursor and open the editor on click. index.html CSS version `20261107-no-underline`.

### 2026-11-07: No duplicated date and priority in Your tasks (edited in Claude Code)

- On desktop the row meta line under the title shows only the project; date and priority already have their own columns. On phones (≤700px) those columns are hidden, so the meta line still shows "Project · November 3 · Medium priority" via `.meta-phone` (now with the full month instead of 2026-11-03). Backup: `work/app-before-meta-dedupe.js`. index.html CSS version `20261107-meta-dedupe`.

### 2026-11-07: Reschedule icon next to the due date in Your tasks (edited in Claude Code)

- On desktop the reschedule icon in Your tasks now sits right after the date in the Due date column (bare black icon like Today and Week, menu opens under it, left-aligned). It used to float at the right edge of the title column and looked tied to Priority.
- `row()` renders `quickMove(t)` twice: inside `.date` (desktop) and inside `.resched-phone` in `.task-main` (phones, where the date column is hidden). CSS shows one or the other at 700px. Due date column is 150px.
- Backup: `work/app-before-resched-by-date.js`. index.html CSS version `20261107-resched-by-date2`.

### 2026-11-07: Fix for tasks without a date + cleanup of removed features (edited in Claude Code)

- **Bug fixed:** after Inbox was removed, any task with an empty date (left over from Inbox, or from an older backup) crashed the Tasks and Calendar screens (`monthTasks()` called `startsWith` on an empty value). Now `fillDates()` gives such tasks today's date on load and on backup import, and saves once. `monthTasks()` is also guarded.
- **Removed dead code** (none of it was reachable on screen):
  - Inbox branches in `render()`, `editor()` and the quick-date handler (`data-shift="inbox"`), plus the "repeat needs a date" check (date is always required now).
  - Bulk select: `selecting`, `selected`, `bulk()`, `#bulk-bar`, the select-row markup, `data-select-mode` / `data-bulk` / `data-select` handlers.
  - Subtasks: the `subtasks` copy in `editor()` and in `complete()`. `valid()` still accepts a `subtasks` field so old backups import fine.
  - CSS for `.bulk-bar`, `.select-row`, `.subtask-*`, `.subdone`, `.form-grid h3`.
- Checked in the browser: undated task gets today's date; tick/untick; new task with Tomorrow + Weekly; reschedule Next week; completing a repeat creates the next one; delete; Calendar Month/Week; Settings. No console errors.
- Backups: `work/app-before-cleanup.js`, `work/tracker-before-cleanup.css`. index.html CSS version `20261107-cleanup`.

### 2026-11-07: Undated tasks are listed, not auto-dated (edited in Claude Code)

- Owner's call: instead of giving undated tasks today's date (previous entry), they now just appear at the end of Your tasks with "No date", in every month. They are not shown in Today or the calendar and never count as overdue. Opening one asks for a date on save, since the date field is required. `fillDates()` is removed; the `monthTasks()` guard stays, so the crash fix still holds.

### 2026-11-07: Due date is optional again (edited in Claude Code)

- Owner's call: the Due date field in the editor is no longer required. Clear it to save a task with no date; such tasks go to the end of Your tasks as "No date" (see previous entry). A repeating task still needs a date: saving Repeat ≠ None with an empty date shows "Choose a date for a repeating task".

### 2026-11-07: Your tasks columns spread out (edited in Claude Code)

- On desktop the title column took all spare width, leaving a big gap before Priority. Columns are now `30px minmax(180px,2.4fr) 1fr 1.3fr 1fr`, so the spare width is shared between Priority, Due date and Status. Phones unchanged. index.html CSS version `20261107-columns`.

### 2026-11-07: Settings refresh (edited in Claude Code)

- **Week start** is now a pink Sunday | Monday switch (same `.mode-switch` / `.mode-pill` as Month | Week), `data-week-start` buttons. The old `#week-start` select and its change handler are gone.
- **Remove sample tasks** button in the Sample tasks card: removes only tasks with ids `sample-v1-*` (asks first, shows the count). The user's own tasks stay. `sampleDataVersion` stays 1, so samples are not re-seeded on reload.
- **Delete all tasks** card: empties the tracker after a confirm ("cannot be undone", suggests exporting a backup first). Button style `.btn.danger` (white with dark red text, pink on hover). Not re-seeded on reload either.
- Cards are in two columns on desktop, one column on phones.
- Checked in the browser: Monday switch changes the calendar's first day; remove samples, add them back, delete all, reload stays empty. Backup: `work/app-before-settings.js`. index.html CSS version `20261107-settings`.
