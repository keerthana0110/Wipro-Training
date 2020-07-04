import java.util.Scanner;

public class Main {
	private static Scanner sc;
	public static void main(String[] args) 
	{
		int number, i;
		sc = new Scanner(System.in);
		
		
		number = sc.nextInt();	
		
		for(i = number; i >= 0; i--)
		{
			System.out.print(i +"\t"); 
		}	
	}
}
