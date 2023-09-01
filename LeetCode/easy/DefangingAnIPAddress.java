/*
Given a valid (IPv4) IP address, return a defanged version of that IP address.
A defanged IP address replaces every period "." with "[.]".

Example 1:
Input: address = "1.1.1.1"
Output: "1[.]1[.]1[.]1"
 */
public class DefangingAnIPAddress {
    public static String defangIPaddr(String address) {
        String defangedIP = "";
        int len = address.length();
        for(int i = 0; i < len; i++) {
            if(address.charAt(i) == '.') {
                defangedIP += "[.]";
            }
            else {
                defangedIP += address.charAt(i);
            }
        }
        return defangedIP;
    }
}
