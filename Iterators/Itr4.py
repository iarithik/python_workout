import time
def time_counter(iterable):
    list_time_opr = []
    for i,value in enumerate(iterable):
        list_time_opr.append(time.perf_counter_ns())
        current_time_opr = list_time_opr[i] - list_time_opr[i-1]
        yield (current_time_opr,value)
      
obj = time_counter(['a','b','c','d'])
for i in obj:
    print(i)