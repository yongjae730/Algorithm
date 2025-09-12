import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int x = sc.nextInt();

        int[] arr1 = new int[n];

        for (int i = 0; i < n; i++) {
            int num = sc.nextInt();
            arr1[i] = num;
        }

        for (int j = 0; j < n; j++) {

            if (arr1[j] < x) {
                System.out.print(arr1[j] + " ");
            }
        }

    }
}