# src/preprocess_data.py

import pandas as pd
from web3 import Web3
import os
from dotenv import load_dotenv

load_dotenv()

INFURA_PROJECT_ID = os.getenv('INFURA_PROJECT_ID')

def classify_transaction(tx_row, w3):
    to_address = tx_row['to']
    if pd.isnull(to_address):
        return 'Contract Creation'
    elif w3.eth.get_code(to_address) == b'':
        return 'Value Transfer'
    else:
        return 'Contract Interaction'

def preprocess_transactions(df):
    w3 = Web3(Web3.HTTPProvider(f'https://mainnet.infura.io/v3/{INFURA_PROJECT_ID}'))
    df['tx_type'] = df.apply(lambda row: classify_transaction(row, w3), axis=1)
    df.sort_values('blockNumber', inplace=True)
    return df

if __name__ == '__main__':
    df = pd.read_csv('../data/transactions.csv')
    df_processed = preprocess_transactions(df)
    df_processed.to_csv('../data/transactions_processed.csv', index=False)
    print("Pré-processamento concluído e salvo em data/transactions_processed.csv")
