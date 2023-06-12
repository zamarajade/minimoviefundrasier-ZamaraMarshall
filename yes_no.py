#functions go here


#main routine goes here
while True:
  want_instructions = input("Do you need instructions for this program? Y/N ").lower()
  
  if want_instructions == "y" or want_instructions == "yes":
    print("Instructions go here")
  elif want_instructions == "n" or want_instructions == "no":
    pass
  else:
    print("Please answer either yes or no")