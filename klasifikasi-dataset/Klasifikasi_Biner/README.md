# Identifikasi Dataset: Klasifikasi Biner

## Definisi

**Klasifikasi biner** adalah tugas klasifikasi dengan **tepat 2 kelas** pada kolom target, dan setiap baris data hanya memiliki **1 label** dari 2 kelas tersebut (contoh: Yes/No, 0/1, spam/bukan spam).

Ciri yang dicek pada setiap dataset:

1. Jumlah kelas pada kolom target harus **2**.
2. Setiap sampel hanya punya **satu** label (bukan beberapa label sekaligus).
3. Dua kelas bersifat **saling lepas** (sampel tidak bisa masuk keduanya).

## Dataset yang Diidentifikasi

| No | Dataset | Kolom target | Jumlah kelas | Hasil identifikasi |
|----|---------|--------------|--------------|--------------------|
| 1 | Telco Customer Churn | `Churn` | 2 (Yes, No) | **Klasifikasi biner** |
| 2 | Wine Quality | `quality` | 7 nilai (skor 3 sampai 9) | Bukan biner (multikelas) |
| 3 | Mobile Price Classification | `price_range` | 4 (0, 1, 2, 3) | Bukan biner (multikelas) |

---

## 1. Telco Customer Churn (benar, klasifikasi biner)

- **Sumber:** https://www.kaggle.com/datasets/blastchar/telco-customer-churn
- **Ukuran:** 7.043 baris, 21 kolom (19 fitur, 1 target, 1 ID pelanggan).
- **Kolom target:** `Churn`, berisi `Yes` (pelanggan berhenti berlangganan) atau `No` (pelanggan bertahan).

**Kenapa masuk klasifikasi biner:**

- Kolom target hanya punya **2 nilai**, yaitu `Yes` dan `No`.
- Setiap pelanggan hanya punya **1 label**: berhenti atau tidak berhenti.
- Dua kelas saling lepas, karena seorang pelanggan tidak mungkin berhenti dan bertahan sekaligus.
- Tidak ada rekayasa target. Dua kelas ini sudah bawaan dataset aslinya.

## 2. Wine Quality (bukan klasifikasi biner)

- **Sumber:** https://www.kaggle.com/datasets/ruthgn/wine-quality-data-set-red-white-wine
- **Ukuran:** 6.497 baris (1.599 red dan 4.898 white).
- **Kolom target:** `quality`, skor kualitas wine dari penilaian ahli.

**Kenapa tidak masuk klasifikasi biner:**

- Kolom target berisi **lebih dari 2 nilai** (skor 3, 4, 5, 6, 7, 8, 9), sehingga ada 7 kelas.
- Skor ini berurutan (ordinal), jadi jenisnya **multikelas**.
- Dataset ini sering dijadikan biner dengan threshold, misalnya `quality >= 6` dianggap wine bagus. Itu hasil **rekayasa target** oleh peneliti. Data aslinya tetap multikelas.

## 3. Mobile Price Classification (bukan klasifikasi biner)

- **Sumber:** https://www.kaggle.com/datasets/iabhishekofficial/mobile-price-classification
- **Ukuran:** 2.000 baris (`train.csv`), 21 kolom.
- **Kolom target:** `price_range`, kategori harga HP.

**Kenapa tidak masuk klasifikasi biner:**

- Kolom target punya **4 kelas**: 0 (murah), 1 (menengah), 2 (mahal), 3 (sangat mahal).
- Tiap kelas berisi 500 baris, jadi dataset ini seimbang di 4 kelas.
- Tiap HP hanya punya 1 label, tetapi pilihan labelnya lebih dari 2, sehingga jenisnya **multikelas**.

---

## Cara Verifikasi dengan Python

```python
import pandas as pd

telco = pd.read_csv("WA_Fn-UseC_-Telco-Customer-Churn.csv")
wine = pd.read_csv("winequality.csv")        # sesuaikan nama file hasil download
mobile = pd.read_csv("train.csv")            # train.csv dari Mobile Price Classification

print("Telco  :", telco["Churn"].nunique(), telco["Churn"].unique())
print("Wine   :", wine["quality"].nunique(), sorted(wine["quality"].unique()))
print("Mobile :", mobile["price_range"].nunique(), sorted(mobile["price_range"].unique()))
```

Jika jumlah nilai unik pada kolom target sama dengan 2, dataset tersebut adalah klasifikasi biner. Jika lebih dari 2 dan tiap baris hanya punya satu label, dataset tersebut adalah multikelas.

## Kesimpulan

| Dataset | Jumlah kelas target | Jenis |
|---------|---------------------|-------|
| Telco Customer Churn | 2 | Biner |
| Wine Quality | 7 | Multikelas |
| Mobile Price Classification | 4 | Multikelas |

Dari tiga dataset, hanya **Telco Customer Churn** yang termasuk klasifikasi biner.
