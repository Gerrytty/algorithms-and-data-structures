public class ToLowerCase {
    public static String toLowerCase(String str) {
        String s = "";
        for(int i = 0; i < str.length(); i++) {
            int c = (int) str.charAt(i);
            if(c > 64 && c < 91) {
                s += (char) (c + 32);
            }
            else {
                s += (char) c;
            }
        }
        return s;
    }
}
