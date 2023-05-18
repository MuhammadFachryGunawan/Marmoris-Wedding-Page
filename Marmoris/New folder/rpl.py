#untuk nge-print menu yang ada
print("Paket Giganet special untukmu")
print("1. 45GB/Rp100rb")
print("2. 50GB/Rp100rb")
print("3. 13GB/Rp100rb")
print("4. 16GB/Rp100rb")
print("5. info")
print("6. paket lainnya")

pilihan = int(input("masukkann pilihan anda : ")) #membuat variabel pilihan dan meminta input kepada user berupa int
con = input("apakah anda ingin cancel/send ") #membuat variabel con dan meminta user untuk memilih pilihan yang sudah disediakan
#melalukan perulangan if untuk mengecek pilihan user dari 1 sampai 6
if(pilihan == 1): 
    print("anda masuk ke menu 1")
elif(pilihan == 2):
    print("anda masuk ke menu 2")
elif(pilihan == 3):
    print("anda masuk ke menu 3")
elif(pilihan == 4):
    print("anda masuk ke menu 4")
elif(pilihan == 5):
    print("anda masuk ke menu 5")
elif(pilihan == 6):
    print("anda masuk ke menu 6")
#kalau tidak ada angka diatas yang dipilih oleh user maka akan dijalankan perintah dibawah
else: 
    print("anda tidak memilih menu apapun")
    exit
#kalau user memilih cancel maka dia akan langsung keluar dari program
if(con == "cancel"):
    print("anda keluar dari menu")
else:
    exit