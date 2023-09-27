class Solution {
    public int removeDuplicates(int[] nums) {

        int currNum = nums[0];

        int currIndex = 0;
        int zeroAt = -1;
        for (int i = 1; i < nums.length; i++) {

            if (nums[i] == currNum) {
                nums[i] = 0;

                if (zeroAt == -1) {
                    zeroAt = i;
                }
            }

            else {
                currNum = nums[i];
                if (zeroAt != -1) {
                    nums[zeroAt] = nums[i];
                    zeroAt += 1;
                    nums[i] = 0;
                }
                currIndex += 1;
            }

        }

        return currIndex + 1;
    }
}
