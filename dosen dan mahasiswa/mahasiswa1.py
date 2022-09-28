class Mahasiswa:
    def init(self, npm, nama, daftar_nilai_mk):
        self.npm = npm
        self.nama = nama
        self.daftar_nilai_mk = daftar_nilai_mk
        self.angkatan = 2000 + int(npm[0:2])
        self.kode_fakultas = npm[2:4]
        self.kode_prodi = npm[4:6]

    tabel_nilai = {
        'A':
        4.0,
        'A-':
        3.75,
        'AB':
        3.5,
        'B+':
        3.25,
        'B':
        3.0,
        'B-':
        2.75,
        'BC':
        2.5,
        'C+':
        2.25,
        'C':
        2.0,
        'D':
        1.0,
        'E': 0.0,
    }
    total_sks = 0
    total_nilai = 0
    for nilai_mk in self.daftar_nilai_mk:
        sks = nilai_mk['sks']
    nilai = nilai_mk['nilai']
    total_sks += sks
    total_nilai += sks * tabel_nilai.get(nilai, 0)
    self.ipk = 0 if total_sks == 0 \
        else total_nilai / total_sks


if name == ' main ':
    burhan = Mahasiswa(
        npm='202103034',
        nama='Mohamad Burhanudin', daftar_nilai_mk=[
            {
                'matakuliah': 'Pendidikan Agama Islam', 'sks': 2,
                'nilai': 'A',
            },
            {
                'matakuliah': 'Praktikum Aplikasi Komputer I', 'sks': 1,
                'nilai': 'A-',
            },
            {
                'matakuliah': 'Pendidikan Pancasila', 'sks': 2,
                'nilai': 'B+',
            },
            {
                'matakuliah': 'Konsep Pemrograman', 'sks': 4,
                'nilai': 'A',
            },
        ])


print('Profil Mahasiswa')
print('================')
print('NPM:', burhan.npm)
print('Nama:', burhan.nama)
print('Angkatan:', burhan.angkatan)
print('Kode Fakkultas:', burhan.kode_fakultas)
print('Kode Program Studi:', burhan.kode_prodi)
print('IPK:', burhan.ipk)
