# log_analyzer_simple.py
# Simple Log File Analyzer – detect errors & warnings and generate a report

import re
import os

# -------- CONFIGURATION --------
log_file = "sample.log"           # path to your log file
report_file = "log_report.txt"    # output report file

# -------- REGEX PATTERNS --------
error_pattern = re.compile(r"(ERROR|Error|error)")
warning_pattern = re.compile(r"(WARNING|Warning|warning)")

# -------- VARIABLES TO STORE RESULTS --------
errors = []
warnings = []
total_lines = 0

# -------- ANALYZE THE LOG FILE --------
with open(log_file, "r", errors="ignore") as file:
    for line in file:
        total_lines += 1
        if error_pattern.search(line):
            errors.append(line.strip())
        elif warning_pattern.search(line):
            warnings.append(line.strip())

# -------- GENERATE SIMPLE REPORT --------
with open(report_file, "w") as report:
    report.write("===== LOG FILE ANALYSIS REPORT =====\n")
    report.write(f"Total Lines Scanned: {total_lines}\n")
    report.write(f"Total Errors Found: {len(errors)}\n")
    report.write(f"Total Warnings Found: {len(warnings)}\n\n")

    report.write("---- ERRORS ----\n")
    for e in errors:
        report.write(e + "\n")

    report.write("\n---- WARNINGS ----\n")
    for w in warnings:
        report.write(w + "\n")

print("✅ Analysis complete! Report generated:", report_file)

