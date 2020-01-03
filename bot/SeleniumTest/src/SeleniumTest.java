
import static org.junit.Assert.*;
import static org.junit.Assert.assertNotNull;
import static org.junit.Assert.assertTrue;

import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.TimeUnit;

import org.junit.AfterClass;
import org.junit.Before;
import org.junit.BeforeClass;
import org.junit.Test;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;

import org.openqa.selenium.Keys;
import org.openqa.selenium.StaleElementReferenceException;
import org.openqa.selenium.interactions.Actions;
import org.openqa.selenium.JavascriptExecutor;

import io.github.bonigarcia.wdm.WebDriverManager;


public class SeleniumTest {
	private static WebDriver driver;
	private static WebDriverWait wait; 
	
	@BeforeClass
	public static void postMessage() throws Exception
	{
		WebDriverManager.chromedriver().setup();
		driver = new ChromeDriver();
		
		driver.get("https://csc510-projecthq.slack.com/");	

		// Wait until page loads and we can see a sign in button.
		wait = new WebDriverWait(driver, 30);
		wait.until(ExpectedConditions.visibilityOfElementLocated(By.id("signin_btn")));

		// Find email and password fields.
		WebElement email = driver.findElement(By.id("email"));
		WebElement pw = driver.findElement(By.id("password"));

		// Enter our email and password
		// If running this from Eclipse, you should specify these variables in the run configurations.
		email.sendKeys(System.getenv("SLACK_EMAIL"));
		pw.sendKeys(System.getenv("SLACK_PASSWORD"));

		// Click
		WebElement signin = driver.findElement(By.id("signin_btn"));
		signin.click();

		// Wait until we go to general channel.
		wait.until(ExpectedConditions.titleContains("general"));
		
		
	}
	
	
	@AfterClass
	public static void tearDown() throws Exception{
		driver.close();
		driver.quit();
	}
	
	@Test
	public void TestCase3_Alternative() throws Exception{
	
		driver.get("https://csc510-projecthq.slack.com");

		wait = new WebDriverWait(driver, 30);
		wait.until(ExpectedConditions.titleContains("general"));

		// Type something
		//The id of input message is "undefined" as shown in our Slack. 
		WebElement messageBox = driver.findElement(By.id("undefined"));
		assertNotNull(messageBox);

		Actions actions = new Actions(driver);
		actions.moveToElement(messageBox);
		actions.click();
		actions.sendKeys("summary");
		actions.sendKeys(Keys.RETURN);
		actions.build().perform();

		Thread.sleep(3000);
	}
	
	
	@Test
	public void TestCase1_HappyPath() throws Exception{
	
		driver.get("https://csc510-projecthq.slack.com");

		wait = new WebDriverWait(driver, 30);
		wait.until(ExpectedConditions.titleContains("general"));

		// Type something
		WebElement messageBox = driver.findElement(By.id("undefined"));
		assertNotNull(messageBox);

		Actions actions = new Actions(driver);
		actions.moveToElement(messageBox);
		actions.click();
		actions.sendKeys("How to install JAVA?");
		actions.sendKeys(Keys.RETURN);
		actions.build().perform();

		wait.withTimeout(3, TimeUnit.SECONDS).ignoring(StaleElementReferenceException.class);
		
		messageBox = driver.findElement(By.xpath("//button[@class = "overflow_ellipsis" and text()='Yes']"));
		//System.out.println(messageBox.getAttribute("overflow_ellipsis"));
		assertNotNull(messageBox);
		//actions = new Actions(driver);
		actions.moveToElement(messageBox);
		actions.click();
		Thread.sleep(3000);
	}
	
	@Test
	public void TestCase2_HappyPath() throws Exception{
	
		//driver.get("https://csc510-projecthq.slack.com");

		//wait = new WebDriverWait(driver, 30);
		//wait.until(ExpectedConditions.titleContains("general"));

		// Type something
		//WebElement messageBox = driver.findElement(By.id("undefined"));
		//assertNotNull(messageBox);

		WebElement messageBox = driver.findElement(By.xpath("//button[@class = "overflow_ellipsis" and text()='Yes, Search it on StackOverFlow']"));
		assertNotNull(messageBox);
		Actions actions = new Actions(driver);
		actions.moveToElement(messageBox);
		actions.click();
		Thread.sleep(3000); 
	}
	
	@Test
	public void TestCase3_HappyPath() throws Exception{
		WebElement messageBox = driver.findElement(By.id("undefined"));
		assertNotNull(messageBox);
		
		Actions actions = new Actions(driver);
		actions.moveToElement(messageBox);
		actions.click();
		actions.sendKeys("How to install JAVA?");
		actions.sendKeys(Keys.RETURN);
		actions.build().perform();
		
		wait.withTimeout(3, TimeUnit.SECONDS).ignoring(StaleElementReferenceException.class);
		Thread.sleep(3000);
	}
	
	@Test
	public void TestCase1_AlternativePath() throws Exception{
		driver.get("https://csc510-projecthq.slack.com");

		wait = new WebDriverWait(driver, 30);
		wait.until(ExpectedConditions.titleContains("general"));

		// Type something
		WebElement messageBox = driver.findElement(By.id("undefined"));
		assertNotNull(messageBox);

		Actions actions = new Actions(driver);
		actions.moveToElement(messageBox);
		actions.click();
		actions.sendKeys("How to install JAVA?");
		actions.sendKeys(Keys.RETURN);
		actions.build().perform();

		wait.withTimeout(3, TimeUnit.SECONDS).ignoring(StaleElementReferenceException.class);
		
		messageBox = driver.findElement(By.xpath("//button[@class = "overflow_ellipsis" and text()='No']"));
		//System.out.println(messageBox.getAttribute("overflow_ellipsis"));
		assertNotNull(messageBox);
		//actions = new Actions(driver);
		actions.moveToElement(messageBox);
		actions.click();
		Thread.sleep(3000);
	}
	
	@Test
	public void TestCase2_AlternativePath() throws Exception{
		driver.get("https://csc510-projecthq.slack.com");

		wait = new WebDriverWait(driver, 30);
		wait.until(ExpectedConditions.titleContains("general"));

		// Type something
		WebElement messageBox = driver.findElement(By.id("undefined"));
		assertNotNull(messageBox);

		Actions actions = new Actions(driver);
		actions.moveToElement(messageBox);
		actions.click();
		actions.sendKeys("How to install JAVA?");
		actions.sendKeys(Keys.RETURN);
		actions.build().perform();

		wait.withTimeout(3, TimeUnit.SECONDS).ignoring(StaleElementReferenceException.class);
		
		messageBox = driver.findElement(By.xpath("//button[@class = "overflow_ellipsis" and text()='Yes']"));
		//System.out.println(messageBox.getAttribute("overflow_ellipsis"));
		assertNotNull(messageBox);
		//actions = new Actions(driver);
		actions.moveToElement(messageBox);
		actions.click();
		Thread.sleep(3000);
	
		WebElement messageBox = driver.findElement(By.xpath("//button[@class = "overflow_ellipsis" and text()='No, Thanks']"));
		assertNotNull(messageBox);
		Actions actions = new Actions(driver);
		actions.moveToElement(messageBox);
		actions.click();
		Thread.sleep(3000); 
	
	}
	
	
	
	
	
}
