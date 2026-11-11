import pandas as pd 

servers = pd.read_csv("servers.csv")
print(servers)
servers["percent"] = (servers["used"] / servers["total"]) * 100

def classify(percent):
    if percent >= 100:
        return "Over Limit"
    elif percent >= 90:
        return "Warning"
    else:
        return "OK"