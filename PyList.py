#Python lesson - 
#\Documents\LearnPython\Pylist.py
#Reverse a list

x=range(6)
for n in x:
    print(n)


numbers = [1,2,3,4,5,6,7,8,9]
total_items = len(numbers)
for i in range(total_items//2):
    end_index = total_items-i-1
    temp = numbers[end_index]
    numbers[end_index]=numbers[i]
    numbers[i] = temp
    print(numbers)
