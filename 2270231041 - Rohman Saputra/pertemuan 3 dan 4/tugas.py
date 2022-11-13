print("----------------- SELAMAT DATANG DI WARROENK ROHMAN -----------------")
nama = input("MASUKKAN NAMA ANDA : ")
Alamat = input("MASUKKAN ALAMAT : ")
No_telp = input("MASUKKAN NO TELP")
Tanggal = input("MASUKKAN TANGGAL")

def fungsimakanan():
   global totalmkn
   global porsi
   global mkn
   print ("\n----------------- Menu Makanan -----------------")
   print("1. Roti sandwich - Rp 15000")
   print("2. Mie rebus - Rp 9000")
   print("3. Bubur ayam - Rp 10000")
   nomor=int(input("Masukan Pilihan: "))
   porsi= int(input("Berapa Porsi: "))

   if nomor==1:
       totalmkn=porsi*15000
       print (porsi," Porsi Roti sandwich = Rp", totalmkn)
       mkn=("Roti sandwich")
   elif nomor==2:
       totalmkn=porsi*9000
       print (porsi," Porsi Mie rebus = Rp", totalmkn)
       mkn=("Mie rebus")
   elif nomor==3:
       totalmkn=porsi*10000
       print (porsi, " Porsi Bubur ayam = Rp", totalmkn)
       mkn=("Bubur ayam")
   else:
      print("Pilihan tidak ada, silahkan masukan lagi!!!")
      fungsimakanan()

def fungsiminuman():
   global totalmnm
   global mnm
   global gelas
   print("\n----------------- Menu Minuman -----------------")
   print("1. Es kelapa - Rp 5000")
   print("2. Es lychee - Rp 10000")
   print("3. es coklat - Rp 10000")
   nomor=int(input("Masukan Pilihan: "))
   gelas= int(input("Berapa Gelas: "))

   if nomor==1:
       totalmnm=gelas*5000
       print (gelas," Es kelapa = Rp", totalmnm)
       mnm=(" es kelapa")
   elif nomor==2:
       totalmnm=gelas*10000
       print (gelas, " Gelas Es lychee = Rp", totalmnm)
       mnm=("Es lychee")
   elif nomor==3:
       totalmnm=gelas*10000
       print (gelas, " Gelas Es coklat = Rp", totalmnm)
       mnm=("es coklat")
   else:
      print("Pilihan tidak ada, silahkan masukan lagi!!")
      fungsiminuman()

fungsimakanan()
fungsiminuman()
totalsemua=totalmkn+totalmnm

print("\nTotal harus Dibayar: Rp",totalsemua)
uang=int(input("Uang Tunai Pembeli: Rp "))
kembalian=int(uang-totalsemua)
print("Kembalian :",kembalian)

print("\n==================================")
print("========== STRUK PEMBELIAN =========")
print("==================================")
print ("Nama\t\t:",nama)
print ("Alamat\t\t:",Alamat)
print ("No telp\t\t:",No_telp)
print ("Tanggal\t\t:",Tanggal)

print ("Beli\t\t:",porsi,mkn,"( Rp", totalmkn,")")
print ("\t\t ",gelas,mnm,"( Rp", totalmnm,")")
print ("Tagihan\t\t: Rp",totalsemua)
print ("Dibayar\t\t: Rp",uang)
print ("Kembalian\t: Rp",kembalian)
print("==================================")
print("==================================")

