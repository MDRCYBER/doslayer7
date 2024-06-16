from scapy.all import *

# URL target untuk pengiriman permintaan POST
url = 'https://tokodukun.com/'  # Ganti dengan URL yang sesuai

# Data yang ingin dikirim dalam permintaan POST
data = {'key': 'value'}  # Ganti dengan data yang sesuai jika diperlukan

# Fungsi untuk mengirim permintaan POST
def send_post_request(url, data):
    headers = 'POST ' + url + ' HTTP/1.1\r\n' \
              'Host: tokodukun.com\r\n' \
              'Content-Type: application/x-www-form-urlencoded\r\n'

    # Ubah data menjadi format x-www-form-urlencoded
    encoded_data = '&'.join([f"{key}={value}" for key, value in data.items()])

    payload = headers + f'Content-Length: {len(encoded_data)}\r\n\r\n' + encoded_data

    # Kirim paket menggunakan scapy
    send(IP(dst="tokodukun.com")/TCP(dport=3306)/Raw(load=payload), verbose=False)

# Jumlah permintaan POST yang ingin dikirim
jumlah_permintaan = 10  # Ganti sesuai kebutuhan Anda

# Loop untuk mengirim permintaan POST sebanyak jumlah yang diinginkan
for _ in range(jumlah_permintaan):
    send_post_request(url, data)
    print(f'Permintaan POST ke-{_ + 1} berhasil dikirim.')