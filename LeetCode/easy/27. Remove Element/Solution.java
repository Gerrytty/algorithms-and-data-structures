class Solution {
    public int removeElement(int[] nums, int val) {
        int currentZero = -1;

        int k = 0;

        for (int i = 0; i < nums.length; i++) {
            if (nums[i] == val) {

                if (currentZero == -1) {
                    currentZero = i;
                }

                nums[i] = 0;
                k += 1;
            }
            else if (currentZero != -1) {
                nums[currentZero] = nums[i];
                nums[i] = 0;
                currentZero += 1;
            }
        }

        return nums.length - k;
    }
}