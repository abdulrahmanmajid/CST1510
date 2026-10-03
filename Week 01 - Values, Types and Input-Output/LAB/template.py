"""
RECORD CHECK  -  my version
===========================

Name  : Abdul Rahman Majid
Lane  : AI / Data Science
Date  : 3/10/2026

Run it:   python template.py
"""

# ==================================================================== INPUT
survey_name = input("Enter the name of your survey: ")
number_of_surveys_collected = float(input("Enter the number of surveys collected: "))
number_of_surveys_expected = float(input("Enter the number of surveys expected: "))


# ================================================================== PROCESS
difference = number_of_surveys_collected - number_of_surveys_expected
percent_collected = number_of_surveys_collected / number_of_surveys_expected * 100

# this extra line shows how much percent of the surveys are missing from the expected total
percent_missing = 100 - percent_collected


# =================================================================== OUTPUT
print()
print("=" * 34)
print(f"  RECORD CHECK  -  {survey_name}")
print("=" * 34)

print(f"  {'Collected':<12}{number_of_surveys_collected:>14.2f}")
print(f"  {'Expected':<12}{number_of_surveys_expected:>14.2f}")
print(f"  {'Difference':<12}{difference:>+14.2f}")
print(f"  {'Collected %':<12}{percent_collected:>14.2f} %")
print(f"  {'Missing %':<12}{percent_missing:>14.2f} %")

print("=" * 34)


# ==========================================================================
# Before you finish:
#
#    [ ] Run it three times with different numbers
#    [ ] Run it with a total of 0 and write the error in your journal
#    [ ] Check every variable name says what it holds
#    [ ] Show it to the person next to you
