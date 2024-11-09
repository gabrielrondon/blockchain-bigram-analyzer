bigram


python3 -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate

pip install -r requirements.txt


python3 src/collect_data.py
python3 src/preprocess_data.py
python3 src/bigram_model.py
python3 src/anomaly_detection.py
python3 src/predict_next_action.py
