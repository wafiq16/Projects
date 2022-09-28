#include "stdio.h"

int main()
{
    int assignment_score[10], midterm_exam_score[10], final_exam_score[10], temp[3];
    double final_score[10], average[3];

    printf("input score for each student\n");

    // input score
    for (int i = 0; i < 10; i++)
    {
        printf("\nstudent - %d\n", i + 1);
        printf("assignment_score = ");
        scanf("%d", &assignment_score[i]);
        printf("midterm_exam_score = ");
        scanf("%d", &midterm_exam_score[i]);
        printf("final_exam_score = ");
        scanf("%d", &final_exam_score[i]);
    }

    printf("\n");

    // final score
    for (int i = 0; i < 10; i++)
    {
        final_score[i] = ((double)assignment_score[i] * 30 / 100) + ((double)midterm_exam_score[i] * 30 / 100) + ((double)final_exam_score[i] * 40 / 100);
        printf("Final score for student - %d = %f\n", i + 1, final_score[i]);
    }

    printf("\n");

    // convert to grade
    for (int i = 0; i < 10; i++)
    {
        if (final_score[i] > 80)
        {
            printf("Grade student - %d is A\n", i + 1);
        }
        else if (final_score[i] <= 80 && final_score[i] > 65)
        {
            printf("Grade student - %d is B\n", i + 1);
        }
        else if (final_score[i] <= 65 && final_score[i] > 50)
        {
            printf("Grade student - %d is C\n", i + 1);
        }
        else if (final_score[i] <= 50 && final_score[i] > 40)
        {
            printf("Grade student - %d is D\n", i + 1);
        }
        else
        {
            printf("Grade student - %d is E\n", i + 1);
        }
    }

    printf("\n");

    // sorting
    for (int i = 0; i < 10; i++)
    {
        for (int j = 0; j < 10; j++)
        {
            if (assignment_score[j] > assignment_score[i])
            {
                temp[0] = assignment_score[j];
                assignment_score[j] = assignment_score[i];
                assignment_score[i] = temp[0];
            }

            if (midterm_exam_score[j] > midterm_exam_score[i])
            {
                temp[1] = midterm_exam_score[j];
                midterm_exam_score[j] = midterm_exam_score[i];
                midterm_exam_score[i] = temp[1];
            }

            if (final_exam_score[j] > final_exam_score[i])
            {
                temp[2] = final_exam_score[j];
                final_exam_score[j] = final_exam_score[i];
                final_exam_score[i] = temp[2];
            }
        }
    }
    // max, min, average
    for (int i = 0; i < 10; i++)
    {
        average[0] += assignment_score[i];
        average[1] += midterm_exam_score[i];
        average[2] += final_exam_score[i];
    }

    printf("\n");

    printf("assignment score\n");
    printf("average score is %f\n", average[0] / 10);
    printf("minimum score is %d \n", assignment_score[0]);
    printf("maximum score is %d \n", assignment_score[10 - 1]);

    printf("\n");

    printf("midterm exam score\n");
    printf("average score is %f\n", average[1] / 10);
    printf("minimum score is %d \n", midterm_exam_score[0]);
    printf("maximum score is %d \n", midterm_exam_score[10 - 1]);

    printf("\n");

    printf("final exam score\n");
    printf("average score is %f \n", average[2] / 10);
    printf("minimum score is %d \n", final_exam_score[0]);
    printf("maximum score is %d \n", final_exam_score[10 - 1]);

    printf("\n");

    return 0;
}