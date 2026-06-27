# Python Lessons for Accounting Major Students

This is an 8-week beginner Python program for college students majoring in Accounting.

Each week is designed as a 1-hour lesson and includes:

- A weekly README.md
- Simple Python examples
- Accounting-related practice ideas

## Course Goal

The goal is to help accounting students learn practical Python skills for:

- Basic calculations
- Excel and CSV data work
- Financial analysis
- Automation
- Reporting
- Simple databases
- Jupyter Notebook usage
- Git and project organization

## Folder Structure

```text
python-lesson/
├── README.md
├── week-1/
├── week-2/
├── week-3/
├── week-4/
├── week-5/
├── week-6/
├── week-7/
└── week-8/
```

## Recommended Setup

Create a virtual environment:

### Windows CMD

```cmd
py -3.12 -m venv C:\Users\benchvue\env312
C:\Users\benchvue\env312\Scripts\activate.bat
```

### Windows PowerShell

```powershell
py -3.12 -m venv C:\Users\benchvue\env312
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
C:\Users\benchvue\env312\Scripts\Activate.ps1
```

### macOS

```bash
python3.12 -m venv ~/env312
source ~/env312/bin/activate
```

Install useful packages:

```bash
python -m pip install --upgrade pip
pip install pandas openpyxl matplotlib requests
```

## VS Code Setup

1. Open this folder in VS Code.
2. Press Ctrl + Shift + P.
3. Select `Python: Select Interpreter`.
4. Choose your virtual environment Python executable.

Example Windows path:

```text
C:\Users\benchvue\env312\Scripts\python.exe
```

## Weekly Plan

| Week | Topics |
|---|---|
| Week 1 | Python basics, variables, print, simple accounting calculations |
| Week 2 | Control flow, loops, functions |
| Week 3 | Lists, dictionaries, transactions, account balances |
| Week 4 | Files, CSV, dates |
| Week 5 | Excel automation with openpyxl |
| Week 6 | Pandas for accounting data analysis |
| Week 7 | Charts, automation, APIs |
| Week 8 | SQL, Jupyter, Git/GitHub, final project |
