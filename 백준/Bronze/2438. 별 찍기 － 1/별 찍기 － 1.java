import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int star = sc.nextInt();

        String ans = "";
        for (int i = 1; i <= star; i++) {
            ans += "*";
            System.out.println(ans);
        }
    }
}