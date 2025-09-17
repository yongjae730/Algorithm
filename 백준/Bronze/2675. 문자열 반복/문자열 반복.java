import java.util.*;
import java.lang.*;
import java.io.*;

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();

        for (int i = 0; i < t; i++) {
            String ans = "";

            int r = sc.nextInt();
            String s = sc.next();

            for (int k = 0; k < s.length(); k++) {
                for (int j = 0; j < r; j++) {
                    ans += s.charAt(k);
                }
            }

            System.out.println(ans);
        }
    }
}