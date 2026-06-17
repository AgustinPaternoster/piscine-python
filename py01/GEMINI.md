# AI Context & Guidelines - Piscine Python Module 01: Array

This file provides system-level context and rules for the AI coding assistant (Gemini/Antigravity) working on the "Piscine Python for datascience - 1" project.

## 🚨 Critical Constraints (Must follow at all times)

1. **Python Version:** Always write code compatible with **Python 3.10**.
2. **Explicit Imports Only:**
   - DO NOT use wildcard imports (e.g., `from pandas import *` or `from numpy import *` are STRICTLY FORBIDDEN).
   - Use explicit imports (e.g., `import numpy as np`).
3. **No Global Variables:** Never declare or use global variables.
4. **No Code in Global Scope:**
   - All executable code must be inside functions.
   - Every program/tester must use a `main()` entry point:
     ```python
     def main():
         # tests and error handling
         ...

     if __name__ == "__main__":
         main()
     ```
5. **Documentation:** Every function must have a clear docstring (`__doc__`).
6. **Linter Compliance (flake8):**
   - The code must comply with flake8 coding standards (`alias norminette=flake8`).
7. **Exception Handling:**
   - All expected exceptions must be caught and handled with clear error messages. Uncaught exceptions will invalidate the exercises.
8. **Pre-edit Notification:**
   - BEFORE editing any file, you MUST explain clearly in the chat/terminal what changes you are going to make.

---

## 🛠️ Exercises Requirements Summary

### ex00: Give my BMI
- **Directory:** `ex00/`
- **File:** `give_bmi.py`
- **Prototypes:**
  - `def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:`
  - `def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:`
- **Rules:** Use `numpy` or any table manipulation library. Handle size mismatches and type errors.

### ex01: 2D array
- **Directory:** `ex01/`
- **File:** `array2D.py`
- **Prototype:** `def slice_me(family: list, start: int, end: int) -> list:`
- **Rules:** Print input shape, slice the array using slicing methods, print new shape, and return the sliced array. Use `numpy` or table manipulation library.

### ex02: load my image
- **Directory:** `ex02/`
- **File:** `load_image.py`
- **Prototype:** `def ft_load(path: str) -> array:`
- **Rules:** Load JPG/JPEG images, print shape/format, and print RGB pixel values. Handle errors with clear messages.

### ex03: zoom on me
- **Directory:** `ex03/`
- **Files:** `load_image.py`, `zoom.py`
- **Rules:** Load `animal.jpeg`, print info, zoom/slice to 400x400 (single color channel), and display with axes/scale. Handle errors.

### ex04: rotate me
- **Directory:** `ex04/`
- **Files:** `load_image.py`, `rotate.py`
- **Rules:** Load `animal.jpeg`, cut a square, and transpose it.
- **CRITICAL:** DO NOT use any libraries for the transpose operation. The transpose algorithm must be implemented manually.

### ex05: Pimp my image
- **Directory:** `ex05/`
- **Files:** `load_image.py`, `pimp_image.py`
- **Prototypes:** `ft_invert`, `ft_red`, `ft_green`, `ft_blue`, `ft_grey`.
- **Operator Restrictions:**
  - Invert: `=`, `+`, `-`, `*`
  - Red: `=`, `*`
  - Green: `=`, `-`, `*`
  - Blue: `=`
  - Grey: `=`, `/`
