# Week 5 — Error Handling

Stop programs from crashing on bad data. Catch errors, clean up safely, and raise your own — the natural next step after Week 4's file and CSV work.

**Live site:** https://benchvue.github.io/python-lesson/week-5/

## Topics

`try` / `except` · Exception types · `finally` · `raise` · `try/except/else` · Resilient data loops

## Lessons

| # | Topic | Animation | Code | Idea |
|---|-------|-----------|------|------|
| 01 | try / except | [▶ Demo](https://benchvue.github.io/python-lesson/week-5/01_try_except.html) | [.py](01_try_except.py) | An error in `try` jumps to `except` — no crash. |
| 02 | Exception types | [▶ Demo](https://benchvue.github.io/python-lesson/week-5/02_except_types.html) | [.py](02_except_types.py) | Match each error to its own handler. |
| 03 | finally | [▶ Demo](https://benchvue.github.io/python-lesson/week-5/03_finally.html) | [.py](03_finally.py) | `finally` always runs — ideal for cleanup. |
| 04 | raise | [▶ Demo](https://benchvue.github.io/python-lesson/week-5/04_raise.html) | [.py](04_raise.py) | Throw your own error when a rule is broken. |
| 05 | try / except / else | [▶ Demo](https://benchvue.github.io/python-lesson/week-5/05_try_except_else.html) | [.py](05_try_except_else.py) | `else` runs only when there was no error. |

## Putting it together

| # | Topic | Animation | Code | Idea |
|---|-------|-----------|------|------|
| 06 | Safe CSV total | [▶ Demo](https://benchvue.github.io/python-lesson/week-5/06_safe_csv_total.html) | [.py](06_safe_csv_total.py) | Total a CSV with broken rows — skip them, don't crash. |

**06 output** — the loop survives bad and empty rows:

```
Skipped bad row: oops
Skipped bad row: (empty)
Total of good rows: 3700.0
Rows skipped: 2
```

## Quiz

Test yourself after the lessons — 6 quick questions with instant feedback and score.

| Quiz | Open | Covers |
|------|------|--------|
| Week 5 Quiz | [▶ Start](https://benchvue.github.io/python-lesson/week-5/quiz_week5.html) | try/except, error types, finally, raise, else, safe loops. |

**Questions**

1. `try: int("abc")` then `except ValueError` + a later print → **bad then done**
2. What does `10 / 0` raise? → **ZeroDivisionError**
3. When does `finally` run? → **Always**
4. `raise ValueError("nope")` caught by `except ... as e: print(e)` → **nope**
5. When does `else` run? → **Only if try had no error**
6. try/except around `float(row)` in a loop, on a bad row → **That row is skipped, loop continues**

## Common errors to know

| Error | Happens when… |
|-------|---------------|
| `ValueError` | `int("abc")` — right type, bad value |
| `ZeroDivisionError` | dividing by 0 |
| `TypeError` | `10 / "x"` — wrong type |
| `KeyError` | a dict key that doesn't exist |
| `FileNotFoundError` | opening a file that isn't there |

## Run in Terminal (macOS)

```bash
cd /Users/you/Documents/python-lesson/week-5   # go to the folder
python3 01_try_except.py                       # catches a ValueError
python3 06_safe_csv_total.py                   # totals a messy CSV
```

Tip: type the start of a filename and press **Tab ⇥** to auto-complete it.

## Practice

Take your Week 4 CSV reader and wrap the `float(row["amount"])` call in `try/except`.
Count how many rows were skipped, and print the total of the valid ones.

Every animation has **▶ Play / ❚❚ Pause / ⤓ Step Into / ⤾ Step Over / ■ Stop** —
Step Into walks into each function or loop pass, Step Over runs it as one step.
