# Identifikasi Dataset: Klasifikasi Multilabel

**Klasifikasi multilabel**: satu sampel boleh punya **lebih dari satu label aktif sekaligus** (kolom target lebih dari satu dan bisa aktif bersamaan).

| No | Dataset | Kolom target | Jenis sebenarnya | Hasil identifikasi | Notebook |
|----|---------|--------------|------------------|--------------------|----------|
| 1 | Jigsaw Toxic Comment Classification | 6 kolom label (`toxic`, `severe_toxic`, `obscene`, `threat`, `insult`, `identity_hate`) | Multilabel | **Klasifikasi multilabel** | `Jigsaw_Toxic_Comment/Analisis_Jigsaw_Toxic_Comment.ipynb` |
| 2 | MNIST Digit Recognizer | `label` (digit 0 sampai 9) | Multikelas | Bukan multilabel | `MNIST_Digit_Recognizer/Identifikasi_MNIST_Digit_Recognizer.ipynb` |
| 3 | SMS Spam Collection | `v1` (ham / spam) | Biner | Bukan multilabel | `SMS_Spam_Collection/Identifikasi_SMS_Spam.ipynb` |

Penjelasan lengkap "kenapa masuk / kenapa tidak" menyusul, mengikuti format di `../Klasifikasi_Biner/README.md`.
