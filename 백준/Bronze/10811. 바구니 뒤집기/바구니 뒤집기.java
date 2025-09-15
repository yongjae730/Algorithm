import java.util.*;

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int m = sc.nextInt();

        int[] arr = new int[n];

        for (int i = 0; i < n; i++) {
            arr[i] = i+1;
        }

        for (int k = 0; k < m; k++) {
            int i = sc.nextInt() - 1;
            int j = sc.nextInt() - 1;

            // i와 j가 만나거나 교차하기 전까지 반복
            while (i < j) {
                // 값 교환(swap)
                int temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;

                // 포인터 이동
                i++;
                j--;
            }
        }
        for (int q = 0; q<n; q++) {
            System.out.print(arr[q] + " ");
        }
    }
}