/*
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:
Input: 123
Output: 321
 */

public class ReverseInteger {
    public static int reverse(int x) {
        if(x < Integer.MIN_VALUE + 1 || x > Integer.MAX_VALUE) {
            return 0;
        }
        boolean d = x < 0;
        x = d ? -x : x;
        int rez = 0;
        while (x  > 0) {
            rez = rez * 10 + x % 10;
            x /= 10;
        }
        return d ? -rez : rez;

    }
}
