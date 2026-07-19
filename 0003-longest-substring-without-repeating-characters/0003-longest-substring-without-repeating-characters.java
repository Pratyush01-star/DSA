public class Solution {
    public int lengthOfLongestSubstring(String s) {
        int a = 0;

        for (int i = 0; i < s.length(); i++) {
            boolean[] visited = new boolean[128];
            int len = 0;

            for (int j = i; j < s.length(); j++) {
                if (visited[s.charAt(j)])
                    break;

                visited[s.charAt(j)] = true;
                len++;
            }

            if (len > a)
                a = len;
        }

        return a;
    }
}