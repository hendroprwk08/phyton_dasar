usia = 43

if usia > 25:
    print('Pemuda dan Dewasa') 
else:
    print('Anak')

#masuk ke bahasan elif ( else if )
#DepKesRI menggolongkan usia dengan pembagian seperti berikut:
#https://yhantiaritra.wordpress.com/2015/06/03/kategori-umur-menurut-depkes/

if usia >= 65:
    print('manula')
elif usia >= 56 and usia < 65:
    print('lansia akhir')
elif usia >= 46 and usia < 56:
    print('lansia awal')
elif usia >= 36 and usia < 46:
    print('dewasa akhir')
elif usia >= 26 and usia < 36:
    print('dewasa awal')
elif usia >= 17 and usia < 26:
    print('remaja akhir')
elif usia >= 12 and usia < 17:
    print('remaja awal')
elif usia >= 6 and usia < 12:
    print('kanak-kanak')
else:
    print('balita')

     