# Len [ ENGLISH ]

# Len is a Python function that allows us
# to count how long a string, list, etc., is.

example = "Len counts all the characters in a string"
print(len(example)) # Inside the parentheses goes what you want to count
# Output: 44

example_list = ['we', 'can', 'count', 'things', 'in', 'lists']
print(len(example_list))
# Output: 6
# But why 6? Well, because we're just counting
# how many objects are inside the list.
# Not the characters of the texts.

# It doesn't matter what object is inside the list; it will be counted
example_list_two = [4, "numbers", True, "all sorts of things"]
print(len(example_list_two))
# Output: 4

# Do you want to count the characters of each item inside
# the list? For that, we can use a for loop.
for i in example_list_two:
    # Here, the for loop goes through all the objects in the list one by one

    count = len(str(i)) # In this line, str() changes the value of 'i' (the objects)
                          # to strings. But why? Well, because len() DOES NOT count numbers.
                          # len(3) will give you a Value Error.
    print(count)
    # Outputs: 1
    #         7
    #         4
    #         18
