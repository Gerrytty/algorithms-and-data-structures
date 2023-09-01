public class MySqrt {
    public static int mySqrt(int x) {
        if(x < 2) {
            return x;
        }
        int left = 1; int right = 2;
        boolean flag = true;
        while (flag) {
            if(left * left <= x && right * right >= x) {
                flag = false;
                return right * right > x ? left : right;
            }
            left += 1; right += 1;
        }
        return x;
    }
}
