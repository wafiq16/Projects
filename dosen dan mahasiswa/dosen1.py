from datetime import date


class Dosen:
    def init(self, nama, gelar_depan, gelar_belakang, tgl_lahir, riwayat_ngajar):
        self.nama = nama
        self.gelar_depan = gelar_depan
        self.gelar_belakang = gelar_belakang
        self.tgl_lahir = tgl_lahir
        self.riwayat_ngajar = riwayat_ngajar
        self.nama_lengkap = gelar_depan + ' ' \
            if gelar_depan else ''
        self.nama_lengkap += nama
        self.nama_lengkap += ', ' + gelar_belakang \
            if gelar_belakang else ''
        skr = date.today()
        bln_lahir = tgl_lahir.month
        hari_lahir = tgl_lahir.day
        self.umur = skr.year - tgl_lahir.year
        if (skr.month, skr.day) < (bln_lahir, hari_lahir):
            self.umur -= 1

        self.mata_kuliah = []
        for ngajar in riwayat_ngajar:
            matkul = ngajar['matkul']
        if matkul not in self.mata_kuliah:
            self.mata_kuliah.append(matkul)


if name == ' main ':
    andika = Dosen(
        nama='Andika Bayu Saputra', gelar_depan=None, gelar_belakang='S.Kom., M.Kom.', tgl_lahir=date(1986, 1, 21),

        riwayat_ngajar=[
            {
                'semester': '2019-1',
                'matkul': 'Pengantar Rekayasa Software', 'prodi': 'Informatika',
            },
            {
                'semester': '2019-2',
                'matkul': 'Data Engineering for Business', 'prodi': 'Informatika',
            },
            {
                'semester': '2020-1',
                'matkul': 'Pengantar Rekayasa Software', 'prodi': 'Informatika',
            },
            {
                'semester': '2020-2',
                'matkul': 'Data Engineering for Business', 'prodi': 'Informatika',
            },
            {
                'semester': '2021-1', 'matkul': 'Logika Informatika', 'prodi': 'Informatika',
            },
        ])
print('Profil Dosen')
print('============')
print('Nama lengkap:', andika.nama_lengkap)
print('Umur:', andika.umur, 'tahun')
print('Mata kuliah:')
print('\n'.join(['\t{}. {}'.format(i + 1, mk)
                 for i, mk in enumerate(andika.mata_kuliah)]))
