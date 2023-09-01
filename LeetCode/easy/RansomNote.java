import java.util.HashMap;

class Solution {
    public boolean canConstruct(String ransomNote, String magazine) {
        
        HashMap<Character, Integer> magazineHashMap = new HashMap<>();

        for (int i = 0; i < magazine.length(); i++) {
            if (magazineHashMap.get(magazine.charAt(i)) == null) {
                magazineHashMap.put(magazine.charAt(i), 1);
            }
            else {
                magazineHashMap.put(magazine.charAt(i), magazineHashMap.get(magazine.charAt(i)) + 1);
            }
        }

        for (int i = 0; i < ransomNote.length(); i++) {

            Character ch = ransomNote.charAt(i);

            if (magazineHashMap.get(ch) == null) {
                return false;
            }
            if (magazineHashMap.get(ch) <= 0) {
                return false;
            }
            
            magazineHashMap.put(ch, magazineHashMap.get(ch) - 1);

        }

        return true;

    }
}