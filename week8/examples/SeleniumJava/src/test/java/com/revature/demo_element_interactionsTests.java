package com.revature;

import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;

import static org.junit.jupiter.api.Assertions.assertEquals;

/**
 * Demo: Element Interactions in Selenium
 * 1. WebElement represents any HTML element
 * 2. Basic interactions: click, sendKeys, clear
 * 3. Information getters: getText, getAttribute, getCssValue
 * 4. State checks: isDisplayed, isEnabled, isSelected
 *
 * TEST site: https://the-internet.herokuapp.com
 */

@DisplayName("Element Interactions Demo")
public class demo_element_interactionsTests {

    private WebDriver driver;
    private static final String BASE_URL = "https://the-internet.herokuapp.com";

    @BeforeEach
    void setUp(){
        driver = new ChromeDriver();
        driver.manage().window().maximize();
    }

    @AfterEach
    void tearDown() {
        if(driver != null){
            driver.quit();
        }
    }

    //1. Basic Click Operations
    @Test
    @DisplayName(("click() - Basic button click"))
    void click_basicButton() {
        /* click() simulates a mouse click on the element
         * works on buttons, links, checkboxes, etc.
         */
        driver.get(BASE_URL + "/add_remove_elements/");

        //Find and click the "Add Element" button
        WebElement addButton = driver.findElement(
                By.xpath("//button[text()='Add Element']")
        );

        //Before clicking
        int elementsBefore = driver.findElements(By.className("added-manually")).size();
        System.out.println("Elements before click: " +elementsBefore);

        //click the button
        addButton.click();

        //After clicking
        int elementsAfter = driver.findElements(
                By.className("added-manually")).size();
        System.out.println("Elements after click: " + elementsAfter);

        assertEquals(elementsBefore +1, elementsAfter);
    }
}
