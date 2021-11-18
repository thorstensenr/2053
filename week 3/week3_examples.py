# input
name = input('What is your name?')
print(name)

age = input("How old are you?")
print(age)
# input is read in as a string
# need to convert string to int before using it as an int
age = int(age)
print("Next year you will be",age+1)

# you can convert to int in same line as input
num = int(input("Enter a number"))

# place try block around conversion to int
# this will catch an exception if user enters something other than an int
num = 'y'
while not isinstance(num, int):
    try:
        num = int(input("Enter a number"))
    except ValueError:
        print("You must enter a number")

# prints each argument with a space between them
print('kathleen','malone')

# use end parameter to change the end line of a print statement
# default is a new line
# change to space
print('line 1',end=" ")
print('line 2')
# use sep parameter to change the separator between arguments
# change to commas
print(1,2,3,4, sep = ',', end=' ')
print(5,6,7,8, sep=',')

# Reading files
#open file and store in text variable
file = open('top_ten_movies.txt', 'r')
text = file.read()
print(text)

# use with to manage resources
with open('top_ten_movies.txt') as file:
    # store file in text variable
    text = file.read()
# the above stores the file as one long array of characters
# this prints the character at index place 220
print(text[220])

# preferred way to read in files
# store each line of file in variable
with open('top_ten_movies.txt', 'r') as file:
    for line in file:
        # the file is stored with a new line at the end of each line
        # don't print another line with the print function
        print(line, end='')

movies=[]
with open('movies_only.txt', 'r') as file:
    for line in file:
        # use rstrip to remove end line
        # view movies list without the rstrip to see '\n'
        movies.append(line.rstrip())
print(movies)

# use split method to split each line into tokens and store in list
# line is split based on spaces between words
heights=[]
with open('heights.txt', 'r') as file:
    for line in file:
        info = line.split()
        print(info)
        print(info[0], info[1], "is",info[2],"inches tall.")