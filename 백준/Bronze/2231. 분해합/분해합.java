import java.io.*;
import java.util.*;

public class Main { // 백준 2231번, 분해합 (브루트 포스)
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());

        int min = n; // 어차피 최소값은 n보다 작기때문

        for (int i = n; i > 0; i--) {
            int sum = i;
            int num = i;
            while (num != 0) {
                sum += num % 10;
                num = num / 10;
            }
            if (sum == n) {
                min = i;
            }
        }

        System.out.println(min == n ? 0 : min);

    }
}
