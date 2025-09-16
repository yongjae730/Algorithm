import java.util.*;

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int tc = sc.nextInt();
        for (int i = 0; i < tc; i++) {
            String word = sc.next();
            System.out.print(word.charAt(0));
            int lastStr = word.length() -1;
            System.out.println(word.charAt(lastStr));
        }
    }
}