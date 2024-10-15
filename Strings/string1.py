def pig_latin():
    word = input(" Please enter the word to be translated to pig latin ")
    vowels ="aeiou"
    output=""
    if (word[0] in vowels):
            output = word+"way"
    else:
        output = word[1:] + word[0]+"ay"
    print(f"Ding ding your results are ready! The translation of {word} in pig latin is {output}")

pig_latin()