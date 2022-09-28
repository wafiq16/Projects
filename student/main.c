#include "stdio.h"
#include "string.h"

int get_gps(double Tugas, double UTS, double UAS);
char get_grade(float gps);

int main()
{
    char nomor_siswa[5][20], nama_siswa[5][20], tidak_lulus[100], lulus[100], temp[20];
    float GPS[5], UTS[5], UAS[5], Tugas[5];
    for (int i = 0; i < 5; i++)
    {
        printf("masukkan nama siswa ke %d : ", i + 1);
        scanf("%s", &nama_siswa[i]);
        printf("masukkan nomor siswa ke %d : ", i + 1);
        scanf("%s", &nomor_siswa[i]);
    }

    FILE *f = fopen("student.txt", "w");
    if (f == NULL)
    {
        printf("Error opening file!\n");
        // exit(1);
        return 0;
    }

    FILE *fp = fopen("progcon.txt", "w");
    if (fp == NULL)
    {
        printf("Error opening file!\n");
        // exit(1);
        return 0;
    }

    FILE *fw = fopen("web.txt", "w");
    if (fw == NULL)
    {
        printf("Error opening file!\n");
        // exit(1);
        return 0;
    }

    for (int i = 0; i < 5; i++)
    {
        printf("nama siswa ke %d : %s", i + 1, nama_siswa[i]);
        printf(" nomor siswa ke %d : %s \n", i + 1, nomor_siswa[i]);
        fprintf(f, "%s %s\n", nomor_siswa[i], nama_siswa[i]);
    }

    for (int i = 0; i < 5; i++)
    {
        printf("masukkan nilai siswa ke %d : %s \n", i + 1, nama_siswa[i]);
        printf("Nilai Tugas : ");
        scanf("%f", &Tugas[i]);
        printf("Nilai UTS : ");
        scanf("%f", &UTS[i]);
        printf("Nilai UAS : ");
        scanf("%f", &UAS[i]);
    }

    for (int i = 0; i < 5; i++)
    {
        // printf("nama siswa ke %d : %s", i + 1, nama_siswa[i]);
        // printf(" nomor siswa ke %d : %s \n", i + 1, nomor_siswa[i]);
        printf("\n\nsiswa ke %d : %s \n", i + 1, nama_siswa[i]);
        printf("Nilai Tugas : ");
        printf("%f", Tugas[i]);
        printf("  Nilai UTS : ");
        printf("%f", UTS[i]);
        printf("  Nilai UAS : ");
        printf("%f", UAS[i]);

        fprintf(fp, "%f %f %f\n", Tugas[i], UTS[i], UAS[i]);
        fprintf(fw, "%f %f %f\n", Tugas[i], UTS[i], UAS[i]);
    }

    fclose(f);
    fclose(fp);
    fclose(fw);

    FILE *fstudent;
    fstudent = fopen("student.txt", "r");

    FILE *fprogcon;
    fprogcon = fopen("progcon.txt", "r");

    FILE *fweb;
    fweb = fopen("web.txt", "r");

    FILE *fout;
    fout = fopen("ouput.txt", "w");

    for (int i = 0; i < 5; i++)
    {
        fscanf(fstudent, "%s %s", &nomor_siswa[i], &nama_siswa[i]);
    }

    for (int i = 0; i < 5; i++)
    {
        fscanf(fprogcon, "%f %f %f", &Tugas[i], &UTS[i], &UAS[i]);
    }

    for (int i = 0; i < 5; i++)
    {
        // printf("nama siswa ke %d : %s", i + 1, nama_siswa[i]);
        // printf(" nomor siswa ke %d : %s \n", i + 1, nomor_siswa[i]);
    }

    printf("%-10s%-13s%-13s%-13s%-13s%-13s\n\n", "Name", "Assignment", "Mid Exam", "Final Exam", "Final Score", "Grade");

    for (int i = 0; i < 5; i++)
    {
        // printf("\n\nsiswa ke %d : %s \n", i + 1, nama_siswa[i]);
        // printf("Nilai Tugas : ");
        // printf("%f", Tugas[i]);
        // printf("  Nilai UTS : ");
        // printf("%f", UTS[i]);
        // printf("  Nilai UAS : ");
        // printf("%f", UAS[i]);
        GPS[i] = get_gps(Tugas[i], UTS[i], UAS[i]);
        printf("%-10s%-13f%-13f%-13f%-13.2f%-13c\n", nama_siswa[i], Tugas[i], UTS[i], UAS[i], GPS[i], get_grade(GPS[i]));
        if (GPS[i] <= 55)
        {
            sprintf(temp, " %s", nama_siswa[i]);
            strcat(tidak_lulus, temp);
        }
        else
        {
            sprintf(temp, " %s", nama_siswa[i]);
            strcat(lulus, temp);
            // sprintf(lulus, "%s ", nama_siswa[i]);
        }
        // printf("  GPS : ");
        // printf("%f", GPS[i]);
        // printf("  Grade : ");
        // printf("%c", get_grade(GPS[i]));
    }
    printf("lulus : %s", lulus);
    printf("\ntidak lulus : %s", tidak_lulus);
    for (int i = 0; i < 5; i++)
    {
        fprintf(fout, "%s %s %f %c\n", nomor_siswa[i], nama_siswa[i], GPS[i], get_grade(GPS[i]));
    }

    fclose(fstudent);
    fclose(fprogcon);
    fclose(fweb);
    fclose(fout);

    return 0;
}

int get_gps(double Tugas, double UTS, double UAS)
{
    return Tugas * 30 / 100 + UTS * 30 / 100 + UAS * 40 / 100;
}

char get_grade(float gps)
{
    char grade;
    if (gps >= 85)
    {
        grade = 'A';
    }
    else if (gps >= 70 && gps < 85)
    {
        grade = 'B';
    }
    else if (gps >= 60 && gps < 70)
    {
        grade = 'C';
    }
    else if (gps >= 55 && gps < 60)
    {
        grade = 'D';
    }
    else if (gps < 55)
    {
        grade = 'E';
    }
    return grade;
}