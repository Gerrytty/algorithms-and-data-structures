class Solution {
    public int maxProfit(int[] prices) {

        if (prices == null || prices.length == 0) {
            return 0;
        }

        int left = 0;
        int right = 1;
        int maxProfit = 0;

        while (right < prices.length) {
            int profit = prices[right] - prices[left];

            maxProfit = Math.max(profit, maxProfit);

            if (prices[right] < prices[left]) {
                left = right;
            }

            right++;
        }

        return maxProfit;

    }
}