import os

import pandas as pd

# 1. Load the CSV
df = pd.read_csv("test_data.csv")

# Optional: normalize column names if needed
# Expected columns: test_name, module, status/pass, duration_ms

# 2. Print basic info
print("══════════════════════════════════════")
print("  Test Results Analysis")
print("══════════════════════════════════════\n")

print(f"  Total Tests:    {len(df)}")
print("\nColumn names and dtypes:")
print(df.dtypes)

print("\nFirst 5 rows:")
print(df.head())

# Detect pass/fail column
if "passed" in df.columns:
    pass_col = "passed"
    passed = df[pass_col].astype(bool)
elif "status" in df.columns:
    pass_col = "status"
    passed = df[pass_col].str.lower().eq("pass")
else:
    raise ValueError("CSV must contain either a 'passed' column or a 'status' column.")

# 3. Aggregate metrics
total_tests = len(df)
pass_rate = passed.mean() * 100
avg_duration_ms = df["duration_ms"].mean()
avg_duration_sec = avg_duration_ms / 1000

slowest = df.loc[df["duration_ms"].idxmax()]
fastest = df.loc[df["duration_ms"].idxmin()]

print(f"\n  Total Tests:    {total_tests}")
print(f"  Pass Rate:      {pass_rate:.1f}%")
print(f"  Avg Duration:   {avg_duration_ms:,.0f}ms ({avg_duration_sec:.2f}s)")
print(f"  Slowest:        {slowest['test_name']} ({slowest['duration_ms']:,.0f}ms)")
print(f"  Fastest:        {fastest['test_name']} ({fastest['duration_ms']:,.0f}ms)")

# 4. Group by module
df["_passed_bool"] = passed

module_summary = (
    df.groupby("module")
    .agg(
        Tests=("test_name", "count"),
        Pass_Rate=("_passed_bool", lambda x: x.mean() * 100),
        Avg_Duration=("duration_ms", "mean"),
    )
    .reset_index()
)

print("\n  ── By Module ──")
print(f"  {'Module':<12} {'Tests':>5} {'Pass Rate':>10} {'Avg Duration':>14}")

for _, row in module_summary.iterrows():
    print(
        f"  {row['module']:<12} "
        f"{int(row['Tests']):>5} "
        f"{row['Pass_Rate']:>9.1f}% "
        f"{row['Avg_Duration']:>11,.0f}ms"
    )

# 5. Filter and display
failed_tests = df[~df["_passed_bool"]][["test_name", "module", "duration_ms"]]
slow_tests = df[df["duration_ms"] > 1500][["test_name", "module", "duration_ms"]]
auth_tests = df[df["module"] == "auth"]

print("\n  ── Failed Tests ──")
for _, row in failed_tests.iterrows():
    print(f"  {row['test_name']:<22} {row['module']:<9} {row['duration_ms']:>6,.0f}ms")

print("\n  ── Tests Slower Than 1500ms ──")
print(slow_tests.to_string(index=False))

print('\n  ── Tests in "auth" Module ──')
print(auth_tests.to_string(index=False))

# 6. Add computed column
df["duration_sec"] = df["duration_ms"] / 1000

# 7. Sort and export
df_sorted = df.drop(columns=["_passed_bool"]).sort_values(
    by="duration_ms", ascending=False
)

os.makedirs("output", exist_ok=True)
df_sorted.to_csv("output/results_sorted.csv", index=False)

print("\nSaved sorted results to output/results_sorted.csv")
