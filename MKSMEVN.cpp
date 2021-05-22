#include <iostream>
using namespace std;

int main()
{
    int test;
    cin>>test;
    while(test--)
    {
        int n,i;
        cin>>n;
        int a[n];
        int sum=0;
        int answer;
        for(i=0;i<n;i++)
        {
            cin>>a[i];
            sum+=a[i];
        }
        if(sum%2==0)
        {
            cout<<0<<endl;
        }
        else
        {
            answer=0;
            for(i=0;i<n;i++)
            {
                if((a[i]%2==0) && ((a[i]+1)/2-1<=0))
                {
                    answer=1;
                    break;
                }
            }
            if(answer==0)
            {
                cout<<-1<<endl;
            }
            else
            {
                cout<<1<<endl;
            }
        }
    }
	return 0;
}
