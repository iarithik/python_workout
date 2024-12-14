from FP8 import gematria_dict

sc_dict = gematria_dict()

def gematria_for(word):
    score = sum( sc_dict.get(char,0)
                for char in word)
    return score

def file_score(filename):
    with open(filename,'r') as f:
        score_dict = { word.strip() : gematria_for(word.strip())
                      for word in f }
    return score_dict

def gematria_equal_words(word,filename):
    word_score = gematria_for(word.lower())
    score_dict = file_score(filename)

    result = [word
                for word,score in score_dict.items()
                if word_score == score] 
    return result

output = gematria_equal_words('cat','D:/Hottie/Files/words.txt')
print(output)