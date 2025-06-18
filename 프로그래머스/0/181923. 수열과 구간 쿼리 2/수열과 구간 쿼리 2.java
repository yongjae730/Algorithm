class Solution {
    public int[] solution(int[] arr, int[][] queries) {
        int[] answer = new int[queries.length];
        
        for (int i =0 ; i<queries.length; i++) {
            int s = queries[i][0];
            int e = queries[i][1];
            int result = -1;
            int diff = 1000000;
            for (int j = s; j <= e; j++) {
                int k = queries[i][2];
                if (arr[j]-k < diff) {
                    if (arr[j]-k>0) {
                        result = arr[j];
                        diff = arr[j]-k;
                    }
                } 
            }
            answer[i] = result;
        }
        
        
        return answer;
    }
}