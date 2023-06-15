#function goes here


#checks user has entered yes / no to a question
def yes_no(question):

  while True:
    response = input(question).lower()
    if response == "yes" or response == "y":
      return "yes"
    elif response == "no" or response == "n":
      return "no"
    else:
      print("Please enter yes or no.")
      
#checks user response is not blank
def not_blank(question):

  while True:
    response = input(question)

    if response == "":
      print("Sorry this can't be blank. Please try again.")
    else:
      return response

#checks users enter an integer to a given question
def num_check(question):

  while True:

    try:
        response = int(input(question))
        return response

    except ValueError:
      print("Please enter an integer.")
      
#main routine goes here

#set maximum amount of tickets below
MAX_TICKETS = 3
tickets_sold = 0

#ask user if they want to see instructions
want_instructions = yes_no(
  "Do you need instructions for this program? Y/N ").lower()

if want_instructions == "yes":
  print("Instructions go here")

print()

#loop to sell tickets

while tickets_sold < MAX_TICKETS:
  name = not_blank("Enter your name (or 'xxx' to quit) ")

  if name == "xxx":
    break

  age = num_check("Age: ")

  if 12 <= age <= 120:
    pass
  elif age < 12:
    print("Sorry you are too young for this movie.")
    continue
  else:
    print("?? That looks like a typo, please try again.")
    continue

  tickets_sold += 1

#output number of tickets sold

if tickets_sold < MAX_TICKETS:
  print("You have sold {} ticket/s. There is {} ticket/s remaining".format(
    tickets_sold, MAX_TICKETS - tickets_sold))
else:
  print("Congratulations, you have sold all available tickets")
