class Solution {
    public boolean canReach(int[] start, int[] target) {
        int colorStart = (start[0] + start[1]) % 2;
        int colorTarget = (target[0] + target[1]) % 2;
        return colorStart == colorTarget;
    }
}