# Program that checks how many vowels and consonants inputted word has.


def main():
    word = input("Enter a word: ")
    vowel = "aeiouy"
    vowels_counter = 0
    consonant_counter = 0

    for i in range(len(word)):
        if word[i] in vowel:
            vowels_counter += 1
        else:
            consonant_counter += 1

    print(f"The word \"{word}\" contains {vowels_counter} vowels and {consonant_counter} consonants.")


if __name__ == "__main__":
    main()
