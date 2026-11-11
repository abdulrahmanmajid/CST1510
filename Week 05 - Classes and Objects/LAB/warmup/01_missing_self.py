# BROKEN ON PURPOSE.
# Run it, read the last line, then fix it.

class Record:
    def status(self, percent):    # it was missing self, python passes the object in by itself so it needs self first
        return percent

r = Record()
print(r.status(95))
