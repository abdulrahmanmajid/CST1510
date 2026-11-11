# BROKEN ON PURPOSE.
# Run it, read the last line, then fix it.

record = {"label": "R-001", "value": 87.0, "limit": 100.0}

print(record["label"]) # the fix was to switch from "status" to "label", since the dictionary does not have a key called "status".
