#functions go here
def yes_no(question):

  while True:
    response = input(question).lower()
    if response == "yes" or response == "y":
      return "yes"
    elif response == "no" or response == "n":
      return "no"
    else: print("Please enter yes or no.")
      


#main routine goes here
want_instructions = yes_no("Do you need instructions for this program? Y/N ").lower()

if want_instructions == "yes":
  print("Instructions go here")
