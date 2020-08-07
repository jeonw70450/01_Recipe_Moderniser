#ask useer format
recipe_name= input("What is the recipe name?")


error = "Your recipe has numbers in it"
has_errors= ""



#
for letter in recipe_name:
  if letter.isdigit() == True:
    print (error)
    has_errors = "yes"
    break


#give user feedback"
if has_errors != "yes":
  print ("You are Okay!")

