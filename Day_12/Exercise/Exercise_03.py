# Modifying Global Scope.
enemies=1
def increase_enemies():
    # enemies+=1  <-- In this case it's will give you error.
    # Because python consider it as a new variable which is not defined.
    # to increment this global variable named enemies. You have modify it using
    # using global keyword. like below
    # global enemies
    # enemies+=1
    # But the above method is not a good practice. it's create bug's
    # in your program if you want to print the enemies it's value
    # would change after anywhere you call this varible 
    # so instead of that you can use the return method to modify it.
    return enemies+1
increase_enemies()
print(f"enemies inside function {increase_enemies()} \nenimies outside the function: {enemies}")