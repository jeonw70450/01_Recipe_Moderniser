def num_check(question):
  
  
  
  error = "Please enter a number greater than zero"




  valid = False
  while not valid:
    try:
      response = float(input(question))
      if response <= 0:
        print(error)
      else: 
       return response


    except ValueError:
      print(error)


serving_size=num_check("What is the recipe service size?")
desired_size = num_check("How many servings are needed?")

scale_factor = desired_size / serving_size

print("Scale Factor: {}" .format(scale_factor))


