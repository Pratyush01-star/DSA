class Solution {
    public long gcdSum(int[] nums) {
     int max=nums[0];
     int[] arr=new int[nums.length];
     for(int i=0;i<nums.length;i++){
        if(max<nums[i]){
           max=nums[i];
        }
        int k=gcd(nums[i],max);
        arr[i]=k;
     }

     Arrays.sort(arr);

     int s=0,e=nums.length-1;
     long sum=0;
     while(s<e){
        sum+=gcd(arr[s],arr[e]);
        s++;
        e--;
     }
     return sum;
   }

   int gcd(int a,int b){
        while (b != 0) {
            int temp = b;
            b = a % b;
            a = temp;
          }
        return a;
   }
}