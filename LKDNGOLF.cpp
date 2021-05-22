#include <iostream>
using namespace std;

int main() {
	int test,n,x,y,k;
	cin>>test;
	while(test--)
	{
	    cin>>n>>x>>k;
	    y=(n+1)%k;
	    if(x%k==0 || x%k==y)
	        cout<<"Yes\n";
	    else
	        cout<<"No\n";
	}
	return 0;
}
