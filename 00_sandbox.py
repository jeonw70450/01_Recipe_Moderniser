#This is a sandbox area where I test out my code.


#Not Blank function goes here
def recipe(question):

    valid = False
    while not valid:
        response = input(question)

        if response == "":
            continue
        else:
            return response


#The main code
print("Today we are going to make food")
recipe_name = recipe("What is the recipe name?")
print("You are making {}".format(recipe_name))
