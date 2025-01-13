import datetime
import random

MAX_BET = 1000
MIN_BET = 10
LINES = 3


class Player:
    def __init__(self, first_name, last_name, birth_date):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        
    def get_details(self):
        return f""" Haligtree Lounge welcomes you {self.first_name} {self.last_name}!
    Wishing you great luck on your journey to win big!"""
        
class SlotMachine(Player):
    def __init__(self, first_name, last_name, birth_date, deposit, bet):
        super().__init__(first_name, last_name, birth_date)
        self.deposit = deposit
        self.bet = bet
        
    def check_age(self):
        birth_date = datetime.date(int(birth_date[0]), int(birth_date[1]), int(birth_date[2]))
        today = datetime.date.today()
        curr_age = today - birth_date
        if curr_age.days < 6570:
            print("You are not eligible to play this game.")
    
    def get_deposit(self,deposit):
        deposit = input("Enter the amount you want to deposit: $")
        if deposit.isdigit():
            self.deposit = int(deposit)
            if self.deposit < MIN_BET:
                print("Minimum deposit amount is $10.")
            elif self.deposit > MAX_BET:
                print("Maximum deposit amount is $1000.")
            else: 
                print(f"Your deposit amount is ${self.deposit}.")
                
    def get_bet(self, bet):
        bet = input("Enter the amount you want to bet: $")
        if bet.isdigit():
            self.bet = int(bet)
            if self.bet < MIN_BET:
                print("Minimum bet amount is $10.")
            elif self.bet > MAX_BET:
                print("Maximum bet amount is $1000.")
        return self.bet
    
    def get_balance(self):
        self.balance = self.deposit - self.bet
        return self.balance
    
    def bet_on_lines(self, first_line, second_line, third_line):
        self.first_line = first_line
        self.second_line = second_line
        self.third_line = third_line
        
        first_line = random.randint(0, 7)
        second_line = random.randint(0, 7)
        third_line = random.randint(0, 7)
        
        return first_line, second_line, third_line
    
    def winning_conditions(self):
        if self.first_line == self.second_line == self.third_line == 0:
            print("Better luck next time!")
            self.balance = self.deposit - self.bet
            print(f"Your balance is ${self.balance}.")
            choice = input("Do you wish to continue playing? Y/N:")
            if choice == "Y":
                self.get_bet()
            else: 
                print("Thank you for playing!")
        elif self.first_line == self.second_line == self.third_line == 7:
            print("You hit the jackpot!")
            self.balance = self.balance + self.bet * 10
        else:
            print("better luck next time!")
            

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
birth_date = input("Enter your birth date in 'YYYY-MM-DD' format seperated with spaces: ").split()

p = Player(first_name, last_name, birth_date)
print(p.get_details())
deposit = input("Enter the amount you want to deposit: $")
bet = input("Enter the amount you want to bet: $")
slot = SlotMachine(first_name, last_name, birth_date, deposit, bet)
slot.check_age()
slot.get_deposit(deposit)
slot.get_bet(bet)
slot.get_balance()
slot.bet_on_lines()
slot.winning_conditions()
