"""
RECORD CHECK  -  my version
===========================

Name  : Abdul Rahman Majid
Lane  : AI
Date  : 9/11/2026

Run it:   python template.py

Type "quit" as the dataset name to stop.
"""

# ============================================================== FUNCTIONS
def status_of(percent):
    """Return the status based on the percent value."""
    if percent >= 100:
        return "OVER LIMIT"
    elif percent >= 90:
        return "WARNING"
    else:
        return "OK"
    
def check(value, limit):
    """Return the difference and percent based on value and limit."""
    difference = limit - value
    percent = value / limit * 100
    return difference, percent



def print_report(label, value, limit, difference, percent, status):
    """Print the report based on the provided parameters."""
    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {label}")
    print("=" * 34)
    print(f"  {'Loaded':<12}{value:>14.2f}")
    print(f"  {'Expected':<12}{limit:>14.2f}")
    print(f"  {'Missing':<12}{difference:>14.2f}")
    print(f"  {'Percent':<12}{percent:>14.2f} %")
    print(f"  {'Status':<12}{status:>14}")
    print("=" * 34)
    print()


# keeps count of how many records came back OVER LIMIT
over_limit_count = 0

while True:

    # ================================================================ INPUT
    dataset_name = input("Dataset name (or 'quit'): ")
    if dataset_name == "quit":
        break

    rows_loaded = float(input("Rows loaded: "))
    rows_expected = float(input("Rows expected: "))

    # ============================================================== PROCESS
    difference, percent = check(rows_loaded, rows_expected)
    status = status_of(percent)

    if status == "OVER LIMIT":
        over_limit_count += 1

    # =============================================================== OUTPUT
    print_report(dataset_name, rows_loaded, rows_expected, difference, percent, status)

# runs once, after the loop has ended
print(f"Records over limit: {over_limit_count}")


# ==========================================================================
# Before you finish:
#
#    [ ] Run it three times with different numbers
#    [ ] Run it with a total of 0 and note the error (do not fix it yet)
#    [ ] Check every variable name says what it holds
