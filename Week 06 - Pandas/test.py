import pandas as pd
l = [10, 20, 30, 40]
S = pd.Series(l)
print(S)

dc = {"Name": ["Alice", "Bob", "Charlie", "David"], "Age": [25, 30, 35, 40], "Marks": [85, 90, 95, 80]}
df = pd.DataFrame(dc)
print(df)


s = pd.DataFrame({"Server Name": ["Server 1", "Server 2", "Server 3", "Server 4"], "used": [80, 90, 100, 110], "total": [100, 100, 100, 100]})

s["Server Name"] = (s["used"] / s["total"]) * 100

over_limit = s[s["Server Name"] >= 100]
print(over_limit)
print(s)