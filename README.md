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

## Evaluasi Model

Evaluasi dilakukan pada data uji (2.044 data, rasio 60:40).

### Metrik klasifikasi

| Model | Accuracy | Precision | Recall | F1-Score |
|---|---|---|---|---|
| Logistic Regression | 0,9511 | 0,0000 | 0,0000 | 0,0000 |
| Decision Tree | 0,8982 | 0,1029 | 0,1400 | 0,1186 |
| Gradient Boosting Classifier | 0,9486 | 0,1429 | 0,0100 | 0,0187 |

### Metrik regresi (MAE, MSE, R²)

| Model | MAE | MSE | R² | Jarak R² ke 1 |
|---|---|---|---|---|
| Logistic Regression | 0,0489 | 0,0489 | -0,0514 | 1,0514 |
| Decision Tree | 0,1018 | 0,1018 | -1,1870 | 2,1870 |
| Gradient Boosting Classifier | 0,0514 | 0,0514 | -0,1040 | 1,1040 |

### Analisis

- Nilai R² ketiga model negatif, sehingga **jauh dari 1**. Artinya model tidak lebih baik daripada menebak rata-rata target.
- Logistic Regression memiliki R² paling mendekati 1 (-0,0514), sedangkan Decision Tree paling jauh (-1,1870).
- MAE dan MSE bernilai sama karena target hanya berisi 0 dan 1.
- Metrik regresi digunakan sesuai ketentuan tugas, namun kurang cocok untuk klasifikasi. Untuk data tidak seimbang seperti ini (kasus stroke sekitar 5%), Recall dan F1-Score lebih tepat. Menurut metrik tersebut, Decision Tree adalah yang terbaik dalam mendeteksi stroke.