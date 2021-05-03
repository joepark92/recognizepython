num1 = 42 #storing an int 42
num2 = 2.3 #storing a float 2.3
boolean = True #boolean value
string = 'Hello World' #string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #lists
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #dictionary
fruit = ('blueberry', 'strawberry', 'banana') #tuple
print(type(fruit)) #fruit is a tuple
print(pizza_toppings[1]) #this will print 'Sausage' in the terminal
pizza_toppings.append('Mushrooms') #add topping to the list
print(person['name']) #printsoutput 'John' in the terminal
person['name'] = 'George' #changes 'name' from John to George
person['eye_color'] = 'blue' #add value to dictionary
print(fruit[2]) #output banana

if num1 > 45:
    print("It's greater") #conditional num1 is not greater than 45
else:
    print("It's lower") #output will be It's lower

if len(string) < 5:
    print("It's a short word!") #if the length of the word inside len() is shorter than 5 letters, the output will be it's a short word
elif len(string) > 15:
    print("It's a long word!")
else:
    print("Just right!") #this is the output since 'string' is between 5 and 15

for x in range(5):
    print(x) #output: 0,1,2,3,4
for x in range(2,5):
    print(x) #output 2,3,4
for x in range(2,10,3):
    print(x) #output 2,5,8
x = 0
while(x < 5):
    print(x)
    x += 1 #output: 0,1,2,3,4

pizza_toppings.pop() #nothing happens
pizza_toppings.pop(1) #sausage will be removed

print(person) #output: the dictionary 'person'
person.pop('eye_color') #removes the eye color from the dictionary
print(person) #output: the dictionary 'person' without eye color

for topping in pizza_toppings:
    if topping == 'Pepperoni':
        continue
    print('After 1st if statement')
    if topping == 'Olives':
        break #output: 'After 1st if statement' 3 times until it reaches Olives

def print_hello_ten_times():
    for num in range(10):
        print('Hello') 

print_hello_ten_times() #output: Hello 10 times

def print_hello_x_times(x):
    for num in range(x):
        print('Hello')

print_hello_x_times(4) #output: Hello 4 times

def print_hello_x_or_ten_times(x = 10):
    for num in range(x):
        print('Hello')

print_hello_x_or_ten_times() #output: Hello 10 times
print_hello_x_or_ten_times(4) #output: Hello 4 times


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)