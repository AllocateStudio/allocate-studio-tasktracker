#!/usr/bin/env python3
"""Builds the Etsy download: index.html and the two PDF guides at the top, everything else in app/.

Reads the last commit (not the working folder), so unfinished edits never ship.
The PDFs are printed from packaging/welcome.html and packaging/start-here.html with headless Chrome.
Usage: python3 build-customer-zip.py [output folder, default ~/Desktop/etsy]
"""
import pathlib, re, shutil, subprocess, sys, tempfile, zipfile

NAME = 'AllocateStudio-TaskTracker'
GUIDES = {'welcome.html': 'Task_Tracker_Welcome.pdf', 'start-here.html': 'Task_Tracker_StartHere.pdf'}
CHROME = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
repo = pathlib.Path(__file__).resolve().parent
out_root = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else '~/Desktop/etsy').expanduser()


def git(*args, text=True):
    return subprocess.run(['git', *args], cwd=repo, capture_output=True, check=True, text=text).stdout


def committed(path, binary=False):
    return git('show', 'HEAD:' + path, text=not binary)


def replace(text, old, new):
    assert old in text, old
    return text.replace(old, new)


def tracked(prefix):
    return git('ls-tree', '-r', '--name-only', 'HEAD', prefix).split()


folder = out_root / NAME
if folder.exists():
    shutil.rmtree(folder)
app = folder / 'app'
app.mkdir(parents=True)

# One script and one stylesheet instead of several loose files.
(app / 'app.bundle.js').write_text(committed('month-picker.js') + '\n' + committed('app.js'))
(app / 'styles.css').write_text(committed('styles.css') + '\n' + committed('tracker.css'))

html = committed('index.html')
html = replace(html, 'href="styles.css"', 'href="app/styles.css"')
html = re.sub(r'\n\s*<link rel="stylesheet" href="tracker\.css\?v=[^"]*" />', '', html)
assert 'tracker.css' not in html
html = html.replace('href="assets/', 'href="app/assets/')
html = replace(
    html,
    '    <script src="month-picker.js"></script>\n    <script src="app.js"></script>',
    '    <script src="app/app.bundle.js"></script>',
)
(folder / 'index.html').write_text(html)

for path in tracked('assets'):
    (app / path).parent.mkdir(parents=True, exist_ok=True)
    (app / path).write_bytes(committed(path, binary=True))

# Print the guides from the committed HTML.
with tempfile.TemporaryDirectory() as tmp:
    tmp = pathlib.Path(tmp)
    for path in tracked('packaging') + tracked('assets/fonts') + ['assets/allocate-studio-logo.png']:
        (tmp / path).parent.mkdir(parents=True, exist_ok=True)
        (tmp / path).write_bytes(committed(path, binary=True))
    for page, pdf in GUIDES.items():
        target = folder / pdf
        subprocess.run(
            [CHROME, '--headless=new', '--disable-gpu', '--no-pdf-header-footer', '--allow-file-access-from-files',
             f'--user-data-dir={tmp / "chrome"}', f'--print-to-pdf={target}', (tmp / 'packaging' / page).as_uri()],
            check=True, capture_output=True,
        )
        assert target.exists() and target.stat().st_size > 20000, pdf
        shutil.copy2(target, out_root / pdf)

zip_path = out_root / (NAME + '.zip')
zip_path.unlink(missing_ok=True)
with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as z:
    for f in sorted(folder.rglob('*')):
        if f.is_file() and f.name != '.DS_Store':
            z.write(f, f.relative_to(out_root))

print(zip_path)
