#!/bin/bash
# 1) Buat repo KOSONG bernama "classic-ciphers" di GitHub
# 2) Ganti USERNAME di bawah, lalu jalankan: ./push.sh
USER=nanda628h
git init -q -b main
git add .
git commit -qm "Tugas cipher klasik: Caesar, Vigenere, Columnar Transposition"
git remote add origin https://github.com/$USER/classic-ciphers.git
git push -u origin main
