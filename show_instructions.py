#functions

#checks that user enters a valid response
def string_checker(question, num_letters, valid_responses):

  error = "Please choose {} or {}".format(valid_responses[0], valid_responses[1])

  while True:

    response = input(question).lower()

    for item in valid_responses:
      if response == item[:num_letters] or response == item:
        return item

    print(error)

def show_instructions():
    print('''\n
***** Instructions *****

For each ticket, enter...
- The person's name (can't be blank)
- Age (between 12 and 120)
- Payment method (cash / credit)

When you have entered all the users, press 'xxx' to quit.

The program will then display the ticket details
including the cost of each ticket, the total cost
and the total profit.

This information will also be automatically written
to a text file.

*************************''')

#variables

yes_no_list = ["yes", "no"]

#main

#ask user if they want to see instructions
want_instructions = string_checker("Do you want to read the instructions (y/n): ",1, yes_no_list)

if want_instructions == "yes":
  show_instructions()

print()