def main():
    file_contents = get_text()
    words_num = count_words(file_contents)
    letters_num = count_letters(file_contents)
    print("--- Report of frankenstein.txt ---")
    print(f"The number of words in this book are {words_num}!")
    print()
    sorted_letters = dict(sorted(letters_num.items(), key=lambda item: item[1])) #converted dictionary to a list of dictionaries?
    for letter in sorted_letters:
        num = letters_num[letter]
        print(f"The character '{letter}' was found {num} times!")
    print("--- End of report ---")

def get_text():    
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    return file_contents

def count_words(file_contents):
    words = file_contents.split()
    return len(words)

def count_letters(file_content):
    alphabet = {}
    for letter in file_content:
            if letter.isalpha():
                lowered_letter = letter.lower()
                if lowered_letter not in alphabet:
                    alphabet[lowered_letter] = 1
                else:
                    alphabet[lowered_letter] += 1
    return alphabet

def sort_on(dict):
    return dict["num"]

main()