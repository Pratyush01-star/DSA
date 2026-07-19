public class Solution{
 public int findGCD(int[] a){
       
        int min=a[0];
        int max=a[0];

        for (int i=0;i<a.length;i++){
            if(a[i]<min)
            min=a[i];
            
            if(a[i]>max)
            max=a[i];

        }
        System.out.println("Minimum ="+ min);
        System.out.println("Maximum ="+ max);

int x=max;
int y=min;
while(y!=0){
    int temp=y;
    y=x%y;
    x=temp;

}
return x;
    }
}
