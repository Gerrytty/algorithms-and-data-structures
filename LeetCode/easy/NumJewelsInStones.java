/*
You're given strings J representing the types of stones that are jewels, and S representing the stones you have.
Each character in S is a type of stone you have.  You want to know how many of the stones you have are also jewels.
The letters in J are guaranteed distinct, and all characters in J and S are letters.
Letters are case sensitive, so "a" is considered a different type of stone from "A".

Example 1:
Input: J = "aA", S = "aAAbbbb"
Output: 3
*/

public class NumJewelsInStones {
    public static int numJewelsInStones(String J, String S) {
        int c = 0;
        for(int i = 0; i < J.length(); i++) {
            char stone = J.charAt(i);
            for(int j = 0; j < S.length(); j++) {
                if(stone == S.charAt(j)) {
                    c++;
                }
            }
        }
        return c;
    }
}
