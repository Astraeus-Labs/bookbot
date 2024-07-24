
filename = "books/frankenstein.txt"
def main():
    with open(filename) as f:
        print(f"--- Begin report of {filename} ---")
        frankenstein = f.read()
        print(f"Number of words: {word_count(frankenstein.split())}")
        letters = number_of_characters(frankenstein)
        print(f"Number of characters: {len(letters)}")
        characters = letter_list(letters)
        characters.sort(reverse=True, key=sort_on)
        for character in characters:
            print(f"The '{character['character']} character was found {character['num']} times")


def word_count(words):
    return len(words)


def number_of_characters(text):
    lc_text = text.lower()
    dict = {}
    for letter in lc_text:
       dict[letter] = dict.get(letter, 0) + 1
       

    return dict

def letter_list(character_dict):
    result = []
    for character, count in character_dict.items():
        new_item = {
            "character":character,  
            "num": count  
        }
        result.append(new_item)

    return result

def dict_to_list(dict):
    return list(dict.items())

def sort_on(dict,key="num"):
    return dict[key]

main()