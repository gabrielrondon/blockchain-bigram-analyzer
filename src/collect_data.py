# src/collect_data.py

import os
from web3 import Web3
import pandas as pd
from dotenv import load_dotenv
from etherscan import Etherscan

load_dotenv()

INFURA_PROJECT_ID = os.getenv('INFURA_PROJECT_ID')
INFURA_PROJECT_SECRET = os.getenv('INFURA_PROJECT_SECRET')  # Se aplicável
ETHERSCAN_API_KEY = os.getenv('ETHERSCAN_API_KEY')

# Configurar conexão com o Infura
if INFURA_PROJECT_SECRET:
    infura_url = f'https://:{INFURA_PROJECT_SECRET}@mainnet.infura.io/v3/{INFURA_PROJECT_ID}'
else:
    infura_url = f'https://mainnet.infura.io/v3/{INFURA_PROJECT_ID}'

w3 = Web3(Web3.HTTPProvider(infura_url))

# Instanciar o cliente do Etherscan
eth = Etherscan(ETHERSCAN_API_KEY)

def collect_transactions(start_block, end_block):
    transactions = []

    for block_number in range(start_block, end_block):
        block = w3.eth.get_block(block_number, full_transactions=True)
        for tx in block['transactions']:
            # Obter informações adicionais usando a API do Etherscan, se necessário
            # Exemplo: obter o status da transação
            tx_receipt = w3.eth.get_transaction_receipt(tx['hash'])
            tx_status = tx_receipt['status']
            
            transactions.append({
                'from': tx['from'],
                'to': tx['to'],
                'value': tx['value'],
                'hash': tx['hash'].hex(),
                'blockNumber': tx['blockNumber'],
                'status': tx_status
            })
    df = pd.DataFrame(transactions)
    return df

if __name__ == '__main__':
    start_block = 10000000
    end_block = 10000010
    df_transactions = collect_transactions(start_block, end_block)
    df_transactions.to_csv('data/transactions.csv', index=False)
    print("Coleta de dados concluída e salva em data/transactions.csv")
