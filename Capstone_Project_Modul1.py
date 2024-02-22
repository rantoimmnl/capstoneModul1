from tabulate import tabulate

# Contoh isi Buku Yellow Pages sebagai data awal
yellowPages = {
    'Andi': ['+6285210220304','Jln. Sekar No. 12'],
    'PLN' : ['+622210010','Jln. Ir. H. Djuanda No. 10'],
    'Bank BRI Bandung' : ['+6222700800','Jln. Cipondoh No. 5'],
    'Kantor Walikota Bandung' : ['+622100200', 'Jln. Soetta No. 155']
}

#Sortir data berdasarkan abjad pada key, yakni nama
yellowPages_sorted = dict(sorted(yellowPages.items()))

# Judul Kolom pada tabel penyajian data buku Yellow Pages
#dalam hal ini, isi buku Yellow Pages selalu berupa nama, nomor telepon, dan alamat pemilik nomor telepon, sehingga tidak dibutuhkan penambahan jenis data baru 
headers = ('Nama', 'Nomor Telepon', 'Alamat')

#fungsi menu utama
def main():
    print(f'''\n ***Selamat Datang dalam Program Yellow Pages*** \n
                     1. Lihat Data Nomor Telepon \n
                     2. Cari Data Nomor Telepon \n
                     3. Tambahkan Data Nomor Telepon \n
                     4. Perbarui Data Nomor Telepon \n
                     5. Hapus Data Nomor Telepon \n
                     6. Keluar \n
          ''')
    menu = int(input('Silahkan pilih nomor menu yang anda tuju: '))
    return menu

#fungsi penyajian isi buku Yellow Pages
def nomor_satu():
    listYP = []
    
    #data buku Yellow Pages disimpan dalam dictionary, dengan key berupa nama dan  value berupa list yang terdiri dari nomor telepon dan alamat
    #sehingga untuk menampilkannya dalam bentuk tabulate yang lebih rapi, dictionary tsb diubah dahulu kedalam bentuk list
    for key, val in yellowPages_sorted.items(): 
        listYP.append([key] + val)
          
    # Print the tabulated result
    print(tabulate(listYP, headers=headers))

#fungsi pencarian data berdasarkan nama pemilik nomor telepon
def nomor_dua():
    subMenu2 = int(input(f'''
                             1. Cari berdasarkan nama \n
                             2. Kembali ke menu utama \n
                             Silahkan pilih sub menu yang anda tuju: '''))
    
    #pencarian data dengan kata kunci berupa nama
    if subMenu2 == 1:
        hasilYP = []
        kataKunci = (input(f'''Silahkan masukkan kata kunci: '''))        
        for key, val in yellowPages_sorted.items():            
            if kataKunci.lower() in key.lower():
                hasilYP.append([key] + val)                       
        
        #apabila ditemukan kesamaan kata kunci dengan nama pemilik telepon, segala data dengan kesamaan thd kata kunci akan ditampilkan
        if len(hasilYP) == 0:
            print('***Data yang anda cari tidak tersedia*** \n ***Kembali ke menu utama***')
        else:
            print('Berikut hasil pencarian data: ')
            print(tabulate(hasilYP, headers=headers))
    elif subMenu2 == 2:
        True
    
#fungsi penambahan data ke dalam buku Yellow Pages
def nomor_tiga():
    print('Silahkan masukkan data baru sebagai berikut: ')
    nama = str(input('Masukkan nama pemilik nomor telepon yang akan ditambahkan: '))
    
    #pemeriksaan adanya duplikat antara data yang akan ditambahkan dengan data eksisting pada buku Yellow Pages
    for key in yellowPages_sorted.keys():
        duplikat = 0
        if nama == key:
            duplikat += 1
            break
    
    #jika duplikat bernilai 1, artinya ditemukan kesamaan penuh antara data yang akan ditambahkan dengan data eksisting, dan sebaliknya
    if duplikat == 1:
            print('\n Tidak dapat menambahkan data: data ini telah tersedia dalam buku. Kembali ke submenu... \n')            
            nomor_tiga()            
    else:
        noTelp = str(input('Masukkan nomor telepon yang akan ditambahkan (diawali dengan +62): '))
        alamat = str(input('Masukkan alamat pemilik nomor telepon yang akan ditambahkan: '))
        newYP_key = nama
        
        yellowPages_add = {}
        yellowPages_add[newYP_key]= [noTelp, alamat]

        #penggabungan data yang baru dimasukkan dengan data eksisting
        #penggabungan dilakukan dengan mengubahnya menjadi set, lalu menggabungkan kedua data dan mengurutkannya sesuai abjad pada key
        yellowPages_concat = {}
        yellowPages_concat = set(yellowPages_add.keys()).union(yellowPages_sorted.keys())
        yellowPages_concat_sorted = sorted(yellowPages_concat)
        #selanjutnya, set tsb akan diubah menjadi dictionary untuk memperoleh key-value yang sesuai, agar selanjutnya dapat diubah menjadi list
        yellowPages_add_sorted = {}
        for key in yellowPages_concat_sorted:
            if key in yellowPages_add:
                yellowPages_add_sorted[key] = yellowPages_add[key]
            if key in yellowPages_sorted:
                yellowPages_add_sorted[key] = yellowPages_sorted[key]
        
        #pengubahan dari dicitonary menjadi list bertujuan untuk memungkinkan penyajian data dengan benar dalam tabulate
        listYP = []
        for key, val in yellowPages_add_sorted.items():
            listYP.append([key] + val)
        
        print('\n Berikut data nomor telepon terbaru: \n')
        print(tabulate(listYP, headers=headers))
    
        return yellowPages_add_sorted

#fungsi pengubahan data pada buku Yellow Pages
def nomor_empat():
    nama_update = str(input('Masukkan nama pengguna telepon yang datanya ingin anda ubah: '))
    
    #pengecekan ada tidaknya data yang ingin diubah pada buku Yellow Pages 
    if nama_update in yellowPages_sorted.keys():
        noTelp_update = str(input('Masukkan nomor telepon terbaru (diawali dengan +62): '))
        alamat_update = str(input('Masukkan alamat terbaru: '))
        updateYP_key = nama_update
        updateYP_val = [noTelp_update, alamat_update]

        #data yang terdapat pada buku Yellow Pages diubah sesuai dengan inputan yang diberikan, lalu diurutkan kembali    
        yellowPages_sorted[updateYP_key] = updateYP_val            
        yellowPages_sorted_update = dict(sorted(yellowPages_sorted.items()))
        
        #penyajian data terbaru sesuai hasil ubahan yang diberikan
        listYP = []
        for key, val in yellowPages_sorted_update.items():
            listYP.append([key] + val)
        print('Berikut data nomor telepon terbaru: \n')
        print(tabulate(listYP, headers=headers))
    else:
        print('***Data yang ingin diubah tidak ditemukan*** \n')
        main()
    
    return yellowPages_sorted_update
    
#fungsi menghapus data pemilik nomor telepon
def nomor_lima():
    nama_del = str(input('Masukkan nama pemilik telepon yang ingin anda hapus datanya: '))
    
    #pencarian data yang sesuai inputan pada buku Yellow Pages
    listYP_key = []
    for key , val in yellowPages_sorted.items():
        if nama_del.lower() in str(key.lower()):
            listYP_key.append([key] + val)
    
    #pengecekan ada tidaknya data eksisting yang sesuai dengan kata kunci penghapusan data
    #apabila data sesuai, maka proses penghapusan data dilanjutkan
    if len(listYP_key) == 0:
        print('***Data tersebut tidak ditemukan***')
        nomor_lima()
    else:
        #penyajian data yang sesuai dengan kata kunci penghapusan data yang telah diinput user
        #data akan dihapus sesuai dengan input berupa indeks data yang akan dihapus
        print(f'Berikut data yang sesuai dengan kata kunci penghapusan data: ')
        print(tabulate(listYP_key, headers=headers, showindex=True))
        delNum = int(input('Pilih data yang akan dihapus (ketikkan angka indeks data yang ingin dihapus): '))
        del_key = (listYP_key[delNum][0])
        del yellowPages_sorted[del_key]
        print('***Data berhasil dihapus*** \n')

    return yellowPages_sorted

#implementasi program, dimana tiap function digunakan sesuai dengan peruntukan yang tertera dalam menu utama
while True:
    menu = main()
    if menu == 1:
        nomor_satu()
        continue
    if menu == 2:
        nomor_dua()
                
    elif menu == 3:
        yellowPages_sorted = nomor_tiga()         
                
    elif menu == 4:
        yellowPages_sorted = nomor_empat()
                       
    elif menu == 5:
        yellowPages_sorted = nomor_lima()

    elif menu == 6:
        print(f'\n ***Terima kasih***')
        break
    else:
        print('Menu yang anda pilih tidak sesuai')
        continue