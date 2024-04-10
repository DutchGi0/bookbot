def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    text = text.lower()

    character_count = {}

    for char in text:
        if char.isalnum():
            character_count[char] = character_count.get(char, 0) + 1

    return character_count

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    # print(text)
    
    character_counts = count_characters(text)

    word_count = count_words(text)

    print("Book Statistics:")
    print("----------------")
    print(f"Total words: {word_count}")
    print("Characters frequencies:")
    sorted_characters = sorted(character_counts.items(), key=lambda x: x[1], reverse=True)
    for char, count in sorted_characters:
        print(f"The '{char}' characters was found {count} times")

main()
