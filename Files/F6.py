#imports
import json
import glob


def process_data(file):
    scores = { }
    result = [ ]

    with open(file,'r') as f:
        data = json.load(f)
            #data returns list of dictionary
        for i in data:
                #i is dictionary inside the list

            for  key,value in i.items():
                if key in scores:
                    scores[key].append(value)
                else:
                    scores.update({key:[value]})
                #end of loop do the math and send reports and reset scores
                
        for key in scores:
            score_summary = [f'{key} : min {min(scores.get(key))} , max {max(scores.get(key))} , avg {sum(scores.get(key))/len(scores.get(key))}']
            result.extend(score_summary)
        print(result)
    return result       


def print_scores(directory):

    output = [ ]
    pattern = '*.json'

    filename = glob.glob(directory+'/'+pattern)
    for file in filename:  
        #returns file = file's name
        op = process_data(file)
        output.append(op)    
    return output
            

print_scores('D:/Hottie/Files/scores')