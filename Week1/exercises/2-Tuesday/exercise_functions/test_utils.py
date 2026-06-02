import re


# Task 1: Basic Functions
def format_test_name(name):
    """Convert a human-readable name to a test function name.

    Example:
        format_test_name("Valid Login") → "test_valid_login"
        format_test_name("  Search Results Page  ") → "test_search_results_page"

    Rules:
        - Lowercase
        - Spaces replaced with underscores
        - Leading/trailing whitespace stripped
        - Prefixed with "test_"
    """
    cleaned = name.strip().lower().replace(" ", "_")
    return f"test_{cleaned}"


def is_valid_test_name(name):
    """Check if a string is a valid test function name.

    Rules:
        - Must start with "test_"
        - Must contain only lowercase letters, digits, and underscores
        - Must be at least 6 characters (e.g., "test_x")

    Returns: bool
    """
    if len(name) < 6:
        return False

    pattern = r"^test_[a-z0-9_]+$"
    return bool(re.match(pattern, name))


assert format_test_name("Valid Login") == "test_valid_login"
assert format_test_name("  Search Results  ") == "test_search_results"
assert is_valid_test_name("test_login") == True  # noqa: E712
assert is_valid_test_name("login_test") == False  # noqa: E712
assert is_valid_test_name("test_") == False  # noqa: E712


# Task 2: Default Parameters
def create_test_result(name, status="pass", duration_ms=0, error=None):
    """Create a test result dictionary.

    Args:
        name: Test name (required)
        status: "pass" or "fail" (default: "pass")
        duration_ms: Execution time in ms (default: 0)
        error: Error message if failed (default: None)

    Returns:
        dict with keys: name, status, duration_ms, error
    """
    return {"name": name, "status": status, "duration_ms": duration_ms, "error": error}


def format_duration(ms, unit="ms"):
    """Format a duration value with the specified unit.

    Args:
        ms: Duration in milliseconds
        unit: "ms", "s", or "min" (default: "ms")

    Returns:
        Formatted string like "1,200ms" or "1.20s" or "0.02min"
    """
    if unit == "ms":
        return f"{ms:,}ms"

    if unit == "s":
        seconds = ms / 1000
        return f"{seconds:.2f}s"

    if unit == "min":
        minutes = ms / 1000 / 60
        return f"{minutes:.2f}min"


r1 = create_test_result("test_login")
assert r1 == {"name": "test_login", "status": "pass", "duration_ms": 0, "error": None}

r2 = create_test_result(
    "test_checkout", status="fail", duration_ms=2300, error="Timeout"
)
assert r2["status"] == "fail"
assert r2["error"] == "Timeout"

assert format_duration(1200) == "1,200ms"
assert format_duration(1200, "s") == "1.20s"


# Task 3: *args and **kwargs
def calculate_stats(*scores):
    """Calculate statistics for any number of scores.

    Returns:
        dict with keys: count, total, average, min, max

    Raises:
        ValueError if no scores provided
    """
    if not scores:
        raise ValueError("At least one score is required")

    stats = {
        "count": len(scores),
        "total": sum(scores),
        "average": sum(scores) / len(scores),
        "min": min(scores),
        "max": max(scores),
    }

    return stats


def build_test_config(**settings):
    """Build a test configuration with defaults.

    Default config:
        browser: "chrome"
        headless: False
        timeout: 30
        retries: 0
        base_url: "http://localhost:3000"

    Any **settings passed override the defaults.

    Returns: dict
    """
    config = {
        "browser": "chrome",
        "headless": False,
        "timeout": 30,
        "retries": 0,
        "base_url": "http://localhost:3000",
    }

    config.update(settings)

    return config


stats = calculate_stats(85, 92, 78, 95, 88)
assert stats["count"] == 5
assert stats["average"] == 87.6
assert stats["min"] == 78
assert stats["max"] == 95

config = build_test_config(headless=True, timeout=60)
assert config["browser"] == "chrome"  # default
assert config["headless"] == True  # overridden  # noqa: E712
assert config["timeout"] == 60  # overridden


# Task 4: Multiple Return Values & Composition
def analyze_results(*results):
    """Analyze a list of test result dicts.

    Args:
        *results: test result dicts (from create_test_result)

    Returns:
        tuple of (passed_count, failed_count, pass_rate, avg_duration)
    """
    if not results:
        return (0, 0, 0.0, 0.0)

    passed_count = sum(1 for r in results if r["status"] == "pass")
    failed_count = sum(1 for r in results if r["status"] == "fail")

    total_results = len(results)
    pass_rate = (passed_count / total_results) * 100

    total_duration = sum(r["duration_ms"] for r in results)
    avg_duration = total_duration / total_results

    return (
        passed_count,
        failed_count,
        pass_rate,
        avg_duration,
    )


def generate_report(*results):
    """Generate a formatted test report string.

    Calls analyze_results() internally and formats the output.

    Returns: formatted multi-line string
    """
    passed, failed, pass_rate, avg_duration = analyze_results(*results)

    report = (
        "Test Report\n"
        "-----------\n"
        f"Total Tests: {passed + failed}\n"
        f"Passed: {passed}\n"
        f"Failed: {failed}\n"
        f"Pass Rate: {pass_rate:.1f}%\n"
        f"Average Duration: {avg_duration:.2f}ms"
    )

    return report


results = [
    create_test_result("test_login", "pass", 1200),
    create_test_result("test_search", "pass", 850),
    create_test_result("test_checkout", "fail", 2300, "Timeout"),
    create_test_result("test_profile", "pass", 450),
]

passed, failed, rate, avg = analyze_results(*results)
assert passed == 3
assert failed == 1
assert rate == 75.0
