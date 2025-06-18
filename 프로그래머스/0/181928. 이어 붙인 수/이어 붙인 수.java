class Solution {
    public int solution(int[] num_list) {
        int answer = 0;
        
        String num_even = "";
        String num_odd = "";
        
        for (int num: num_list) {
            if (num%2 == 0) {
                num_even += String.valueOf(num);
            } else {
                num_odd += String.valueOf(num);
            }
        }
        answer += Integer.valueOf(num_even) + Integer.valueOf(num_odd);
        
        
        return answer;
    }
}