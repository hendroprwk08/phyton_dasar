#---array = tipe data yang memiliki banyak nilai
list = [10, 20, 30, 40]
print(list)

#---membaca data array
print(list[0])
print(list[1])
print(list[2])
print(list[3])
print('berapakah jumlah nilai array', len(list)) #length

#---menambahkan nilai kedalam array
list.append(50) #satu nilai
print('sudah ditambahkan 50', list)

list = list + [60, 70, 80, 90] #beberapa nilai
print('sudah ditambahkan 60, 70, 80 dan 90', list)

#---menghapus array?
list.remove(50) #menghapus berdasarkan nilai
print('hapus nilai 50', list)

list.pop(3) #menghapus berdasarkan index
print('hapus index ke-3', list)

list = list * 2 #memasukkan nilai sendiri 2 kali
print('mengulang nilai dirinya sendiri', list)

#---memilih nilai array 
print('index antara 2 hingga 3', list[2:3])
print('index dibawah 3', list[:3])
print('index ke 3 dari belakang', list[-3:])

#---array multidimensi ( 2 dimensi )
list_multi = [ [1, 2], [3, 4], [5, 6], [7, 8] ]
print(list_multi)

#bagaimana?
#1 2
#3 4
#5 6
#7 8

#menampilkan array
for i in range(len(list_multi)):
   for j in range(len(list_multi[i])):
      if j == 1:
         print (list_multi[i][j])
      else:
         print (list_multi[i][j], end =" ") #, end =" " agar print tidak melakukan "enter"






 






