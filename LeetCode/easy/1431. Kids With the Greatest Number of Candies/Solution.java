import java.util.*;

class Solution {
    public List<Boolean> kidsWithCandies(int[] candies, int extraCandies) {
        Boolean[] ans = new Boolean[candies.length];

        int max = -1;

        for (int candy : candies) {
            if (candy > max) {
                max = candy;
            }
        }

        for (int i = 0; i < candies.length; i++) {
            if (candies[i] + extraCandies >= max) {
                ans[i] = true;
            }
            else {
                ans[i] = false;
            }
        }

        return Arrays.asList(ans);
    }
}