# pyright: strict

from dataclasses import dataclass

NUMBER_OF_ATTEMPTS = 3


@dataclass
class UserInfo:
    username: str
    location: str
    pin: str
    balance: int


def sign_up(registered_users: list[UserInfo]):
    username = input("Enter your username: ")
    location = input("Enter your location: ")
    pin = input("Enter a 4 digit pin: ")
    initial_balance = int(input("Enter your starting balance: "))

    registered_users.append(UserInfo(username, location, pin, initial_balance))

    print("You have been signed up!")
    print()


def get_users_balance(registered_users: list[UserInfo]):
    username = input("Enter your username: ")

    for user_info in registered_users:
        if user_info.username == username and is_user_authorized(user_info):
            return user_info.balance

    print("Username not found")
    exit(1)


def is_user_authorized(user_info: UserInfo):
    for attempt_number in range(NUMBER_OF_ATTEMPTS, 0, -1):
        pin = input("Enter your pin: ")

        if pin != user_info.pin:
            print(f"Wrong pin {attempt_number - 1} attempts remaining \n")
            continue

        return True

    return False


def manage_balance(balance: int):
    while True:
        print()
        print("Welcome to the E-bank")
        print()
        print("Please select your transaction: ")
        print("1. Withdraw")
        print("2. Deposit")
        print("3. Balance")
        print("4. Logout")
        print()

        choice = int(input("Select your choice: "))
        if choice == 1:
            balance = withdraw(balance)

        elif choice == 2:
            balance = deposit(balance)

        elif choice == 3:
            print(balance)

        elif choice == 4:
            print("Logging out...")
            print()
            break

        else:
            print("Invalid Choice")


def withdraw(balance: int):
    withdrawal_amount = int(input("Enter the amount to withdraw: "))

    if withdrawal_amount > balance:
        print("Withdrawal amount exceeds account balance!!!")
        return balance

    balance -= withdrawal_amount
    print(f"Withdrew {withdrawal_amount}. Balance: {balance}")

    return balance


def deposit(balance: int):
    deposition_amount = int(input("Enter the amount to deposit: "))

    balance += deposition_amount
    print(f"Deposited {deposition_amount}. Balance: {balance}")

    return balance


def main():
    registered_users = [UserInfo("Rohit", "New York", "2015", 10000)]

    while True:
        print("1. Login")
        print("2. Sign Up")
        print("3. Exit")
        choice = int(input("What do you want to do? "))
        print()

        if choice not in [1, 2, 3]:
            print("Invalid Choice")
            continue

        if choice == 3:
            return

        if choice == 2:
            sign_up(registered_users)

        balance = get_users_balance(registered_users)

        manage_balance(balance)


if __name__ == "__main__":
    main()