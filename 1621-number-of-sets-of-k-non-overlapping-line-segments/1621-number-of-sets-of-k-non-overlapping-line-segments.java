
class Solution {
    static final int MOD = 1000000007;

    public int numberOfSets(int n, int k) {

        long[][] dp = new long[n + 1][k + 1];
        for (int i = 0; i <= n; i++) {
            dp[i][0] = 1;
        }

        for (int j = 1; j <= k; j++) {

            long sum = 0;
            for (int i = 1; i <= n; i++) {
                if (i >= 2) {
                    sum = (sum + dp[i - 1][j - 1]) % MOD;
                }
                dp[i][j] = (dp[i - 1][j] + sum) % MOD;
            }
        }
        return (int) dp[n][k];
    }
}