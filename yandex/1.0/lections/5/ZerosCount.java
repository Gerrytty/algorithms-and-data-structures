import java.util.Arrays;

public class ZerosCount {

    public static int getZerosCountOnInterval(int start, int end, int[] arr) {
        return arr[end] - arr[start];
    }

    public static void main(String[] args) {
        int[] input = {0, 0, 1, 0, 2, 0, 0};
        int[] zeros = new int[input.length + 1];

        for (int i = 1; i < input.length + 1; i++) {
            if (input[i - 1] == 0) {
                zeros[i] = zeros[i - 1] + 1;
            }
            else {
                zeros[i] = zeros[i - 1];
            }
        }

        Arrays.stream(zeros).forEach(num -> {
            System.out.print(num + " ");
        });

        System.out.println("\n" + getZerosCountOnInterval(0, 7, zeros));
    }
}
