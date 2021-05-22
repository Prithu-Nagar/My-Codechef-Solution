#include<bits/stdc++.h>
using namespace std;

int main() {
	int test;
	cin>>test;
	while(test--)
	{
	    int n,i,result;
	    cin>>n;
	    vector<pair<int,int>> p,q;
	    for(i=0;i<n;i++)
	    {
	        int x;
	        cin>>x;
	        p.push_back({i+1,x});
	    }
	    if(n==2)
	    {
	        cout<<"1\n";
	        continue;
	    }
	    q.push_back(p[0]);
	    q.push_back(p[1]);
	    result=1;
	    int len=q.size();
	    for(i=2;i<n;i++)
	    {
	        while(q.size()>=2)
	        {
	            double l1=((double)q[len-1].second - (double)q[len-2].second)/((double)q[len-1].first - (double)q[len-2].first);
	            double l2=((double)p[i].second - (double)q[len-1].second)/((double)p[i].first - (double)q[len-1].first);
	            if(l1<=l2)
	            {
	                q.pop_back();
	                len--;
	            }
	            else
	                break;
	        }
	        q.push_back(p[i]);
	        len++;
	        result=max(result,q[len-1].first - q[len-2].first);
	    }
	    cout<<result<<endl;
	}
	return 0;
}
