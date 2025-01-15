import datetime as dt
import random as rn

MIN_DEPOSIT = 10
MAX_DEPOSIT = 1000

class Person:
    def __init__(self, first_name, last_name, birth_date):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        
    def get_details(self):
        return f"""
    G'day {self.first_name} {self.last_name}!!!
    Haligtree Lounge welcomes you. G'Luck on your winnings."""
        
    def parse_birth_date(self):
        year, month, day = map(int, self.birth_date)
        today = dt.date.today()
        b_date = dt.date(year, month, day)
        age = today.year - b_date.year - ((today.month, today.day) < (b_date.month, b_date.day))
        return age
    
class SlotMachine(Person):
    def __init__(self, first_name, last_name, birth_date):
        super().__init__(first_name, last_name, birth_date)
        self.balance = 0
        
    def age_check(self):
        age = self.parse_birth_date()
        return age 
    
    def get_deposit(self):
        while True:
            deposit = input("Enter the amount of money you want to deposit: $")
            if deposit.isdigit():
                deposit = int(deposit)
                if MIN_DEPOSIT <= deposit <= MAX_DEPOSIT:
                    self.balance += deposit
                    print(f"Deposit successful! Your balance is now ${self.balance}.")
                    break
                else:
                    print(f"Please enter an amount between ${MIN_DEPOSIT} - ${MAX_DEPOSIT}.")
            else:
                print("Please enter a valid number.")
        return self.balance
        
    def get_bet(self):
        while True:
            bet = input("Enter the amount you want to bet: $")
            if bet.isdigit():
                bet = int(bet)
                if bet > self.balance:
                    print("Insufficient balance. Please deposit more money or lower your bet.")
                else:
                    self.balance -= bet
                    print(f"Bet accepted! You bet ${bet}. Remaining balance: ${self.balance}.")
                    return bet
            else:
                print("Please enter a valid number.")
        
    def winning_conditions(self):
        bet = self.get_bet()
        
        first_line = rn.randint(0,7)
        second_line = rn.randint(0,7)
        third_line = rn.randint(0,7)
        print(f"Slot results: {first_line} | {second_line} | {third_line}")
        if first_line == second_line == third_line == 0:
            print("Better luck next time :(")
        elif first_line == second_line == third_line == 7:
            available_balance = bet * 10
            self.balance += available_balance
            print(f"Congratulations, you hit the jackpot! You won ${available_balance}.")
        else:
            print("Better luck next time:(")
        
        print(f"Your available balance is ${self.balance}.")
        


first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
birth_date = input("Enter your date of birth in 'YYYY-MM-DD' format: ").split(" ")

person = Person(first_name, last_name, birth_date)
print(person.get_details())

slot = SlotMachine(first_name, last_name, birth_date)
age = slot.age_check()

if age >= 18:
    print("You are eligible to play!")
    slot.get_deposit()
    slot.winning_conditions()
else:
    print(f"You are not eligible to play as your age ({age}) is less than the minimum required age.")
