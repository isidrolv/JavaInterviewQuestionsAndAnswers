# Self-Test App

Python tools for generating and running Java interview question quizzes.

## Prerequisites

```bash
pip install pyyaml matplotlib
```

> `tkinter` is required for the Windows GUI app and ships with most Python distributions.
> Install it via your OS package manager if it is missing (e.g. `sudo apt install python3-tk`).

## Scripts

| Script | Description |
|---|---|
| `java_quiz_console.py` | Terminal-based interactive quiz |
| `java_quiz_win.py` | Windows GUI quiz (tkinter) |
| `generate_java_questions.py` | Generates `data/java-questions.json` from the root `readme.md` |
| `fix_truncated_options.py` | Repairs truncated answer options in `data/java-questions.json` |
| `_inspect.py` | Debugging helper — prints specific questions from the JSON |

## Usage

Run all scripts from **any** working directory; they resolve paths relative to their own location.

### Console quiz

```bash
python self-test-app/java_quiz_console.py
```

### Windows GUI quiz

```bash
python self-test-app/java_quiz_win.py
```

### (Re-)generate questions from readme

```bash
python self-test-app/generate_java_questions.py
```

### Fix truncated options

```bash
python self-test-app/fix_truncated_options.py
```

## Configuration

Edit `self-test-app/config.yml` to adjust font sizes, window dimensions, the pass
threshold, and the maximum number of questions shown per session.

## Data

`self-test-app/data/java-questions.json` — the question bank used by both quiz apps.
