
#include<stdio.h>
#include<stdlib.h>

struct node
{
	int r;
	int c;
	struct node *next;
} *top1,*top2;

int main()
{
	int arr1[50][50]={0};
	int arr2[50][50]={0};
	int mul[50][50]={0};
	int n;
	int i=0,j=0,c=0;
	struct node *curr=NULL;


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
				struct node *temp=(struct node*)malloc(sizeof(struct node));
				temp->r=i;
				temp->c=j;
				temp->next=NULL;
				if(top1==NULL)
				{
					top1=temp;
					curr=temp;
				}
				else
				{
					curr->next=temp;
					curr=temp;
				}
			}
		}
	}


	printf("Enter the entries of the matrix 2\n");
	for(i=0;i<n;i++)
	{
		for(j=0;j<n;j++)
		{
			scanf("%d",&arr2[i][j]);
			if(arr2[i][j]!=0)
			{
				struct node *temp=(struct node*)malloc(sizeof(struct node));
				temp->r=i;
				temp->c=j;
				temp->next=NULL;
				if(top2==NULL)
				{
					top2=temp;
					curr=temp;
				}
				else
				{
					curr->next=temp;
					curr=temp;
				}
			}
		}
	}

	int sum[50]={0};
	int curr1;
	if(top1!=NULL)
		curr1=top1->r;



	while(top1!=NULL)
	{
		if(top1->r!=curr1)
		{
			for(j=0;j<n;j++)
			{
				mul[curr1][j]=sum[j];
				sum[j]=0;
			}
			curr1=top1->r;
		}

		struct node *temp=top2;

		while(temp!=NULL)
		{
			if(temp->r==top1->c)
			{
				sum[temp->c]+=arr1[curr1][top1->c]*arr2[temp->r][temp->c];
			}
			temp=temp->next;
		}
		top1=top1->next;
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
