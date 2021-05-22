#include<iostream>
#include<bits/stdc++.h>
using namespace std;

int main() {
	int test;
	cin>>test;
	while(test--)
	{
	    int n,x,i;
	    cin>>n>>x;
	    pair<int,int> a[n];
	    for(i=0;i<n;i++)
	    {
	        cin>>a[i].second>>a[i].first;
	    }
	    sort(a,a+n);
	    for(i=n-1;i>=0;i--)
	    {
	        if(a[i].second<=x)
	        {
	            cout<<a[i].first<<endl;
	            break;
	        }
	    }
	}
	return 0;
}
