# BROKEN ON PURPOSE.
# Run it, read the last line, then fix it.

def check(value, limit):
    status = "OVER LIMIT" if value > limit else "OK"
    return status # we werent returning status

status = check(87, 100) # we werent defining what status is 

print(status)
