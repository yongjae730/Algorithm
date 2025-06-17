class Solution {
    public int solution(int a, int b, int c) {
        int answer = 0;
        int p1 = a+b+c;
        int p2 = (int) (Math.pow(a,2)+Math.pow(b,2)+Math.pow(c,2));
        int p3 = (int) (Math.pow(a,3)+Math.pow(b,3)+Math.pow(c,3));
        if (a != b && a!=c && b!= c) {
            answer = p1;
        } else if (a==b && b==c) {
            answer = p1*p2*p3;   
        } else {
            answer = p1*p2;
        }
        return answer;
    }
}