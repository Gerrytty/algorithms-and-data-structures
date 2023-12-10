public class Solution {

    public boolean isSubsequence(String s, String t) {

        char[] sArray = s.toCharArray();
        char[] tArray = t.toCharArray();

        int left = 0;
        int right = 0;

        while (left < s.length() && right < t.length()) {

            if (sArray[left] == tArray[right]) {
                left++;

            }

            right++;

        }

        return left == s.length();
    }
}
