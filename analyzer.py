import pandas as pd
import matplotlib.pyplot as plt

error_count = 0
warning_count = 0
info_count = 0

with open("sample.log", "r") as file:
    for line in file:
        line = line.lower()

        if "error" in line or "failed" in line or "critical" in line:
            error_count += 1

        elif "warning" in line or "warn" in line:
            warning_count += 1

        else:
            info_count += 1

print("ERRORS:", error_count)
print("WARNINGS:", warning_count)
print("INFO:", info_count)

# Save CSV
data = {
    "Type": ["ERRORS", "WARNINGS", "INFO"],
    "Count": [error_count, warning_count, info_count]
}

df = pd.DataFrame(data)
df.to_csv("report.csv", index=False)

print("Report generated successfully")

# ===== GRAPH =====
plt.figure(figsize=(6,4))
plt.bar(data["Type"], data["Count"])
plt.title("Log Analysis Report")
plt.xlabel("Log Type")
plt.ylabel("Count")
plt.savefig("log_graph.png")
print("Graph saved as log_graph.png")
