
while attempts!=0:
    print(f"You've {attempts} attempts remaining!")
    guessed_number=int(input("Make a Guess: "))
    if guessed_number==RANDOM_NUMBER:
        print(f"The number is: {RANDOM_NUMBER} You win!! 🎉")
        break
    if guessed_number!=RANDOM_NUMBER :
        attempts-=1
        if guessed_number<RANDOM_NUMBER:
            print(f"Too Low")
        elif guessed_number>RANDOM_NUMBER:
            print("Too high")
        if attempts==0:
            clear()
            print("Game Over\nYou Loose!🤣")