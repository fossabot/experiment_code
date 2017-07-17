#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#define MAXNUM 5
#define MAXTIME 20
struct sjf
{
    char name[8];
    int arrivetime;
    int servicetime;
    int runtime;
    int is_over;//是否运行完
    int starttime;
    int finishtime;
    int turnaroundtime;
    float rightturnaroundtime;
}p[MAXNUM];
 
 
static int j=0,k=0,l=0;//j当前正在执行的进程 k当前时间已经到达的最大进程 l是否没有进程运行
 
 
//读取进程数据
void readProcess()
{
    int i;
    char str[200];
    FILE *fp;
    char *token;
    if ((fp=fopen("Process","rt"))==NULL)
    {
        printf("读取文件失败!\n");
        getchar();
        exit(1);
    }
    printf("|--------------------------------------|\n");
    printf("|--进程名称--|--到达时间--|--服务时间--|\n");
    for (i=0;i<MAXNUM;i++)
    {
        fgets(str,200,fp);
        //printf("%s\n",str);
        token = strtok(str, " ");
        strcpy(p[i].name,token);
        printf("|     %s     |",p[i].name);
        token = strtok( NULL, " ");
        p[i].arrivetime=atof(token);
        printf("%6d      ",p[i].arrivetime);
        token = strtok( NULL, " ");
        p[i].servicetime=atof(token);
        printf("|%6d      |\n",p[i].servicetime);
        p[i].runtime=0;
        p[i].is_over=0;
    }
    fclose(fp);
}
 
void print()
{
int i,num1=0;
float num2=0;
printf("|--进程名称--|--到达时间--|--服务时间--|--开始时间--|--结束时间--|--周转时间--|--带权周转时间--|\n");
for (i=0;i<MAXNUM;i++)
{
p[i].turnaroundtime=p[i].finishtime-p[i].starttime;
p[i].rightturnaroundtime=p[i].turnaroundtime;
p[i].rightturnaroundtime/=p[i].servicetime;
num1+=p[i].turnaroundtime;
num2+=p[i].rightturnaroundtime;
printf("|     %s     |%6d      |%6d      |%6d      |%6d      |%6d      |%9.2f       |\n",p[i].name,p[i].arrivetime,p[i].servicetime,p[i].starttime,p[i].finishtime,p[i].turnaroundtime,p[i].rightturnaroundtime);
}
printf("平均周转时间:%d\n平均带权周转时间:%0.2f\n",num1/MAXNUM,num2/MAXNUM);
}
 
void sort()
{
    int i,ii;
    for(i=0;i<MAXNUM;i++)
    {
        for(ii=0;ii<i;ii++)
        {
            if((p[i].arrivetime<p[ii].arrivetime)||((p[i].arrivetime==p[ii].arrivetime)&&(p[i].servicetime<p[ii].servicetime)))
            {
                struct sjf temp;
                temp=p[i];
                p[i]=p[ii];
                p[ii]=temp;
            }
        }
    }
}
void is_over(int time)
{printf("%d.00:\t进程%d运行%d\n",time,j,p[j].runtime);
if(p[j].runtime==1)//开始时间
{p[j].starttime=time;}
    if(p[j].runtime==p[j].servicetime)
    {
    p[j].is_over=1;
    printf("%d.00:\t进程%d运行结束\n",time,j);
    p[j].finishtime=time+1;
    int m;
    int temp=j;
    for(m=0;m<=k;m++)
    {if(p[m].is_over==0)
    {
    temp=m;//从到达的进程里选择一个没有执行完的进程
    break;//跳出循环
    }}
    for(m=0;m<=k;m++)
    {
    if(p[m].is_over==0){
        if(p[m].servicetime<p[temp].servicetime)
        {temp=m;}}
    }
    //判断是否没有进程了
    if(temp==j)
    {printf("%d.00:\t现在没有挂起的进程了!!\n",time);
    l=1;
    }else{
    j=temp;
    printf("%d.00:\t下一秒将运行进程%d\n",time,j);
    l=0;
    }
 
    }else{//没有运行完
 
    }
}
void sjf()
{
int time;
int i;
for(time=0;time<MAXTIME;time++)
{
int aaa=0;
    for(i=0;i<MAXNUM;i++)
    {
    if(p[i].arrivetime==time&&i!=0)
    {
        k=i;
        p[j].runtime+=1;
        is_over(time);
        aaa=1;
        printf("%d.00:\t进程%d到达\n",time,k);
        if(l==1)
        {
        j=i;
        printf("%d.00:\t进程%d开始运行\n",time,j);
        l=0;
        }else{
        if(p[i].servicetime<p[j].servicetime)
        {//抢占
 
        printf("%d.00:\t%d进程抢占,%d进程挂起\n",time,i,j);
        j=i;
        }else{
 
        }
        }
 
    }else{
        if(p[i].arrivetime==time&&i==0)//i==0
        {
        p[i].starttime=p[i].arrivetime;
        k=0;
        aaa=1;
        j=0;
        p[j].runtime+=1;
        printf("%d.00:\t进程%d开始运行\n",time,j);
        is_over(time);
        }
    }
    }
if(aaa==0&&l==0)
{
p[j].runtime+=1;
is_over(time);
}
if(aaa==0&&l==1)
{printf("%d.00:\t无进程运行\n",time);}
}
 
}
 
 
int main()
{
readProcess();
sort();
sjf();
print();
 
return 0;
}
// <http://0x55aa.sinaapp.com/%e7%ae%97%e6%b3%95-%e7%bc%96%e7%a8%8b/423.html> 
