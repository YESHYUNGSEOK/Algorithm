#include <iostream>
#include <queue>
#define MAX 100

using namespace std;

int N, M;
int board[MAX][MAX];
queue<pair<int, int> > q;

void bfs()
{
	int dx[4] = {-1, 1, 0, 0};
	int dy[4] = {0, 0, -1, 1};
	q.push(make_pair(0, 0));
	board[0][0] = 1;
	while (!q.empty())
	{
		int bx = q.front().first;
		int by = q.front().second;
		q.pop();
		for (int i = 0; i < 4; i++)
		{
			int x = bx + dx[i];
			int y = by + dy[i]; 
			if (x >= 0 && x < N && y >= 0 && y < M && !board[x][y])
			{
				board[x][y] = board[bx][by] + 1;
				q.push(make_pair(x, y));
			}
		}
	}
}

int main()
{
	cin >> N >> M;
	for (int i = 0; i < N; i++)
	{
		string row;
		cin >> row;
		for (int j = 0; j < M; j++)
		{
			if (row[j] == '1')
				board[i][j] = 0;
			else
				board[i][j] = 1;
		}
	}
	bfs();
	cout << board[N-1][M-1] << endl;
	return 0;
}