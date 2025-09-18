import java.util.Scanner;

public class Main { // 2908번 상수(문자열)
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        String a = sc.next();
        String b = sc.next();

        sc.close();

        String sbA = new StringBuilder(a).reverse().toString();
        String sbB = new StringBuilder(b).reverse().toString();

        int resultA = Integer.parseInt(sbA);
        int resultB = Integer.parseInt(sbB);

        System.out.println(resultA > resultB ? resultA : resultB);

    }
}
