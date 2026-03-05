#include <stdio.h>

int visited[4][4][2];

int valid(int m,int c)
{
    int mr = 3-m;
    int cr = 3-c;

    if(m<0 || c<0 || m>3 || c>3)
        return 0;

    if(m>0 && c>m)
        return 0;

    if(mr>0 && cr>mr)
        return 0;

    return 1;
}

void BFS()
{
    int queue[100][3];
    int front=0,rear=0;

    queue[rear][0]=3;
    queue[rear][1]=3;
    queue[rear][2]=0;
    rear++;

    visited[3][3][0]=1;

    int move[5][2]={{1,0},{2,0},{0,1},{0,2},{1,1}};

    while(front<rear)
    {
        int m=queue[front][0];
        int c=queue[front][1];
        int boat=queue[front][2];

        front++;

        printf("M:%d C:%d Boat:%d\n",m,c,boat);

        if(m==0 && c==0 && boat==1)
        {
            printf("Goal Reached\n");
            return;
        }

        for(int i=0;i<5;i++)
        {
            int nm=m,nc=c,nb=boat;

            if(boat==0)
            {
                nm-=move[i][0];
                nc-=move[i][1];
                nb=1;
            }
            else
            {
                nm+=move[i][0];
                nc+=move[i][1];
                nb=0;
            }

            if(valid(nm,nc) && !visited[nm][nc][nb])
            {
                visited[nm][nc][nb]=1;

                queue[rear][0]=nm;
                queue[rear][1]=nc;
                queue[rear][2]=nb;
                rear++;
            }
        }
    }
}

int main()
{
    BFS();
}