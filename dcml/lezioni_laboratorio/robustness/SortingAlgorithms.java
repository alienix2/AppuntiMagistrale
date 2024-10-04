package main;

import java.util.Arrays;

/**
 * 
 */

/**
 * @author Tommy
 *
 */
public class SortingAlgorithms {
	
	public static void bubbleSort(int[] a) {
	    boolean sorted = false;
	    int temp;
	    while(!sorted) {
	        sorted = true;
	        for (int i = 0; i < a.length - 1; i++) {
	            if (a[i] > a[i+1]) {
	                temp = a[i];
	                a[i] = a[i+1];
	                a[i+1] = temp;
	                sorted = false;
	            }
	        }
	    }
	}
	
	public static void insertionSort(int[] array) {
	    for (int i = 1; i < array.length; i++) {
	        int current = array[i];
	        int j = i - 1;
	        while(j >= 0 && current < array[j]) {
	            array[j+1] = array[j];
	            j--;
	        }
	        // at this point we've exited, so j is either -1
	        // or it's at the first element where current >= a[j]
	        array[j+1] = current;
	    }
	}
	
	public static void selectionSort(int[] array) {
	    for (int i = 0; i < array.length; i++) {
	        int min = array[i];
	        int minId = i;
	        for (int j = i+1; j < array.length; j++) {
	            if (array[j] < min) {
	                min = array[j];
	                minId = j;
	            }
	        }
	        // swapping
	        int temp = array[i];
	        array[i] = min;
	        array[minId] = temp;
	    }
	}
	
	public static void mergeSort(int[] array, int left, int right) {
	    if (right <= left) return;
	    int mid = (left+right)/2;
	    mergeSort(array, left, mid);
	    mergeSort(array, mid+1, right);
	    merge(array, left, mid, right);
	}
	
	private static void merge(int[] array, int left, int mid, int right) {
	    // calculating lengths
	    int lengthLeft = mid - left + 1;
	    int lengthRight = right - mid;

	    // creating temporary subarrays
	    int leftArray[] = new int [lengthLeft];
	    int rightArray[] = new int [lengthRight];

	    // copying our sorted subarrays into temporaries
	    for (int i = 0; i < lengthLeft; i++)
	        leftArray[i] = array[left+i];
	    for (int i = 0; i < lengthRight; i++)
	        rightArray[i] = array[mid+i+1];

	    // iterators containing current index of temp subarrays
	    int leftIndex = 0;
	    int rightIndex = 0;

	    // copying from leftArray and rightArray back into array
	    for (int i = left; i < right + 1; i++) {
	        // if there are still uncopied elements in R and L, copy minimum of the two
	        if (leftIndex < lengthLeft && rightIndex < lengthRight) {
	            if (leftArray[leftIndex] < rightArray[rightIndex]) {
	                array[i] = leftArray[leftIndex];
	                leftIndex++;
	            }
	            else {
	                array[i] = rightArray[rightIndex];
	                rightIndex++;
	            }
	        }
	        // if all the elements have been copied from rightArray, copy the rest of leftArray
	        else if (leftIndex < lengthLeft) {
	            array[i] = leftArray[leftIndex];
	            leftIndex++;
	        }
	        // if all the elements have been copied from leftArray, copy the rest of rightArray
	        else if (rightIndex < lengthRight) {
	            array[i] = rightArray[rightIndex];
	            rightIndex++;
	        }
	    }
	}
	
	static void heapify(int[] array, int length, int i) {
	    int leftChild = 2*i+1;
	    int rightChild = 2*i+2;
	    int largest = i;

	    // if the left child is larger than parent
	    if (leftChild < length && array[leftChild] > array[largest]) {
	        largest = leftChild;
	    }

	    // if the right child is larger than parent
	    if (rightChild < length && array[rightChild] > array[largest]) {
	        largest = rightChild;
	    }

	    // if a swap needs to occur
	    if (largest != i) {
	        int temp = array[i];
	        array[i] = array[largest];
	        array[largest] = temp;
	        heapify(array, length, largest);
	    }
	}

	public static void heapSort(int[] array) {
	    if (array.length == 0) return;

	    // Building the heap
	    int length = array.length;
	    // we're going from the first non-leaf to the root
	    for (int i = length / 2-1; i >= 0; i--)
	        heapify(array, length, i);

	    for (int i = length-1; i >= 0; i--) {
	        int temp = array[0];
	        array[0] = array[i];
	        array[i] = temp;

	        heapify(array, i, 0);
	    }
	}
	
	static int partition(int[] array, int begin, int end) {
	    int pivot = end;

	    int counter = begin;
	    for (int i = begin; i < end; i++) {
	        if (array[i] < array[pivot]) {
	            int temp = array[counter];
	            array[counter] = array[i];
	            array[i] = temp;
	            counter++;
	        }
	    }
	    int temp = array[pivot];
	    array[pivot] = array[counter];
	    array[counter] = temp;

	    return counter;
	}

	public static void quickSort(int[] array, int begin, int end) {
	    if (end <= begin) return;
	    int pivot = partition(array, begin, end);
	    quickSort(array, begin, pivot-1);
	    quickSort(array, pivot+1, end);
	}
	
	public static void wonkySort(int[] array) {
		if(array.length %2 == 0) {
		    for (int i = 0; i < array.length; i++) {
		        int min = array[i];
		        int minId = i;
		        for (int j = i+1; j < array.length; j++) {
		            if (array[j] < min && array[j] > 0) {
		                min = array[j];
		                minId = j;
		            }
		        }
		        // swapping
		        int temp = array[i];
		        array[i] = min;
		        array[minId] = temp;
		    }
		}
	}

}
