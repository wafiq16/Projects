# python 3.6
import time
# import library waktu

from paho.mqtt import client as mqtt_client
# import library mqtt python

broker = 'broker.hivemq.com'
# mqtt broker
port = 1883
# port tcp untuk mqtt
topic = "/lionair711/boarding"
# mqtt topik
client_id = 'lionair-0'
# client id mqtt
username = 'lionair711'
# username mqtt
password = '12345678'
# password mqtt

boarding = ["16:23", "20:00", "05:37"]
# initial boarding data
transit = ["singapure, bangkok", "jakarta", "balikpapan"]
# initial transit data

with open('boarding.txt', 'w') as filehandle:
    # buka file boarding .txt
    for listitem in boarding:
        # mengambil tiap item di list
        filehandle.write('%s\n' % listitem)
        # menulis tiap item pada tiap baris
with open('lokasi.txt', 'w') as filehandle:
    # buka file lokasi.txt
    for listitem in transit:
        # mengambil tiap item di list
        filehandle.write('%s\n' % listitem)
        # menulis tiap item pada tiap baris
# menuliskan data awal pada file txt


def connect_mqtt() -> mqtt_client:
    # definisi fungsi connect
    def on_connect(client, userdata, flags, rc):
        # definisi fungsi status connect
        if rc == 0:
            print("Connected to MQTT Broker!")
            # kondisi kalau connect
            # print status
        else:
            print("Failed to connect, return code %d\n", rc)
            # kondisi ketika tidak connect
            # print status

    client = mqtt_client.Client(client_id)
    # inisialisasi koneksi
    client.username_pw_set(username, password)
    # inisialisasi username dan password
    client.on_connect = on_connect
    # memberikan fungsi handler on_connect pada client
    client.connect(broker, port)
    # menguhubungkan client berdasarkan broker dan port
    return client
    # mengembalikan client sebagai return function


def publish(client):
    # definisi fungsi publish
    next = False
    # inisialisasi flag perubahan data
    while True:
        # loop abadi
        changes = input('Any change : ')
        # input apakah ada perubahan
        if changes == 'y':
            # kondisi ada perubahan
            change = input('What change : ')
            # input jenis perubahan

            my_boarding = open("boarding.txt", "r")
            boarding_list = my_boarding.readlines()
            # membuka file dan membaca tiap baris sebagai list
            # print(boarding_list)

            my_trancite = open("lokasi.txt", "r")
            trancite_list = my_trancite.readlines()
            # membuka file dan membaca tiap baris sebagai list
            # print(trancite_list)

            new_boarding_list = []
            new_trancite_list = []
            # inisialisasi list perubahan data

            if change == 't':
                # perubahan data transit
                for i in range(len(trancite_list)):
                    # mengambil tiap data pada data transit
                    # print(new_trancite_list[i])
                    # print(trancite_list[i])
                    new_trancite_list.append(input('') + '\n')
                    # mengambil pembaharuan data
                    if new_trancite_list[i] == trancite_list[i]:
                        # meninjau apakah terdapat kesamaan data
                        # print("tidak ada perubahan data")
                        next = True
                        # flag data sama aktif
                        # break
            else:
                # jika tidak ada perubahan data
                new_trancite_list = trancite_list

            if change == 'b':
                # perubahan data boarding
                for i in range(len(boarding_list)):
                    # mengambil jumlah data pada data boarding
                    new_boarding_list.append(input('') + '\n')
                    # mengambil data boarding baru
                    if new_boarding_list[i] == boarding_list[i]:
                        # meninjau apakah ada data yang sama dengan data yang lama
                        # print("tidak ada perubahan data")
                        next = True
                        # flag data sama aktif
                        # break
            else:
                new_boarding_list = boarding_list
                # tidak ada perubahan data
            if next:
                # meninjau apakah flag kesamaan data aktif
                print("tidak ada perubahan data")
                # print kondisi jika flag aktif
                continue
                # melanjutkan pada loop berikutnya, sehingga data tidak dikirim ke client

            msg = str(listToString(new_boarding_list))
            # mengubah data boarding baru ke dalam string
            msg2 = str(listToString(new_trancite_list))
            # mengubah data transit baru ke dalam string
            result = client.publish(topic, msg)
            # mengirim data boarding
            result2 = client.publish(topic, msg2)
            # mengirim data transit
            # result: [0, 1]
            status = result[0]
            # status pengiriman
            if status == 0:
                print(f"Send success")
                # print status pengiriman
            else:
                print(f"Send Failed")
                # print status pengiriman


def run():
    # definisi fungsi run
    client = connect_mqtt()
    # definisi client mqtt
    time.sleep(2)
    # menunggu koneksi
    client.loop_start()
    # memulai loop abadi untuk mqtt
    publish(client)
    # menjalankan fungsi publish untuk client


def listToString(s):

    # initialize an empty string
    str1 = ""

    # traverse in the string
    for ele in s:
        str1 += ele

    # return string
    return str1


if __name__ == '__main__':
    run()
    # menjalankan fungsi run yang akan menjalankan client mqtt
