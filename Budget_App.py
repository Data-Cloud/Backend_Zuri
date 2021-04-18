name = input("Welcome! What's your name?\n")
print (f'Welcome, {name}')
amount_initial = input('How much do you currently have?\n')
print (f'You have N {amount_initial}')
print ('categories you can make purchase for include: \n food \n clothing \n entertainment']
       
amount_food = input('How much would you pay for food? \n')
amount_clothing = input('How much would you pay for clothing? \n')
amount_entertainment = input('How much would you pay for entertainment? \n')

amount = amount_food+amount_clothing+amount_entertainment


print ('Your total Budget is %s' %amount)


