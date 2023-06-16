#functions go here

#calculate ticket price based on age
def calc_ticket_price(var_age):

  #ticket is $7.50 for users under 16
  if var_age < 16:
    price = 7.5

  #ticket is $10.50 for users under 65
  elif var_age < 65:
    price = 10.5

  #ticket is $6.50 for seniors (65+)
  else:
    price = 6.5

  return price



#main routine goes here

#loop for testing...
while True:

  #get age (assume users input a valid integer)
  age = int(input("Age: "))

  #calculate ticket cost
  ticket_cost = calc_ticket_price(age)
  print("Age: {}, Ticket Price: ${:.2f}".format(age, ticket_cost))

  