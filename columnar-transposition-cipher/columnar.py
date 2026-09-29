"""Columnar Transposition Cipher - IF4020 Kriptografi.
Plainteks ditulis per baris dengan lebar = panjang kunci, cipherteks dibaca
per kolom. Kunci berupa angka (lebar kolom) ATAU kata kunci (mis. TOMBAK)
yang urutan alfabetnya menentukan urutan pembacaan kolom.
"""
import math


def _order(key):
    """Urutan indeks kolom sesuai peringkat alfabet kata kunci."""
    if isinstance(key, int):
        return list(range(key))
    key = key.upper()
    return sorted(range(len(key)), key=lambda i: (key[i], i))


def encrypt(plainteks, key, pad="X"):
    teks = "".join(c for c in plainteks if c.isalpha()).upper()  # buang spasi
    order = _order(key)
    n = len(order)
    teks += pad * (-len(teks) % n)
    rows = [teks[i:i + n] for i in range(0, len(teks), n)]
    return "".join(row[col] for col in order for row in rows)


def decrypt(cipherteks, key):
    c = cipherteks.replace(" ", "").upper()
    order = _order(key)
    n = len(order)
    if len(c) % n:
        raise ValueError("Panjang cipherteks harus kelipatan panjang kunci.")
    nrows = len(c) // n
    grid = [[""] * n for _ in range(nrows)]
    pos = 0
    for col in order:
        for r in range(nrows):
            grid[r][col] = c[pos]
            pos += 1
    return "".join("".join(row) for row in grid).lower()


def main():
    while True:
        print("\n=== COLUMNAR TRANSPOSITION CIPHER ===")
        print("1. Enkripsi\n2. Dekripsi\n3. Keluar")
        pil = input("Pilih menu: ").strip()
        if pil in ("1", "2"):
            teks = input("Teks : ")
            k = input("Kunci (angka atau kata kunci, mis. 6 / TOMBAK): ").strip()
            key = int(k) if k.isdigit() else k
            try:
                print("Hasil:", encrypt(teks, key) if pil == "1" else decrypt(teks, key))
            except ValueError as e:
                print("Error:", e)
        elif pil == "3":
            break
        else:
            print("Menu tidak valid.")


if __name__ == "__main__":
    main()