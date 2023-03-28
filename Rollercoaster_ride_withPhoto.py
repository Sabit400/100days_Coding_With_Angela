height = int(input("What is your height?"))
bill = 0
if height > 120:
    print("You can ride the Roller coaster")
    age = int(input("What's your age?"))
    if age < 12:
        bill = 5
        print("Your ticket price is $5")
    elif age <= 18:
        bill = 7
        print("Your ticket price is $7")
    else:
        bill = 12
        print("Adult ticket price is $12")

    wants_photo = input("Do you want a photo? Y or N. ")
    if wants_photo == "Y":
        bill += 3
    print(f"Your final bill is ${bill}")

else:
    print("You have to grow more come back next year.")
