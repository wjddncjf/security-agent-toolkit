count = 0

with open("raw_logs.txt", "r", encoding="utf-8") as f:
    for line in f:
        if "WARN" in line:
            count = count + 1

print("WARN", count, "줄")