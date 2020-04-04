#include <bits/stdc++.h>
int main(int argc, char const *argv[])
{
    int t, z;
    std::cin >> t;
    for (int z = 0; z < t; z++)
    {
        std::string str;
        int i, n;
        std::cin >> n;
        std::vector<std::pair<int, std::pair<int, int>>> v;
        int je[n], cm[n];
        for (int i = 0; i < n; i++)
        {

            std::cin >> je[i] >> cm[i];
            v.push_back({je[i], {cm[i], i}});
            str += 'C';
        }

        std::sort(v.begin(), v.end());
        int c = 0, j = 0, count = 0;
        for (int i = 0; i < v.size(); i++)
        {

            if (v[i].first >= c)
            {
                str[v[i].second.second] = 'C';
                c = v[i].second.first;
            }

            else if (v[i].first >= j)
            {
                str[v[i].second.second] = 'J';
                j = v[i].second.first;
            }

            else
            {
                count = 1;
                break;
            }
        }
        if (count == 1)
        {
            std::cout << "Case #" << z + 1 << ": "
                      << "IMPOSSIBLE" << std::endl;
            continue;
        }
        std::cout << "Case #" << z + 1 << ": " << str << std::endl;
    }
    return 0;
}

