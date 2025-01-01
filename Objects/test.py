word = "00101"
score_list =[]

for i in range(1,len(word)):
    l_string = word[:i]
    r_string = word[i:]

    count_l = l_string.count('0')
    count_r = r_string.count('1')

    score = count_l + count_r

    score_list.append(score)

print(f" max score is {max(score_list)}")