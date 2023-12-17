kode = input()
pesan = input()

panjang_kode = len(kode)
panjang_pesan = len(pesan)

if panjang_kode != panjang_pesan:
    print("Panjang kalimat berbeda, pesan palsu")
    exit()

bintang_count = 0
pagar_count = 0
hasil_pesan = ""

for i in range(panjang_kode):
    if kode[i] == ' ' and pesan[i] == ' ':
        hasil_pesan += ' '
    elif kode[i] == pesan[i]:
        hasil_pesan += '*'
        bintang_count += 1
    else:
        hasil_pesan += '#'
        pagar_count += 1

print(hasil_pesan)
print('* =', bintang_count)
print('# =', pagar_count)

if bintang_count >= pagar_count:
    print("Pesan asli")
else:
    print("Pesan palsu")
