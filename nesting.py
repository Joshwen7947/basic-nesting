price_person = int(input('Ticket price:'))
price_baggage = int(input('Baggage cost:'))
price_food = int(input('Price of food on board:'))
total = price_person + price_baggage + price_food
print('Price to pay:', total)
# 
# 
# 
name = input('Employee:')
jobs = int(input('Mandatory jobs done:'))
extra_jobs = int(input('Extra jobs done:'))
score =  jobs*15 + extra_jobs*20
print(name, '- rating', score)
# 
# 
# 
salary = int(input('Monthly salary:'))
over_time = int(input('Amount of Overtime:'))
bonus = salary*0.01*over_time
print('Bonus:', bonus)
#  
# 
# 
#deduction of state income tax
salary = int(input('What is your monthly salary:'))
tax_rate = 0.16
tax_rate = salary*tax_rate
salary = salary - tax_rate
print('Deducted:', tax_rate)
print("You'll get:", salary)