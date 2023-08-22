#This is my python project
#Working on it as part of VarsityTutors Python Class
#December 12th, 2022
#Email: mabonga@gmail.com
#name = input('What is your name?\n')
#print('Hi, %s.' % name)

age = 37
print(age)
height = 5.9
print(height)
first_name = "Edward"
print(first_name)

second_age = "38"
print(second_age)

fruits = ["apple", "mango","pear", "kiwi","oranges"]
snacks = ["cookies", "candy","icecream", "cake","chocolate"]
student_ages = [16, 15, 32, 39, 18, 20]
student_heights = [20.7, 15.1, 10.5, 20.1, 18.1, 20.3]

list_of_lists = [fruits, snacks, student_ages, student_heights]

  
#This function is used to print the age
def print_age():
  print("My age is", age)



print_age()

def print_height():
  print("My Height is", height)


print_height()

#This function will print the ages for all the students
def print_ages():
  for age in student_ages:
    print(age)

print_ages()

#def print_fruits():
#  for k in fruits:
#     print(k) 

#print_fruits()


def print_fruits():
  for index in range(len(fruits)):
     fruit = fruits[index]
     print(fruit)

print_fruits()



def make_fruits_uppercase():
  for index in range(len(fruits)):
     fruit = fruits[index]
     fruits[index] = fruit.upper()
     print(fruits[index])
  

make_fruits_uppercase()

def print_shopping():
  for i in range(len(list_of_lists)):
      list = list_of_lists[i]
      for j in range(len(list)):
          element = list[j]
          print(element)

        
print_shopping()  

fruits.append("passion")
fruits.remove("KIWI")

print_fruits()

def double_student_ages():
   for i in range(len(student_ages)):
     age = student_ages[i]
     student_ages[i] = age*2


double_student_ages()

print_ages()
   
     
def print_reverse_list(): #this function is used to print a reverse function for a list.
    for i in range(len(fruits) - 1, -1, -1):
        print(fruits[i])
fruits = ["apple", "mango","pear", "kiwi","oranges"]
print_reverse_list()



# Our original list of numbers
numbers = [1, 2, 3, 4, 5]

# We want to get the total number of items in the list
total_items = len(numbers)

# We will loop only half of the total_items (that's why we use total_items // 2)
for i in range(total_items // 2):
    # We calculate the corresponding index from the end of the list
    end_index = total_items - i - 1

    # We temporarily save the value from the end of the list
    temp = numbers[end_index]

    # We swap the value at the current position with the value from the end
    numbers[end_index] = numbers[i]

    # We assign the temporarily saved value to the current position
    numbers[i] = temp

# Now, we print the list which has been reversed in-place
print(numbers)  # Outputs: [5, 4, 3, 2, 1]


numbers.reverse()
print(numbers)  # Outputs: [5, 4, 3, 2, 1]
# Outputs: [5, 4, 3, 2, 1]
