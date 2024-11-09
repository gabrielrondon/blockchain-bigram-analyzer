# src/anomaly_detection.py

import pickle

def detect_anomalies(new_sequence, bigram_probabilities, threshold=0.01):
    from nltk import bigrams
    new_bigrams = list(bigrams(new_sequence))
    anomalies = []
    for bg in new_bigrams:
        prob = bigram_probabilities.get(bg, 0)
        if prob < threshold:
            anomalies.append({'bigram': bg, 'probability': prob})
    return anomalies

if __name__ == '__main__':
    # Carregar o modelo de bigramas
    with open('../data/bigram_model.pkl', 'rb') as f:
        bigram_probabilities = pickle.load(f)

    # Exemplo de nova sequência
    new_sequence = ['Value Transfer', 'Contract Interaction', 'Contract Creation', 'Value Transfer']
    anomalies = detect_anomalies(new_sequence, bigram_probabilities)

    if anomalies:
        print("Bigramas anômalos detectados:")
        for anomaly in anomalies:
            print(f"Bigrama: {anomaly['bigram']}, Probabilidade: {anomaly['probability']}")
    else:
        print("Nenhuma anomalia detectada.")
