package Selenium_Day1;
import org.openqa.selenium.chrome.*;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;

import java.time.Duration;
import java.util.List;


public class Locator {

	public static void main(String[] args)
	{
		WebDriver driver= new ChromeDriver();
		driver.get("https://demo.opencart.com");
		
		driver.findElement(By.name("search")).sendKeys("HP LP3065");
		List<WebElement> links=driver.findElements(By.tagName("a"));
		List<WebElement> images=driver.findElements(By.tagName("img"));
		driver.findElement(By.xpath("//*[@id='search']/button")).click();
		
		System.out.println("Total number of LINKS in the page : "+links.size());
		System.out.println("Total number of IMAGES in the page: "+images.size());
		
		driver.quit();
	}

}
