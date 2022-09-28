# reference
# https: // www.teamtrainit.com/demo/algoritma/cf/teori.php

# Rule
hujan_maka_banjir = 0.85
aspirasi_maka_kerusuhan = 0.9
lokerPekerjaan_maka_kerusuhan = -0.75
banjir_atau_kerusuhan_krisisEkonomi = 0.8

# Hipotesis
hujan = 0.7
# lowongan_pekerjaan tapi tidak aspirasi
loker_tapi_tidakAspirasi = aspirasi_maka_kerusuhan + lokerPekerjaan_maka_kerusuhan

# kepastian krisis ekonomi
cf_total_1 = hujan * hujan_maka_banjir * banjir_atau_kerusuhan_krisisEkonomi
cf_total_2 = (lokerPekerjaan_maka_kerusuhan + aspirasi_maka_kerusuhan) * \
    banjir_atau_kerusuhan_krisisEkonomi

print("cf_1 : ", cf_total_1)
print("cf_2 : ", cf_total_2)

print("cf   : ", max(cf_total_1, cf_total_2))
