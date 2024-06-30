import time

print("enter your card details")

time.sleep(7)
id = "dhrumil7"
password = 1234
user = input("user id: ")
pin = int(input("password: "))
balance = 7000
if (user==id) & (pin == password):
    while True:
        print("""
            1 == balance
            2 == withdraw
            3 == deposite
            4 == exist
            """
        )
        try:
            opt = int(input("enter your choise: "))
        except:
            print("enter valid option")

        if opt == 1:
            print(f"balnce {balance}")
        if opt == 2:
            withdraw = int(input("please enter amount: "))
            balance = balance - withdraw
            print(f"{withdraw} is debited")
            print(f"{balance} is balance")

        if opt == 3:
            deposite = int(input("deposite amount: "))
            balance = balance + deposite
            print(f"{deposite} amount")
            print(f"{balance} amount")

        if opt == 4:
            break

else:
    print("enter wrong details")
