#This is a sandbox area where I test out my code.


#Not Blank function goes here
def not_blank(question):

    valid = False
    while not valid:
      response = input(question)
    
      if response == "":
        continue 
      else:
       return response



#The main code
print("Today we are going to make food")
recipe_name= not_blank("What is the recipe name?")
print("You are making {}".format(recipe_name))
