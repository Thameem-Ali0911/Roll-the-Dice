import random

while True:
    choice = input("Roll the dice ?(y/n)").lower()
    if choice == 'y':
        d1 = random.randint(1, 6)
        d2 = random.randint(1, 6)
        print(f"({d1},{d2})")
    elif choice == 'n':
        print("Thank's for playing !")
        break
    else:
        print("Invalid !!")
