from string1 import translate_to_pig

def pl_sentence():
    input_string = input("Please enter the sentence to be translated")
    converted_sentence = parse_pig(input_string)
    print(f"Your original sentence is {input_string} and translated sentence is {converted_sentence}")


def parse_pig(string):
    x = string.split()
    pig_latin_sentence =""
    for i, val in enumerate(x):
        output = translate_to_pig(val)
        pig_latin_sentence = pig_latin_sentence+ output + " "
    return pig_latin_sentence


if __name__ == "__main__":
    pl_sentence()