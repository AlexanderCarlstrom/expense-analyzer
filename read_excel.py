import pandas as pd
import datetime as dt


def read_excel(file):
    columns = {'Transaktionsdatum': 'date', 'Inköpsställe': 'description', 'Belopp': 'amount'}

    data = pd.read_excel(file, engine='openpyxl', skiprows=9, usecols=columns.keys())
    data = data.rename(columns=columns)

    # data.to_csv('csv_input.csv', encoding='utf-8', index=False, header=False)

    transactions = []

    for row in data.itertuples():
        (_index, date, description, amount) = row
        transactions.append(Transaction(dt.datetime.strptime(date, '%Y-%m-%d').date(), description, float(amount)))

    return transactions


class Transaction:
    def __init__(self, date, description, amount):
        self.date = date
        self.description = description
        self.amount = amount
