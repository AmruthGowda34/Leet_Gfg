// class Bitonic{
//     public static int ascending(int arr[],int key,int range){
//         int l=0;
//         int h=range;
//         int mid=0;
//         while(l<=h){
//             mid=(l+h)/2;
//             if(arr[mid]==key){
//                 return mid;
//             }
//             else if(arr[mid]>key){
//                 h=mid-1;
//             }
//             else{
//                 l=mid+1;
//             }
//         }
//         return -1;
//     }

//     public static int descending(int arr[],int key,int range){
//         int l=range;
//         int h=arr.length-1;
//         int mid=0;
//         while(l<=h){
//             mid=(l+h)/2;
//             if(arr[mid]==key){
//                 return mid;
//             }
//             else if(arr[mid]>key){
//                 l=mid+1;
//             }
//             else{
//                 h=mid-1;
//             }
//         }
//         return -1;
//     }

//     public static int find_bitonic_point(int arr[]){
//         int l=0;
//         int r=arr.length-1;
//         int mid=0;
//         while(l<=r){
//             mid=(l+r)/2;
//             if(arr[mid]>arr[mid-1] && arr[mid]>arr[mid+1]){
//                 return mid;
//             }
//             if(arr[mid]>arr[mid-1] && arr[mid]<arr[mid+1]){
//                 l=mid+1;
//             }
//             else{
//                 r=mid;
//             }
//         }
//         return -1;
//     }
    
//     public static int search_bitonic(int arr[],int key,int bindex){
//         if(key==arr[bindex]){
//             return bindex;
//         }
//         if(key>arr[bindex]){
//             return -1;
//         }
//         int re1=ascending(arr, key, bindex-1);
//         if(re1!=-1){
//             return re1;
//         }
//         int re2=descending(arr, key, bindex+1);
//         if(re2!=-1){
//             return re2;
//         }
//         return -1;
//     }
//     public static void main(String[] args) {
//         int arr[]={5,6,7,8,9,10,3,2,1};
//         int key=8;
//         int bindex=find_bitonic_point(arr);
//         System.out.println(search_bitonic(arr, key, bindex));
//     }
// }

class Bitonic {

    // Binary search in ascending part
    public static int ascending(int arr[], int key, int range) {

        int l = 0;
        int h = range;

        while(l <= h) {

            int mid = (l + h) / 2;

            if(arr[mid] == key) {
                return mid;
            }
            else if(arr[mid] > key) {
                h = mid - 1;
            }
            else {
                l = mid + 1;
            }
        }

        return -1;
    }


    // Binary search in descending part
    public static int descending(int arr[], int key, int range) {

        int l = range;
        int h = arr.length - 1;

        while(l <= h) {

            int mid = (l + h) / 2;

            if(arr[mid] == key) {
                return mid;
            }
            else if(arr[mid] > key) {
                l = mid + 1;
            }
            else {
                h = mid - 1;
            }
        }

        return -1;
    }


    // Find bitonic/peak index
    public static int find_bitonic_point(int arr[]) {

        int l = 0;
        int r = arr.length - 1;

        while(l < r) {

            int mid = (l + r) / 2;

            if(arr[mid] < arr[mid + 1]) {
                // We are on ascending side
                l = mid + 1;
            }
            else {
                // We are on descending side or at peak
                r = mid;
            }
        }

        return l;
    }


    // Search key in bitonic array
    public static int search_bitonic(int arr[], int key, int bindex) {

        if(key == arr[bindex]) {
            return bindex;
        }

        // Key cannot exist if it is greater than the maximum
        if(key > arr[bindex]) {
            return -1;
        }

        // Search ascending part
        int re1 = ascending(arr, key, bindex - 1);

        if(re1 != -1) {
            return re1;
        }

        // Search descending part
        int re2 = descending(arr, key, bindex + 1);

        if(re2 != -1) {
            return re2;
        }

        return -1;
    }


    public static void main(String[] args) {

        int arr[] = {5, 6, 7, 8, 9, 10, 3, 2, 1};

        int key = 8;

        int bindex = find_bitonic_point(arr);

        System.out.println("Bitonic point: " + bindex);

        System.out.println("Key found at index: "
                + search_bitonic(arr, key, bindex));
    }
}