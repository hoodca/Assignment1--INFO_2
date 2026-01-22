import os
import random
import string
from datetime import datetime

MEMORABLE_LOG = "memorable_passwords.txt"
RANDOM_LOG = "random_passwords.txt"


def _resolve_wordlist_path(wordlist_path):
    script_dir = os.path.abspath(os.path.dirname(__file__) or ".")
    return os.path.join(script_dir, wordlist_path)


def _load_wordlist(wordlist_path, required):
    resolved = _resolve_wordlist_path(wordlist_path)
    if not os.path.exists(resolved):
        if required:
            raise FileNotFoundError(f"Wordlist file not found: {resolved}")
        return []
    with open(resolved, "r") as file:
        return [line.strip() for line in file if line.strip()]

def generate_random_password(length=12, include_punctuation=True):
    "Generates a random password of specified length."
    if length < 4:
        raise ValueError("Password length should be at least 4 characters.")

    characters = string.ascii_letters + string.digits
    if include_punctuation:
        characters += string.punctuation

    return ''.join(random.choice(characters) for _ in range(length))


def generate_memorable_password(
    wordlist_path="nouns.txt",
    num_words=4,
    words=None,
):
    "Generates a memorable password using random words from a wordlist."
    word_pool = words

    if word_pool is None:
        word_pool = _load_wordlist(wordlist_path, required=True)

    if len(word_pool) < num_words:
        raise ValueError("Not enough words in the wordlist to generate the password.")

    selected_words = random.sample(word_pool, num_words)
    return "-".join(selected_words)


def log_password(password, log_file="password_log.txt"):
    "Logs the generated password with a timestamp to a log file."
    with open(log_file, "a") as file:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"{timestamp} - {password}\n")


def run_mass_test(wordlist_path="nouns.txt", total=1000):
    "Generates many passwords for quick testing."
    wordlist = _load_wordlist(wordlist_path, required=False)
    if not wordlist:
        print(f"Wordlist missing at {_resolve_wordlist_path(wordlist_path)}. Memorable passwords will fail.")

    for _ in range(total):
        if random.choice(["mem", "rand"]) == "mem" and wordlist:
            pw = generate_memorable_password(num_words=random.randint(2, 4), words=wordlist)
            log_password(pw, MEMORABLE_LOG)
        else:
            pw = generate_random_password(
                length=random.randint(8, 16),
                include_punctuation=random.choice([True, False]),
            )
            log_password(pw, RANDOM_LOG)

    print(f"Generated {total} passwords and logged them successfully.")


def main():
    print("Choose an option:")
    print("1) Generate memorable password")
    print("2) Generate random password")
    print("3) Run test (1000 passwords)")

    choice = input("Enter 1, 2, or 3: ").strip()

    if choice == "1":
        num_words = input("How many words (default 4)? ").strip()
        num_words = int(num_words) if num_words else 4
        password = generate_memorable_password(num_words=num_words)
        print("Memorable password:", password)
        log_password(password, MEMORABLE_LOG)

    elif choice == "2":
        length = input("Length (default 12)? ").strip()
        length = int(length) if length else 12
        include_punct = input("Include punctuation? (y/N) ").strip().lower() == "y"
        password = generate_random_password(length=length, include_punctuation=include_punct)
        print("Random password:", password)
        log_password(password, RANDOM_LOG)

    elif choice == "3":
        run_mass_test()
    else:
        print("Invalid choice. Please run again.")


if __name__ == "__main__":
    main()