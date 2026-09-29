# Classic Ciphers

Tugas mata kuliah IF4020 Kriptografi (Ragam Cipher Klasik, Bagian 1).
Berisi 3 aplikasi cipher klasik dalam Python:

| Folder | Jenis | Cara menjalankan |
|---|---|---|
| `caesar-cipher/` | Substitusi (abjad-tunggal), plus brute force | `python caesar-cipher/caesar.py` |
| `vigenere-cipher/` | Substitusi (abjad-majemuk) | `python vigenere-cipher/vigenere.py` |
| `columnar-transposition-cipher/` | Transposisi (kunci angka / kata kunci) | `python columnar-transposition-cipher/columnar.py` |

## Tes
Setiap folder punya tes berdasarkan contoh di materi kuliah:
```bash
pip install pytest
cd caesar-cipher && pytest
cd ../vigenere-cipher && pytest
cd ../columnar-transposition-cipher && pytest
```
