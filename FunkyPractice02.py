
# setup a function w/List, Dictionary as 'Parameters'
def func(list, dict):
    print("This is the list: ", list)
    print("This is the dict: ", dict)

# define list to be used as an Argument in the func
fruit = ["Pears", "Peaches", "Apples", "Grapes"]

# define dictionay to be used as an Argument in the func
cars = {"Volvo", "Audi", "Ford", "Chevrolette"}

# call the function
func(fruit, cars)

# call the function but list only element 1 from the list
func(fruit[1], cars)
