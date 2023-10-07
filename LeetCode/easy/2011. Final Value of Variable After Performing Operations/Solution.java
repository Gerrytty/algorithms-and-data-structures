class Solution {
    public int finalValueAfterOperations(String[] operations) {
        byte ans = 0;

        for (int i = 0; i < operations.length; i++) {
            if (operations[i].charAt(0) == '-' || operations[i].charAt(2) == '-') {
                ans--;
            }
            else {
                ans++;
            }
        }

        return ans;
    }
}