arr = [10, 20, 30, 40, 50]
print("nilai awal:", arr)

#akses nilai array
print(arr[0])
print(arr[1])
print(arr[2])
print(arr[3])
print(arr[4])

#mendapatkan panjang array
print("panjang array", len(arr))

#menambahkan nilai array
arr.append(60)
print("tambah 60:", arr)

#membuang nilai array
arr.remove(20)
print("hapus 20:", arr)

#membuang array dengan pop
arr.pop(3) #3 adalah index array
print("hapus index ke-3:", arr)

#ubah nilai array
arr[1] = 70
print("ubah index ke 1 menjadi 70:", arr)

#menggabung nilai array (concat)
arr = arr + [ 80, 90, 100]
print("menambahkan nilai array 80, 90 dan 100:", arr)

#mengulang nilai array
arr = arr * 5
print("repeat 5x:", arr)

#menampilkan array dalam loop
for x in arr:
  print(x)

#memilih nilai array yang ingin ditampilkan
print('antara index ke 1 dan 3', arr[1:3]) 
print('dibawah index ke 3', arr[:3])  
print('index ke 3 dari belakang', arr[-3:])  
print('dibawah index ke 1 dari belakang', arr[:-1])  

#array multidimensi
arr_multi = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]
print('array multidimensi', arr_multi)

#menampilkan array
for i in range(len(arr_multi)):
   for j in range(len(arr_multi[i])):
      if j == 1:
         print (arr_multi[i][j])
      else:
        print (arr_multi[i][j], end =" ")

#bagaimana dengan array 3 dimensi?
#https://1.bp.blogspot.com/-3vljVVzojuA/XV7FeM21AeI/AAAAAAAAAzE/rLM3LJlgTxMK8mwKX156rPAXOdfMsVfKQCLcBGAs/s400/array-3-dimensi.png