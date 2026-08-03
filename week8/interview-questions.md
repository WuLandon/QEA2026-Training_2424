# Interview Questions: Week 8 - Selenium, System Testing

Each question includes a **Where to study** line. Start with the primary link, then follow any supporting links when you need examples or a deeper explanation.

## Beginner (Foundational)

### Q1: What is the difference between `find_element` and `find_elements` in Python Selenium?
**Keywords:** Single, List, NoSuchElementException, Empty List

**Where to study:** [Find Methods and Screenshots — `find_element` vs `find_elements`](1-monday/written/find-methods-screenshots-python.md#find_element-vs-find_elements)

<details>
<summary>Click to Reveal Answer</summary>

`find_element` returns a single WebElement and raises a `NoSuchElementException` if no matching element is found. `find_elements` returns a list of all matching WebElements and returns an empty list (rather than raising an exception) if no elements match the locator.
</details>

---

### Q2: What is the purpose of the `By` class in Python Selenium?
**Keywords:** Locator Strategies, Element Location, ID, CSS Selector, XPath

**Where to study:** [Element Locator Strategies — The `By` Class](1-monday/written/locator-strategies-python.md#the-by-class) and [Locator Strategy Comparison](1-monday/written/locator-strategies-python.md#locator-strategy-comparison)

<details>
<summary>Click to Reveal Answer</summary>

The `By` class provides constants for specifying locator strategies when finding elements. It includes options like `By.ID`, `By.NAME`, `By.CLASS_NAME`, `By.TAG_NAME`, `By.LINK_TEXT`, `By.PARTIAL_LINK_TEXT`, `By.CSS_SELECTOR`, and `By.XPATH`. Using the `By` class makes the code more readable and allows you to specify how elements should be located.
</details>

---

### Q3: What is the difference between implicit waits and explicit waits in Selenium?
**Keywords:** Global Timeout, Specific Condition, WebDriverWait, expected_conditions

**Where to study:** [Waiting Strategies Overview](1-monday/written/waiting-window-handling-python.md#waiting-strategies-overview), [Implicit Waits](1-monday/written/waiting-window-handling-python.md#implicit-waits), and [Explicit Waits with `WebDriverWait`](1-monday/written/waiting-window-handling-python.md#explicit-waits-with-webdriverwait)

<details>
<summary>Click to Reveal Answer</summary>

Implicit waits set a global timeout that applies to all `find_element` calls - Selenium will poll the DOM until the element is found or the timeout expires. Explicit waits (using `WebDriverWait` with `expected_conditions`) wait for a specific condition to be true for a specific element, providing more fine-grained control. Explicit waits are preferred because they can wait for conditions like visibility, clickability, or text presence.
</details>

---

### Q4: What is System Testing and how does it differ from Integration Testing?
**Keywords:** Complete System, Requirements, Component Interactions, End-to-End

**Where to study:** [System Testing — What is System Testing?](2-tuesday/written/system-testing.md#what-is-system-testing), [System Testing vs Other Testing Levels](2-tuesday/written/system-testing.md#system-testing-vs-other-testing-levels), and [Integration Testing vs System Testing](2-tuesday/written/integration-testing.md#integration-testing-vs-system-testing)

<details>
<summary>Click to Reveal Answer</summary>

System Testing validates the complete, integrated system against specified requirements from an end-user perspective. It tests the system as a whole. Integration Testing focuses on testing the interactions and interfaces between individual components or modules. System testing occurs after integration testing and tests broader end-to-end workflows, while integration testing verifies that components work correctly when combined.
</details>

---

### Q5: What is Behavior-Driven Development (BDD) and what problem does it solve?
**Keywords:** Collaboration, Business Language, Given-When-Then, Three Amigos

**Where to study:** [BDD — What is Behavior-Driven Development?](3-wednesday/written/bdd-intro.md#what-is-behavior-driven-development), [The Three Amigos](3-wednesday/written/bdd-intro.md#the-three-amigos), and [Benefits of BDD](3-wednesday/written/bdd-intro.md#benefits-of-bdd)

<details>
<summary>Click to Reveal Answer</summary>

BDD is a software development approach that bridges the gap between technical and business stakeholders by writing tests in natural language that everyone can understand. It solves the problem of miscommunication between business requirements and implementation by using executable specifications written in Given-When-Then format. The Three Amigos practice (Business, Developer, QA) ensures shared understanding before development begins.
</details>

---

### Q6: What is Gherkin and what are its main keywords?
**Keywords:** Feature, Scenario, Given, When, Then

**Where to study:** [Gherkin Syntax Overview](3-wednesday/written/feature-scenario-step-syntax.md#gherkin-syntax-overview), [The Feature Keyword](3-wednesday/written/feature-scenario-step-syntax.md#the-feature-keyword), [The Scenario Keyword](3-wednesday/written/feature-scenario-step-syntax.md#the-scenario-keyword), and [Step Keywords](3-wednesday/written/feature-scenario-step-syntax.md#step-keywords)

<details>
<summary>Click to Reveal Answer</summary>

Gherkin is a business-readable, domain-specific language used to describe software behavior in BDD frameworks like Cucumber and Behave. Its main keywords are: `Feature` (describes the feature being tested), `Scenario` (a specific test case), `Given` (preconditions/setup), `When` (actions being performed), `Then` (expected outcomes), and `And`/`But` (additional steps that take the meaning of the previous keyword).
</details>

---

### Q7: What is a stub and what is a driver in Integration Testing?
**Keywords:** Test Double, Top-Down, Bottom-Up, Simulate

**Where to study:** [Integration Testing — Stubs and Drivers](2-tuesday/written/integration-testing.md#stubs-and-drivers), [Top-Down Integration](2-tuesday/written/integration-testing.md#3-top-down-integration), and [Bottom-Up Integration](2-tuesday/written/integration-testing.md#4-bottom-up-integration)

<details>
<summary>Click to Reveal Answer</summary>

A stub is a dummy implementation of a lower-level module used in top-down integration testing. It simulates the behavior of modules that haven't been developed or integrated yet. A driver is a dummy implementation that calls the module under test, used in bottom-up integration testing. It simulates higher-level modules that would normally call the component being tested.
</details>

---

### Q8: What is the difference between Cucumber (Java) and Behave (Python)?
**Keywords:** Gherkin, Step Definitions, Context Object, Hooks

**Where to study:** [Behave as Python's Cucumber](4-thursday/written/behave.md#behave-as-pythons-cucumber), [Comparison with Cucumber-JVM](4-thursday/written/behave.md#comparison-with-cucumber-jvm), [Behave Step Definitions](4-thursday/written/behave-framework.md#step-definitions), [The Context Object](4-thursday/written/behave-framework.md#the-context-object), and [`environment.py` Hooks](4-thursday/written/behave-fixtures.md#environmentpy-hooks)

<details>
<summary>Click to Reveal Answer</summary>

Both Cucumber and Behave use Gherkin feature files, so the specifications look very similar. Their glue code and lifecycle APIs differ: Cucumber-JVM commonly uses Java annotations (`@Given`, `@When`, `@Then`) and Java objects to hold scenario state, while Behave uses Python decorators (`@given`, `@when`, `@then`) and a `context` object for sharing state. Behave defines hooks in `environment.py`; Cucumber-JVM commonly defines hooks with `@Before` and `@After`. Cucumber can also integrate with dependency-injection libraries, but dependency injection is not required for every Cucumber project.
</details>

---

### Q9: What is Playwright and how does it differ from Selenium?
**Keywords:** Microsoft, Auto-Wait, Browser Contexts, W3C WebDriver

**Where to study:** [Playwright — What is Playwright?](5-friday/written/playwright-java.md#what-is-playwright), [Playwright vs Selenium](5-friday/written/playwright-java.md#playwright-vs-selenium), and [Key Playwright Advantages](5-friday/written/playwright-java.md#key-playwright-advantages)

<details>
<summary>Click to Reveal Answer</summary>

Playwright is a modern browser automation library developed by Microsoft. It provides locator-based auto-waiting, isolated browser contexts, web-first assertions, tracing, video recording, and network interception through one API. Selenium is based on the W3C WebDriver standard and has a larger ecosystem, broader language support, and support for more browser and legacy environments. Playwright supports Chromium, Firefox, and WebKit with closely integrated browser builds. Architecture may affect performance, but the stronger interview distinction is Playwright's built-in waiting, isolation, and debugging features versus Selenium's standardized, broad ecosystem.
</details>

---

### Q10: What are Browser Contexts in Playwright and why are they useful?
**Keywords:** Isolation, Parallel Execution, Session, Cookies

**Where to study:** [Playwright Browser Management — Browser Contexts](5-friday/written/playwright-browser-management-java.md#browser-contexts), [Incognito Mode](5-friday/written/playwright-browser-management-java.md#incognito-mode), and [Proper Browser Cleanup](5-friday/written/playwright-browser-management-java.md#proper-browser-cleanup)

<details>
<summary>Click to Reveal Answer</summary>

Browser Contexts are isolated browser sessions within a single browser instance. Each context has its own cookies, local storage, and session data—they don't share state. This allows a test runner to execute tests in parallel without session conflicts, lets different users be logged in simultaneously, and provides clean state without restarting the browser. Contexts are much faster to create than new browser instances.
</details>

---

## Intermediate (Application)

### Q11: You have a web application where content loads dynamically via AJAX. How would you handle waiting for this content in Python Selenium?
**Hint:** Think about `WebDriverWait` and `expected_conditions`.

**Where to study:** [Explicit Waits with `WebDriverWait`](1-monday/written/waiting-window-handling-python.md#explicit-waits-with-webdriverwait), [Expected Conditions](1-monday/written/waiting-window-handling-python.md#expected-conditions-ec), and [Practical Explicit Wait Examples](1-monday/written/waiting-window-handling-python.md#practical-explicit-wait-examples)

<details>
<summary>Click to Reveal Answer</summary>

You should use explicit waits with `WebDriverWait` and appropriate expected conditions. For example:

```python
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

wait = WebDriverWait(driver, 10)
element = wait.until(EC.visibility_of_element_located((By.ID, "ajax-content")))
```

You might also wait for a loading spinner to disappear using `EC.invisibility_of_element_located()`, or wait for specific text using `EC.text_to_be_present_in_element()`. Avoid using `time.sleep()` as it wastes time and creates brittle tests.
</details>

---

### Q12: A product owner asks you to write a BDD scenario for a shopping cart feature. They say "users should be able to add items to their cart." What questions would you ask in a Three Amigos session, and write an example scenario.
**Hint:** Think about edge cases, validation, and acceptance criteria.

**Where to study:** [The Three Amigos](3-wednesday/written/bdd-intro.md#the-three-amigos), [Acceptance Criteria Definition](3-wednesday/written/user-stories-acceptance-criteria.md#acceptance-criteria-definition), [Given-When-Then Format](3-wednesday/written/user-stories-acceptance-criteria.md#given-when-then-format), and [Writing Effective Scenarios](3-wednesday/written/feature-scenario-step-syntax.md#writing-effective-scenarios)

<details>
<summary>Click to Reveal Answer</summary>

Questions to ask:
- What happens if the item is out of stock?
- Is there a maximum quantity limit?
- Should logged-out users be able to add items?
- What confirmation should the user see?
- Can the same item be added multiple times?

Example scenario:
```gherkin
Feature: Shopping Cart
  As a customer
  I want to add items to my cart
  So that I can purchase them later

  Scenario: Add available item to cart
    Given the product "Blue Widget" is in stock
    And I am viewing the product page for "Blue Widget"
    When I click the "Add to Cart" button
    Then my cart should contain 1 item
    And I should see a confirmation message "Blue Widget added to cart"

  Scenario: Cannot add out-of-stock item
    Given the product "Red Widget" is out of stock
    When I try to add "Red Widget" to my cart
    Then I should see an error message "This item is currently unavailable"
```
</details>

---

### Q13: Your team needs to run the same test scenario across multiple browsers (Chrome, Firefox, Safari). How would you approach this in Playwright vs Selenium?
**Hint:** Consider browser launching and parallel execution.

**Where to study:** [Playwright Browser Management — Launching Browsers](5-friday/written/playwright-browser-management-java.md#launching-browsers), [Cross-Browser Testing](5-friday/written/playwright-browser-management-java.md#cross-browser-testing), and [Playwright Parallel Execution](5-friday/written/playwright-java.md#3-parallel-execution)

<details>
<summary>Click to Reveal Answer</summary>

**Playwright approach:**
Parameterize the test with JUnit and launch Playwright's Chromium, Firefox, and WebKit browser types:
```java
// Use the installed Chrome channel; omit setChannel for bundled Chromium.
Browser chromeBrowser = playwright.chromium().launch(
    new BrowserType.LaunchOptions().setChannel("chrome"));
Browser firefoxBrowser = playwright.firefox().launch();
Browser webkitBrowser = playwright.webkit().launch();
```
Browser contexts give each test an inexpensive, isolated session. JUnit configuration or another test runner controls whether Java tests actually execute concurrently. Also, WebKit testing is useful Safari-engine coverage, but Playwright's WebKit build is not the branded Safari browser.

**Selenium approach:**
You need separate WebDriver instances for each browser:
```python
from selenium import webdriver
chrome_driver = webdriver.Chrome()
firefox_driver = webdriver.Firefox()
# Safari requires SafariDriver setup
```
Your test runner can run local WebDriver instances concurrently; Selenium Grid is useful when you need remote or distributed browser execution.

Playwright's advantage is a consistent API, lightweight isolated contexts, and closely integrated browser tooling. Selenium's advantage is standards-based automation of installed browsers, including actual Safari through SafariDriver, plus broader browser and infrastructure support.
</details>

---

### Q14: You're writing integration tests for a service that depends on a payment gateway that isn't available in your test environment. How would you approach this?
**Hint:** Consider stubs and what behavior to simulate.

**Where to study:** [Stubs and Drivers](2-tuesday/written/integration-testing.md#stubs-and-drivers), especially [Stubs for Top-Down Testing](2-tuesday/written/integration-testing.md#stubs-for-top-down-testing), and [Identifying Integration Points](2-tuesday/written/integration-testing.md#identifying-integration-points)

<details>
<summary>Click to Reveal Answer</summary>

Create a stub that simulates the payment gateway's behavior:

```python
class PaymentGatewayStub:
    def process_payment(self, amount, card_details):
        """Stub that simulates payment processing"""
        # Simulate successful payment
        if card_details.get('number', '').startswith('4111'):
            return {'success': True, 'transaction_id': 'STUB-TXN-123'}
        # Simulate declined card
        if card_details.get('number', '').startswith('4000'):
            return {'success': False, 'error': 'Card declined'}
        return {'success': False, 'error': 'Invalid card'}
```

The stub should:
1. Handle the main success path
2. Simulate common failure scenarios (declined card, timeout)
3. Return realistic response formats
4. Allow testing edge cases without real transactions

This tests your service's integration with the payment adapter boundary without depending on the unavailable gateway. Because a stub can drift from the real provider's contract, also schedule contract tests or tests against the gateway's sandbox when one is available.
</details>

---

## Advanced (Deep Dive)

### Q15: Explain how Playwright's auto-wait mechanism works under the hood and why it's considered more reliable than Selenium's approach. What conditions does Playwright check before performing actions?

**Where to study:** [Writing Your First Playwright Test — Auto-Waiting Behavior](5-friday/written/writing-first-playwright-test-java.md#auto-waiting-behavior), [Playwright — Auto-Wait](5-friday/written/playwright-java.md#1-auto-wait), and [Web-First Assertions](5-friday/written/playwright-java.md#2-web-first-assertions)

<details>
<summary>Click to Reveal Answer</summary>

Playwright resolves the locator and performs actionability checks required by the requested action. For `page.locator("#button").click()`, it waits until the locator resolves to exactly one element and checks that the element is:

1. **Visible** - It has a visible, non-empty bounding box
2. **Stable** - It is not moving or animating
3. **Receives Events** - It is not obscured at the action point
4. **Enabled** - It is not disabled

Other actions use the checks relevant to them—for example, `fill()` also requires the element to be editable. Playwright waits up to the configured timeout and fails with a timeout error if the requirements never become true.

This is often more reliable because waiting is built into locator actions and Playwright assertions retry until their expected condition is met. Selenium also supports reliable synchronization, but the test author usually expresses it with explicit waits such as `WebDriverWait`; ordinary assertion libraries do not automatically retry. Playwright reduces common timing gaps, though it cannot eliminate all flaky tests.
</details>

---

## Question Distribution Summary

| Difficulty | Count | Percentage |
|------------|-------|------------|
| Beginner | 10 | 67% |
| Intermediate | 4 | 27% |
| Advanced | 1 | 6% |
| **Total** | **15** | **100%** |

## Topics Covered

- **Monday**: Python Selenium (locators, waits, `By` class, `find_element`/`find_elements`)
- **Tuesday**: System Testing vs Integration Testing (stubs, drivers, test levels)
- **Wednesday**: Cucumber & BDD (Gherkin, Three Amigos, Given-When-Then)
- **Thursday**: Behave Framework (Python BDD, context object, comparison with Cucumber)
- **Friday**: Playwright (auto-wait, browser contexts, architecture comparison with Selenium)

## How to Study This Question Bank

1. **Answer before revealing.** Give yourself 60–90 seconds to answer aloud, then open the answer and identify what you omitted.
2. **Use a four-part interview structure.** State the definition, explain how it works, give the important tradeoff, and finish with a concrete example.
3. **Practice the comparison questions as tables.** Make two columns for system vs integration testing, Cucumber vs Behave, and Playwright vs Selenium. Recall at least three meaningful differences without looking.
4. **Write the application answers from memory.** Re-create the explicit-wait snippet for Q11, a Gherkin scenario for Q12, the cross-browser structure for Q13, and a small payment stub for Q14.
5. **Use spaced repetition.** Review missed questions the next day, three days later, and one week later. Spend less time rereading answers you already recall correctly.
6. **Run a mock interview.** Record yourself answering five randomly selected questions. Listen for vague claims, missing examples, and answers longer than two minutes.

