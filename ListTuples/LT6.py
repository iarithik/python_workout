PEOPLE = [('Donald', 'Trump', 7.85),
('Vladimir', 'Putin', 3.626),
('Jinping', 'Xi', 10.603)] 
print("              ")

def format_sort_records(string_list):
    for people in string_list:
        new_string=''
        for i in people:
            if type(i) == int or type(i) == float:
                i = f'{i:.2f}'
            new_string +=i[ : 10] + ' '

            if len(i) <= 10 :
                new_string += (10-len(i))*' '                 

        print(new_string)

format_sort_records(PEOPLE)