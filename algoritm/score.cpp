#include "stdio.h"

int main()
{
    int total = 0;
    // how much score will be
    printf("Welcome, how much your score will be?\n");
    scanf("%d", &total);

    int score[total];
    // input score
    for (int i = 0; i < total; i++)
    {
        printf("score-%d = ", i + 1);
        scanf("%d", &score[i]);
    }

    // sort
    int temp = 0;
    for (int i = 0; i < total; i++)
    {
        for (int j = 0; j < total; j++)
        {
            if (score[j] > score[i])
            {
                temp = score[j];
                score[j] = score[i];
                score[i] = temp;
            }
        }
    }
    // show sort result
    for (int i = 0; i < total; i++)
    {
        printf("%d\n", score[i]);
    }

    // max min score
    printf("minimum score is %d \n", score[0]);
    printf("maximum score is %d \n", score[total - 1]);

    // average
    double average = 0;
    for (int i = 0; i < total; i++)
    {
        average += score[i];
    }
    average /= total;
    printf("average is %f \n", average);

    int count_A = 0;
    int count_B = 0;
    int count_C = 0;
    int count_D = 0;
    int count_E = 0;
    // grade
    for (int i = 0; i < total; i++)
    {
        // cout << "Math "<< endl;
        if (score[i] > 85)
        {
            count_A++;
        }
        else if (score[i] < 85 && score[i] >= 70)
        {

            count_B++;
        }
        else if (score[i] < 70 && score[i] >= 60)
        {

            count_C++;
        }
        else if (score[i] < 60 && score[i] >= 55)
        {

            count_D++;
        }
        else if (score[i] < 55)
        {
            count_E++;
        }
    }
    printf("Total A = %d\n", count_A);
    printf("Total B = %d\n", count_B);
    printf("Total C = %d\n", count_C);
    printf("Total D = %d\n", count_D);
    printf("Total E = %d\n", count_E);
    // median
    double median = 0;
    if (total % 2 == 0)
    {
        median = (double)(score[total / 2] + score[(total / 2) - 1]) / 2;
        printf("median is %f \n", median);
    }
    else
    {
        median = score[(total) / 2];
        printf("median is %f \n", median);
    }

    // mode
    int maxValue = 0, maxCount = 0, i, j;

    for (i = 0; i < total; ++i)
    {
        int count = 0;

        for (j = 0; j < total; ++j)
        {
            if (score[j] == score[i])
                ++count;
        }

        if (count > maxCount)
        {
            maxCount = count;
            maxValue = score[i];
        }
    }
    printf("mode is %d \n", maxValue);

    return 0;
}
