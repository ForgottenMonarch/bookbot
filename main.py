import sys
from stats import counting_words
from stats import counting_unique_characters
from stats import sort_on
from stats import sorts_chars
def get_book_text(path_to_file):
    with open(path_to_file) as f:
        contents = f.read()
       
    return contents


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book_string = get_book_text(sys.argv[1])
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}")
    print("----------- Word Count ----------")
    counting_words(book_string)
    print("--------- Character Count -------")
    results = sorts_chars(counting_unique_characters(book_string))
    for item in results:
        char = item["char"]
        num = item["num"]
        if char.isalpha():
            print(f"{char}: {num}")
    print("============= END ===============")
main()