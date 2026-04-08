import json
import random
import string
from pathlib import Path


class Bank:
    database = 'data.json'
    data = []

    # Load data
    if Path(database).exists():
        try:
            with open(database) as f:
                data = json.load(f)
        except:
            data = []

    @classmethod
    def save(cls):
        with open(cls.database, 'w') as f:
            json.dump(cls.data, f, indent=4)

    @staticmethod
    def generate_account():
        chars = string.ascii_letters + string.digits + "!@#$%"
        return ''.join(random.choices(chars, k=8))

    @classmethod
    def find_user(cls, acc, pin):
        return next((u for u in cls.data if u['accountNo'] == acc and u['pin'] == pin), None)

    # -----------------------------

    def create_account(self, name, age, email, pin):
        if age < 18 or len(str(pin)) != 4:
            return "Invalid age or PIN"

        user = {
            "name": name,
            "age": age,
            "email": email,
            "pin": pin,
            "accountNo": self.generate_account(),
            "balance": 0
        }

        Bank.data.append(user)
        Bank.save()
        return user

    def deposit(self, acc, pin, amount):
        user = self.find_user(acc, pin)
        if not user:
            return "User not found"

        if amount <= 0 or amount > 10000:
            return "Invalid amount"

        user['balance'] += amount
        Bank.save()
        return "Deposited successfully"

    def withdraw(self, acc, pin, amount):
        user = self.find_user(acc, pin)
        if not user:
            return "User not found"

        if amount > user['balance']:
            return "Insufficient balance"

        user['balance'] -= amount
        Bank.save()
        return "Withdraw successful"

    def get_details(self, acc, pin):
        user = self.find_user(acc, pin)
        return user if user else "User not found"

    def update(self, acc, pin, name=None, email=None, new_pin=None):
        user = self.find_user(acc, pin)
        if not user:
            return "User not found"

        if name:
            user['name'] = name
        if email:
            user['email'] = email
        if new_pin:
            user['pin'] = int(new_pin)

        Bank.save()
        return "Updated successfully"

    def delete(self, acc, pin):
        user = self.find_user(acc, pin)
        if not user:
            return "User not found"

        Bank.data.remove(user)
        Bank.save()
        return "Account deleted"