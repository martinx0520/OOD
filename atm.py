"""

ATM Account
Requirements:
1. Bank card associated with the account and financial institution
2. Know PIN number
3. Screen show prompt to users

"""

from abc import ABC, abstractmethod

class Transaction(ABC):
    def __init__(self, customerId, receiverId=None):
        self._customerId = customerId
    
    def get_customer_id(self):

    @abstractmethod
    def get_transaction_description(self):
        pass

class Deposit(Transaction):
    def __init__(self, customerId, amount):
        super().__init__(customerId)
        self._amount = amount
    
    def get_transaction_description(self):
        return f'User {self.get_customer_id()} deposited {self._amount} to account {self.get_customer_id()}'

class Withdrawal(Transaction):
    def __init__(self, customerId, amount):
        super().__init__(customerId)
        self._amount = amount

    def get_transaction_description(self):
        return f'User {self.get_customer_id()} withdrew {self._amount} from account {self.get_customer_id()}'

class Transfer(Transaction):
    def __init__(self, customerId, receiverId, amount)
        super().__init__(customerId)
        self._receiverId = receiverId
        self._amount = amount

    def get_transaction_description(self):
        

class BankCard:
    def __init__(self, customerId, name, balance, financial_institution, pin):
        self._customerId = customerId
        self._name = name
        self._balance = balance
        self._financial_institution = financial_institution
        self._pin = pin
        self._logged_in = False

    def get_balance(self)

    def get_pin(self)

    def set_logged_in(self)

    def deposit(self, amount):
        self._balance += amount

    def withdrawal(self, amount):
        self._balance -= amount

class ATM:
    def __init__(self, accounts, transactions):
        self._accounts = accounts
        self._transaction = transactions

    def get_account(self, customerId):
        return self._accounts[customerId]

    def get_accounts(self)

    def deposit(self, customerId, amount):
        account = self.get_account(customerId)
        if not account._logged_in:
            raise Exception("Invalid operation")
        account.deposit(amount)

        transaction = Deposit(customerId, amount)
        transaction.get_transaction_description()

    def withdraw(self, customerId, amount):
        if amount > self.get_account(customerId).get_balance():
            raise Exception("Insufficient Funds")
        account = self.get_account(customer_id)
        if not account._logged_in:
            raise Exception("Invalid operation")
        account.withdrawal(amount)

        transaction = Withdrawal(customerId, amount)
        transaction.get_transaction_description()

    def transfer(self, customerId, receiverId, amount):
        if amount > self.get_account(customer_id).get_balance():
            raise Exception("Insufficinet Funds")
        account = self.get_account(customer_id)
        if not account._logged_in:
            raise Exception("Invalid operation")
        account.withdrawal(amount)
        
        receiver_account = self.get_account(receiverId)
        receiver.deposit(amount)

        transaction = Transfer(customerId, amount)
        transaction.get_transaction_description()

    def login(self, customerId, entered_pin):
        account = self.get_account(customerId)
        if account.get_pin() == entered_pin:
            account._logged_in = True
        else:
            account._logged_in = False



















