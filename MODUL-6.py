def desimal_ke_biner(n):
    return bin(n)[2:] 

def desimal_ke_oktal(n):
    return oct(n)[2:]

def desimal_ke_heksa(n):
    return hex(n)[2:].upper()

def biner_ke_desimal(b):
    return int(b, 2)

def oktal_ke_desimal(o):
    return int(o, 8)

def heksa_ke_desimal(h):
    return int(h, 16)

angka = 179 

print(f"Desimal: {angka}")
print(f"Biner: {desimal_ke_biner(angka)}")
print(f"Oktal: {desimal_ke_oktal(angka)}")
print(f"Heksadesimal: {desimal_ke_heksa(angka)}")

biner = "10110011"
oktal = "263"
heksa = "B3"

print(f"Biner ke Desimal: {biner_ke_desimal(biner)}")
print(f"Oktal ke Desimal: {oktal_ke_desimal(oktal)}")
print(f"Heksadesimal ke Desimal: {heksa_ke_desimal(heksa)}")
