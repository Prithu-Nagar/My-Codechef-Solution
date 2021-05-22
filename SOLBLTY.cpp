#include <iostream>
using namespace std;

int main() {
	int test,n,x,y,sum;
	cin>>test;
	while(test--)
	{
	    cin>>n>>x>>y;
	    sum=x+(100-n)*y;
	    cout<<sum*10<<endl;
	}
	return 0;
}
