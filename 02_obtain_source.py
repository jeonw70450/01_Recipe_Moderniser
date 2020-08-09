#This is a sandbox area where I test out my code.

#Get's the source of the recipe Name
#Defintion
def recipe(question, error_message, num_ok):
  error = error_message


  valid=False
  while not valid:
    response = input(question)
    has_errors = ""

    if num_ok != "yes":
      for letter in response:
        if letter.isdigit() == True:
          has_errors = "yes"
          break

    if response == "":
      print (error)
      continue
    elif has_errors != "":
      print(error)
      continue
    else:
      return response


source = recipe("Where is the recipe from? ", "The recipe source can't be blank, ", "yes")

print("The Recipe is from {}".format(source))