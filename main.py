import sqlite3 as sq
from time import sleep
import datetime as dt

class Bank():
    def __init__(self):
        self.conn = sq.connect("database.db")
        self.cur = self.conn.cursor()
        print("Main Menu")
        print("1. Withdrawl")
        print("2. Deposit")
        print("3. Balance Status") 
        print("4. Open New Account")
        print("5. Exit")
        while True:
            ch = int(input("Enter your choice = "))
            if ch == 1:
                self.withdrawl()
            elif ch == 2:
                self.deposit()
            elif ch == 3:
                self.balStatus()
            elif ch == 4:
                self.newAcc()            
            elif ch == 5:
                print("Thanks for using our service. Do come again.")
                self.cur.close()
                self.conn.close()
                sleep(1)
                exit()
            else:
                print("Please check your input...")
    
    def withdrawl(self):
        accNo = int(input("Enter your Account no = "))
        query = ("select Account_no from Accounts where Account_No > 0")
        self.cur.execute(query)
        temp = self.cur.fetchall()
        data_accNo = [i[0] for i in temp]
        counter = 0
        trails = 2
        if accNo in data_accNo:
            pin = int(input("Enter your pin no = "))
            query = (f"select Pin from Accounts where Account_no = {accNo}")
            self.cur.execute(query)
            data_pin = self.cur.fetchall()[0][0]
            while counter != 3:
                if data_pin == pin: 
                    withBal = int(input("Enter amount to withdraw = "))
                    query = (f"select Balance from Accounts where Account_no = {accNo}")
                    self.cur.execute(query)
                    accBal = self.cur.fetchall()[0][0]
                    if withBal > accBal:
                        print("You Have insufficient Balance in your account please try again...") 
                    else:
                        accBal -= withBal
                        print(f"Thanks for using our service. Remaining funds in your account = {accBal}")
                        query = (f"update Accounts set Balance = {accBal} where Account_no = {accNo}")
                        self.cur.execute(query)
                        self.conn.commit()
                    break
                else:
                    print("Incorrect Pin. Please Try again.")
                    if trails > 0:
                        print(f"You got {trails} more incorrect trials left.")
                    trails -= 1
                    counter += 1
                    if counter == 3:
                        print("Incorrect pin trials over please start over.")
                        break
                    pin = int(input("Enter your pin no = "))
                    continue
        else:
            print("No Record Found in Our Database. Please Try Again...!")
    
    def deposit(self):
        accNo = int(input("Enter your Account no = "))
        query = ("select Account_no from Accounts where Account_No > 0")
        self.cur.execute(query)
        temp = self.cur.fetchall()
        data_accNo = [i[0] for i in temp]
        counter = 0
        trails = 2
        if accNo in data_accNo:
            pin = int(input("Enter your pin no = "))
            query = (f"select Pin from Accounts where Account_no = {accNo}")
            self.cur.execute(query)
            data_pin = self.cur.fetchall()[0][0]
            while counter != 3:
                if data_pin == pin: 
                    depBal = int(input("Enter amount to deposit = "))
                    query = (f"select Balance from Accounts where Account_no = {accNo}")
                    self.cur.execute(query)
                    accBal = self.cur.fetchall()[0][0]
                    accBal += depBal
                    print(f"Thanks for using our service. Your updated balance = {accBal}")
                    query = (f"update Accounts set Balance = {accBal} where Account_no = {accNo}")
                    self.cur.execute(query)
                    self.conn.commit()
                    break
                else:
                    print("Incorrect Pin. Please Try again.")
                    if trails > 0:
                        print(f"You got {trails} more incorrect trials left.")
                    trails -= 1
                    counter += 1
                    if counter == 3:
                        print("Incorrect pin trials over please start over.")
                        break
                    pin = int(input("Enter your pin no = "))
                    continue
        else:
            print("No Record Found in Our Database. Please Try Again...!")
    
    def balStatus(self):
        accNo = int(input("Enter your Account no = "))
        query = ("select Account_no from Accounts where Account_No > 0")
        self.cur.execute(query)
        temp = self.cur.fetchall()
        data_accNo = [i[0] for i in temp]
        counter = 0
        trails = 2
        if accNo in data_accNo:
            pin = int(input("Enter your pin no = "))
            query = (f"select Pin from Accounts where Account_no = {accNo}")
            self.cur.execute(query)
            data_pin = self.cur.fetchall()[0][0]
            while counter != 3:
                if data_pin == pin: 
                    query = (f"select Balance from Accounts where Account_no = {accNo}")
                    self.cur.execute(query)
                    accBal = self.cur.fetchall()[0][0]
                    print(f"Balance in your account = {accBal}")
                    print("Thanks for using our service")
                    break
                else:
                    print("Incorrect Pin. Please Try again.")
                    if trails > 0:
                        print(f"You got {trails} more incorrect trials left.")
                    trails -= 1
                    counter += 1
                    if counter == 3:
                        print("Incorrect pin trials over please start over.")
                        break
                    pin = int(input("Enter your pin no = "))
                    continue
        else:
            print("No Record Found in Our Database. Please Try Again...!")

    def newAcc(self):
        name = input("Enter your name = ")
        gender = input("Enter your gender = ")
        y, m, d = input("Enter your dob (yyyy-mm-dd)= ").split("-")
        dob = dt.date(int(y), int(m), int(d))
        age = int(input("Enter your age = "))
        mob = int(input("Enter your mobile no = "))
        bal = int(input("Deposit your initial amount = "))
        pin = int(input("Please select any 4 digit numeric pin for your account = "))
        query = (f"insert into Accounts (Name, Gender, DOB, Age, Mobile_No, Balance, Pin) values ('{name}', '{gender}', '{dob}', {age}, {mob}, {bal}, {pin});")
        self.cur.execute(query)
        self.conn.commit()
        query = (f"select Account_No from Accounts where Name = '{name}'")
        self.cur.execute(query)
        accno = self.cur.fetchall()
        print("Conguragtulations...!! Your account is successfully created.")
        print(f"Your account number is {accno[0][0]}. Please remember this as it is very important you will require it while doing any transaction.")

if __name__ == "__main__":
    a = Bank()
    a