/*旋转圆盘的解密问题*/
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

/*6个转盘，前3个存储的是即时状态，后3个存储的是初始状态！！*/
char rotors[6][27];
/*每个转盘的当前步进值*/
int steps[3];

/*顺时针旋转某个转盘一个步进，
  index表示转盘号，m表示每个转盘一共多少个字母*/
void Rotate(char *rotor, int m)
{
    int i;
    char temp;
    /*先转换为偏移值，有正有负*/
    for(i=0; i<m; i++)
        rotor[i]=rotor[i] - ('A' + i);
    
    /*旋转*/
    temp=rotor[m-1];
    for(i=m-1;i>0;i--)
        rotor[i]=rotor[i-1];
    rotor[0]=temp;
    
    /*复原为字符串，同时矫正负数值*/
    for(i=0; i<m; i++)
        rotor[i]='A' + ( (i + rotor[i] + m) % m);
}

/*整体转动一次！m为每个转盘的字符数*/
void RotateRotors(int m)
{
    steps[0]++;
    Rotate(rotors[0],m);
    if(steps[0]==m)
    {
        steps[0]=0;
        steps[1]++;
        Rotate(rotors[1],m);
    }
    if(steps[1]==m)
    {
        steps[1]=0;
        steps[2]++;
        Rotate(rotors[2],m);
    }
}

/*根据输出的密文，得出原文，都是大写字母*/
char GetPlainChar(const char* rotor, char c)
{
    char *p=strchr(rotor, c);
    return 'A'+(p-rotor);
}

/*复原到初始状态*/
void ResetRotors()
{
    steps[0]=steps[1]=steps[2]=0;
    /*设置圆盘的初始状态*/
    strcpy(rotors[0], rotors[3]);
    strcpy(rotors[1], rotors[4]);
    strcpy(rotors[2], rotors[5]);
}

int main()
{
    int m, n, count=1, i;
    char line[1024], *s;
    
    while(1)
    {
        /*读入密码数*/
        gets(line);
        m=atoi(line);
        if(m==0)
            break;
            
        /*每个test case之间插入一个空行*/
        if(count!=1) printf("\n");
        
        printf("Enigma %d:\n", count++);
        /*读入三个rotor*/
        gets(rotors[3]);
        gets(rotors[4]);
        gets(rotors[5]);
        
        /*读取输入的密文数*/
        gets(line);
        n=atoi(line);/*读取换行符*/
        
        /*解密*/
        for(i=0;i<n;i++)
        {
            /*设置圆盘的初始状态*/
            ResetRotors();
            
            gets(line);
            s=line;            
            while(*s)
            {
                *s=GetPlainChar(rotors[2],*s);
                *s=GetPlainChar(rotors[1],*s);
                *s=GetPlainChar(rotors[0],*s);
                *s=*s - 'A' + 'a';/*化为小写字母*/
                RotateRotors(m);
                s++;
            }
            printf("%s\n", line);
        }
    }
    return 0;
}