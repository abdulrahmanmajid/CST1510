"""
RECORD CHECK  -  my version
===========================

Name  : Abdul Rahman Majid
Lane  : AI
Date  : 5/10/2026

Run it:   python template.py

Type "quit" as the dataset name to stop.
"""

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
    # rows still missing from the expected total
    difference = rows_expected - rows_loaded
    percent = rows_loaded / rows_expected * 100

    # checked from most specific to least, the first True one wins
    if percent >= 100:
        status = "OVER LIMIT"
        over_limit_count += 1
    elif percent >= 90:
        status = "WARNING"
    else:
        status = "OK"

    # =============================================================== OUTPUT
    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {dataset_name}")
    print("=" * 34)
    print(f"  {'Loaded':<12}{rows_loaded:>14.2f}")
    print(f"  {'Expected':<12}{rows_expected:>14.2f}")
    print(f"  {'Missing':<12}{difference:>14.2f}")
    print(f"  {'Percent':<12}{percent:>14.2f} %")
    print(f"  {'Status':<12}{status:>14}")
    print("=" * 34)
    print()

# runs once, after the loop has ended
print(f"Records over limit: {over_limit_count}")


# ==========================================================================
# Before you finish:
#
#    [ ] Run it three times with different numbers
#    [ ] Run it with a total of 0 and note the error (do not fix it yet)
#    [ ] Check every variable name says what it holds
