count = 0

while count < 5:
   print(count)
   count += 1 #sama dengan "count = count + 1"

#while - break [jika count >= 5 maka hentikan looping]
while True:
   print(count)
   count += 1 #increment
   if (count >= 5):
      break

#studi kasus: cetak nomer ganjil
for x in range(10):
   #cek ganjilnya
   if x % 2 == 0: #modulus (sisa bagi)
      continue
   print(x) 

"""
latihan
Buatlah program untuk menampilkan bilangan 
yang memiliki kelipatan 3, jika sudah ditemukan sebanyak 
variable "sampai", maka berhenti proses loopingnya.
Gunakan while atau for dan break 
"""
mulai = input('Mulai dari: ')
sampai = input('Sampai: ') 
temuan = input('Jumlah temuan? ')