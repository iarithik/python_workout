def wordcount(Filename):
    op_dict = {}
    with open(Filename,'r') as f:
        count_char = 0
        count_lines=0
        total_word = []
        
        for current_line in f: 
            count_char += len(current_line)
            word = current_line.split()
            total_word += word
            count_lines+=1
        unique_word = set(total_word)

    #print
    print(f"Number of characters (including whitespace) { count_char}")
    print(f"Number of words (separated by whitespace)  {len(total_word)}")
    print(f"Number of lines {count_lines}")
    print(f"Number of unique words {len(unique_word)}")

    return op_dict

if __name__ == "__main__":
    op = wordcount('Files/wcfile.txt')
