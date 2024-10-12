class ATM:
    def __init__(self) -> None:
        self.balance = 0.0

    def check_balance(self):
        return self.balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError('Deposit amount must be positive.')
        self.balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError('Withdraw amount must be positive.')

        if amount > self.balance:
            raise ValueError('Insuficient funds.')

        self.balance -= amount


class ATMController:
    def __init__(self) -> None:
        self.atm = ATM()

    def display_menu(self):
        print('Welcome to the ATM!')
        print('1. Check Balance')
        print('2. Deposit')
        print('3. Withdraw')
        print('4. Exit')

    def check_balance(self):
        print(f'Your current balance is: ${self.atm.check_balance()}.')

    def get_number(self, hint):
        try:
            number = float(input(hint))
        except ValueError:
            print('Please enter a valid number.')
        return number

    def withdraw(self):
        while True:
            try:
                amount = self.get_number('Enter the amount to withdraw: ')
                self.atm.withdraw(amount)
                print(f'Successfully withdraw ${amount}')
                break
            except ValueError as e:
                print(e)

    def deposit(self):
        while True:
            try:
                amount = self.get_number('Enter the amount to deposit: ')
                self.atm.deposit(amount)
                print(f'Successfully deposited ${amount}')
                break
            except ValueError as e:
                print(e)

    def get_choice(self):
        try:
            choice = int(input('Please choose an option: '))
        except ValueError:
            print('Please enter a valid number.')
        return choice

    def run(self):
        while True:
            self.display_menu()
            choice = self.get_choice()

            if choice == 1:
                self.check_balance()
            elif choice == 2:
                self.deposit()
            elif choice == 3:
                self.withdraw()
            elif choice == 4:
                print('Thank you for using ATM!')
                break
            else:
                print('Choice unavalaible!')
                break


def main():
    atm = ATMController()
    atm.run()


if __name__ == '__main__':
    main()
