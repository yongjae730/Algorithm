import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int m = sc.nextInt();

        int[] arr = new int[n];

        for (int q = 0; q < m; q++) {
            int i = sc.nextInt();
            int j = sc.nextInt();
            int k = sc.nextInt();

            for (int w = i; w <= j; w++) {
                arr[w - 1] = k;
            }

        }

        for (int s = 0; s < n; s++) {
            System.out.print(arr[s] + " ");
        }

    }
}