"""Caesar Cipher - IF4020 Kriptografi.
Enkripsi: c = (p + k) mod 26 | Dekripsi: p = (c - k) mod 26
"""


def _shift(text, k):
    out = []
    for ch in text:
        if ch.isalpha() and ch.isascii():
            start = ord('A') if ch.isupper() else ord('a')
            out.append(chr((ord(ch) - start + k) % 26 + start))
        else:
            out.append(ch)  # bukan huruf: dibiarkan
    return "".join(out)


def encrypt(plainteks, k):
    return _shift(plainteks, k)


def decrypt(cipherteks, k):
    return _shift(cipherteks, -k)


def brute_force(cipherteks):
    """Exhaustive key search: coba semua 26 kunci."""
    return [(k, decrypt(cipherteks, k)) for k in range(26)]


def main():
    while True:
        print("\n=== CAESAR CIPHER ===")
        print("1. Enkripsi\n2. Dekripsi\n3. Brute force (tanpa kunci)\n4. Keluar")
        pil = input("Pilih menu: ").strip()
        if pil == "1":
            teks = input("Plainteks : ")
            k = int(input("Kunci (0-25): "))
            print("Cipherteks:", encrypt(teks, k).upper())
        elif pil == "2":
            teks = input("Cipherteks: ")
            k = int(input("Kunci (0-25): "))
            print("Plainteks :", decrypt(teks, k).lower())
        elif pil == "3":
            teks = input("Cipherteks: ")
            for k, hasil in brute_force(teks):
                print(f"k={k:2d}  {hasil.lower()}")
        elif pil == "4":
            break
        else:
            print("Menu tidak valid.")


if __name__ == "__main__":
    main()