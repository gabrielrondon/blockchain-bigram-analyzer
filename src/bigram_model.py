# src/bigram_model.py

import pandas as pd
from nltk import bigrams
from collections import Counter
import nltk

nltk.download('punkt')

def build_bigram_model(tx_types_sequence):
    # Criar bigramas
    tx_bigrams = list(bigrams(tx_types_sequence))

    # Contar frequências
    bigram_counts = Counter(tx_bigrams)
    unigram_counts = Counter(tx_types_sequence)

    # Calcular probabilidades
    bigram_probabilities = {}
    for bigram in bigram_counts:
        bigram_probabilities[bigram] = bigram_counts[bigram] / unigram_counts[bigram[0]]

    return bigram_probabilities

if __name__ == '__main__':
    df = pd.read_csv('../data/transactions_processed.csv')
    tx_types_sequence = df['tx_type'].tolist()
    bigram_probabilities = build_bigram_model(tx_types_sequence)

    # Salvar o modelo
    import pickle
    with open('../data/bigram_model.pkl', 'wb') as f:
        pickle.dump(bigram_probabilities, f)
    print("Modelo de bigramas salvo em data/bigram_model.pkl")
