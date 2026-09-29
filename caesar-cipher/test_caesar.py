from caesar import encrypt, decrypt, brute_force


def test_contoh_slide():
    assert encrypt("awasi asterix dan", 3) == "dzdvl dvwhula gdq"
    assert encrypt("the quick brown fox jumps over the lazy dog", 18) == \
        "lzw imauc tjgof xgp bmehk gnwj lzw dsrq vgy"


def test_dekripsi():
    assert decrypt("DZDVL DVWHULA GDQ", 3) == "AWASI ASTERIX DAN"
    assert decrypt(encrypt("Halo PIN-ku: 123456", 10), 10) == "Halo PIN-ku: 123456"


def test_brute_force():
    hasil = dict(brute_force("XMZVH"))
    assert hasil[21] == "CREAM"
    assert dict(brute_force("VIVBQ SQBI SMBMUC LQ ICTI"))[8] == "NANTI KITA KETEMU DI AULA"


def test_rot13():
    assert encrypt("ROTATE", 13) == "EBGNGR"