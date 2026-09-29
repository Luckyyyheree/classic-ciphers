from vigenere import encrypt, decrypt


def test_contoh_1_slide():
    p = "kriptografiklasikdengancipheralfabetmajemuk"
    c = "VRUEBCTCARXSZNDIWSMBTLNOXXVRCAXUIPREMMYMAHV"
    assert encrypt(p, "lampion").upper() == c
    assert decrypt(c, "lampion") == p.upper()


def test_contoh_2_slide():
    p = "she sells sea shells by the seashore"
    assert encrypt(p, "key").upper() == "CLC CIJVW QOE QRIJVW ZI XFO WCKWFYVC"