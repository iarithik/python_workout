# #imports
# from operator import itemgetter
# import collections

# #function for power
# numbers = range(5)
# output = [ ]
# for number in numbers:
#     output.append(number * number)
# print(output)
# print(numbers)


# #list comprhensions
# print([number * number for number in range(5) ])


# #function like sqaure brackets
# final = 'abcd'
# final = itemgetter(-1)(final)
# print(final)

# #count of elements in dict
# c = collections.Counter('abcdab')
# print(c)

#mapping and formating strings
# class Default(dict):
#     def __missing__(self, key):
#         return key
# output ='{name} was born in {country}'.format_map(Default(name='Guido'))
# print(output)
s