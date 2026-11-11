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

# ====================================================================== CLASS
# 1. Define a class called Record.
#
#    Threshold : __init__(self, label, value, limit) storing all three as
#                attributes. No methods yet.
#    Typical   : add a method status(self) that returns "OVER LIMIT" (100%+),
#                "WARNING" (90%+) or "OK", worked out from self.value and
#                self.limit. Give it a one-line docstring.
#    Excellent : also add over_limit_count as a class-level running total -
#                see the note below.

class Record:
    # shared by every Record - one running total for the whole class
    over_limit_count = 0

    def __init__(self, label, value, limit):
        """Store the dataset name, rows loaded and rows expected."""
        self.label = label
        self.value = value
        self.limit = limit

    def difference(self):
        """Return how many rows are missing (negative if there are extra)."""
        return self.limit - self.value

    def percent(self):
        """Return rows loaded as a percentage of rows expected."""
        return (self.value / self.limit) * 100

    def status(self):
        """Return OVER LIMIT, WARNING or OK based on the percent."""
        if self.percent() >= 100:
            return "OVER LIMIT"
        elif self.percent() >= 90:
            return "WARNING"
        else:
            return "OK"


# ==================================================================== RECORDS
# 2. Create your records.
#
#    Threshold : create at least 2 Record instances directly in the code.
#    Typical   : same, but now print each one's .status() as well.
#    Excellent : instead, write load_records(path) that reads label,value,limit
#                lines from a file and returns a list of Record objects. Make
#                your own data file, one record per line.

def load_records(path):
    """Read label,value,limit lines from a file and return a list of Records."""
    records = []
    with open(path) as f:
        for line in f:
            label, value, limit = line.strip().split(",")
            records.append(Record(label, float(value), float(limit)))
    return records


records = load_records("datasets.txt")


# ==================================================================== OUTPUT
# 3. Print a report for each record.
#
#    Threshold : label, value, limit, inside a border.
#    Typical   : add the result of .status().
#    Excellent : also keep a running count of how many came back OVER LIMIT
#                across every record, and print that once, after the loop.
#                (Simplest: a plain variable outside the loop, same pattern
#                as Week 4. If you want it to live ON the object instead,
#                that is a stretch worth trying - but a variable is enough.)

for record in records:
    status = record.status()   # called once, then reused below

    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {record.label}")
    print("=" * 34)

    print(f"  {'Loaded':<12}{record.value:>14.2f}")
    print(f"  {'Expected':<12}{record.limit:>14.2f}")
    print(f"  {'Missing':<12}{record.difference():>14.2f}")
    print(f"  {'Percent':<12}{record.percent():>14.2f} %")
    print(f"  {'Status':<12}{status:>14}")

    if status == "OVER LIMIT":
        Record.over_limit_count += 1

    print("=" * 34)

# runs once, after the loop has ended
print()
print(f"Records over limit: {Record.over_limit_count}")


# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it and check every record's numbers by hand
#    [ ] Check every method only reads/changes its OWN object (self) -
#        nothing reaches outside itself
#    [ ] Check every method and __init__ has a one-line docstring
