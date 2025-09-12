import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();

        int[] arr = new int[n];

        int max = -1000001;
        int min = 1000001;

        for (int i = 0; i < n; i++) {
            int num = sc.nextInt();
            arr[i] = num;
        }

        for (int j = 0; j < n; j++) {
            if (arr[j] > max) {
                max = arr[j];
            }
            if (arr[j] < min) {
                min = arr[j];
            }
        }

        System.out.print(min + " " + max);
    }
}