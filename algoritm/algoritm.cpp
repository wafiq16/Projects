#include "stdio.h"
#include <algorithm>
// Global Variable

int count_semester = 0, count_A = 0, count_B = 0, count_C = 0, count_D = 0, count_E = 0;

int each_A[10];
int each_B[10];
int each_C[10];
int each_D[10];
int each_E[10];

int temp_score[5][10];

double GPA[10], total_gpa;

struct IPK
{
    int math, science, language, social, nationality;
};

IPK semester[10];

void show_grade();
void lowest_highest();
void count_grade();
void GPA_ALL();

int main()
{

    // input total semester
    printf("total semester = \n");
    scanf("%d", &count_semester);

    // input score each major every semester
    for (int i = 0; i < count_semester; i++)
    {
        printf("\nSemester %d \n", i + 1);
        printf("Range score 0-100\n");
        printf("Math = ");
        scanf("%d", &semester[i].math);
        printf("Science = ");
        scanf("%d", &semester[i].science);
        printf("Language = ");
        scanf("%d", &semester[i].language);
        printf("Social = ");
        scanf("%d", &semester[i].social);
        printf("Nationality = ");
        scanf("%d", &semester[i].nationality);
    }
    // a && b in one function
    show_grade();
    // c
    // lowest_highest();
    // d
    count_grade();
    // e
    GPA_ALL();

    return 0;
}

void show_grade()
{
    // convert number to grade based rules and print grade
    for (int i = 0; i < count_semester; i++)
    {
        printf("Semester %d\n", i + 1);
        // cout << "Math "<< endl;
        if (semester[i].math > 85)
        {
            printf("math grade is A\n");
            count_A++;
            each_A[i]++;
        }
        else if (semester[i].math < 85 && semester[i].math >= 70)
        {
            printf("math grade is B\n");
            count_B++;
            each_B[i]++;
        }
        else if (semester[i].math < 70 && semester[i].math >= 60)
        {
            printf("math grade is C\n");
            count_C++;
            each_C[i]++;
        }
        else if (semester[i].math < 60 && semester[i].math >= 55)
        {
            printf("math grade is D\n");
            count_D++;
            each_D[i]++;
        }
        else if (semester[i].math < 55)
        {
            printf("math grade is E\n");
            count_E++;
            each_E[i]++;
        }
        // cout << "Science "<< endl;
        if (semester[i].science > 85)
        {
            printf("science grade is A\n");
            count_A++;
            each_A[i]++;
        }
        else if (semester[i].science < 85 && semester[i].science >= 70)
        {
            printf("science grade is B\n");
            count_B++;
            each_B[i]++;
        }
        else if (semester[i].science < 70 && semester[i].science >= 60)
        {
            printf("science grade is C\n");
            count_C++;
            each_C[i]++;
        }
        else if (semester[i].science < 60 && semester[i].science >= 55)
        {
            printf("science grade is D\n");
            count_D++;
            each_D[i]++;
        }
        else if (semester[i].science < 55)
        {
            printf("science grade is E\n");
            count_E++;
            each_E[i]++;
        }
        if (semester[i].language > 85)
        {
            printf("language grade is A\n");
            count_A++;
            each_A[i]++;
        }
        else if (semester[i].language < 85 && semester[i].language >= 70)
        {
            printf("language grade is B\n");
            count_B++;
            each_B[i]++;
        }
        else if (semester[i].language < 70 && semester[i].language >= 60)
        {
            printf("language grade is C\n");
            count_C++;
            each_C[i]++;
        }
        else if (semester[i].language < 60 && semester[i].language >= 55)
        {
            printf("language grade is D\n");
            count_D++;
            each_D[i]++;
        }
        else if (semester[i].language < 55)
        {
            printf("language grade is E\n");
            count_E++;
            each_E[i]++;
        }

        if (semester[i].social > 85)
        {
            printf("social grade is A\n");
            count_A++;
            each_A[i]++;
        }
        else if (semester[i].social < 85 && semester[i].social >= 70)
        {
            printf("social grade is B\n");
            count_B++;
            each_B[i]++;
        }
        else if (semester[i].social < 70 && semester[i].social >= 60)
        {
            printf("social grade is C\n");
            count_C++;
            each_C[i]++;
        }
        else if (semester[i].social < 60 && semester[i].social >= 55)
        {
            printf("social grade is D\n");
            count_D++;
            each_D[i]++;
        }
        else if (semester[i].social < 55)
        {
            printf("social grade is E\n");
            count_E++;
            each_E[i]++;
        }

        if (semester[i].nationality > 85)
        {
            printf("nationality grade is A\n");
            count_A++;
            each_A[i]++;
        }
        else if (semester[i].nationality < 85 && semester[i].nationality >= 70)
        {
            printf("nationality grade is B\n");
            count_B++;
            each_B[i]++;
        }
        else if (semester[i].nationality < 70 && semester[i].nationality >= 60)
        {
            printf("nationality grade is C\n");
            count_C++;
            each_C[i]++;
        }
        else if (semester[i].nationality < 60 && semester[i].nationality >= 55)
        {
            printf("nationality grade is D\n");
            count_D++;
            each_D[i]++;
        }
        else if (semester[i].nationality < 55)
        {
            printf("nationality grade is E\n");
            count_E++;
            each_E[i]++;
        }
        printf("semester = %d \n", i + 1);
        // get GPA each semester
        GPA[i] = (each_A[i] * 4 * 3) + (each_B[i] * 3 * 3) + (each_C[i] * 2 * 3) + (each_D[i] * 1 * 3) + (each_E[i] * 0 * 3);
        // 60 is total maximum point. 4(A grade) * 3(SKS) * 5(total subject)
        GPA[i] = GPA[i] * 4 / 60;
        printf("GPA = %f\n", GPA[i]);
    }
}

void lowest_highest()
{
    for (int i = 0; i < 5; i++)
    {
        temp_score[i][0] = semester[i].math;
        temp_score[i][1] = semester[i].science;
        temp_score[i][2] = semester[i].language;
        temp_score[i][3] = semester[i].social;
        temp_score[i][4] = semester[i].nationality;
    }
    for (int i = 0; i < 10; i++)
    {
        int n = sizeof(temp_score[i]) / sizeof(temp_score[i][0]);
        std::sort(temp_score, temp_score + n);
        printf("semester terkecil = %d, terbesar = %d", temp_score[i][0], temp_score[i][4]);
    }
}

void GPA_ALL()
{
    for (int i = 0; i < count_semester; i++)
    {
        total_gpa += GPA[i];
    }
    total_gpa = total_gpa / count_semester;
    printf("Final GPA Score = %f \n", total_gpa);
}

void count_grade()
{
    printf("total A = %d\n", count_A);
    printf("total B = %d\n", count_B);
    printf("total C = %d\n", count_C);
    printf("total D = %d\n", count_D);
    printf("total E = %d\n", count_E);
}