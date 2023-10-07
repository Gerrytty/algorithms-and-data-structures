class Solution {
    public double[] convertTemperature(double celsius) {
        double[] ans = {celsius + 273.15, celsius * 1.80 + 32.0};
        return ans;
    }
}