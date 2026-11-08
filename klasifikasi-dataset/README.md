# Klasifikasi Dataset: Biner, Multikelas, dan Multilabel

Repository ini berisi identifikasi dan praktik tiga jenis klasifikasi. Tiap jenis punya 3 dataset dari Kaggle: **1 yang benar** dan **2 pengecoh** (dataset yang sekilas mirip tetapi sebenarnya jenis lain).

## Struktur

```
.
├── Klasifikasi_Biner/
│   ├── README.md                      <- identifikasi: kenapa masuk / tidak masuk biner
│   ├── Telco_Customer_Churn/          <- Analisis_*.ipynb  (dataset benar, praktik lengkap)
│   ├── Wine_Quality/                  <- Identifikasi_*.ipynb (pengecoh)
│   └── Mobile_Price_Classification/   <- Identifikasi_*.ipynb (pengecoh)
├── Klasifikasi_Multikelas/
│   ├── README.md
│   ├── Dry_Bean/                      <- Analisis_*.ipynb
│   ├── Credit_Card_Fraud/             <- Identifikasi_*.ipynb
│   └── PubMed_MultiLabel/             <- Identifikasi_*.ipynb
├── Klasifikasi_Multilabel/
│   ├── README.md
│   ├── Jigsaw_Toxic_Comment/          <- Analisis_*.ipynb
│   ├── MNIST_Digit_Recognizer/        <- Identifikasi_*.ipynb
│   └── SMS_Spam_Collection/           <- Identifikasi_*.ipynb
├── requirements.txt
└── .gitignore
```

- `Analisis_*.ipynb`: praktik lengkap untuk dataset yang benar (Data Collecting, Data Loading, Cleaning, EDA, Processing, Splitting, Modelling dan Evaluasi).
- `Identifikasi_*.ipynb`: pembuktian lewat data kenapa dataset pengecoh bukan jenis klasifikasi di folder tersebut.

## Daftar Dataset

| Kategori | Dataset | Jenis sebenarnya | Status | Link |
|----------|---------|------------------|--------|------|
| Biner | Telco Customer Churn | Biner | ✅ Benar | https://www.kaggle.com/datasets/blastchar/telco-customer-churn |
| Biner | Wine Quality | Multikelas | ❌ Pengecoh | https://www.kaggle.com/datasets/ruthgn/wine-quality-data-set-red-white-wine |
| Biner | Mobile Price Classification | Multikelas | ❌ Pengecoh | https://www.kaggle.com/datasets/iabhishekofficial/mobile-price-classification |
| Multikelas | Dry Bean Dataset | Multikelas | ✅ Benar | https://www.kaggle.com/datasets/sansuthi/dry-bean-dataset |
| Multikelas | Credit Card Fraud Detection | Biner | ❌ Pengecoh | https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud |
| Multikelas | PubMed MultiLabel Text Classification | Multilabel | ❌ Pengecoh | https://www.kaggle.com/datasets/owaiskhan9654/pubmed-multilabel-text-classification |
| Multilabel | Jigsaw Toxic Comment Classification | Multilabel | ✅ Benar | https://www.kaggle.com/c/jigsaw-toxic-comment-classification-challenge/data |
| Multilabel | MNIST Digit Recognizer | Multikelas | ❌ Pengecoh | https://www.kaggle.com/c/digit-recognizer |
| Multilabel | SMS Spam Collection | Biner | ❌ Pengecoh | https://www.kaggle.com/datasets/uciml/sms-spam-collection-dataset |

## Cara Menjalankan

1. Install kebutuhan: `pip install -r requirements.txt`
2. Download dataset dari link Kaggle di atas, lalu taruh file CSV di **folder yang sama dengan notebook-nya**. File data tidak ikut di-push (lihat `.gitignore`).
3. Buka dengan JupyterLab: `jupyter lab`, lalu jalankan notebook dari atas ke bawah.
4. Kalau nama file atau nama kolom di Kaggle berbeda dari yang ada di notebook, sesuaikan variabel `DATA_PATH` dan `TARGET` di bagian Data Loading dan Identifikasi.
