package Selenium_Day1;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.*;


/*
 TEST CASE:
 
 1- Launch Browser
 2- Open URL
 3- Validate Title
 4- Close Browser
 */


public class First_TestCase {

	public static void main(String[] args) 
	{
		WebDriver driver=new ChromeDriver();  								//Launching Driver
		driver.get("https://demo.opencart.com");  							//Opening URL
		
				String title= driver.getTitle();							//Validating Title
				if (title.equals("Your Store"))
			System.out.println("Test Passed: Title Validated");
		else
			System.out.println("Test Failed: Title Doesn't Match");
		
		driver.close();														//Closing Browserr
	}

}
