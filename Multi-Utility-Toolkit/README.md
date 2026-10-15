# Multi-Utility Toolkit

## Introduction
I created this Python toolkit to practise using built-in modules and reusable custom packages in one simple, menu-driven program.

## Features
- Date/time: current date, date differences, formatting, stopwatch, countdown
- Math: arithmetic, factorial, trigonometry, logarithms, compound interest, areas
- Random: numbers, lists, passwords, sample data, demo OTPs, dice game
- UUID4: generate unique identifiers
- Files: write, read and append text notes
- Explore built-in and custom module attributes with `dir()`

## How to run
1. Open the `Multi_Utility_Toolkit` folder in VS Code.
2. Open the VS Code terminal (Terminal > New Terminal).
3. Run `python main.py` (or `py main.py` on Windows).
4. Enter a number from 1 to 7 to choose an operation.

Python 3.8+ is recommended. No third-party packages are required.

## File structure
- `main.py` — menus and application entry point
- `my_package/__init__.py` — marks the folder as a package
- `my_package/file_utils.py` — reusable text-file functions
- `my_package/math_utils.py` — reusable mathematical functions
- `toolkit_notes.txt` — created automatically when you save notes

## Example output
```
Welcome to Multi-Utility Toolkit
1. Datetime and Time Operations
2. Mathematical Operations
3. Random Data Generation
4. Generate Unique Identifier (UUID)
5. File Operations (Custom Module)
6. Explore Module Attributes (dir())
7. Exit
Enter your choice (1-7): 2
--- Mathematical Operations ---
1. Arithmetic
2. Factorial
...
Choose: 2
Enter a non-negative whole number (0-1000): 5
Factorial: 120
```

## What I learned
I learned how to import Python's standard modules, create my own modules, organize them into a package, and reuse functions from different files. I also practised input validation, loops, menus, and the `if __name__ == '__main__'` pattern.

## Notes
Passwords and OTPs are demonstrations. Do not use the displayed OTP as a real login verification system. File write mode replaces old notes; append mode preserves them.
