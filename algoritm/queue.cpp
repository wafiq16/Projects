#include<iostream>

using namespace std;

struct queue 
{
	char nama[30];
	int umur;
};


struct queue sembako[10];

int maks=5;
int head=1;
int tail=1;
// int klmtail=60;

void lambatkan()
{
	int x;
	for(x=1;x<=100000;x++)
	   cout<<"";
}

void tampil(int tail){
{
	int z;
    cout << "head = "<< head << endl;
    cout << "tail = "<< tail << endl;
	for(z=1;z<=tail-1;z++)
	{
        cout << "[" ; 
        cout<<"Nama : "; 
        cout << sembako[z].nama;
        cout<<" Umur : "; 
        cout<< sembako[z].umur;
		cout << "]" ;
	}
}
}

void geser(struct queue *a)
{
	int z;
	for(z=1;z<=tail;z++)
	{
        cout << "[" ; 
        printf("%s",a[z].nama);
        printf(" %d",a[z].umur);
		cout << "]" ;
	}
}

void enqueue(int x)			//x=TAIL
{
	if(x<=maks)
	{
        cout<<"Nama : "; 
        cin>>sembako[x].nama;
        cout<<"Umur : "; 
        cin>>sembako[x].umur;
		geser(sembako);
		tail++;
	}
	else
	{
		cout<<"Sorry... Queue is full!!!";
	}
}

void geser1(struct queue *a)
{
	int x;
    for(x=1;x<=tail-2;x++)
	{
        cout << "[" ; 
        printf("%s",a[x].nama);
        printf(" %d",a[x].umur);
		cout << "]" ;
	}
}

void dequeue(int x)		//x=HEAD
{
	if(tail>head) 
	{
		//njejek
		for(x=1;x<=tail-2;x++)
			sembako[x] = sembako[x+1];

		geser1(sembako);
		tail--;
	}
	else
	{
		cout<< endl <<"Sorry queue is Empty...!!!"<<endl;
	}
}

int main()
{
	int pilih = 0;
	while(pilih != 4)
	{
		// tampil();
        cout << endl;
		cout<<"Menu Utama Antrian"<<endl;
		cout<<"1. Enqueue"<<endl;
		cout<<"2. Dequeue"<<endl;
		cout<<"3. Display Data"<<endl;
		cout<<"4. Exit"<<endl;
		cout<<"Inputkan Pilihan Anda : ";
        cin >> pilih;
		if(pilih==1) enqueue(tail);
		else if(pilih==2) dequeue(head);
		else if(pilih==3) tampil(tail);
        else if(pilih==4) {
            cout << "Keluar :)" << endl;
            break;
        }
        else {
            cout << "Menu tidak sesuai" << endl;
            continue;
        }
    }	
	return 0;
}