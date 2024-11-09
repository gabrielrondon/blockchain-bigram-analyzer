# src/collect_data.py

import os
from web3 import Web3
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

INFURA_PROJECT_ID = os.getenv('INFURA_PROJECT_ID')

def collect_transactions(start_block, end_block):
    w3 = Web3(Web3.HTTPProvider(f'https://mainnet.infura.io/v3/{INFURA_PROJECT_ID}'))

    transactions = []

    for block_number in range(start_block, end_block):
        block = w3.eth.get_block(block_number, full_transactions=True)
        for tx in block['transactions']:
            transactions.append({
                'from': tx['from'],
                'to': tx['to'],
                'value': tx['value'],
                'hash': tx['hash'].hex(),
                'blockNumber': tx['blockNumber']
            })
    df = pd.DataFrame(transactions)
    return df

if __name__ == '__main__':
    start_block = 10000000
    end_block = 10000010
    df_transactions = collect_transactions(start_block, end_block)
    df_transactions.to_csv('../data/transactions.csv', index=False)
    print("Coleta de dados concluída e salva em data/transactions.csv")
