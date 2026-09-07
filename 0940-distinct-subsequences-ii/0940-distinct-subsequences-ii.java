class Solution {
    public int distinctSubseqII(String s) {
    
        int MOD = 1000000007;
        long[] dp = new long[s.length() + 1];

        dp[0] = 1;
        long[] last = new long[26];

        for (int i = 1; i <= s.length(); i++) {
            char ch = s.charAt(i - 1);
            int c = ch - 'a';

            dp[i] = (2 * dp[i - 1]) % MOD;
            dp[i] = (dp[i] - last[c] + MOD) % MOD;
            last[c] = dp[i - 1];
        }
        return (int) ((dp[s.length()] - 1 + MOD) % MOD);
    }
}