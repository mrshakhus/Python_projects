#Написать функцию, которая список числе превращает в список строк

numbers = [i for i in range(4)]

numbers_string = list(map(lambda x: str(x), numbers))

print(numbers_string)
print(numbers)