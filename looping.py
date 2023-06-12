#function goes here


#main routine goes here

#set maximum amount of tickets below
MAX_TICKETS = 3

#loop to sell tickets
tickets_sold = 0

while tickets_sold < MAX_TICKETS:
  name = input("Please enter your name or 'xxx' to quit: ")

  if name == "xxx":
    break

  tickets_sold += 1

#output number of tickets sold
tickets_left = MAX_TICKETS - tickets_sold

if tickets_sold < MAX_TICKETS:
  print("You have sold {} ticket/s. There is {} ticket/s remaining".format(tickets_sold, tickets_left))
else:
  print("Congratulations, you have sold all available tickets")