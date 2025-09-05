import sys
from stats import get_word_count
from stats import get_letter_count
from stats import sort_letter_count

def get_book_text(filepath):
    returnText = ""
    with open(filepath) as f:
        returnText = f.read()
    return returnText

def main():
    if len(sys.argv) == 2:
        path = sys.argv[1]
        print(get_word_count(path))
        letter_counts = get_letter_count(path)
        return_dict = sort_letter_count(letter_counts)
        for item in return_dict:
            print(*item.values(), sep=": ")
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

main()