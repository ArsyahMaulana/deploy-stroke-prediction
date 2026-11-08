# Identifikasi Dataset: Klasifikasi Multikelas

## Definisi

**Klasifikasi multikelas** adalah tugas klasifikasi dengan **lebih dari 2 kelas** pada kolom target, dan setiap baris data hanya memiliki **1 label** dari kelas-kelas tersebut (contoh: jenis kacang, digit 0 sampai 9, kategori harga).

Ciri yang dicek pada setiap dataset:

1. Jumlah kelas pada kolom target harus **lebih dari 2**.
2. Setiap sampel hanya punya **satu** label (bukan beberapa label sekaligus).
3. Kelas-kelasnya **saling lepas** (sampel tidak bisa masuk dua kelas sekaligus).

## Dataset yang Diidentifikasi

| No | Dataset | Kolom target | Jumlah kelas | Hasil identifikasi |
|----|---------|--------------|--------------|--------------------|
| 1 | Dry Bean Dataset | `Class` | 7 | **Klasifikasi multikelas** |
| 2 | Credit Card Fraud Detection | `Class` | 2 (0, 1) | Bukan multikelas (biner) |
| 3 | PubMed MultiLabel Text Classification | beberapa kolom label (A, B, C, ...) | banyak label, bisa aktif bersamaan | Bukan multikelas (multilabel) |

---

## 1. Dry Bean Dataset (benar, klasifikasi multikelas)

- **Sumber:** https://www.kaggle.com/datasets/sansuthi/dry-bean-dataset
- **Ukuran:** 13.611 baris, 17 kolom (16 fitur bentuk dan ukuran biji, 1 target). Setelah 68 baris duplikat dibuang, tersisa 13.543 baris.
- **Kolom target:** `Class`, berisi jenis kacang kering.

| Kelas | Jumlah baris |
|-------|--------------|
| DERMASON | 3.546 |
| SIRA | 2.636 |
| SEKER | 2.027 |
| HOROZ | 1.928 |
| CALI | 1.630 |
| BARBUNYA | 1.322 |
| BOMBAY | 522 |

**Kenapa masuk klasifikasi multikelas:**

- Kolom target punya **7 kelas**, jadi lebih dari 2.
- Setiap biji kacang hanya punya **1 jenis**, sehingga satu baris tidak mungkin berlabel DERMASON dan SIRA sekaligus.
- Kelas-kelasnya saling lepas dan hanya ada **satu kolom target**.
- Jumlah kelas tidak seimbang (BOMBAY hanya 522 baris, DERMASON 3.546 baris), tetapi ketidakseimbangan tidak mengubah jenis klasifikasinya.

## 2. Credit Card Fraud Detection (bukan klasifikasi multikelas)

- **Sumber:** https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud
- **Ukuran:** sekitar 284.807 transaksi, 31 kolom (`Time`, `V1` sampai `V28`, `Amount`, `Class`).
- **Kolom target:** `Class`, berisi `0` (transaksi normal) atau `1` (fraud). Fraud hanya sekitar 0,17% dari seluruh transaksi.

**Kenapa tidak masuk klasifikasi multikelas:**

- Kolom target hanya punya **2 nilai** (`0` dan `1`), jadi jenisnya **biner**, bukan multikelas.
- Dataset ini sangat tidak seimbang, tetapi jumlah kelasnya tetap dua.
- Banyaknya kolom `V1` sampai `V28` bisa menimbulkan kesan "banyak kelas". Kolom-kolom itu adalah **fitur** (hasil transformasi PCA), bukan target.

## 3. PubMed MultiLabel Text Classification (bukan klasifikasi multikelas)

- **Sumber:** https://www.kaggle.com/datasets/owaiskhan9654/pubmed-multilabel-text-classification
- **Ukuran:** sekitar 50 ribu artikel PubMed.
- **Kolom target:** beberapa kolom label biner berhuruf tunggal (A, B, C, dan seterusnya) yang mewakili kategori MeSH. Jumlah pastinya dicek di notebook `Identifikasi_PubMed_MultiLabel.ipynb`.

**Kenapa tidak masuk klasifikasi multikelas:**

- Satu artikel bisa memiliki **beberapa label aktif sekaligus** (misalnya termasuk kategori A dan C dan E). Pada multikelas, satu baris hanya boleh punya satu kelas.
- Targetnya berupa **banyak kolom label** yang bisa bernilai 1 bersamaan, bukan satu kolom berisi satu kelas.
- Dataset ini terlihat seperti multikelas karena labelnya berupa kategori, tetapi sifat label yang boleh aktif bersamaan membuatnya **multilabel**.

---

## Cara Verifikasi dengan Python

```python
import pandas as pd

bean = pd.read_csv("Dry_Bean.csv")          # sesuaikan nama file hasil download
card = pd.read_csv("creditcard.csv")
pub = pd.read_csv("pubmed.csv")             # sesuaikan nama file hasil download

print("Dry Bean   :", bean["Class"].nunique(), "kelas")
print("Credit Card:", card["Class"].nunique(), "kelas", sorted(card["Class"].unique()))

kolom_label = [c for c in pub.columns if len(str(c)) == 1 and str(c).isupper()]
n_aktif = pub[kolom_label].sum(axis=1)
print("PubMed     :", len(kolom_label), "kolom label,",
      f"{(n_aktif > 1).mean() * 100:.1f}% artikel punya lebih dari 1 label aktif")
```

Aturan membacanya:

- Satu kolom target dengan jumlah nilai unik **lebih dari 2** dan satu label per baris: **multikelas**.
- Satu kolom target dengan **2** nilai unik: **biner**.
- Banyak kolom label dan ada baris dengan **lebih dari 1 label aktif**: **multilabel**.

## Kesimpulan

| Dataset | Bentuk target | Jenis |
|---------|---------------|-------|
| Dry Bean Dataset | 1 kolom, 7 kelas | Multikelas |
| Credit Card Fraud Detection | 1 kolom, 2 kelas | Biner |
| PubMed MultiLabel Text Classification | banyak kolom label, bisa aktif bersamaan | Multilabel |

Dari tiga dataset, hanya **Dry Bean Dataset** yang termasuk klasifikasi multikelas.