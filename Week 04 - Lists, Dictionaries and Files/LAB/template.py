"""
RECORD CHECK  -  my version
===========================

Name  : Abdul Rahman Majid
Lane  : AI
Date  : 11/11/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# =================================================================== FUNCTIONS
# 1. Bring back check_record(value, limit) and print_report(...) from Week 3
#    (copy them, or rewrite them - either is fine). check_record returns
#    difference, percent and status. print_report does all of the printing,
#    nothing outside it should contain a print() of its own. Give each a
#    one-line docstring.

def status_of(percent):
    """Return the status based on the percent value."""
    if percent >= 100:
        return "OVER LIMIT"
    elif percent >= 90:
        return "WARNING"
    else:
        return "OK"


def check_record(value, limit):
    """Return the difference, percent and status based on value and limit."""
    difference = limit - value
    percent = value / limit * 100
    status = status_of(percent)
    return difference, percent, status


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


def load_records(path):
    """Read label,value,limit lines from a file and return a list of dicts."""
    records = []
    with open(path) as f:
        for line in f:
            label, value, limit = line.strip().split(",")
            record = {"label": label, "value": float(value), "limit": float(limit)}
            records.append(record)
    return records


# ====================================================================== STORE
# 2. Get your records into a list of dicts, each shaped like:
#        {"label": ..., "value": ..., "limit": ...}
#
#    Threshold : write the list directly in the code - at least 3 records.
#    Typical   : instead, write a function load_records(path) that reads
#                label,value,limit lines from a file and returns the list.
#                Make your own data file, one record per line.
#    Excellent : also write the results out to a new file (one line per
#                record: label, status), as well as printing them.

try:
    records = load_records("datasets.txt")
except FileNotFoundError:
    print("datasets.txt not found - starting with an empty list")
    records = []


# =============================================================== PROCESS + OUTPUT
# 3. Loop over records. For each one, call check_record and print_report.
#
#    Excellent : also keep a running count of how many were OVER LIMIT, and
#                print that once, after the loop ends.

# keeps count of how many records came back OVER LIMIT
over_limit_count = 0

with open("report.txt", "w") as f:
    for record in records:
        difference, percent, status = check_record(record["value"], record["limit"])
        print_report(record["label"], record["value"], record["limit"], difference, percent, status)
        f.write(f"{record['label']},{status}\n")

        if status == "OVER LIMIT":
            over_limit_count += 1

# runs once, after the loop has ended
print(f"Records over limit: {over_limit_count}")


# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it and check every record's numbers are correct by hand
#    [ ] If you are loading from a file, check what happens when the file
#        does not exist - write the error down
#    [ ] Check every function still does one job
