#include <stdio.h>
#include <stdlib.h>

// 01背包问题动态规划算法
int knapsack(int n, int w[], int v[], int c)
{
    int i, j;
    int **dp = (int **)malloc((n + 1) * sizeof(int *));
    for (i = 0; i <= n; i++)
    {
        dp[i] = (int *)malloc((c + 1) * sizeof(int));
    }

    // 初始化边界条件
    for (i = 0; i <= n; i++)
    {
        dp[i][0] = 0;
    }
    for (j = 0; j <= c; j++)
    {
        dp[0][j] = 0;
    }

    // 动态规划求解最优解
    for (i = 1; i <= n; i++)
    {
        for (j = 1; j <= c; j++)
        {
            if (w[i - 1] <= j)
            {
                dp[i][j] = (v[i - 1] + dp[i - 1][j - w[i - 1]]) > dp[i - 1][j] ? (v[i - 1] + dp[i - 1][j - w[i - 1]]) : dp[i - 1][j];
            }
            else
            {
                dp[i][j] = dp[i - 1][j];
            }
        }
    }

    int max_value = dp[n][c];
    // 释放动态分配的内存
    for (i = 0; i <= n; i++)
    {
        free(dp[i]);
    }
    free(dp);
    return max_value;
}

int main()
{
    int n = 5;                  // 物品数量
    int w[] = {2, 4, 1, 5, 3};  // 物品重量
    int v[] = {5, 6, 3, 19, 8}; // 物品价值
    int c = 10;                 // 背包容量

    printf("Max value: %d\n", knapsack(n, w, v, c));
    return 0;
}