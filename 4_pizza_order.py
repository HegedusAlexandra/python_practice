print("Thank you for choosing Python Pizza Deliveries!")
size = input('What size pizza do you want? S, M, or L : ')
add_pepperoni = input('Do you want pepperoni? Y or N : ')
extra_cheese = input('Do you want extra cheese? Y or N : ')

pizza_price = 0
if size == 'S':
  pizza_price+=15
  if add_pepperoni == 'Y' :
    pizza_price += 2
  if extra_cheese == 'Y':
    pizza_price +=1
elif size == 'M':
  pizza_price+=20
  if add_pepperoni == 'Y' :
    pizza_price += 3
  if extra_cheese == 'Y':
    pizza_price +=1
else:
  pizza_price+=25
  if add_pepperoni == 'Y' :
    pizza_price += 3
  if extra_cheese == 'Y':
    pizza_price +=1
  
print(f'Your final bill is: ${pizza_price}.')