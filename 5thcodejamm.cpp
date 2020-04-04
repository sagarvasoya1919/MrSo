#include <bits/stdc++.h>

using namespace std;

int sqr[60][60], n, k, t;
bool r1[60][60], c1[60][60], flag;

void solver(int row, int col, int m) 
{
    if (row == n && col == n + 1 && m == k && !flag) 
    {
        flag = true;
        cout << "Case #" << t << ": " << "POSSIBLE\n";
        for (int i = 1; i <= n; i++) 
        {
            for (int j = 1; j <= n; j++) 
            {
                cout << sqr[i][j] << " ";
            }
            cout << "\n";
        }
        return;
    } 
    else if (row > n) 
    {
        return;
    } 
    else if (col > n) 
    {
        solver(row + 1, 1, m);
    }
    for (int i = 1; i <= n && !flag; i++) 
    {
        if (!r1[row][i] && !c1[col][i]) 
        {
            r1[row][i] = c1[col][i] = true;
            if (row == col) 
            {
                m += i;
            }
            sqr[row][col] = i;

            solver(row, col + 1, m);

            r1[row][i] = c1[col][i] = false;
            if (row == col) 
            {
                m -= i;
            }
            sqr[row][col] = 0;
        }
    } 
}

int main()
{
    int Test;
    scanf(" %d", &Test);
    for (t = 1; t <= Test; t++)
    {
        scanf(" %d %d", &n, &k);
        solver(1, 1, 0);
        if (!flag)
        {
            cout << "Case #" << t << ": " << "IMPOSSIBLE\n";
        }
        flag = false;
    }
    return 0;
}
