import this

zen = """Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
"""

zen_map = dict()
zen = zen.split()

#counting number of identical words
for word in zen:
    zen_map[word.lower()] = 0
for word in zen:
    zen_map[word.lower()] += 1

#finding 3 most frequent words
#by sorting number of words
greatest_number = 0
first_frequent_word = ''
second_frequent_word = ''
third_frequent_word  = ''

for index, counted_word in enumerate(zen_map):
    if index == 0:
        first_frequent_word = counted_word
    if index == 1:
        second_frequent_word = counted_word
    if index == 2:
        third_frequent_word  = counted_word

for counted_word in zen_map:
    if zen_map[counted_word] > greatest_number:
        greatest_number = zen_map[counted_word]
        third_frequent_word = second_frequent_word
        second_frequent_word = first_frequent_word
        first_frequent_word = counted_word
        
print(f'1 место: {first_frequent_word} - {zen_map[first_frequent_word]} раз')
print(f'2 место: {second_frequent_word} - {zen_map[second_frequent_word]} раз')
print(f'3 место: {third_frequent_word} - {zen_map[third_frequent_word]} раз')

#well, that doesn't work


