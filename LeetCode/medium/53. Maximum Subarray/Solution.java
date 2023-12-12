class Solution {
    public int maxSubArray(int[] nums) {
        long maxSum = Long.MIN_VALUE;
        long currSum = 0;

        for (int i = 0; i < nums.length; i++) {

            if (currSum < 0) {
                currSum = nums[i];
            } else {
                currSum += nums[i];
            }

            maxSum = Math.max(maxSum, currSum);
        } 

        return (int) maxSum;

    }
}