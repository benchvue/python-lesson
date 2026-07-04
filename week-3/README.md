# Week 3 — Collections, Functions & Input

Store and summarize accounting data with Python collections, then make programs interactive with functions and `input()`.

**Live site:** https://benchvue.github.io/python-lesson/week-3/

## Topics

Lists · Tuples · Dictionaries · Sets · Function parameters · Local & global scope · `input()` · Type casting

## Lessons

| # | Topic | Demo / Animation | Code | Idea |
|---|-------|------------------|------|------|
| 01 | Transaction list | — | [.py](01_transaction_list.py) | Loop a list of amounts to get a balance. |
| 02 | Account dictionary | — | [.py](02_account_dictionary.py) | Loop a dict of `name: balance` pairs. |
| 03 | Unique vendors | — | [.py](03_unique_vendors.py) | Use a `set` to drop duplicates. |
| 04 | Function parameters | [▶ Demo](https://benchvue.github.io/python-lesson/week-3/04_function_parameters.html) | [.py](04_function_parameters.py) | Values you pass in fill the parameters. |
| 05 | Local & global scope | [▶ Demo](https://benchvue.github.io/python-lesson/week-3/05_scope.html) | [.py](05_scope.py) | Global = everywhere · local = inside a function. |
| 06 | input() | [▶ Demo](https://benchvue.github.io/python-lesson/week-3/06_input.html) | [.py](06_input.py) | Show a prompt, read the user's text. |
| 07 | Text → number | [▶ Demo](https://benchvue.github.io/python-lesson/week-3/07_input_casting.html) | [.py](07_input_casting.py) | `int(input())` — cast a string to an int. |
| 08 | input() → function | [▶ Demo](https://benchvue.github.io/python-lesson/week-3/08_input_to_function.html) | [.py](08_input_to_function.py) | Read a value, convert it, pass it to a function. |

## Reference

| Page | Open | Idea |
|------|------|------|
| Symbols cheat sheet | [open](https://benchvue.github.io/python-lesson/week-3/python_symbols.html) | `[] {} () "" ''` and `! @ # $ % ^ & *` — what each means, with examples. |

## Quiz

Test yourself after the lessons — 5 quick questions with instant feedback and score.

| Quiz | Open | Covers |
|------|------|--------|
| Week 3 Quiz | [▶ Start](https://benchvue.github.io/python-lesson/week-3/quiz_week3.html) | input, casting, function parameters, scope, sets. |

**Questions**

1. What type does `input()` always return? → **str**
2. If the user types 25, `print(int(age) + 1)` → **26**
3. `add_tax(100, 0.1)` where it returns `price + price * rate` → **110.0**
4. Reading a local variable outside its function → **NameError**
5. `len(set(["Amazon", "Amazon", "Staples"]))` → **2**

## Run in Terminal (macOS)

```bash
cd /Users/you/Documents/python-lesson/week-3   # go to the folder
python3 01_transaction_list.py                 # run a lesson
python3 06_input.py                            # interactive — type an answer
```

Tip: type the start of a filename and press **Tab ⇥** to auto-complete it.

## Practice

Build a simple **chart of accounts** as a dictionary, then write a function
`total(accounts)` that returns the sum of all balances. Ask the user for a new
account name and amount with `input()`, cast the amount with `int()`, and add it in.

Each animation (04–08) has **▶ Play / ❚❚ Pause / ■ Stop** controls and runs in any browser.
