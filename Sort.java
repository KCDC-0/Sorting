import java.util.Arrays;

class GfG {

    /////////////////
    // Selection Sort
    /////////////////

    static void selectionSort(int[] arr){
        int n = arr.length;
        for (int i = 0; i < n - 1; i++) {
          
            int min_idx = i;

            for (int j = i + 1; j < n; j++) {
                if (arr[j] < arr[min_idx]) {
                  
                    min_idx = j;
                }
            }

            int temp = arr[i];
            arr[i] = arr[min_idx];
            arr[min_idx] = temp;           
        }
    }


    /////////////////
    // Bubble Sort
    /////////////////

    static void bubbleSort(int arr[], int n){
        int i, j, temp;
        boolean swapped;
        for (i = 0; i < n - 1; i++) {
            swapped = false;
            for (j = 0; j < n - i - 1; j++) {
                if (arr[j] > arr[j + 1]) {
                    
                    temp = arr[j];
                    arr[j] = arr[j + 1];
                    arr[j + 1] = temp;
                    swapped = true;
                }
            }

            if (swapped == false)
                break;
        }
    }


    /////////////////
    // Merge Sort
    /////////////////

    static void merge(int arr[], int l, int m, int r){
        
        int n1 = m - l + 1;
        int n2 = r - m;

        int L[] = new int[n1];
        int R[] = new int[n2];

        for (int i = 0; i < n1; ++i)
            L[i] = arr[l + i];
        for (int j = 0; j < n2; ++j)
            R[j] = arr[m + 1 + j];

        int i = 0, j = 0;

        int k = l;
        while (i < n1 && j < n2) {
            if (L[i] <= R[j]) {
                arr[k] = L[i];
                i++;
            }
            else {
                arr[k] = R[j];
                j++;
            }
            k++;
        }

        while (i < n1) {
            arr[k] = L[i];
            i++;
            k++;
        }

        while (j < n2) {
            arr[k] = R[j];
            j++;
            k++;
        }
    }

    static void mergeSort(int arr[], int l, int r){
        
        if (l < r) {

            int m = l + (r - l) / 2;

            mergeSort(arr, l, m);
            mergeSort(arr, m + 1, r);

            merge(arr, l, m, r);
        }
    }


    /////////////////
    // Insertion Sort
    /////////////////

    static void insertionSort(int arr[]){
        int n = arr.length;
        for (int i = 1; i < n; ++i) {
            int key = arr[i];
            int j = i - 1;

            /* Move elements of arr[0..i-1], that are
               greater than key, to one position ahead
               of their current position */
            while (j >= 0 && arr[j] > key) {
                arr[j + 1] = arr[j];
                j = j - 1;
            }
            arr[j + 1] = key;
        }
    }


    /////////////////
    // Quick Sort
    /////////////////

    static int partition(int[] arr, int low, int high) {

        int pivot = arr[high];
        
        int i = low - 1;

        for (int j = low; j <= high - 1; j++) {
            if (arr[j] < pivot) {
                i++;
                swap(arr, i, j);
            }
        }
        
        swap(arr, i + 1, high);  
        return i + 1;
    }

    static void swap(int[] arr, int i, int j) {
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }

    static void quickSort(int[] arr, int low, int high) {
        if (low < high) {
            
            int pi = partition(arr, low, high);

            quickSort(arr, low, pi - 1);
            quickSort(arr, pi + 1, high);
        }
    }


    /////////////////
    // Heap Sort
    /////////////////

    static void heapify(int[] arr, int n, int i) {

        int largest = i;

        int l = 2 * i + 1;

        int r = 2 * i + 2;

        if (l < n && arr[l] > arr[largest])
            largest = l;

        if (r < n && arr[r] > arr[largest])
            largest = r;

        if (largest != i) {
            int temp = arr[i];
            arr[i] = arr[largest];
            arr[largest] = temp;

            heapify(arr, n, largest);
        }
    }

    static void heapSort(int[] arr) {
        int n = arr.length;

        for (int i = n / 2 - 1; i >= 0; i--)
            heapify(arr, n, i);

        for (int i = n - 1; i > 0; i--) {

            int temp = arr[0];
            arr[0] = arr[i];
            arr[i] = temp;

            heapify(arr, i, 0);
        }
    }


    /////////////////
    // Cycle Sort
    /////////////////

    public static void cycleSort(int arr[])
    {
        int n = arr.length;
          
        for (int cycle_start = 0; cycle_start <= n - 2;
             cycle_start++) {

            int item = arr[cycle_start];

            int pos = cycle_start;
            for (int i = cycle_start + 1; i < n; i++)
                if (arr[i] < item)
                    pos++;

            if (pos == cycle_start)
                continue;

            while (item == arr[pos])
                pos += 1;

            if (pos != cycle_start) {
                int temp = item;
                item = arr[pos];
                arr[pos] = temp;
            }

            while (pos != cycle_start) {
                pos = cycle_start;

                for (int i = cycle_start + 1; i < n; i++)
                    if (arr[i] < item)
                        pos += 1;

                while (item == arr[pos])
                    pos += 1;

                if (item != arr[pos]) {
                    int temp = item;
                    item = arr[pos];
                    arr[pos] = temp;
                }
            }
        }
    }


    /////////////////
    // Merge Sort
    /////////////////

    static void merge(int arr[], int left, int mid1, int mid2, int right) {
        
        int size1 = mid1 - left + 1;
        int size2 = mid2 - mid1;
        int size3 = right - mid2;
        
        int[] leftArr = new int[size1];
        int[] midArr = new int[size2];
        int[] rightArr = new int[size3];
        
        for (int i = 0; i < size1; i++) {
            leftArr[i] = arr[left + i];
        }
        for (int i = 0; i < size2; i++) {
            midArr[i] = arr[mid1 + 1 + i];
        }
        for (int i = 0; i < size3; i++) {
            rightArr[i] = arr[mid2 + 1 + i];
        }

        int i = 0, j = 0, k = 0, index = left;
        while (i < size1 || j < size2 || k < size3) {
            int minValue = Integer.MAX_VALUE, minIdx = -1;

            if (i < size1 && leftArr[i] < minValue) {
                minValue = leftArr[i];
                minIdx = 0;
            }
            if (j < size2 && midArr[j] < minValue) {
                minValue = midArr[j];
                minIdx = 1;
            }
            if (k < size3 && rightArr[k] < minValue) {
                minValue = rightArr[k];
                minIdx = 2;
            }

            if (minIdx == 0) {
                arr[index++] = leftArr[i++];
            } else if (minIdx == 1) {
                arr[index++] = midArr[j++];
            } else {
                arr[index++] = rightArr[k++];
            }
        }
    }
    
    static void threeWayMergeSort(int arr[], int left, int right) {

        if (left >= right) {
            return;
        }
        int mid1 = left + (right - left) / 3;
        int mid2 = left + 2 * (right - left) / 3;

        threeWayMergeSort(arr, left, mid1);

        threeWayMergeSort(arr, mid1 + 1, mid2);

        threeWayMergeSort(arr, mid2 + 1, right);

        merge(arr, left, mid1, mid2, right);
    }



    static void printArray(int[] arr){
        for (int val : arr) {
            System.out.print(val + " ");
        }
        System.out.println();
    }
  
    public static void main(String[] args){
        int[] arr = { 64, 25, 12, 22, 11 };
        int n = arr.length;

        System.out.print("Original array: ");
        printArray(arr);

        //bubbleSort(arr, n);
        //mergeSort(arr, 0, arr.length - 1);
        //insertionSort(arr);
        //quickSort(arr, 0, n - 1);
        //heapSort(arr);
        //cycleSort(arr);
        //threeWayMergeSort(arr, 0, n - 1);


        System.out.print("Sorted array: ");
        printArray(arr);
    }
}

