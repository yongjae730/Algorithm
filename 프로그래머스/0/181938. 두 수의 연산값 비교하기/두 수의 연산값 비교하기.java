class Solution {
    public int solution(int a, int b) {
        int answer = 0;
        
        String ab = String.valueOf(a) + String.valueOf(b);
        
        
        return Math.max(Integer.valueOf(ab),(2*a*b));
    }
}