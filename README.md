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

### 2026-11-07: Today tick animation (edited in Claude Code)

- Ticking a task in Today now shows the tick and the green "done" look right away (colours fade in over .25s), waits ~0.55s, then the list re-renders and every moved item slides to its new place (FLIP animation, .5s). The ticked task stays on top while it slides (`.moving`). Unticking works the same way in reverse.
- Code: `toggleTask(id)` (shared state change), `todayToggle(item,button)` (animation), `data-id` on `.today-item`. Other lists (Your tasks, calendar) toggle instantly as before. Users with "reduce motion" turned on get the instant version.
- Backup: `work/app-before-today-anim.js`. index.html CSS version `20261107-today-anim`.

### 2026-11-07: Shorter pause before the Today slide (edited in Claude Code)

- Owner asked for a shorter pause: the ticked task now waits 0.33s (was 0.55s) before sliding down. `setTimeout` in `todayToggle()`.
- Then shortened again to 0.25s at the owner's request.

### 2026-11-07: Projects in Settings (edited in Claude Code)

- New full-width **Projects** card at the bottom of Settings: every project with its task count, plus Rename and Delete. Personal is the default and can't be renamed or deleted (tasks with no project show as Personal).
- **Rename** opens an inline field (Enter saves, Escape cancels). Renaming to an existing name (case-insensitive, e.g. "Wrok" → "work") asks to merge and moves the tasks into the existing project. The project filter follows a rename.
- **Delete** asks first and moves the project's tasks to Personal.
- Data: two optional fields on `data`: `removedProjects` (hides deleted built-ins Work/Home) and `extraProjects` (keeps a renamed project that has no tasks yet). `projects()` reads both. Older data and backups without them still work; `valid()` ignores extra fields.
- Settings order: Calendar | Backup, Sample tasks | Delete all, Projects.
- Checked in the browser: typo merge, rename, delete, Escape cancels, filter options update, no console errors. Backup: `work/app-before-projects.js`. index.html CSS version `20261107-projects`.
- Personal is listed first (Settings Projects, the project filter and the editor's project suggestions); the rest stay A–Z.

### 2026-11-07: Phone header: Add task on top, month picker full width (edited in Claude Code)

- On phones (≤700px) the header actions stack: "＋ Add task" first (full width, `order:-1`), then the month picker stretched to the full width with the month centred. The Week view gets the same Add task on top; its week picker was already full width. Desktop unchanged. index.html CSS version `20261107-month-full2`.

### 2026-11-07: Phone bottom tab bar, like Bill Calendar (edited in Claude Code)

- On phones (≤700px) Tasks / Calendar / Settings move to a bar fixed at the bottom of the screen, full width, split into three equal tabs, each with an icon over the label (Lucide list-checks, calendar-days, settings; same icons and sizes as Bill Calendar's tab bar). Active tab: lime with an ink border. White bar with a top border and soft shadow, safe-area padding for iPhones. `#app` gets bottom padding so content never sits under it; the toast moves above the bar.
- Code: `tabIcons` in app.js, nav buttons now hold `.tab-icon` + `.tab-label`. Icons are hidden on desktop, where the nav looks as before.
- Checked in the iPhone simulator: bar renders, switching tabs works. Backup: `work/app-before-bottom-nav.js`. index.html CSS version `20261107-bottom-nav`.

### 2026-11-07: Phone header: Add task next to the title (edited in Claude Code)

- Replaces the "Add task on top, full width" layout from earlier today. On phones the header is a grid: title on the left, a normal-size "＋ Add task" on the right (not stretched), and the month or week picker full width underneath. In Week view the Today button sits on its own row under the picker. Desktop unchanged. index.html CSS version `20261107-add-right`.
- Tasks tab icon changed to the owner's pick, Lucide `logs` (three rows of dots and lines), instead of `list-checks`.
- Bottom bar made a bit smaller at the owner's request: icons 22px (was 27), labels 11px, tighter padding; `#app` bottom padding 92px. index.html CSS version `20261107-smaller-bar`.
- Tasks tab icon changed again to the owner's pick: Lucide `list-todo` (a box and a tick beside three lines).

### 2026-11-07: Phone top bar on one line (edited in Claude Code)

- On phones the logo, "TASK TRACKER" and "Saved on this device" now sit on one line (save state right-aligned, 11px, no wrap). Overrides the shared styles.css phone rules that pushed the save state to its own row. Checked at 440px (simulator) and 375px with no horizontal scroll. index.html CSS version `20261107-one-line-top`.

### 2026-11-07: Your tasks: done tasks at the bottom, same tick animation as Today (edited in Claude Code)

- `filteredTasks()` now sorts open tasks first, done tasks last (then by date, then title).
- Ticking a task in Your tasks behaves like Today: tick and done look show at once, 0.25s pause, then rows slide to their new places (0.5s). The shared function is still `todayToggle()`; it now handles `.today-item` and `.task-row` (both carry `data-id`), keyed per list so the same task in Today and the list animates in each. Reduce-motion users get the instant version.
- Backup: `work/app-before-list-done-bottom.js`. index.html CSS version `20261107-list-done-bottom`.

### 2026-11-07: One meta line style everywhere (edited in Claude Code)

- Replaced the "Work · November 7 · High priority" dot-separated lines with one shared `metaLine(t, opts)` in app.js: bold date with a small calendar icon (dark red when overdue), a coloured priority dot with the word (High pink, Medium yellow, Low blue), then the project in grey, plus optional extra words.
- Where: Your tasks on phones (desktop keeps only the project, since date and priority have columns), Today ("Today" / "Was due November 4" / "Completed" as the date text, "In progress" as extra), Calendar Week and the phone day panel (no date, since the day is the heading; "In progress" / "Overdue" as extra).
- Styles: `.meta-line`, `.ml-date`, `.ml-pri`, `.ml-proj`, `.ml-extra` at the end of tracker.css. Removed the now-unused `short()` in `todayCard()`. Backup: `work/app-before-meta-line.js`. index.html CSS version `20261107-meta-line`.
- Owner changed her mind: the new meta line is **only for Your tasks** (phones). Today, Calendar Week and the day panel are back to their previous text exactly as before. `metaLine()` stays and is used only by `row()`. index.html CSS version `20261107-meta-line-list`.

### 2026-11-07: Your tasks filters: "All statuses", search border, phone layout (edited in Claude Code)

- The status filter's first option now reads "All statuses" (value stays `All`, so filtering is unchanged).
- The search field has the same 1px #8b8b90 border and 9px radius as the selects.
- Phones: search takes the full width on the first line, the three filters (statuses, priorities, projects) sit below in three equal columns, 13px text.
- Styles at the end of tracker.css. index.html CSS version `20261107-filters`.

### 2026-11-07: Your tasks on phones show the status (edited in Claude Code)

- Phones hide the status column, so the status pill (To do / In progress / Done / Overdue, same colours as desktop) now sits at the end of the phone meta line, after the project. It wraps under the date on narrow screens.
- New `statusPill(t)` in app.js builds the pill for both the desktop column and the phone line; `row()` passes it to `metaLine()` as `extra`. Desktop is unchanged (`.meta-phone` stays hidden there).
- Smaller pill style `.meta-line .ml-extra .task-status` at the end of tracker.css. index.html CSS version `20261107-phone-status`.
- Follow-up: the pill now always sits on its own line under date, priority and project (`.task-row .meta-line .ml-extra{flex-basis:100%}`), so every pill starts at the same left edge instead of trailing text of different widths. index.html CSS version `20261107-phone-status-line`.

### 2026-11-08: Your tasks phone meta line: no calendar icon before the date (edited in Claude Code)

- Removed the small calendar icon in front of the date (the reschedule button on the right already uses a calendar). Deleted the unused `metaCal` constant in app.js and the `.meta-line .ml-ico` rule in tracker.css. The date stays bold, dark red when overdue. index.html CSS version `20261108-no-date-icon`.

### 2026-11-08: Today card uses the Your tasks meta line (edited in Claude Code)

- Owner asked for Today to match Your tasks. `todayCard()` now uses `metaLine()`: date (bold; dark red when overdue, "Today" when due today, "Completed" when done), coloured priority dot, project, plus "In progress" when relevant. The card colour already says overdue, so the date has no "Was due" prefix and the line stays on one row.
- Removed the now-unused `short()` in `todayCard()`. Added `.today-meta{opacity:1}` and a 2px top margin at the end of tracker.css. Calendar Week is unchanged. index.html CSS version `20261108-today-meta`.

### 2026-11-08: Your tasks desktop priority column with coloured dots (edited in Claude Code)

- The Priority column now shows a coloured dot before the word (High pink #e0457b, Medium yellow #f2c94c, Low blue #9fc0f0), same as the meta line in Today and on phones. The badge span gets `pri-col pr-<Priority>` plus an `<i>`; styles at the end of tracker.css. index.html CSS version `20261108-pri-dots`.

### 2026-11-08: Settings order: Projects right after Calendar preferences (edited in Claude Code)

- New order: Calendar preferences, Projects, then Backup & restore and Sample tasks side by side, then Delete all tasks. Calendar preferences and Delete all tasks are now full width too (`.wide-panel`), so the two-column grid has no empty cells. Phones stay one column. index.html CSS version `20261108-settings-order`.

### 2026-11-08: Settings Projects: "+ Add project" (edited in Claude Code)

- The Projects card has a "+ Add project" button in its head. It opens an inline form at the top of the list (name field, Add, Cancel; Enter adds, Escape cancels). Names are trimmed and capped at 80 characters; an existing name (any case) shows a toast and keeps the form open.
- New `addProject(name)` and `addingProject` state in app.js. A new project goes into `data.extraProjects` (or is un-hidden from `removedProjects` if it is Work/Home), shows with 0 tasks, and appears in the task editor's project list right away. Opening Rename closes the add form and vice versa.
- Small head button styles at the end of tracker.css. index.html CSS version `20261108-add-project`.

### 2026-11-08: Task editor: project is a list with "+ Add new project…" (edited in Claude Code)

- The editor's Project field is now a `<select>` of `projects()` (new tasks default to Personal) with a last option "+ Add new project…" (value `__new__`). Typing a brand new project name in the editor is no longer possible; new projects are added in Settings.
- Choosing "+ Add new project…" closes the editor and opens Settings with the Projects add form open and focused. If a task name was already typed, it asks first ("Leave this task without saving…"); Cancel puts the previous project back and keeps the editor open.
- Safety: the save handler maps a stray `__new__` to Personal. No CSS change.

### 2026-11-08: Today card: overdue date no longer red (edited in Claude Code)

- In the Today card the overdue date stays dark ink, since the pink card already marks it overdue (`.today-meta .meta-line .ml-date.late{color:var(--ink)}`). Your tasks keeps the dark red overdue date. index.html CSS version `20261108-today-date-ink`.
- Fix: the dot styles had un-hidden the priority column on phones (a second "● High" line under each task). `.task-row>.pri-col{display:inline-flex}` now lives inside `@media(min-width:701px)`, so phones hide the column again. index.html CSS version `20261108-pri-phone-fix`.

### 2026-11-08: Today card can be collapsed (edited in Claude Code)

- A chevron button in the top-right corner of the Today card hides or shows the task list. The title, date and the due / overdue / done counts stay visible when collapsed. The choice is remembered on this device in localStorage key `allocate-task-tracker-today-collapsed` (separate from the task data, so backups are unaffected).
- app.js: `todayCollapsed` state, the list and empty message are wrapped in `#today-body`, click handler `data-today-collapse` toggles the class without a full re-render; re-renders keep the state. Button has `aria-expanded` / `aria-controls` and a Show/Hide label.
- Styles at the end of tracker.css (chevron rotates; reduced motion skips the rotation). index.html CSS version `20261108-today-collapse`.

### 2026-11-08: Coloured priority dot everywhere (edited in Claude Code)

- New `priDot(priority, suffix)` helper in app.js renders `<span class="pri-dot pr-X"><i></i>X…</span>`. Used in Calendar Week rows and the phone day panel ("Home · ● Medium priority · In progress") and the calendar cell week meta. Your tasks (desktop column and phone line) and Today already had dots. The filter and editor dropdowns stay plain text (native selects can't show dots).
- `.pri-dot` styles at the end of tracker.css, same colours as elsewhere. index.html CSS version `20261108-pri-dots-all`.

### 2026-11-08: Leftovers: repeat hint, Overdue card, Week meta line (edited in Claude Code)

- Task editor: the "The next task is created when you complete this one." hint under Repeat shows only when a repeat is chosen (hidden for None, toggles live on change via `data-repeat-select` / `.repeat-hint`).
- The Overdue summary card counts every overdue open task, not only the selected month or week, so it matches the Today card. Total / In progress / Completed still follow the selected month or week.
- Calendar Week rows and the phone day panel use `metaLine(t,{date:false})`: priority dot, project, "In progress" when relevant (the day is the heading and the row colour shows overdue, so no date or "Overdue" text). `.week-task-meta{opacity:1}` and spacing at the end of tracker.css. index.html CSS version `20261108-leftovers`.
- Owner decision: no "In progress" text in Today or Calendar Week; the card colour carries the status everywhere there. Your tasks keeps its status pill / column.

### 2026-11-08: In-app confirm dialog instead of the browser confirm() (edited in Claude Code)

- Bug: "Delete all tasks" seemed to do nothing. The code worked, but it relied on the browser's `confirm()`, which some in-app/embedded browsers block silently (it returns false, so nothing happens). The Settings page also did not re-render, so project counts looked unchanged.
- New `ask(message, okLabel, danger)` in app.js shows a small modal `<dialog id="ask">` (Cancel + action button, Cancel focused, Escape = Cancel) and returns a Promise<boolean>. It replaces every `confirm()`: delete all tasks, remove sample tasks, delete task, delete project, merge on rename, leave the editor to add a project, replace on backup import. `renameProject` and `deleteProject` are now async.
- Delete all and Remove sample tasks re-render Settings afterwards. The invalid-backup `alert()` is now a toast; the rare storage-error `alert()` in `save()` is unchanged.
- `.ask-dialog` styles at the end of tracker.css. index.html CSS version `20261108-ask-dialog`.

### 2026-11-08: Repeat hint removed (edited in Claude Code)

- Owner asked to drop the "The next task is created when you complete this one." line under Repeat entirely. Repeating still works the same (completing a repeating task creates the next one). Removed the hint span and its change handler from app.js; `.field-hint[hidden]` CSS is now unused but harmless.

### 2026-11-08: Settings Projects: task counts aligned (edited in Claude Code)

- Rename/Delete buttons and Personal's "Default" now sit in one fixed-width slot `.project-actions` (170px on desktop), so the "N tasks" counts line up in every row. Phones keep the wrapped layout with counts aligned right. index.html CSS version `20261108-project-align`.

### 2026-11-08: Settings cards in one row have equal height (edited in Claude Code)

- `.settings-grid{align-items:stretch}` (was `start`), so Backup & restore and Sample tasks are always the same height, even when Sample tasks' buttons wrap to two lines on narrower screens. index.html CSS version `20261108-settings-equal`.

- 2026-11-09: Settings, Sample tasks card: button labels shortened to "Add samples" and "Remove samples" so both buttons fit on one row, level with the Export/Import buttons in Backup & restore.

- 2026-11-09: Sticky page heading. The title (Task tracker / Task calendar / Settings), the month picker or week controls and the "+ Add task" button stay pinned to the top while scrolling, on desktop and phone. The heading gets a solid page background, and a thin line with a soft shadow appears once it is stuck (`.heading.stuck`, toggled by a scroll listener at the end of app.js). CSS version bumped to `20261109-sticky-heading`.
