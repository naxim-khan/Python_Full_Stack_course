# Scope.
# first we create a variable called enemies and set it to 1
enemies=1
# Then we create a function called increase enemies 
# and we set that variable enemeis to 2 inside function 
# In this programm there is a basic knowledge about scope.
def increase_enemies():
    enemies=2
    print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")
# Local scope
def drink_potion():
    potion_strength=2
    print(potion_strength)
drink_potion()
# print(potion_strength) An error you can only use potion_strength
# when you inside that function other wise you can't use it

# Global Scope
# The only difference between Global and Local Scope is where you define 
# or where you create you variable 
player_health =10 # Global Variable
def drink_potion():
    potion_strength=2 # Local Variable
    print(player_health)
drink_potion()
 # player_health is the perfect example of Global Scope.
