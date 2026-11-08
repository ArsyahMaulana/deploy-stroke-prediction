# Identifikasi Dataset: Klasifikasi Multilabel

## Definisi

**Klasifikasi multilabel** adalah tugas klasifikasi di mana satu sampel boleh memiliki **lebih dari satu label aktif sekaligus**. Targetnya biasanya berupa beberapa kolom label biner (contoh: satu komentar bisa sekaligus *toxic*, *obscene*, dan *insult*).

Ciri yang dicek pada setiap dataset:

1. Target terdiri dari **lebih dari satu kolom label**.
2. Label **tidak saling lepas**: satu sampel bisa aktif di beberapa label sekaligus.
3. Ada sampel dengan **lebih dari 1 label aktif** (sampel juga boleh tidak punya label sama sekali).

## Dataset yang Diidentifikasi

| No | Dataset | Kolom target | Bentuk target | Hasil identifikasi |
|----|---------|--------------|---------------|--------------------|
| 1 | Jigsaw Toxic Comment Classification | 6 kolom label | label biner, bisa aktif bersamaan | **Klasifikasi multilabel** |
| 2 | MNIST Digit Recognizer | `label` | 1 kolom, 10 kelas (digit 0 sampai 9) | Bukan multilabel (multikelas) |
| 3 | SMS Spam Collection | `v1` | 1 kolom, 2 kelas (ham, spam) | Bukan multilabel (biner) |

---

## 1. Jigsaw Toxic Comment Classification (benar, klasifikasi multilabel)

- **Sumber:** https://www.kaggle.com/c/jigsaw-toxic-comment-classification-challenge/data (halaman kompetisi, perlu login dan *Join Competition*).
- **Ukuran:** 159.571 komentar, 8 kolom (`id`, `comment_text`, dan 6 kolom label).
- **Kolom target:** `toxic`, `severe_toxic`, `obscene`, `threat`, `insult`, `identity_hate`. Tiap kolom bernilai 0 atau 1.

Banyak komentar menurut jumlah label yang aktif:

| Jumlah label aktif | Jumlah komentar |
|--------------------|-----------------|
| 0 | 143.346 |
| 1 | 6.360 |
| 2 | 3.480 |
| 3 | 4.209 |
| 4 | 1.760 |
| 5 | 385 |
| 6 | 31 |

**Kenapa masuk klasifikasi multilabel:**

- Target terdiri dari **6 kolom label**, bukan satu kolom.
- Label **bisa aktif bersamaan**: 6,18% komentar punya lebih dari satu label aktif, bahkan 31 komentar aktif di keenam label sekaligus.
- Label sering muncul berpasangan. Pada sampel 20.000 komentar, `toxic` dan `obscene` muncul bersamaan di 999 komentar, dan `toxic` dengan `insult` di 919 komentar.
- Mayoritas komentar (143.346, sekitar 90%) tidak punya label aktif sama sekali. Ini juga hal yang wajar pada multilabel, tetapi tidak mungkin terjadi pada multikelas biasa.

## 2. MNIST Digit Recognizer (bukan klasifikasi multilabel)

- **Sumber:** https://www.kaggle.com/c/digit-recognizer (halaman kompetisi, file yang dipakai `train.csv`).
- **Ukuran:** 42.000 baris, 785 kolom (1 kolom `label` dan 784 kolom piksel gambar 28 x 28).
- **Kolom target:** `label`, berisi digit 0 sampai 9.

**Kenapa tidak masuk klasifikasi multilabel:**

- Targetnya **satu kolom** (`label`) yang berisi **satu nilai** per gambar.
- Ada **10 kelas** yang saling lepas: satu gambar hanya menunjukkan satu digit, tidak mungkin sekaligus angka 3 dan 8.
- Karena itu jenisnya **multikelas**.
- Banyaknya kolom (785) bisa menimbulkan kesan "banyak label". Padahal 784 kolom itu adalah **fitur** (nilai piksel), bukan target.

## 3. SMS Spam Collection (bukan klasifikasi multilabel)

- **Sumber:** https://www.kaggle.com/datasets/uciml/sms-spam-collection-dataset
- **Ukuran:** sekitar 5,5 ribu SMS. File `spam.csv` berisi kolom `v1` (label), `v2` (teks SMS), dan beberapa kolom tambahan tanpa nama yang hampir kosong.
- **Kolom target:** `v1`, berisi `ham` (SMS normal) atau `spam`. Mayoritas data berlabel `ham`.

**Kenapa tidak masuk klasifikasi multilabel:**

- Hanya ada **satu kolom target** dengan **2 nilai** (`ham` dan `spam`), jadi jenisnya **biner**.
- Satu SMS tidak mungkin `ham` dan `spam` sekaligus, jadi tidak ada sampel dengan lebih dari satu label aktif.
- Dataset ini berupa teks seperti Jigsaw, tetapi perbedaannya ada di target: Jigsaw punya 6 kolom label yang bisa aktif bersamaan, sedangkan SMS Spam hanya satu label biner.

---

## Cara Verifikasi dengan Python

```python
import pandas as pd

jigsaw = pd.read_csv("train.csv")           # train.csv milik Jigsaw (folder Jigsaw_Toxic_Comment)
LABELS = ["toxic", "severe_toxic", "obscene", "threat", "insult", "identity_hate"]
n_aktif = jigsaw[LABELS].sum(axis=1)
print("Jigsaw:", len(LABELS), "kolom label,",
      f"{(n_aktif > 1).mean() * 100:.2f}% komentar punya lebih dari 1 label aktif")

mnist = pd.read_csv("train.csv")            # train.csv milik Digit Recognizer (folder MNIST_Digit_Recognizer)
print("MNIST :", mnist["label"].nunique(), "kelas, 1 kolom label")

sms = pd.read_csv("spam.csv", encoding="latin-1")
print("SMS   :", sms.iloc[:, 0].nunique(), "kelas", sms.iloc[:, 0].unique().tolist())
```

Aturan membacanya:

- Banyak kolom label dan ada baris dengan **lebih dari 1 label aktif**: **multilabel**.
- Satu kolom target dengan **lebih dari 2** kelas, satu label per baris: **multikelas**.
- Satu kolom target dengan **2** kelas: **biner**.

Karena nama file `train.csv` dipakai oleh dua dataset berbeda (Jigsaw dan MNIST), jalankan masing-masing potongan kode itu di folder yang sesuai.

## Kesimpulan

| Dataset | Bentuk target | Jenis |
|---------|---------------|-------|
| Jigsaw Toxic Comment Classification | 6 kolom label, bisa aktif bersamaan | Multilabel |
| MNIST Digit Recognizer | 1 kolom, 10 kelas | Multikelas |
| SMS Spam Collection | 1 kolom, 2 kelas | Biner |

Dari tiga dataset, hanya **Jigsaw Toxic Comment Classification** yang termasuk klasifikasi multilabel.