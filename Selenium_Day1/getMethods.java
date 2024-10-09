package Selenium_Day_2;
import java.util.Set;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.*;

import io.opentelemetry.exporter.logging.SystemOutLogRecordExporter;
public class getMethods {

	public static void main(String[] args) throws InterruptedException {
		
		WebDriver driver=new ChromeDriver();
		driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login");
	
		System.out.println(driver.getTitle());						//return title of the page
		
		System.out.println(driver.getCurrentUrl());					//return url of the page
		
		System.out.println(driver.getWindowHandle());				//return ID of the single Browser Window
		
		String title= driver.getTitle();							//Validating Title
		if (title.equals("OrangeHRM"))
	System.out.println("Test Passed: Title Validated");
else
	System.out.println("Test Failed: Title Doesn't Match");
		
		driver.findElement(By.linkText("OrangeHRM, Inc")).click();
		
		Set<String> windowids=driver.getWindowHandles();
		System.out.println(windowids);
		
		
		
		
	}

}
