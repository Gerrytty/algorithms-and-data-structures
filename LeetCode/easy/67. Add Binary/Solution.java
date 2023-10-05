class Solution {
    public String addBinary(String a, String b) {

        char[] ans;
        char[] other;
        int i;
        int j;

        if (a.length() > b.length()) {
            ans = a.toCharArray();
            other = b.toCharArray();
            j = a.length() - 1;
            i = b.length() - 1;
        }
        else {
            ans = b.toCharArray();
            other = a.toCharArray();
            j = b.length() - 1;
            i = a.length() - 1;
        }

        int d = 0;

        while (i >= 0) {

            if (ans[j] == '0' && other[i] == '0') {
                if (d == 1) {
                    d = 0;
                    ans[j] = '1';
                }
            }
            else if (ans[j] == '1' && other[i] == '1') {
                if (d == 0) {
                    ans[j] = '0';
                }
                else {
                    ans[j] = '1';
                }
                d = 1;
            }
            else {
                if (d == 0) {
                    ans[j] = '1';
                }
                else {
                    ans[j] = '0';
                }
            }

            i--;
            j--;

        }

        while (d != 0 && j >= 0) {

            if (ans[j] == '0') {
                ans[j] = '1';
                d = 0;
                break;
            }

            ans[j] = '0';
            j--;
        }

        String result = new String(ans);

        if (d == 0) {
            return result;
        }

        return "1" + result;

    }
}