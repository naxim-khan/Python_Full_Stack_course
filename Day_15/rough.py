from machine_data import MENU,resources
user_input="latte"
update_resources={"water":300,
    "milk":200,
    "coffe":100,}
def resources_spend(user_input):
    flavor=MENU[user_input]
    ingredients=flavor["ingredients"]
    for i in ingredients:
        resources[i]-=ingredients[i]
        update_resources[i]=resources[i]
    print(update_resources)

# user_input="espresso"

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
#     if i_milk>u_milk:
#         print("Sorry Not Enough Milk!")
#     elif i_water>u_water:
#         print("Sorry not enough Water!")
#     elif i_coffe>u_coffe:
#         print("Sorry enough Coffe!")
#     else:
#         resources_spend(user_input)
#         print("Here is your coffe")

# while True:
#     user_input=input("Enter Coffe:").lower()
#     is_resources_sufficient(user_input)
#     option=input("Continue Exit.  : ").lower()
#     if option=='exit':
#         break
flavor=MENU[user_input]
cost=flavor["cost"]
print(cost)
def process_coin():
    total_money=[]
    quarters=float(input("Quarter = "))
    dimes=float(input("Dimes = "))
    nickles=float(input("Nickles = "))
    pennies=float(input("Pennies = "))
    quarters_total=quarters*0.25
    total_money.append(quarters_total)
    dimes_total=dimes*0.10
    total_money.append(dimes_total)
    nickles_total=nickles*0.05
    total_money.append(nickles_total)
    pennies_total=pennies*0.01
    total_money.append(pennies_total)

    total_money=sum(total_money)

    return total_money

total=process_coin()
cost=flavor["cost"]
if total<cost:
    print("hi")

