from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine=MoneyMachine()
coffe_maker=CoffeeMaker()
menu=Menu()

is_on=True
while is_on:
    options=menu.get_items()
    choice=input(f"What would you like? ({options}): ")
    if choice=='report':
        coffe_maker.report()
        money_machine.report()
    elif choice=='off':
        is_on=False
    else:
        drink=menu.find_drink(choice)
        if coffe_maker.is_resource_sufficient(drink):
            money_machine.make_payment(drink.cost)
            coffe_maker.make_coffee(drink)

        # drink=men