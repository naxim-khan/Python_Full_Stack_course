from machine_data import MENU,resources
import os

def clear():
    os.system('cls')

MACHINE_ON=True
MONEY=[]
update_resources={
    "water":300,
    "milk":200,
    "coffe":100,
    }
# print report.
def report():
    Water=update_resources["water"]
    Milk=update_resources["milk"]
    Coffe=update_resources["coffe"]
    
    return print(f"Water : {Water}ml\nMilk  : {Milk}ml\nCoffe : {Coffe}g\nMoney : {sum(MONEY)}$ ")

# Process coins.
def process_coin():
    total_money=[]
    print("Insert Coins: ")
    quarters=float(input("Quarter = "))
    dimes=float(input("Dimes = "))
    nickles=float(input("Nickles = "))
    pennies=float(input("Pennies = "))
    quarters_total=quarters*(0.25) #3.5
    total_money.append(quarters_total)
    dimes_total=dimes*(0.10) # 1.4
    total_money.append(dimes_total)
    nickles_total=nickles*(0.05) #0.7
    total_money.append(nickles_total)
    pennies_total=pennies*(0.01) #0.14
    total_money.append(pennies_total) 

    cost=MENU[user_inputs]
    cost_money=cost["cost"]
    total_money=sum(total_money) # 5.74
    change_money=total_money-cost_money 
    machine_money=cost["cost"]
    if total_money<cost_money:
        print("Sorry not Enough coins. Money refunded.")
        
    else:
        print(f"Here is the change of {change_money:.2f}$")
        print(f"Here is your {user_inputs}☕ Enjoy!")
        resources_spend(user_inputs)
        MONEY.append(machine_money)
        return total_money
    

# Check resources sufficient?
def resources_spend(user_input):
    flavor=MENU[user_input]
    ingredients=flavor["ingredients"]
    for i in ingredients:
        resources[i]-=ingredients[i]
        update_resources[i]=resources[i]  

# def is_resources_sufficient(user_input):
#     flavor=MENU[user_input]
#     ingredients=flavor["ingredients"]
#     i_milk=ingredients["milk"]
#     i_water=ingredients["water"]
#     i_coffe=ingredients["coffe"]
#     # Resources
#     u_milk=update_resources["milk"]
#     u_water=update_resources["water"]
#     u_coffe=update_resources["coffe"]
def is_resources_sufficient(user_input):
    flavor=MENU[user_input]
    ingredients=flavor["ingredients"]
    i_milk=ingredients["milk"]
    i_water=ingredients["water"]
    i_coffe=ingredients["coffe"]
    # Resources
    u_milk=update_resources["milk"]
    u_water=update_resources["water"]
    u_coffe=update_resources["coffe"]
    if i_milk>u_milk:
        print("Sorry Not enough Milk!")
    elif i_water>u_water:
        print("Sorry not enough Water!")
    elif i_coffe>u_coffe:
        print("Sorry not enough Coffe!")
    else:
        process_coin()
        

# Checking inputs
def checking_inputs(User_inputs):
    if User_inputs=='report':
        report()
    elif User_inputs=='espresso'or User_inputs=='latte'or User_inputs=='cappucino':
        is_resources_sufficient(User_inputs)
    elif User_inputs !='espresso'or User_inputs!='latte'or User_inputs!='cappucino' or User_inputs != 'report' or User_inputs!= 'off':
        print("Sorry !! Wrong input!")        
        
# 1. Prompt user by asking "What would you like? (espresso/latte/cappucino): "
while MACHINE_ON:
    user_inputs=input("What would you like? (espresso/latte/cappucino): ").lower()
    checking_inputs(user_inputs)
    # Turn off the Coffe Machine by entering "off" to the prompt.
    if user_inputs=='off':
        MACHINE_ON=False

