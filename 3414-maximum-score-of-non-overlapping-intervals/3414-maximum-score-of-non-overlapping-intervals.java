import java.util.*;

class Solution {

    static class Interval {
        int l;
        int r;
        int w;
        int index;

        Interval(int l, int r, int w, int index) {
            this.l = l;
            this.r = r;
            this.w = w;
            this.index = index;
        }
    }

    static class State {
        long score;
        List<Integer> indices;

        State(long score, List<Integer> indices) {
            this.score = score;
            this.indices = indices;
        }
    }

    Interval[] arr;
    int[] next;
    State[][] dp;
    int n;

    State solve(int i, int k) {

        if (i >= n || k == 0) {
            return new State(0, new ArrayList<>());
        }

        if (dp[i][k] != null) {
            return dp[i][k];
        }

        // Option 1: Skip this interval
        State skip = solve(i + 1, k);

        // Option 2: Take this interval
        State after = solve(next[i], k - 1);

        List<Integer> takeList = new ArrayList<>(after.indices);
        takeList.add(arr[i].index);

        // Sort because final answer must be sorted by index
        Collections.sort(takeList);

        State take = new State(
            arr[i].w + after.score,
            takeList
        );

        // Choose the better option
        if (take.score > skip.score) {
            dp[i][k] = take;
        } 
        else if (take.score < skip.score) {
            dp[i][k] = skip;
        } 
        else {
            // Same score → lexicographically smaller indices
            if (isSmaller(take.indices, skip.indices)) {
                dp[i][k] = take;
            } else {
                dp[i][k] = skip;
            }
        }

        return dp[i][k];
    }

    // Returns true if a is lexicographically smaller than b
    static boolean isSmaller(List<Integer> a, List<Integer> b) {

        int size = Math.min(a.size(), b.size());

        for (int i = 0; i < size; i++) {

            if (!a.get(i).equals(b.get(i))) {
                return a.get(i) < b.get(i);
            }
        }

        // If one is a prefix of the other,
        // shorter one is lexicographically smaller
        return a.size() < b.size();
    }

    public int[] maximumWeight(List<List<Integer>> intervals) {

        n = intervals.size();

        arr = new Interval[n];

        for (int i = 0; i < n; i++) {

            arr[i] = new Interval(
                intervals.get(i).get(0),
                intervals.get(i).get(1),
                intervals.get(i).get(2),
                i
            );
        }

        // Sort by starting position
        Arrays.sort(arr, (a, b) -> {

            if (a.l != b.l) {
                return Integer.compare(a.l, b.l);
            }

            return Integer.compare(a.index, b.index);
        });

        // Store starting positions
        int[] starts = new int[n];

        for (int i = 0; i < n; i++) {
            starts[i] = arr[i].l;
        }

        // Find next non-overlapping interval
        next = new int[n];

        for (int i = 0; i < n; i++) {

            // Need left > current right
            next[i] = upperBound(starts, arr[i].r);
        }

        // DP
        dp = new State[n + 1][5];

        State answer = solve(0, 4);

        int[] result = new int[answer.indices.size()];

        for (int i = 0; i < answer.indices.size(); i++) {
            result[i] = answer.indices.get(i);
        }

        return result;
    }

    // First position where arr[pos] > target
    static int upperBound(int[] arr, int target) {

        int left = 0;
        int right = arr.length;

        while (left < right) {

            int mid = left + (right - left) / 2;

            if (arr[mid] <= target) {
                left = mid + 1;
            } else {
                right = mid;
            }
        }

        return left;
    }
}