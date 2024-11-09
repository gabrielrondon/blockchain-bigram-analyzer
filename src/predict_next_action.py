# src/predict_next_action.py

import pickle

def predict_next_action(current_action, bigram_probabilities):
    candidates = {bg[1]: prob for bg, prob in bigram_probabilities.items() if bg[0] == current_action}
    if candidates:
        next_action = max(candidates, key=candidates.get)
        return next_action
    else:
        return None

if __name__ == '__main__':
    # Carregar o modelo de bigramas
    with open('../data/bigram_model.pkl', 'rb') as f:
        bigram_probabilities = pickle.load(f)

    # Exemplo de uso
    current_action = 'Contract Interaction'
    next_action = predict_next_action(current_action, bigram_probabilities)
    if next_action:
        print(f"Com base em sua ação atual, você pode querer: {next_action}")
    else:
        print("Não há sugestões disponíveis para a ação atual.")
