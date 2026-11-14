import os

sample_log_data = """2026-11-12 10:00:01 INFO System started successfully.
2026-11-12 10:05:23 WARNING High memory usage detected (82%).
2026-11-12 10:12:45 INFO User 'admin' logged in.
2026-11-12 10:15:10 ERROR Database connection timed out.
2026-11-12 10:16:02 WARNING Retrying database connection...
2026-11-12 10:16:05 INFO Database reconnected.
2026-11-12 10:20:30 ERROR Failed to load user profile module.
"""

filename = "app.log"
with open(filename, "w") as file:
    file.write(sample_log_data)


def analyze_log_file(filepath):
    log_counts = {"INFO": 0, "WARNING": 0, "ERROR": 0}
    total_lines = 0

    try:
        if os.path.getsize(filepath) == 0:
            print("Warning: The log file is completely empty.")
            return

        with open(filepath, "r") as file:
            for line in file:
                total_lines += 1
                upper_line = line.upper()

                for keyword in log_counts:
                    if keyword in upper_line:
                        log_counts[keyword] += 1

        print("--- Log File Summary ---")
        for level, count in log_counts.items():
            print(f"{level}: {count}")

        categorized_total = sum(log_counts.values())
        print(f"\nTotal lines read: {total_lines}")
        print(f"Categorized entries: {categorized_total}")
        print(f"Verification passed: {total_lines == categorized_total}")

        if log_counts["ERROR"] > 0:
            print(
                f"\nAlert: {log_counts['ERROR']} critical error(s) found. "
                "Immediate attention needed."
            )
        else:
            print("\nSystem Status: Healthy. No critical errors found.")

    except FileNotFoundError:
        print(f"Error: The file '{filepath}' was not found. Please check the file path.")


analyze_log_file(filename)
