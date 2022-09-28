
# dict_data = dict()
list_input = []
data_input = ''
Dict = {}
Dicts = {}
# Set = {}
print('Selamat datang! Silakan masukkan jadwal KA:')
while 1:

    data_input = input()
    temp = data_input.split(' ')

    if data_input == 'selesai':
        break

    Dict = {'nomor_ka': temp[0], 'tujuan_akhir': temp[1],
            'jam_keberangkatan': temp[2], 'harga_tiket': temp[3]}

    list_input.append(Dict)
    # Dicts = Dict

print('Perintah yang tersedia:')
print('1.  INFO_TUJUAN ')
print('2.  TUJUAN_KELAS < tujuan_akhir > <kelas_kereta > ')
print('3.  TUJUAN_KELAS_TERMURAH <tujuan_akhir> <kelas_kereta> ')
print('4.  TUJUAN_JAM < tujuan_akhir > <jam_keberangkatan > ')
print('5.  TUJUAN_JAM_TERMURAH <tujuan_akhir> <jam_keberangkatan> ')
print('6.  EXIT ')

panjang_list = len(list_input)
# list_tujuan = []
# list_harga = []

while 1:

    data_input = input('Masukkan perintah:')
    list_tujuan = []
    list_harga = []
    if data_input == 'INFO_TUJUAN':
        for i in range(len(list_input)):
            list_tujuan.append(list_input[i]['tujuan_akhir'])
            # if i+1 < len(list_input):
            #     if list_input[i]['tujuan_akhir'] == list_input[i+1]['tujuan_akhir']:
            #         continue
            #     else:
            #         print(list_input[i]['tujuan_akhir'])
            # else:
            #     if list_input[i]['tujuan_akhir'] == list_input[i-1]['tujuan_akhir']:
            #         continue
            #     else:
            #         print(list_input[i]['tujuan_akhir'])
        set_tujuan = set(list_tujuan)
        for e in set_tujuan:
            print(e)
        continue
    elif data_input == 'EXIT':
        print("EXIT Terima kasih sudah menggunakan program ini! ")
        break
    else:
        found = False
        temp = data_input.split(' ')
        if temp[0] == 'TUJUAN_KELAS':
            for i in range(len(list_input)):
                if temp[1] == list_input[i]['tujuan_akhir']:
                    if temp[2] == 'Eksekutif':
                        kelas = 1
                    elif temp[2] == 'Bisnis':
                        kelas = 2
                    elif temp[2] == 'Ekonomi':
                        kelas = 3

                    if str(kelas) == str(list_input[i]['nomor_ka'][0]):
                        print('KA', list_input[i]['nomor_ka'], 'berangkat pukul', list_input[i]
                              ['jam_keberangkatan'], ' dengan harga tiket', list_input[i]['harga_tiket'])
                        found = True
                    elif i == len(list_input) and found == False:
                        print("Tidak ada jadwal KA yang sesuai.")
                        continue
                else:
                    print("Tidak ada jadwal KA yang sesuai.")
                    continue

        elif temp[0] == 'TUJUAN_KELAS_TERMURAH':
            for i in range(len(list_input)):
                if temp[1] == list_input[i]['tujuan_akhir']:
                    if temp[2] == 'Eksekutif':
                        kelas = 1
                    elif temp[2] == 'Bisnis':
                        kelas = 2
                    elif temp[2] == 'Ekonomi':
                        kelas = 3

                    if str(kelas) == str(list_input[i]['nomor_ka'][0]):
                        # print('KA', list_input[i]['nomor_ka'], 'berangkat pukul', list_input[i]
                        #   ['jam_keberangkatan'], ' dengan harga tiket', list_input[i]['harga_tiket'])
                        list_harga.append(list_input[i]['harga_tiket'])
                        # print(list_harga)
                        found = True

                    elif i == len(list_input) and found == False:
                        print("Tidak ada jadwal KA yang sesuai.")
                        continue

            if found == False:
                print("Tidak ada jadwal KA yang sesuai.")
                continue

            elif found:
                list_harga = sorted(list_harga)
                # print(list_harga)
                harga_termurah = list_harga[0]
                # print(harga_termurah)
                for i in range(len(list_input)):
                    if list_input[i]['harga_tiket'] == harga_termurah:
                        print('KA', list_input[i]['nomor_ka'], 'berangkat pukul', list_input[i]
                              ['jam_keberangkatan'], ' dengan harga tiket', list_input[i]['harga_tiket'])

        elif temp[0] == 'TUJUAN_JAM':
            for i in range(len(list_input)):
                if temp[1] == list_input[i]['tujuan_akhir']:
                    if temp[2] == list_input[i]['jam_keberangkatan']:
                        print('KA', list_input[i]['nomor_ka'], 'berangkat pukul', list_input[i]
                              ['jam_keberangkatan'], ' dengan harga tiket', list_input[i]['harga_tiket'])
                        found = True
                    elif i == len(list_input) and found == False:
                        print("Tidak ada jadwal KA yang sesuai.")
                        continue
                else:
                    print("Tidak ada jadwal KA yang sesuai.")
                    continue

        elif temp[0] == 'TUJUAN_JAM_TERMURAH':
            for i in range(len(list_input)):
                if temp[1] == list_input[i]['tujuan_akhir']:
                    if temp[2] == list_input[i]['jam_keberangkatan']:
                        # print('KA', list_input[i]['nomor_ka'], 'berangkat pukul', list_input[i]
                        #   ['jam_keberangkatan'], ' dengan harga tiket', list_input[i]['harga_tiket'])
                        # found = True
                        list_harga.append(list_input[i]['harga_tiket'])
                        # print(list_harga)
                        found = True
                    elif i == len(list_input) and found == False:
                        print("Tidak ada jadwal KA yang sesuai.")
                        continue
                else:
                    print("Tidak ada jadwal KA yang sesuai.")
                    continue

            if found == False:
                print("Tidak ada jadwal KA yang sesuai.")
                continue

            elif found:
                list_harga = sorted(list_harga)
                # print(list_harga)
                harga_termurah = list_harga[0]
                # print(harga_termurah)
                for i in range(len(list_input)):
                    if list_input[i]['harga_tiket'] == harga_termurah:
                        print('KA', list_input[i]['nomor_ka'], 'berangkat pukul', list_input[i]
                              ['jam_keberangkatan'], ' dengan harga tiket', list_input[i]['harga_tiket'])

        else:
            print("Perintah yang dimasukkan tidak valid.")
            continue
