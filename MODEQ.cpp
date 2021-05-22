#include <iostream>
#include<bits/stdc++.h>
using namespace std;
typedef unsigned long long inta;
int main()
{
	inta test;
	cin>>test;
	while(test--)
	{
	    inta n,m,i,a,j;
	    cin>>n>>m;
	    inta c=0;
	    vector <inta> s(n+1,1);
	    for(i=2;i<n+1;i++)
	    {
	        a=m%i;
	        c+=s[a];
	        for(j=a;j<n+1;j+=i)
	            s[j]++;
	    }
	    cout<<c<<"\n";
	}
	return 0;
}
