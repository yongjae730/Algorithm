import java.util.Scanner;

public class Main { // 백준 24723번 문제, 녹색거탑 (조합론)
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = Integer.parseInt(sc.next());
        System.out.print((int)Math.pow(2,n));
    }
}
