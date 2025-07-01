import java.util.Arrays;

class Solution {
    public int solution(int a, int b, int c, int d) {
        int[] dice = {a,b,c,d};
        Arrays.sort(dice);
        
        
        if (dice[0] == dice[3]) {
            // 네 주사위 모두 같을 때
            return 1111*dice[0];
        } else if (dice[0] == dice[2] || dice[1] == dice[3]) {
            // 세 주사위가 같을 때
            // (p, p, p, q) or (p, q, q, q)
            int p = (dice[0] == dice[1]) ? dice[0] : dice[3];
            int q = (dice[0] == dice[1]) ? dice[3] : dice[0];
            return (int) Math.pow(10*p+q,2);
        } else if (dice[0]==dice[1] && dice[2] == dice[3]) {
            // 두 개씩 같은 값이 나올 때
            int p = dice[0];
            int q = dice[2];
            return (p+q)*(q-p);
        } else if (dice[0]==dice[1]) { 
            // a와 b만 같을 때
            return dice[2] * dice[3];
        } else if (dice[1] == dice[2]) { 
            // b와 c만 같을 때
            return dice[0] * dice[3];
        } else if (dice[2] == dice[3]) {
            return dice[0] * dice[1];
        } else {
            return dice[0];
        }
        
        
        
    }
}