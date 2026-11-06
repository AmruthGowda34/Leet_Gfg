import java.util.Arrays;
class GameofTrhons{
    public static void main(String[] args) {
        String s="adamm";
        char arr[]=s.toCharArray();
        int errorCount=0;
        Arrays.sort(arr);
        int i=0;
        while(i<arr.length){
            if(i<arr.length-1 && arr[i]==arr[i+1]){
                i+=2;
            }
            else{
                i++;
                errorCount++;
            }
        }
        if(errorCount<=1){
            System.out.println("Yes");
        }
        else{
            System.out.println("No");
        }
    }
}