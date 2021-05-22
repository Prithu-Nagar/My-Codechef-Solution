#include <iostream>
using namespace std;
#include<bits/stdc++.h>
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);
	int n=4e6+5;
	int a[n],b[n],i,j;
	for(i=0;i<n;i++)
	{
	    a[i]=0;
	    b[i]=i;
	}
	for(i=2;i<n;i++)
	{
	    if(b[i]==i)
	    {
	        b[i]=i-1;
	        for(j=2*i;j<n;j+=i)
	            b[j]=(b[j]/i)*(i-1);
	    }
	}
	for(i=1;i<n;i++)
	{
	    a[i]+=i-1;
	    for(j=2*i;j<n;j+=i)
	        a[j]+=i*((1+b[j/i])/2);
	}
	int test,k;
	cin>>test;
	while(test--)
	{
	    cin>>k;
	    cout<<a[4*k+1]<<"\n";
	}
	return 0;
}
