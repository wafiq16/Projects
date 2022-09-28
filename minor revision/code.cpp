#include <iostream>
// #include <conio.h>
#include <string.h>

using namespace std;

struct Node
{
    char nama[30];
    int umur;
    Node *next;
};

Node *head = NULL;
Node *tail = NULL;

void tambah_belakang()
{
    char a[30];
    int b;
    // Masukan Data-datanya
    cout << "Masukan Nama Teman : ";
    cin >> a;
    cout << "Masukan Umur Teman : ";
    cin >> b;
    // Buat Node Baru :: Memesan Tempat di memory
    Node *baru;
    baru = new Node;
    // Masukan Datanya ke Node Baru
    strcpy(baru->nama, a);
    baru->umur = b;
    // Jika data Teman Belum Ada di Memory
    if (head == NULL)
    {
        head = baru;
        head->next = NULL;
        tail = head;
    }
    // Jika Data Teman sudah ada datanya di Memory
    else
    {
        tail->next = baru;
        tail = baru;
        tail->next = NULL;
    }
}

void tampil()
{
    Node *bantu;
    bantu = head;
    cout << endl;
    if (head != NULL)
    {
        while (bantu != NULL)
        {
            cout << bantu->nama << " " << bantu->umur << " " << endl;
            bantu = bantu->next;
        }
    }
    else
        cout << "Masih kosong\n";

    // getch();
}

void tambah_depan()
{
    char a[30];
    int b;
    // Masukan Data-datanya
    cout << "Masukan Nama Teman : ";
    cin >> a;
    cout << "Masukan Umur Teman : ";
    cin >> b;
    // Buat Node Baru :: Memesan Tempat di memory
    Node *baru;
    baru = new Node;
    // Masukan Datanya ke Node Baru
    strcpy(baru->nama, a);
    baru->umur = b;
    // Jika data Teman Belum Ada di Memory
    if (head == NULL)
    {
        head = baru;
        head->next = NULL;
        tail = head;
    }
    // Jika Data Teman sudah ada datanya di Memory
    else
    {
        baru->next = head;
        head = baru;
    }
}

void cari()
{
    char cari[30];
    cout << "Mencari Nama teman Siapa : ";
    cin >> cari;
    Node *bantu;
    bantu = head;
    if (head != NULL)
    {
        while (bantu != NULL)
        {
            if (strcmp(bantu->nama, cari) == 0)
            {
                cout << "Data ketemu ";
                cout << bantu->nama;
                cout << bantu->umur;
            }
            bantu = bantu->next;
        }
    }
    else
        cout << "Masih kosong\n";

    // getch();
}

// void hapusdepan()
// {
//     if (head == NULL) // list kosong
//         cout << "list masih kosong";
//     else if (head == tail) // list hanya 1 node
//     {
//         delete head; // free :membebaskan memroy dr data
//         head = NULL;
//         tail = NULL;
//     }
//     else
//     { // list banyak (lebih dari 1 node)
//         Node *hapus;
//         hapus = head;
//         head = head->next;
//         delete hapus;
//     }
// }

void hapusbelakang()
{
    if (head == NULL)
        cout << "List masih kosong";
    else if (head == tail)
    {
        delete head;
        head = NULL;
        tail = NULL;
    }
    else
    {
        Node *bantu;
        bantu = head;
        while (bantu->next != tail)
        {
            bantu = bantu->next;
        }
        // Posisi bantu = node sebelum node terakhir
        delete tail;
        bantu->next = NULL;
        tail = bantu;
    }
}

// void hapustengah()
// {
//     if (head == NULL)
//         cout << "List masih Kosong";
//     else if (head == tail)
//     {
//         delete head;
//         head = NULL;
//         tail = NULL;
//     }
//     else // jika node banyak
//     {
//         char x[30];
//         cout << "Manghapus Nama siapa : "; //
//         cin >> x;
//         // jika ternyata yg mau dihapus itu Node Depan
//         if (strcmp(head->nama, x) == 0)
//             hapusdepan();
//         // jika ternyata yg mau dihapus itu Node belakang
//         else if (strcmp(tail->nama, x) == 0)
//             hapusbelakang();
//         else // Jika node berada di tengah
//         {
//             Node *bantu;
//             bantu = head;
//             while (bantu != NULL)
//             {
//                 if (strcmp(bantu->next->nama, x) == 0)
//                 {
//                     // hapus tengah;
//                     Node *hapus;
//                     hapus = bantu->next;
//                     bantu->next = bantu->next->next;
//                     delete hapus;
//                     break; // memaksa berhenti dari loop
//                 }
//                 bantu = bantu->next;
//             }
//         }
//         // Finish
//     }
// }

void hapus(int flag)
{
    if (head == NULL) // list kosong
        cout << "list masih kosong";
    else if (head == tail) // list hanya 1 node
    {
        delete head; // free :membebaskan memroy dr data
        head = NULL;
        tail = NULL;
    }
    else
    { // list banyak (lebih dari 1 node)
        // hapus depan
        if (flag == 1)
        {
            Node *hapus;
            hapus = head;
            head = head->next;
            delete hapus;
        }
        // hapus belakang
        else if (flag == 2)
        {
            Node *bantu;
            bantu = head;
            while (bantu->next != tail)
            {
                bantu = bantu->next;
            }
            // Posisi bantu = node sebelum node terakhir
            delete tail;
            bantu->next = NULL;
            tail = bantu;
        }
        // hapus tengah
        else if (flag == 3)
        {
            char x[30];
            cout << "Manghapus Nama siapa : "; //
            cin >> x;
            // jika ternyata yg mau dihapus itu Node Depan
            if (strcmp(head->nama, x) == 0)
                hapus(1);
            // jika ternyata yg mau dihapus itu Node belakang
            else if (strcmp(tail->nama, x) == 0)
                hapus(2);
            else // Jika node berada di tengah
            {
                Node *bantu;
                bantu = head;
                while (bantu != NULL)
                {
                    if (strcmp(bantu->next->nama, x) == 0)
                    {
                        // hapus tengah;
                        Node *hapus;
                        hapus = bantu->next;
                        bantu->next = bantu->next->next;
                        delete hapus;
                        break; // memaksa berhenti dari loop
                    }
                    bantu = bantu->next;
                }
            }
        }
    }
}

void urut()
{
    Node *sekarang = head;
    Node *index;
    Node *temp;

    int temp_umur = 0;
    char temp_nama[20];

    if (head == NULL) // list kosong
        cout
            << "list masih kosong"
            << endl;
    else
    {
        while (sekarang != NULL)
        {
            // cout << "haha 1" << endl;
            index = sekarang->next;

            while (index != NULL)
            {
                if (sekarang->umur > index->umur)
                {
                    strcpy(temp_nama, sekarang->nama);
                    strcpy(sekarang->nama, index->nama);
                    strcpy(index->nama, temp_nama);

                    temp_umur = sekarang->umur;
                    sekarang->umur = index->umur;
                    index->umur = temp_umur;
                    // temp = sekarang;
                    // sekarang = index;
                    // index = temp;
                }
                index = index->next;
            }
            cout << sekarang->nama << " : " << sekarang->umur << endl;
            sekarang = sekarang->next;
        }
    }
}
// void hapusbelakang()
// {
//     if (head == NULL)
//         cout << "List masih kosong";
//     else if (head == tail)
//     {
//         delete head;
//         head = NULL;
//         tail = NULL;
//     }
//     else
//     {
//         Node *bantu;
//         bantu = head;
//         while (bantu->next != tail)
//         {
//             bantu = bantu->next;
//         }
//         // Posisi bantu = node sebelum node terakhir
//         delete tail;
//         bantu->next = NULL;
//         tail = bantu;
//     }
// }

int main()
{
    int pilih;
    do
    {
        // system("cls");

        cout << endl
             << "1. Menambah Data Di Belakang" << endl;
        cout << "2. Menambah Data Di Depan" << endl;
        cout << "3. Menambah Data Di Tengah" << endl;
        cout << "4. Menghapus Data Belakang" << endl;
        cout << "5. Menghapus Data Depan" << endl;
        cout << "6. Menghapus Data Tengah" << endl;
        cout << "7. Mencari Data " << endl;
        cout << "8. Menampilkan Data" << endl;
        cout << "9. Mengurutkan Data" << endl;
        cout << "10. Keluar Program" << endl;
        cout << "Pilihan Anda [1-10] : ";
        cin >> pilih;
        cout << endl;

        if (pilih == 1)
        {
            tambah_belakang();
            tampil();
        }
        else if (pilih == 2)
        {
            tambah_depan();
            tampil();
        }
        else if (pilih == 3)
        {
            tambah_depan();
            tampil();
        }
        else if (pilih == 4)
        {
            hapus(2);
            tampil();
        }
        else if (pilih == 5)
        {
            hapus(1);
            tampil();
        }
        else if (pilih == 6)
        {
            tampil();
            hapus(3);
        }
        else if (pilih == 7)
        {
            cari();
            // tampil();
        }
        else if (pilih == 8)
            tampil();
        else if (pilih == 9)
        {
            urut();
            tampil();
        }

    } while (pilih != 10);
    return 0;
}