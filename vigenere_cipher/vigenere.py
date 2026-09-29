"""Vigenere Cipher (cipher abjad-majemuk) - IF4020 Kriptografi.
Enkripsi: c_i = (p_i + k_i) mod 26 | Dekripsi: p_i = (c_i - k_i) mod 26
Kunci diulang; hanya huruf yang mengonsumsi kunci, karakter lain dibiarkan.
"""


def _process(text, key, sign):
    key = [ord(c) - 65 for c in key.upper() if c.isalpha() and c.isascii()]
    if not key:
        raise ValueError("Kunci harus berisi minimal satu huruf.")
    out, i = [], 0
    for ch in text:
        if ch.isalpha() and ch.isascii():
            start = ord('A') if ch.isupper() else ord('a')
            out.append(chr((ord(ch) - start + sign * key[i % len(key)]) % 26 + start))
            i += 1
        else:
            out.append(ch)
    return "".join(out)


def encrypt(plainteks, key):
    return _process(plainteks, key, +1)


def decrypt(cipherteks, key):
    return _process(cipherteks, key, -1)


def main():
    while True:
        print("\n=== VIGENERE CIPHER ===")
        print("1. Enkripsi\n2. Dekripsi\n3. Keluar")
        pil = input("Pilih menu: ").strip()
        if pil == "1":
            teks = input("Plainteks : ")
            key = input("Kunci     : ")
            print("Cipherteks:", encrypt(teks, key).upper())
        elif pil == "2":
            teks = input("Cipherteks: ")
            key = input("Kunci      : ")
            print("Plainteks :", decrypt(teks, key).lower())
        elif pil == "3":
            break
        else:
            print("Menu tidak valid.")


if __name__ == "__main__":
    main()