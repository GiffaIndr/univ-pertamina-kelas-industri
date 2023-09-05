# harga_barang = 3999
# uang = 2300 
# if (harga_barang >  uang): 
#     print('uang kamu kurang')
# else: 
#     print('uang cukup') 

# for i in range(angka):
#     if(i % 4 == 0): 
#         print("dor")
#     else: 
#         print(i)

# angka = 28
# if(angka % 4 == 0): 
#     print('dor!')
# elif(angka%7 == 0):
#     print('der!')
# else: 
#     print(angka)

# price = 25000
# kondisi = "baik"

# if(price >= 25000):
#     print("uang Cukup")
#     if(kondisi == "baik"):
#         print('uang laku' )
#     else:
#         print('uang tidak laku')
# else: 
#     print('uang kurang')
    

# j = 0
# while j < 11: 
#     print(f"{j} apa ")
#     j = j + 1

# for i in range(9, -1, -1):
#     print(i)

# def perkalian(angka1, angka2):
#     return angka1 * angka2

# hasil = perkalian(30, 20)
# print(hasil)


# def segitiga (alas, tinggi):
#     return 1/2 * alas * tinggi
# value = segitiga(10, 15)
# print(value)

def derdor(range): 
    if(range % 4 == 0 and range % 7 == 0):
        print('kelipatan 4 dan 7')
    elif(range % 4 == 0): 
        print('dor')
    elif(range % 7 == 0):
        print('der')
    else: 
        print(range)

value = derdor(28)