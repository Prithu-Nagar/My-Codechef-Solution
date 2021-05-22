#include <iostream>
#include<bits/stdc++.h>
using namespace std;

long long int func(long long n,long long e,long long h,long long a,long long b,long long c);
long long int maxv(long long num1, long long num2);
long long int minv(long long num1, long long num2);
int main() {
    int t;
    cin>>t;
    while(t--)
    {
        long long n,e,h,a,b,c;
        cin>>n>>e>>h>>a>>b>>c;
        long long int x;
        x=func(n,e,h,a,b,c);
        if(x==1e15)
            cout<<-1<<endl;
        else
            cout<<x<<endl;
    }
	return 0;
}
long long int func(long long int n,long long int e,long long int h,long long int a,long long int b,long long int c)
{
    long long int ans=1e15,x;
    
    if(n<=0)
    {
        return 0;
    }
    if((n<=e) && (n<=h))
    {
        ans=minv(ans,n*c);
    }
    if(2*n<=e)
    {
        ans=minv(ans,n*a);
    }
    if(3*n<=h)
    {
        ans=minv(ans,n*b);
    }
    if(((h-n)/2>=1) && ((h-n)/2>=n-e))
    {
        if (b-c<0)
        {
            x=minv(n-1,(h-n)/2);
            ans=minv(ans,(b-c)*x+n*c);
        }
        else
        {
            x=maxv(1,n-e);
            ans=minv(ans,(b-c)*x+n*c);
        }
    }
    if( e-n>=1 && e-n >= n-h)
    {   
        if (a-c<0)
        {   
            x=minv(n-1,e-n);
            ans=minv(ans,(a-c)*x+n*c);
        }
        else
        {
            x=maxv(1,n-h);
            ans=minv(ans,(a-c)*x+n*c);
        }
    }
    if ((e/2)>=1 && (e/2 >=(3*n-h+2)/3))
    {
        if ((a-b)<0)
        {
            x=minv(n-1,e/2);
            ans=minv(ans,(a-b)*x+n*b);
        }
        else
        {
            x=maxv(1,(3*n-h+2)/3);
            ans=minv(ans,(a-b)*x+n*b);
        }
    }
    if((e>=3) && (h>=4) && (n>=3))
    {
        ans=minv(ans,a+b+c+func(n-3,e-3,h-4,a,b,c));
    }
    return ans;
}
long long int maxv(long long int num1, long long int num2)
{
    if(num1>num2)
        return num1;
    return num2;
}
long long int minv(long long int num1, long long int num2) 
{
    if(num1>num2)
        return num2;
    return num1;
}