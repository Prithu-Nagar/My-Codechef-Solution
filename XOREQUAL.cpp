#include <iostream>
#include <bits/stdc++.h>
using namespace std;
#define mod 1000000007
#define lli long long int
int main() {
	int test,i;
	cin>>test;
	lli n;
	for(i=0;i<test;i++)
	{
	    cin>>n;
	    lli y;
	    if(n==1)
	        cout<<"1\n";
	    else
	    {
	        n-=1;
	        lli x=2,y=1;
	        while(n>0)
	        {
	            if(n&1)
	            y=y*x%mod;
	            x=x*x%mod;
	            n>>=1;
	        }
	        cout<<y<<"\n";
	    }
	}
	return 0;
}