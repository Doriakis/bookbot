import sys

from stats import get_num_words, get_chars_dict, sort_chars

def main():
    # Check if a path was provided
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    # Get path from terminal argument instead of hardcoded string
    book_path = sys.argv[1]
    
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    sorted_chars = sort_chars(chars_dict)

    print(f"--- Begin report of {book_path} ---")
    print(f"Found {num_words} total words")
    print() # Adds a blank line

    for item in sorted_chars:
        print(f"{item['char']}: {item['count']}")

    print("--- End report ---")

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
main()

