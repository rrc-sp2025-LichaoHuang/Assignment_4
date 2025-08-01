"""This module contains a program that reads through transaction records
and reports the results.

Example:
    $ python pixell_transaction_report.py
"""

__author__ = "COMP-1327 Student, Lichao Huang"
__version__ = "1.0.0"
__credits__ = "COMP-1327 Faculty"

import csv
import os
 
valid_transaction_types = ['deposit', 'withdraw']
customer_data = {}
rejected_transactions = []
transaction_count = 0
transaction_counter = 0
total_transaction_amount = 0
is_valid_record = True
average_transaction_amount = 0
invalid_type = ''

# Clears the terminal
os.system('cls' if os.name == 'nt' else 'clear')

# Get the directory the script is saved to
SCRIPT_DIRECTORY = os.path.dirname(__file__)

# The name of the data file
DATA_FILENAME = "bank_data.csv"

# The absolute path to the data file
DATA_FILE_PATH = f"{SCRIPT_DIRECTORY}/{DATA_FILENAME}"

with open(DATA_FILE_PATH, 'r') as csv_file:
    reader = csv.reader(csv_file)

    # Skip heading line
    next(reader)

    for transaction in reader:
        # Reset valid record and error message for each iteration
        is_valid_record = True
        
        # Stores validation error messages
        validation_errors = []

        # Gets the customer ID from the first column
        customer_id = transaction[0]
        
        # Gets the transaction type from the second column
        transaction_type = transaction[1]

        ### VALIDATION 1 ###
        if transaction[1] in valid_transaction_types:
            pass
        else:
            is_valid_record = False
            invalid_type = f'[The transaction type "{transaction[1]}" is invalid.]'
        ### VALIDATION 2 ###
        # Gets the transaction amount from the third column

        try:
            transaction_amount = float(transaction[2])
        except ValueError:
            is_valid_record = False
            invalid_type = f'["{transaction[2]}" is invalid transaction amount]'
        ### Valid Data Precess ###
        if is_valid_record == True:
            # Initialize the customer's account balance if it doesn't 
            # already exist
            if customer_id not in customer_data:
                customer_data[customer_id] = {'balance': 0, 'transactions': []}
                if transaction_type == 'deposit':
                    customer_data[customer_id]['balance'] = customer_data[customer_id]['balance'] + transaction_amount
                    transaction_count += 1
                    total_transaction_amount += transaction_amount
                else:
                    customer_data[customer_id]['balance'] = customer_data[customer_id]['balance'] - transaction_amount
                    transaction_count += 1
                    total_transaction_amount += transaction_amount
            # Update the customer's account balance based on the 
            # transaction type
            elif transaction_type == 'deposit':
                customer_data[customer_id]['balance'] += transaction_amount
                transaction_count += 1
                total_transaction_amount += transaction_amount
            elif transaction_type == 'withdraw':
                customer_data[customer_id]['balance'] = customer_data[customer_id]['balance'] - transaction_amount
                transaction_count += 1
                total_transaction_amount += transaction_amount
            
            # Record transactions in the customer's transaction history
            customer_data[customer_id]['transactions'].append(
                (transaction_amount, transaction_type))
        
        ### COLLECT INVALID RECORDS ###
        if is_valid_record == False:
            invalid_data = (transaction,invalid_type)
            rejected_transactions.append(invalid_data)

report_title = "PiXELL River Transaction Report"
print(report_title)
print('=' * len(report_title))

# Print the final account balances for each customer
for customer_id, data in customer_data.items():
    balance = data['balance']

    print(f"Customer {customer_id} has a balance of ${balance:,.2f}.")
    
    # Print the transaction history for the customer
    print("Transaction History:")

    for transaction in data['transactions']:
        amount, type = transaction
        print(f"{type.capitalize():>16}:{amount:>12}")
transaction_counter += transaction_count
average_transaction_amount = total_transaction_amount / transaction_counter
    
print(f"AVERAGE TRANSACTION AMOUNT: ${average_transaction_amount:,.2f}")

rejected_report_title = "REJECTED RECORDS"
print(rejected_report_title)
print('=' * len(rejected_report_title))

for rejected_transaction in rejected_transactions:
    print("REJECTED:", rejected_transaction)
