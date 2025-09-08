import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int hour = sc.nextInt();
        int min = sc.nextInt();

        if (min >= 45) {
            min -= 45;
        } else if (min < 45) {
            min = min +60 -45;
            if (hour >0) {
                hour -= 1;
            } else {
                hour =23;
            }
        }

        System.out.println(hour + " " +min);

        sc.close();
    }
}