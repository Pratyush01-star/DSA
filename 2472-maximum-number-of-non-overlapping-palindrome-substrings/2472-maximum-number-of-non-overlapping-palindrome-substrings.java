class Solution {
    public int maxPalindromes(String s, int k) {
        int n = s.length();
        boolean[][] pal = new boolean[n][n];

        for (int len = 1; len <= n; len++) {
            for (int i = 0; i + len <= n; i++) {
                int j = i + len - 1;

                if (len == 1) {
                    pal[i][j] = true;
                } 
                else if (len == 2) {
                    pal[i][j] = (s.charAt(i) == s.charAt(j));
                } 
                else {
                    pal[i][j] = (s.charAt(i) == s.charAt(j))
                             && pal[i + 1][j - 1];
                }
            }
        }
        int[] dp = new int[n + 1];

        for (int j = 0; j < n; j++) {
            dp[j + 1] = dp[j];
            for (int i = 0; i <= j - k + 1; i++) {

                if (pal[i][j]) {
                    dp[j + 1] = Math.max(
                        dp[j + 1],
                        dp[i] + 1
                    );
                }
            }
        }
        return dp[n];
    }
}