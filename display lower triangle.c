#include<stdio.h>
#include<conio.h>
#include<stdlib.h>

int main()
{
    int a[3][3],i,j;
    printf("Enter nine numbers for matrix");

    for(i=0;i<=2;i++)
      for(j=0;j<=2;j++)
        scanf("%d",&a[i][j]);

    printf("\nMatrix entered by you is \n");

    for(i=0;i<=2;i++)
    {
        for(j=0;j<=2;j++)
        {
            printf("  %d",a[i][j]);
        }
        printf("\n\n");
    }

    printf("\nLower triangle of this matrix is \n");

    for(i=0;i<=2;i++)
    {
        for(j=0;j<=2;j++)
        {
            if(i>=j&&i+j>=2)
              printf("  %d",a[i][j]);
            else
              printf("   ");
        }
      printf("\n\n");
    }

 getch();
}
