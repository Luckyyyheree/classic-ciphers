from columnar import encrypt, decrypt

P = "sistem dan teknologi informasi itb"


def test_kunci_angka():
    c = "SDNIAIAONSSNLFITTOOIEEGRTMKIMB"
    assert encrypt(P, 6) == c
    assert decrypt(c, 6) == "sistemdanteknologiinformasiitb"


def test_kata_kunci_tombak():
    c = "EEGRTTTOOIMKIMBSNLFIIAONSSDNIA"
    assert encrypt(P, "TOMBAK") == c
    assert decrypt(c, "TOMBAK") == "sistemdanteknologiinformasiitb"