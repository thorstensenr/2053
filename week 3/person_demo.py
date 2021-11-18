from person import Person

# calls __init__
joe = Person("Joe", "Smith")
ned = Person("Ned","Bradley")

ned.say_hello()
joe.say_hello()
# calls __str__
print(joe)
