buah = ['apel','anggur', 'jeruk','semangka']

#penambahan list
buah.append('pepaya')

#penambahan nilai pada index ke 2
buah.insert(2, 'pisang')

#semua
print(buah)

#satuan
print(buah[0])
print(buah[1])
print(buah[2])
print(buah[3])

#tampilkan berdasarkan range
print(buah[1:3])
print(buah[:2])
print(buah[2:])

#jumlah
print (len(buah))

#tampilkan
for x in buah:
  print(x)

#membuang nilai
buah.remove('jeruk')

#membuang dengan index
buah.pop(3)
buah.pop() #membuang nilai terakhir

#tampilkan
for i in range(len(buah)):
  print(buah[i])

