class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {

        if (nums2.length < 1) {
            return;
        }

        int[] ans = new int[m + n];

        int nums1Counter = 0;
        int nums2Counter = 0;
        int ansCounter = 0;

        while (ansCounter < nums1.length) {

            if (nums2Counter < n && nums1Counter < m && nums1[nums1Counter] <= nums2[nums2Counter]) {
                ans[ansCounter++] = nums1[nums1Counter++];
            }
            else if (nums2Counter < n) {
                ans[ansCounter++] = nums2[nums2Counter++];
            }
            else {
                if (nums1Counter < m) {
                    ans[ansCounter++] = nums1[nums1Counter++];
                }
            }
        }

        for (int i = 0; i < ans.length; i++) {
            nums1[i] = ans[i];
        }

    }
}