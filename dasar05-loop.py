#Prints out the numbers 0,1,2,3,4
for x in range(5):
    print(x)

#Prints out 3,4,5
for x in range(3, 6):
    print(x)

#Prints out 3,5,7
for x in range(3, 8, 2):
    print(x)

#Prints out 0,1,2,3,4
count = 0
while count < 5:
    print(count)
    count += 1  # This is the same as count = count + 1 

# Prints out 0,1,2,3,4

count = 0
while True:
    print(count)
    count += 1
    if count >= 5:
        break

# Prints out only odd numbers - 1,3,5,7,9
for x in range(10):
    # Check if x is even
    if x % 2 == 0:
        continue
    print(x)   


#list dan penambahan angka
angka = [20, 13, 55, 47, 11, 21, 40, 32]
for x in angka:
    print(x)

#range
#range(start, stop, step)
#jika range(2, 11) artinya masukkan index 2 hingga 11
#jika range(2, 11, 2) artinya masukkan index 2 hingga 11 step 2

#menambahkan nilai kedalam array
for i in range(3, 20, 2): 
    angka.append(i)    

print('List telah ditambahkan')
for x in angka:
    print(x)

#hanya menampilkan array tertentu
print('hanya menampilkan index ke 4: '+ str(angka[4]) )    