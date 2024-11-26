#imports
import os

def find_all_longest_word(directory):
    all_longest_word_dict ={}

    
    for filename in os.listdir(directory):
        file_path = os.path.join(directory,filename)
        if file_path.endswith('.txt'):
            cur_longest_word = find_longest_word(file_path)
            all_longest_word_dict.update({filename:cur_longest_word})
    
    return all_longest_word_dict


def find_longest_word(file_path):
    longest_word = ""
    words =[]

    with open(file_path,'r',encoding='utf-8') as f:
        for current_line in f:
            words = current_line.split()
            for word in words:
                if len(word) > len(longest_word):
                    longest_word = word

    return longest_word

if __name__ == "__main__":
    directory = 'D:/Hottie/Files/books'
    op = find_all_longest_word(directory)
    print(op)