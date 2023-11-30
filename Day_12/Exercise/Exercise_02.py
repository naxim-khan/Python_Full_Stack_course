# Block Scope
# Python have no block scope like other languages.
game_level=3
enemies=["Skeleton 💀","Zombies 👻","Alien 👽"]

if game_level < 5:
    new_enemie=enemies[0]

print(new_enemie)
# in the above new_enemie is inside the if statement block of code.
# but i can also access it out side the block if statement so that's how
# the python don't have block scope concept.
