package main;

public class Test {
	private static int intTest[] = {1, 2, 3, 9, 7, 11};
	private static int nullTest[] = null;
	private static int negativeTest[] = {-3, -4, 0, 5, 4};
	public static void main(String args[]){
		printArray(intTest);
		SortingAlgorithms.wonkySort(intTest);
		printArray(intTest);
//		printArray(nullTest);
//		SortingAlgorithms.insertionSort(nullTest);
//		printArray(nullTest);
		printArray(negativeTest);
		SortingAlgorithms.wonkySort(negativeTest);
		printArray(negativeTest);
	}
	
	public static void printArray(int[] array) {
		for(int i = 0; i<array.length; i++) {
			System.out.print(array[i] + ",");
		}
		System.out.println();
	}
}

