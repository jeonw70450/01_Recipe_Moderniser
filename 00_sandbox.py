#This is a sandbox area where I test out my code.


#Defintion
def recipe(question):
  error = "Your recipe has numbers in it!"

  valid=False
  while not valid:
    response=input(question)
    has_errors = ""

    for letter in response:
     if letter.isdigit() == True:
      
      has_errors = "yes"
      break

    if response == "":
      continue
    elif has_errors != "":
      print(error)
      continue
    else:
      return response




recipe_name=recipe("What is the recipe name?")
print("You are making {}".format(recipe_name))