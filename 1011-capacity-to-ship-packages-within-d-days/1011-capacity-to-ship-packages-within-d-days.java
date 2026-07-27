class Solution {

    public int shipWithinDays(int[] weights, int days) {

        int low = 0;
        int high = 0;
    
         for (int time : weights) {
            low = Math.max(low, time);
            high += time;
        }

        while (low < high) {
            int mid = low + (high - low) / 2;

            if (canAssign(weights, days, mid)) {
                high = mid;
            } else {
                low = mid + 1;
            }
        }

        return low;
    }

    private boolean canAssign(int[] weights, int days, int maxTime) {

        int pilots = 1;
        int currentTime = 0;

        for (int weight : weights) {

            if (currentTime + weight <= maxTime) {
                currentTime += weight;
            } else {
                pilots++;
                currentTime = weight;

                if (pilots > days) {
                    return false;
                }
            }
        }

        return true;
    }
}