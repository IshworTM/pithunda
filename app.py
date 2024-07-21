#Making a chat bot Barista


def main():
  print("Hello, Welcome to Ish's Cafe!!!!!!!!!!!!!!!!!")

  name = input("Enter your name:\n>> ").lower()

  if name == "ben":
    evilism = input("Are you that EVIL BEN??\n>> ").lower()
    if evilism == "yes" or evilism == "y":
      print("You MONSTER you aren't allowed here, leavee...\n")
      return
    else:
      print("OHH You are that rare Ben, You are most welcome!!!\n")
  else:
    print(f"Hey, {name}!! Thank you very much for coming in today,\n")

  menu = "\n* Black Coffee\n* Cappuccino\n* Espresso\n* Milk Tea\n* Black Tea\n* Shake\n* Latte\n* Hot Chocolate\n"

  print("Here is the menu: \n" + menu)

  order=input("\nWhat would you like?\n-> ")

  if order == "Black Coffee":
    price = 40
  elif order == "Cappuccino":
    price = 60
  elif order == "Espresso":
    price = 55
  elif order == "Milk Tea":
    price = 20
  elif order == "Black Tea":
    price = 10
  elif order == "Shake":
    price = 50
  elif order == "Latte":
    price = 25
  elif order == "Hot Chocolate":
    price = 80
  else:
    print ("Sorry,We don't have that here.. \n")
    exit()

  order_total = int( input("\nHow many of these " + order +" Would you like sir?\n-> "))

  total= order_total * price

  print("\nAlright, we'll get your " + str(order_total)+" " +str(order)+ " ready here in a moment!\n")

  print("Sir, Your total is: Rs." + str(total) + "\n" )
  
  
  if __name__ == "__main__":
    main()