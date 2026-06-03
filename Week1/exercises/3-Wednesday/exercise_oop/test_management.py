class TestCase:
    """Represents a single test case.

    Class Attributes:
        total_created (int): Count of all TestCase objects ever created

    Instance Attributes:
        name (str): Test name (e.g., "test_login_valid")
        description (str): What this test verifies
        priority (str): "high", "medium", or "low" (default: "medium")
        tags (list): Labels like ["smoke", "regression"]
    """

    total_created = 0

    def __init__(self, name, description="", tags=None, priority="medium") -> None:
        if not self.is_valid_name(name):
            raise ValueError("Test name must start with 'test_' and contain no spaces.")

        self.name = name
        self.description = description
        self.tags = tags if tags is not None else []
        self.priority = priority

        TestCase.total_created += 1

    def run(self):
        """Simulate running the test. Return True for pass, False for fail.
        For now, use: return "fail" not in self.name
        """
        return "fail" not in self.name

    @classmethod
    def from_dict(cls, data):
        """Create a TestCase from a dictionary.
        Example: TestCase.from_dict({"name": "test_login", "priority": "high"})
        """
        return cls(
            data["name"],
            data.get("description", ""),
            data.get("tags", []),
            data.get("priority", "medium"),
        )

    @staticmethod
    def is_valid_name(name):
        """Check if name starts with 'test_' and has no spaces."""
        return name.startswith("test_") and " " not in name


class TestResult:
    """The outcome of running a single test.

    Instance Attributes:
        test_name (str): Which test was run
        status (str): "pass" or "fail"
        duration_ms (float): How long it took
        error_message (str or None): Error details if failed
    """

    def __init__(self, test_name, status, duration_ms, error_message=None) -> None:
        self.test_name = test_name
        self.status = status
        self.duration_ms = duration_ms
        self.error_message = error_message

    def summary(self):
        """Return a one-line summary like: '✅ test_login (120ms)'"""
        icon = "✅" if self.status == "pass" else "❌"
        return f"{icon} {self.test_name} {self.duration_ms}ms"


class TestSuite:
    """A collection of test cases.

    Instance Attributes:
        name (str): Suite name
        tests (list): List of TestCase objects

    Methods:
        add_test(test): Add a TestCase
        remove_test(name): Remove by name
        get_by_priority(priority): Return tests matching the priority
        count(): Return number of tests
    """

    def __init__(self, name) -> None:
        self.name = name
        self.tests = []

    def add_test(self, test):
        self.tests.append(test)

    def remove_test(self, name):
        self.tests = [test for test in self.tests if test.name != name]

    def get_by_priority(self, priority):
        return [test for test in self.tests if test.priority == priority]

    def count(self):
        return len(self.tests)


class TestRunner:
    """Executes a TestSuite and collects results.

    Methods:
        run(suite): Run all tests in a suite, return list of TestResult
        summary(results): Print a formatted summary
    """

    def run(self, suite):
        """Run each test in the suite and return a list of TestResults."""
        import random
        import time

        results = []
        for test in suite.tests:
            start = time.time()
            passed = test.run()
            duration = (time.time() - start) * 1000
            # Simulate varying duration
            duration += random.uniform(50, 500)
            result = TestResult(
                test.name,
                "pass" if passed else "fail",
                round(duration, 1),
                None if passed else f"{test.name} assertion failed",
            )
            results.append(result)
        return results

    def summary(self, results):
        passed = sum([1 for res in results if res.status == "pass"])
        failed = len(results) - passed

        print("Test Results:")
        for res in results:
            print(res.summary())
            if res.error_message:
                print(f"    Error: {res.error_message}")

        print(f"\nPassed: {passed}")
        print(f"Failed: {failed}")
        print(f"Total: {len(results)}")


def main():
    tests = [
        TestCase("test_login_valid", "Valid user can log in", ["smoke"], "high"),
        TestCase(
            "test_profile_update", "User can update profile", ["regression"], "medium"
        ),
        TestCase(
            "test_fail_password_reset", "Password reset flow", ["regression"], "high"
        ),
        TestCase("test_logout", "User can log out", ["smoke"], "low"),
        TestCase.from_dict(
            {
                "name": "test_checkout",
                "description": "Checkout completes successfully",
                "priority": "high",
                "tags": ["smoke", "payment"],
            }
        ),
        TestCase.from_dict(
            {
                "name": "test_fail_search_results",
                "description": "Search returns expected results",
                "priority": "medium",
                "tags": ["search"],
            }
        ),
    ]

    suite = TestSuite("Core App Suite")
    for test in tests:
        suite.add_test(test)

    high_priority_tests = suite.get_by_priority("high")
    print("High Priority Tests:")
    for t in high_priority_tests:
        print(f"- {t.name}")

    runner = TestRunner()
    results = runner.run(suite)
    print()
    runner.summary(results)


if __name__ == "__main__":
    main()
