def ubbi_dubbi():
    input_word = input("Hi there! Please enter your word here :")
    output_word = ubdb_translate(input_word)
    print(f"Hi lovelies! The translation of word {input_word} is {output_word}")

vowels ="aeiou"
def ubdb_translate(word):
    output =""
    for w in word:
        if w in vowels:
            output = output+"ub"+w
        else:
            output = output+w
    return output

if __name__ == "__main__":
    ubbi_dubbi()