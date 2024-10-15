def pig_latin():
    word = input(" Please enter the word to be translated to pig latin ")
    if word.isalpha():
        output = translate_to_pig(word)
        print(f"Ding ding your results are ready! The translation of {word} in pig latin is {output}")
    else:
        print(f"Please include only alphabets")


def translate_to_pig(word):
    vowels ="aeiou"
    output=""
    if (word[0].lower() in vowels):
            output = word+"way"
    else:
        output = word[1: ] + word[0].lower()+"ay"
    return output
pig_latin()

