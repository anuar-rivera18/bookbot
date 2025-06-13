from stats import *
import sys

def get_book_text(filepath):
    with open(filepath) as fp:
        return fp.read()

def main():
    if (len(sys.argv) != 2):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book_path = sys.argv[1]
        book_text  = get_book_text(book_path)
        sorted_chars = sort_dict(count_chars(book_text))

        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {book_path}...")
        print("----------- Word Count ----------")
        print(f"Found {count_words(book_text)} total words")
        print("--------- Character Count -------")
        for value in sorted_chars:
            if(value["char"].isalpha()):
                print(f"{value["char"]}: {value["num"]}")
        print("============= END ===============")
   
main()