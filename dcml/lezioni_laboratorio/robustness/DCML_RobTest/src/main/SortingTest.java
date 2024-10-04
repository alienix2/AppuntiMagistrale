package main;

import java.util.Arrays;

/**
 * 
 */

/**
 * @author Tommy
 *
 */
public class SortingTest {

	private static int[][] TEST_INPUTS = {null, new int[]{-1, -10}, new int[]{1, 14, 6, -3}};
	
	/**
	 * @param args
	 */
	public static void main(String[] args) {
		for(int[] array : TEST_INPUTS){
			System.out.println("\nTesting input \t" + Arrays.toString(array));
			testAlgorithms(array);
		}
	}
	
	public static void testAlgorithms(int[] array){
		int arrLength = array == null ? 0 : array.length;
		int[] copiedArray = array == null ? null : Arrays.copyOf(array, arrLength);
		try {
			SortingAlgorithms.bubbleSort(copiedArray);
			System.out.println("BubbleSort: \t" + Arrays.toString(copiedArray));
		} catch(Exception ex){
			System.out.println("BubbleSort Failed");
		}
		copiedArray = array == null ? null : Arrays.copyOf(array, arrLength);
		try {
			SortingAlgorithms.insertionSort(copiedArray);
			System.out.println("InsertionSort: \t" + Arrays.toString(copiedArray));
		} catch(Exception ex){
			System.out.println("InsertionSort Failed");
		}
		copiedArray = array == null ? null : Arrays.copyOf(array, arrLength);
		try {
			SortingAlgorithms.quickSort(copiedArray, 0, copiedArray.length-1);
			System.out.println("QuickSort: \t" + Arrays.toString(copiedArray));
		} catch(Exception ex){
			System.out.println("QuickSort Failed");
		}
		copiedArray = array == null ? null : Arrays.copyOf(array, arrLength);
		try {
			SortingAlgorithms.mergeSort(copiedArray, 0, copiedArray.length-1);
			System.out.println("MergeSort: \t" + Arrays.toString(copiedArray));
		} catch(Exception ex){
			System.out.println("MergeSort Failed");
		}
		copiedArray = array == null ? null : Arrays.copyOf(array, arrLength);
		try {
			SortingAlgorithms.heapSort(copiedArray);
			System.out.println("HeapSort: \t" + Arrays.toString(copiedArray));
		} catch(Exception ex){
			System.out.println("HeapSort Failed");
		}
		copiedArray = array == null ? null : Arrays.copyOf(array, arrLength);
		try {
			Arrays.sort(copiedArray);
			System.out.println("Arrays-Sort: \t" + Arrays.toString(copiedArray));
		} catch(Exception ex){
			System.out.println("Arrays-Sort Failed");
		}
		copiedArray = array == null ? null : Arrays.copyOf(array, arrLength);
		try {
			SortingAlgorithms.wonkySort(copiedArray);
			System.out.println("Wonky-Sort: \t" + Arrays.toString(copiedArray));
		} catch(Exception ex){
			System.out.println("Wonky-Sort Failed");
		}
	}


}
