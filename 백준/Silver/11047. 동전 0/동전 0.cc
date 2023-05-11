#include <iostream>
#include <vector>
#define endl "\n"

using namespace std;

int N, K, answer;
vector<int> v(10);

int main(void)
{
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr);

	cin >> N >> K;
	for (int i = 0; i < N; i++)
		cin >> v[i]; 
	while (K)
	{
		int coin = 0;
		for (int i = 0; i < N; i++)
		{
			if (v[i] > coin && v[i] <= K)
				coin = v[i];
		}
		K -= coin;
		answer += 1;
	}
	cout << answer << endl;
	return 0;
}