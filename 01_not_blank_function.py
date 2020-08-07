#Defintion

def recipe(question):

  valid=False
  while not valid:
    response=input(question)

    if response == "":
      continue
    else:
      return response


#Main code 
recipe_name=recipe("What is the recipe name?")
print("You are making {}".format(recipe_name))