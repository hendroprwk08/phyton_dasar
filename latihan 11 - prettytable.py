from prettytable import PrettyTable

#install module prettytable dahulu agar tampilan list menjadi lebih rapi
#kita tak dapat memodifikasi data pada pretty table (hanya menampilkan)
#masuk ke C:\Users\user\AppData\Local\Programs\Python\Python39\Scripts
#shift + klik kanan -> open powershell window here
#ketik pip install PTable
#selengkapnya https://pypi.org/project/prettytable/

tbl = PrettyTable()

#membuat tabel
tbl.field_names = ["Nama", "Usia"]

#isi tabel
tbl.add_row(["Joko", 12])
tbl.add_row(["Andika", 11])
tbl.add_row(["Yuni", 15])
tbl.add_row(["Ingrid", 12])

#hapus baris (index ke 1)
tbl.del_row(1) 

print(tbl)