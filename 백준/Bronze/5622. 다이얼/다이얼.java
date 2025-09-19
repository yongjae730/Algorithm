import java.util.Scanner;

public class Main { // 백준 5622번, 다이얼 (문자열)
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        String word = sc.next();
        String[] arr = new String[]{"ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"};
        int time = 0;

        for (int i = 0; i < word.length(); i++) {
            for (int j = 0; j < arr.length; j++) {
                for (int k = 0; k < arr[j].length(); k++) {
                    if (word.charAt(i) == arr[j].charAt(k)) {
                        time += j + 3;
                    }
                }
            }
        }
        System.out.println(time);
    }
}
