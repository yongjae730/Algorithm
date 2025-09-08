import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        sc.close();

        int n = N / 4;
        String str = "";
        for (int i = 0; i < n; i++) {
            str += "long ";
        }

        System.out.println(str + "int");

    }
}