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
client_id = 'lionair-971'
# client id mqtt
username = 'lionair711'
# username mqtt
password = '12345678'
# password mqtt


def connect_mqtt() -> mqtt_client:
    # definisi fungsi connect
    def on_connect(client, userdata, flags, rc):
        # definisi fungsi status connect
        if rc == 0:
            # kondisi kalau connect
            print("Connected to MQTT Broker!")
            # print status
        else:
            # kondisi ketika tidak connect
            print("Failed to connect, return code %d\n", rc)
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


def subscribe(client: mqtt_client):
    def on_message(client, userdata, msg):
        print(
            f"Pemberitahuan kepada penumpang bahwa terdapat perubahan jadwal \n `{msg.payload.decode()}`")
        # print(len(msg.payload.decode()))
        if len(msg.payload.decode()) == 18:
            with open('boarding.txt', 'w') as filehandle:
                # for listitem in msg.payload:
                filehandle.writelines(msg.payload.decode())
        else:
            with open('lokasi.txt', 'w') as filehandle:
                # for listitem in msg.payload:
                filehandle.writelines(msg.payload.decode())

    client.subscribe(topic)
    client.on_message = on_message


def run():
    # definisi fungsi run
    client = connect_mqtt()
    # definisi client mqtt
    # time.sleep(2)
    # menunggu koneksi
    subscribe(client)
    # menjalankan fungsi publish untuk client
    client.loop_forever()
    # memulai loop abadi untuk mqtt


if __name__ == '__main__':
    run()
    # menjalankan fungsi run yang akan menjalankan client mqtt
