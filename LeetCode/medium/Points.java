import java.lang.reflect.Array;
import java.security.AlgorithmConstraints;
import java.util.Arrays;

class Points {
    public static void main(String[] args) {
        int[][] arr = {
                {1, 3}, {2, 2}, {3, 3}, {4, 4}, {5, 5},
                {5, 1}, {4, 2}, {3, 3}, {2, 4}, {1, 5}
        };
//        int[][] arr = {
//                {1, 1}, {2, 2}, {3, 3}
//        };
//        int[][] arr = {
//                {0, 0}, {1, 1}, {1, -1}
//        };
//        int[][] arr = {
//                {1, 1}, {3, 2}, {5, 3}, {4, 1}, {2, 3}, {1, 4}
//        };
//        int[][] arr = {
//                {-1, 1}, {-2, 3}, {1, 1}, {4, 4}
//        };
//        int[][] arr = {
//                {0,0}, {1, 0}, {2, 0}, {3, 0}, {5, 0}
//        };
//        int[][] arr = {
//                {0,0}, {0, 1}, {0, 2}, {0, 4}, {0, 5}
//        };
//        int[][] arr = {
//                {3, 0}, {4, 1}, {0, 2}, {1, 3}, {2, 4}
//        };
//        int[][] arr = {
//                {4, 2}, {3, 3}, {2, 4}
//        };
//        int[][] arr = {
//                {1, 1}, {2, 3}, {1, 1}
//        };
        System.out.println("max points on line = " + maxPoints(arr));
        int[][] a = {
                {1, 1, 0}, {1, 0, 1}, {0, 0, 0}
        };
        flipAndInvertImage(a);
    }
    public static int maxPoints(int[][] points) {
        int max = 0;
        int sizeArr = 0;
        int len = points.length;
        int maxPositiveNumber = 0;
        int minNegativeNumber = 0;

        boolean allPositive = true;
        for (int i = 0; i < len; i++) {
            int x = points[i][0];
            int y = points[i][1];
            if(x < 0 || y < 0) {
                allPositive = false;
            }
        }

        if(!allPositive) {
            for (int i = 0; i < len; i++) {
                int x = points[i][0];
                int y = points[i][1];
                if(x >= 0) {
                    if(x > maxPositiveNumber) {
                        maxPositiveNumber = x;
                    }
                }
                if(y >= 0) {
                    if(y > maxPositiveNumber) {
                        maxPositiveNumber = y;
                    }
                }
                if(x < 0) {
                    if(x < minNegativeNumber) {
                        minNegativeNumber = x;
                    }
                }
                if(y < 0) {
                    if(y < minNegativeNumber) {
                        minNegativeNumber = y;
                    }
                }
            }
        }

        else if(allPositive) {
            for (int i = 0; i < len; i++) {
                int x = points[i][0];
                int y = points[i][1];
                if(x > maxPositiveNumber) {
                    maxPositiveNumber = x;
                }
                if(y > maxPositiveNumber) {
                    maxPositiveNumber = y;
                }
            }
        }

        sizeArr = maxPositiveNumber + Math.abs(minNegativeNumber) + 1;

        int[][] arr = new int[sizeArr][sizeArr];

        minNegativeNumber = Math.abs(minNegativeNumber);

        if (!allPositive) {
            for (int i = 0; i < len; i++) {
                arr[points[i][0] + minNegativeNumber][points[i][1] + minNegativeNumber] = 1;
            }
        }

        if (allPositive) {
            for (int i = 0; i < len; i++) {
                arr[points[i][0]][points[i][1]] = 1;
            }
        }

        ///////checking

        for (int i = 0; i < sizeArr; i++) {
            int c = 0;
            for (int j = 0; j < sizeArr; j++) {
                if(arr[i][j] == 1) {
                    c++;
                }
            }
            if(c > max) {
                max = c;
            }
        }

        for (int i = 0; i < sizeArr; i++) {
            int c = 0;
            for (int j = 0; j < sizeArr; j++) {
                if(arr[j][i] == 1) {
                    c++;
                }
            }
            if(c > max) {
                max = c;
            }
        }

        int startI = 0;
        if (sizeArr > 1) {
            startI = len - 2;
        }
        int startJ = 0;
        for (int i = 0; i < sizeArr; i++) {
            int x = startI - i; int y = startJ;
            int c = 0;
            boolean flag = !(x < 0 || x == sizeArr || y == sizeArr || y < sizeArr);
            while (flag) {
                if(arr[x][y] == 1) {
                    c++;
                }
                x++;
                y++;
                if(x == sizeArr) {
                    flag = false;
                }
            }
            if(c > max) {
                max = c;
            }
        }

        startI = 0;
        startJ = 1;
        for (int i = 0; i < sizeArr - 1; i++) {
            int x = startI; int y = startJ + i; int c = 0;
            boolean flag = !(y < 0 || y == sizeArr);
            while (flag) {
                if(arr[x][y] == 1) {
                    c++;
                }
                x++;
                y++;
                flag = !(y == sizeArr);
            }
            if(c > max) {
                max = c;
            }
        }

        startI = 1;
        startJ = 0;
        for (int i = 0; i < sizeArr; i++) {
            int x = startI + i; int y = startJ; int c = 0;
            boolean b = !(x >= sizeArr);
            while (b) {
                if(arr[x][y] == 1) {
                    c++;
                }
                x--; y++;
                b = !(x < 0 || y >= sizeArr);
            }
            if(c > max) {
                max = c;
            }
        }

        startI = sizeArr - 1;
        startJ = 0;
        for (int i = 0; i < sizeArr; i++) {
            int x = startI; int y = startJ + i; int c = 0;
            boolean b = !(y == sizeArr);
            while(b) {
                if(arr[x][y] == 1) {
                    c++;
                }
                x--; y++;
                b = (!(x < 0 || y >= sizeArr));
            }
            if(c > max) {
                max = c;
            }
        }


        for(int i = 0; i < sizeArr; i++) {
            for(int j = 0; j < sizeArr; j++) {
                System.out.print(arr[i][j] + " ");
            }
            System.out.println();
        }
        return max;
    }

    public static int[][] flipAndInvertImage(int[][] A) {
        int len = A.length;
        for(int i = 0; i < len; i++) {
            for(int j = 0; j < len; j++) {
                A[i][j] = A[i][j] ^ 1;
            }
        }
        for(int i = 0; i < len; i++) {
            int[] arr = A[i];
            int[] arr2 = new int[len];
            for(int j = 0; j < len; j++) {
                arr2[j] = arr[len - j - 1];
            }
            A[i] = arr2;
        }
        return A;
    }
}