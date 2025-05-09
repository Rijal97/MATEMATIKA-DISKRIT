print("TABEL KEBENARAN KONJUNGSI")
print("-------------------------")
print("P\t|Q\t|P AND Q")
print("-------------------------")

for P in [True,False]:
    for Q in [True,False]:
        Konjungsi = P and Q
        print(f"{P}\t{Q}\t{Konjungsi}")
        
print("TABEL KEBENARAN DISJUNGSI")
print("-------------------------")
print("P\t|Q\t|P OR Q")
print("-------------------------")

for P in [True,False]:
    for Q in [True,False]:
        Disjungsi = P or Q
        print(f"{P}\t{Q}\t{Disjungsi}")
        
print("TABEL KEBENARAN NEGASI")
print("----------------------")
print("P\t|NOT P")
print("----------------------")

for P in [True,False]:
    Negasi = not P
    print(f"{P}\t{Negasi}")
