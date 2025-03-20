public class binarySearch{
    public static int search(int[] array, int value)
    {
        return binarySearch(array, value, 0, array.length-1);
    }

    public static int binarySearch(int[] array, int value, int low, int high)
    {

        // {
        //     int mid = (high + low)/2;
        //    if(low > high){
        //         return -1;
        //     }
        //     else if(array[mid] == value){
        //         return mid;
        //     }
        //     else{
        //         if(array[mid] > value){
        //             return(binarySearch(array, value, low, mid-1));
        //         }
        //         else{
        //             return(binarySearch(array, value, mid+1, high));
        //         }
        //     }
        // }
        int mid = (high + low)/2;
        if(array.length < 1 ||
            mid == low ||
            mid == high && 
            (array[mid] > array[high] || 
            array[mid] < array[low] || 
            (array[mid] < array[high] && array[mid] > array[low]))){
            return -1;
        }
        if(array[mid] == value){
            return mid;
        }
        else{
            if(array[mid] > value){
                return(binarySearch(array, value, low, mid));
            }
            else{
                return(binarySearch(array, value, mid, high));
            }
        }
    }
    public static void main(String[] Args){
        System.out.println(search(new int[]{},100 ));
    }
}

