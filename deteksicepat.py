i = 0
soal =['Saat ini saya sedang merasakan demam','Saat ini saya sedang merasakan kesulitan bernafas','Saat ini saya sedang mengalami nyeri tenggorokan',' Saat ini saya sedang merasakan batuk / pilek','Lama penyakit kurang dari 14 hari']
nilai = []
data = []
status = ''


n = int(input("Masukkan Jumlah Orang : "))
while i<n:
    print("\nData ke-",i+1)
    s_Nama = input("Masukkan Nama : ")
    s_Umur = int(input("Masukkan Umur :"))
    a_Alamat = input("Masukkan Alamat: ")

    print("DETEKSI  MANDIRI CEPAT COVID-19")
    for i in range (len(soal)):
            print(soal[i])
            print("1. Ya")
            print("2. Tidak")
            jawab = int(input("Pilihan =>"))
            if jawab == 1:
                nilai.append(10)
            else:
                nilai.append(5)

    rataNilai = sum(nilai)/5
    if rataNilai >=5:
                status="tidak aman"
    else:
                status="aman"
    print(status)
    data.append({"Nama" : s_Nama,"Umur" : s_Umur, "Alamat" : a_Alamat,  "status" : status})
    i += 1 
        
        
print("\n\nDAFTAR ORANG DETEKSI  MANDIRI COVID-19")
print('--------------------------------------------------------------------------------------------------------------------')
print('Nama                    Umur                    Alamat                    Status')
print('--------------------------------------------------------------------------------------------------------------------')
for d in data:
    print(d['Nama'],"                  ",d['Umur'],"                   ",d['Alamat'],"                   ",d['status'])
    print('--------------------------------------------------------------------------------------------------------------------')
