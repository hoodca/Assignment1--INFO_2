# Assignment1--INFO_2

# Password Generator
A lightweight Python tool for generating random and memorable passwords, complete with automatic timestamped logging and an optional 1000‑password stress test.

This script supports:

- Random passwords with optional punctuation

- Memorable passwords built from a wordlist

- Automatic logging to separate files

- A simple command‑line menu

- A mass‑generation test for benchmarking or assignment requirements

# Features
- Random Passwords with adjustable length and optional punctuation (uses letters + digits)
- Memorable Passwords built from a wordlist (can configure number of words)
- Logging each generated password (each saved with a timestamp):
  - Memorable passwords → `memorable_passwords.txt`
  - Random passwords → `random_passwords.txt`
Example:
```
2026-01-22 14:35:10 - correct-horse-battery-staple
```
- Mass test mode which runs a 1000-password generation test.

# Installation
1. Ensure you have Python 3.7+ installed.
2. Place your wordlist file (default: `nouns.txt`) in the same directory as the script.
3. Save the script as `password_generator.py` (or any name you prefer).

# Usage
Run the script from the terminal:
```
python password_generator.py
```
You'll see a menu:
```
Choose an option:
1) Generate memorable password
2) Generate random password
3) Run test (1000 passwords)
```
Option 1 — Memorable Password
You’ll be prompted for the number of words (default: 4).

Option 2 — Random Password
You’ll be prompted for:

Length (default: 12)

Whether to include punctuation

Option 3 — Mass Test
Automatically generates 1000 passwords and logs them.

# How it Works
- `_resolve_wordlist_path(path)`
Ensures the wordlist path is resolved relative to the script’s directory.
- `_load_wordlist(path, required)`
Loads the wordlist into memory.
If `required=True` and the file is missing → raises an error.
- `generate_random_password(...)`
Builds a password from:

`string.ascii_letters`

`string.digits`

`string.punctuation` (optional)
- `generate_memorable_password(...)`
Randomly samples words from the wordlist and joins them with hyphens.
- `log_password(password, file)`
Appends the password + timestamp to the specified log file.
- `run_mass_test(...)`
- - Runs 1000 iterations of:
  - Randomly choosing password type
  - Generating the password

Logging it

# Notes
- If `nouns.txt` is missing, memorable passwords will fail (and the script warns you).
- Random passwords require a minimum length of 4.
- Wordlist must contain at least num_words entries.
