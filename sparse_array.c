#include<stdio.h>

int main()
{
	int arr1[50][50]={0};
	int arr2[50][50]={0};
	int mul[50][50]={0};
	int n;
	int i=0,j=0,c=0;
	int count1=0,count2=0;

	int pos1[5000]={0},pos2[5000]={0};

	printf("Enter the value of n where n x n is the order of matrix:");
	scanf("%d",&n);
	
	printf("Enter the entries of the matrix 1\n");

	for(i=0;i<n;i++)
	{
		for(j=0;j<n;j++)
		{
			scanf("%d",&arr1[i][j]);
			if(arr1[i][j]!=0)
			{
				pos1[c]=i;
				pos1[c+1]=j; 
				c+=2;
				count1++;
			}
		}
	}

	c=0;	

	printf("Enter the entries of the matrix 2\n");
	for(i=0;i<n;i++)
	{
		for(j=0;j<n;j++)
		{
			scanf("%d",&arr2[i][j]);
			if(arr2[i][j]!=0)
			{
				pos2[c]=j;
				pos2[c+1]=i;
				c+=2;
				count2++;
			}
		}
	}



	



	int sum[50]={0};
	int curr1=pos1[0];

	for(i=0;i<count1;i++)
	{
		if(pos1[2*i]!=curr1)
		{
			for(j=0;j<n;j++)
			{
				mul[curr1][j]=sum[j];
				sum[j]=0;
			}
			curr1=pos1[2*i];
		}

		for(j=0;j<count2;j++)
		{
			

			if(pos1[2*i+1]==pos2[2*j+1])
			{
				sum[pos2[2*j]]+=arr1[curr1][pos1[2*i+1]]*arr2[pos2[2*j+1]][pos2[2*j]];
			}
		}
	}

	for(j=0;j<n;j++)
		mul[curr1][j]=sum[j];



	printf("Matrix 1:-\n");
	for(i=0;i<n;i++)
	{
		for(j=0;j<n;j++)
			printf("%d ",arr1[i][j]);
		printf("\n");
	}

	printf("Matrix 2:-\n");
	for(i=0;i<n;i++)
	{
		for(j=0;j<n;j++)
			printf("%d ",arr2[i][j]);
		printf("\n");
	}
	printf("Multiplication Matrix:-\n");
	for(i=0;i<n;i++)
	{
		for(j=0;j<n;j++)
			printf("%d ",mul[i][j]);
		printf("\n");
	}
} 
