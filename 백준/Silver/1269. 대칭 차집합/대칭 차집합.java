import java.util.*;
import java.io.*;

public class Main { // 백준 1269번 문제, 대칭 차집합 (집합과 맵)
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());


        HashSet<Integer> A = new HashSet<>(); // 집합 A
        HashSet<Integer> B = new HashSet<>(); // 집합 B

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            A.add(Integer.parseInt(st.nextToken()));
        }
        st = new StringTokenizer(br.readLine());
        for (int j = 0; j < M; j++) {
            B.add(Integer.parseInt(st.nextToken()));
        }
        int result = 0;
        // A-B
        HashSet<Integer> temp = new HashSet<>();
        temp.addAll(A);
        A.removeAll(B);

        // B-A
        B.removeAll(temp);

        result = A.size() + B.size();

        System.out.print(result);
    }
}
