class Solution {
    public boolean isMonotonic(int[] nums) {

        if (nums.length <= 2) {
            return true;
        }

        int firstNum = nums[0];
        char order = 0;

        for (int i = 1; i < nums.length; i++) {
            if (nums[i] > firstNum) {

                if (order == 2) {
                    return false;
                }

                order = 1;
            }

            else if (nums[i] < firstNum) {

                if (order == 1) {
                    return false;
                }

                order = 2;
            }

            firstNum = nums[i];
        }

        return true;

    }
}