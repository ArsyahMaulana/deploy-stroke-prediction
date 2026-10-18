# Deployment Model Prediksi Stroke

Model Gradient Boosting Classifier untuk memprediksi stroke, disajikan sebagai API dengan Flask.

## Dataset
Stroke Prediction Dataset (fedesoriano) di Kaggle: [tempel link halaman Kaggle]

## Cara menjalankan
1. pip install -r requirements.txt
2. python testing_deploy.py
3. Di terminal lain: curl.exe -X POST http://127.0.0.1:5000/predict -H "Content-Type: application/json" -d "@data.json"

## Isi repository
- testing_deploy.py : API Flask
- gbc_model.joblib : model terlatih
- data.json : contoh data masukan
- Latihan_Mandiri.ipynb : notebook praktikum