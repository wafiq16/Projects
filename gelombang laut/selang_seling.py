import math
import numpy as np
import matplotlib.pyplot as plt

# fungsi cari galat


def getGalat(N):
    g = 9.81
    # percepatan gravitasi
    # banyak langkah
    L = 5
    # ujung ujung interval
    Xmin = -L
    Xmax = L
    dx = (L-(-L))/N
    # jarak grid a ke b
    hL = 10
    # tinggi awal di sebelah kiri dinding, x = 0
    hR = 4
    # tinggi awal di sebelah kanan dinding
    dt = 0.05 * dx
    # langkah waktu t
    t_stop = 0.2
    # t max untuk dt

    # ========================= perhitungan shock wave ==============================
    c_L = math.sqrt(g*hL)
    # kecepatan gelombang di kiri
    c_R = math.sqrt(g*hR)
    # kecepatan gelombang di kanan
    Smin = -101.0
    # awal bracketing bisection methode untuk shock speed s
    Smax = 0.0
    # akhir bracketing bisection methode untuk shock speed s
    for i in range(100):
        S = (Smin+Smax)/2.0
        # bisecting
        u2 = S-c_R*c_R/4.0/S*(1.0+math.sqrt(1.0+8.0*S*S/c_R/c_R))
        # fungsi emplisit kecepatan dibelakang shock
        c2 = c_R * math.sqrt(0.5*(math.sqrt(1.0+8.0*S*S/c_R/c_R)-1.0))
        # fungsi emplisit kecepatan gelombang dibelakang shock
        func = -2.0 * c_L - u2 + 2.0 * c2
        if func > 0.0:
            Smin = S
        else:
            Smax = S
        # prosedur bisection

    # ==================== Membuat grid ============================
    start = -L+dx/2
    # definisi titik start
    stop = L+dx/2
    # definisi titik stop
    step = dx
    # definisi langkah
    x = np.arange(start=start, stop=stop, step=step)
    # membuat range x
    h = [0.0 for x in range(N)]
    # ruang kedalaman
    u = [0.0 for x in range(N)]
    # ruang kecepatan
    q = [0.0 for x in range(N)]
    # ruang debit

    xodd = [0.0 for x in range(int(N/2))]
    # x untuk daerah ganjil
    uodd = [0.0 for x in range(int(N/2))]
    # u untuk daerah ganjil
    qodd = [0.0 for x in range(int(N/2))]
    # q untuk daerah ganjil

    # print(int(N/2))

    xeven = [0.0 for x in range(int(N/2))]
    # x untuk daerah genap
    heven = [0.0 for x in range(int(N/2))]
    # h untuk daerah genap
    qeven = [0.0 for x in range(int(N/2))]
    # q untuk daerah genap

    # membuat ruang perhitungan

    # ============ Membuat klasifikasi grid berdasarkan kecepatan dan kedalaman air ===============
    # % = 0, grid genap && %!= 0, grid ganjil

    # mengisi nilai dari x genap dan ganjil dari matrix x
    for i in range(N):
        if np.mod(i, 2) == 0:
            xeven[int(i/2)] = x[i]
        else:
            # print(i)
            xodd[int((i-1)/2)] = x[i]

    # kondisi awal
    for i in range(N):
        if i < int(N/2):
            h[i] = hL
        else:
            h[i] = hR

    # inisiasi t awal, matrix g dan u awal
    t = 0
    h[0] = hL
    h[int(N)-1] = hR
    u[0] = 0
    u[int(N)-1] = 0

    # menghitung nilai galat selama t sampai t_stop
    while t < t_stop:
        # definisi buffer matrix
        hh = h
        uu = u
        hnew = [0 for x in range(N)]
        unew = [0 for x in range(N)]

        # menghitung matrix h baru
        for i in range(2, N-1):
            if np.mod(i, 2) == 0:
                hhtiph = hh[i]
                uuiph = uu[i+1]
                qiph = hhtiph * uuiph
                hhtimh = hh[i-2]
                uuimh = uu[i-1]
                qimh = hhtimh * uuimh
                # print(i)
                hnew[i] = hh[i] - dt/(2*dx) * (qiph - qimh)

        # memberi batasan pada matrix h baru
        for i in range(N):
            if i < 3:
                hnew[i] = hL
                unew[i] = 0
            elif i > N-3:
                hnew[i] = hR
                unew[i] = 0

        # perhitungan untuk galat U
        for i in range(3, N-3):
            if np.mod(i, 2) != 0:
                uutipl = uu[i]
                uuti = uu[i-2]

                uuip3h = uu[i+2]
                hhtip3h = hh[i+1]
                qip3h = uuip3h * hhtip3h

                uuiph = uu[i]
                hhtiph = hh[i-1]
                qiph = uuiph * hhtiph

                qipl = 0.5*(qiph+qip3h)

                hhtimh = hh[i-3]
                uuimh = uu[i-2]
                qimh = hhtimh * uuimh

                qi = 0.5*(qiph + qimh)

                hhipl = hh[i+1]
                hhi = hh[i-1]
                hhiph = 0.5*(hhi+hhipl)
                hipl = hnew[i+1]
                hi = hnew[i-1]
                hiph = 0.5*(hipl + hi)
                unew[i] = (1/hiph) * (hhiph*uuiph - dt/(2*dx)*(qipl*uutipl -
                                                               qi*uuti + 0.5*g*(math.pow(hipl, 2) - math.pow(hi, 2))))

        # memberi nilai pasti galat h dan u baru pada kondisi tertentu
        for i in range(N):
            if i < 4:
                hnew[i] = hL
                unew[i] = 0
            elif i > N-4:
                hnew[i] = hR
                unew[i] = 0

        # memasukkan nilai h dan u baru ke matrix h dan u
        h = hnew
        u = unew
        # menambah nilai t yang digunakan pada iterasi
        t = t + dt

        # inisiasi index pada u dan h exac
        start = Xmin+dx/2
        stop = Xmax-dx/2
        step = dx

        # mengisi nilai index pada u dan h exac
        u_ex = np.arange(start=start, stop=stop, step=step)
        h_ex = np.arange(start=start, stop=stop, step=step)

        # inisiasi nilai xC untuk proses selanjutnya
        xC = x

        # fungsi mencari nilai h dan u exact
        for i in range(int(np.max(xC.shape))-1):
            if(xC[i]) <= -c_L * t:
                u_ex[i] = 0.0
                h_ex[i] = hL
            elif xC[i] <= -(u2+c2)*t:
                u_ex[i] = 2.0/3.0*(xC[i]/t + math.sqrt(g*hL))
                h_ex[i] = 4.0/(9*g) * \
                    math.pow((-xC[i]/(2.0*t) + math.sqrt(g*hL)), 2)
            elif xC[i] < -S*t:
                u_ex[i] = -u2
                h_ex[i] = math.pow(c2, 2)/g
            else:
                u_ex[i] = 0.0
                h_ex[i] = hR

        # mencari q exac
        Q_ex = h_ex * u_ex

        # inisiasi matrix galat h(genap) dan u(ganjil) exac
        hevenex = [0 for x in range(int(N/2))]
        uoddex = [0 for x in range(int(N/2))]
        for i in range(N-1):
            if np.mod(i, 2) == 0:
                heven[int(i/2)] = h[i]
                hevenex[int(i/2)] = h_ex[i]
            else:
                uodd[int((i-1)/2)] = u[i]
                uoddex[int((i-1)/2)] = u_ex[i]

    # nilai galat u dan h akhir
    E_u = 1 / (N/2)*sum(abs(np.array(uodd) - np.array(uoddex)))
    E_h = 1 / (N/2)*sum(abs(np.array(heven) - np.array(hevenex)))
    return E_u, E_h
    # return value fungsi


# inisiasi list input
N = [100, 200, 400, 800, 1600, 3200]

# inisiasi list ouput galat U dan H
NU = []
NH = []

# mencari jumlah input
a = len(N)

# mencetak dalam bentuk tabel dan mengisi nilai galat U dan H pada list
print("+===============++=============+")
print("| Galat ke |     U    |    H    |")
print("+--------------++--------------+")
for i in range(a):
    b, c = getGalat(N[i])
    NU.append(b)
    NH.append(c)
    print("| "+str(i+1) + "        |  " +
          str(round(b, 4)) + "  |  " + str(round(c, 4)) + " |")
    print("+--------------++--------------+")
print("+===============++=============+")

# menampilkan galat U dan H pada grafik
plt.plot(N, NU, label='Galat U(kecepatan aliran air)')
plt.plot(N, NH, label='Galat H(ketinggian aliran air)')
plt.legend()
