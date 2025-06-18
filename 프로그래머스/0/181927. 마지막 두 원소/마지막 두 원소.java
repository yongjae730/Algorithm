class Solution {
    public int[] solution(int[] num_list) {
        int n = num_list.length;
        int[] answer = new int[n+1];
        
        
        for (int i=0; i<num_list.length; i++) {
            answer[i] = num_list[i];
        }
        
        int last = num_list[n-1];
        int second_last = num_list[n-2];
        
        if (last > second_last) {
            answer[n] = last - second_last;
        } else {
            answer[n] = last*2;
        }
        
        
        
        return answer;
    }
}