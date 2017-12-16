package HackerRank;

import java.util.Scanner;

public class Sirion1 {

	public static void main(String[] args) 
	{
		Scanner scan=new Scanner(System.in);
		int n=scan.nextInt();		// Size of array
		int k=scan.nextInt();		// Difference of elements in array
		int arr[]=new int[n];
		
		for(int i=0; i<n; i++)		//Scanning array elements
		{
			arr[i]=scan.nextInt();
		}
		
		System.out.println(CalculateCount(arr,n,k));

	}

	private static int CalculateCount(int[] arr, int n, int k) 
	{
		int count=0;
		for(int i=0; i<n; i++)
		{
			for(int j=i+1; j<n; j++)
			{
				if(Math.abs(arr[i] - arr[j]) == k)		// Checking the difference
				{
					count++;
				}
			}
		}	
		return count;
	}

}
