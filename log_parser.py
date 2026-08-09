import re
from collections import Counter

LOG_FILE = "sample_logs.txt"
SUSPICIOUS_FILE = "suspicious_logs.txt"
REPORT_FILE = "security_report.txt"

FAILED_LOGIN_KEYWORDS = [
    "failed login",
    "authentication failed",
    "invalid login",
    "unauthorized"
]

BRUTE_FORCE_THRESHOLD = 3


def read_logs(filename):
    """Read log entries from a file."""
    try:
        with open(filename, "r") as file:
            return file.readlines()
    except FileNotFoundError:
        print(f"Error: {filename} not found.")
        return []


def extract_ip(log):
    """Extract an IPv4 address from a log entry."""
    match = re.search(r"\b(?:\d{1,3}\.){3}\d{1,3}\b", log)

    if match:
        return match.group()

    return None


def find_suspicious_logs(logs):
    """Find suspicious security events."""
    suspicious = []

    for log in logs:
        lower_log = log.lower()

        if any(keyword in lower_log for keyword in FAILED_LOGIN_KEYWORDS):
            suspicious.append(log.strip())

    return suspicious


def count_failed_attempts(suspicious_logs):
    """Count failed login attempts by IP address."""
    ip_counter = Counter()

    for log in suspicious_logs:
        ip = extract_ip(log)

        if ip:
            ip_counter[ip] += 1

    return ip_counter


def save_suspicious_logs(logs):
    """Save suspicious logs to a separate file."""
    with open(SUSPICIOUS_FILE, "w") as file:
        for log in logs:
            file.write(log + "\n")


def generate_report(suspicious_logs, ip_counter):
    """Generate a security analysis report."""

    with open(REPORT_FILE, "w") as file:

        file.write("SECURITY LOG ANALYSIS REPORT\n")
        file.write("=" * 40 + "\n\n")

        file.write(f"Total suspicious events: {len(suspicious_logs)}\n\n")

        file.write("Failed Login Attempts by IP:\n")
        file.write("-" * 40 + "\n")

        for ip, count in ip_counter.items():
            file.write(f"{ip}: {count} failed attempts\n")

        file.write("\nPotential Brute-Force Sources:\n")
        file.write("-" * 40 + "\n")

        brute_force_found = False

        for ip, count in ip_counter.items():
            if count >= BRUTE_FORCE_THRESHOLD:
                file.write(
                    f"[ALERT] {ip} - {count} failed login attempts\n"
                )
                brute_force_found = True

        if not brute_force_found:
            file.write("No potential brute-force sources detected.\n")


def main():

    print("=" * 50)
    print("      JAGSPIRE SECURITY LOG ANALYZER")
    print("=" * 50)

    logs = read_logs(LOG_FILE)

    if not logs:
        return

    suspicious_logs = find_suspicious_logs(logs)

    ip_counter = count_failed_attempts(suspicious_logs)

    save_suspicious_logs(suspicious_logs)

    generate_report(suspicious_logs, ip_counter)

    print(f"\nTotal log entries: {len(logs)}")
    print(f"Suspicious entries: {len(suspicious_logs)}")

    print("\nFailed login attempts:")

    for ip, count in ip_counter.items():
        print(f"  {ip}: {count}")

    print("\nPotential brute-force sources:")

    found = False

    for ip, count in ip_counter.items():
        if count >= BRUTE_FORCE_THRESHOLD:
            print(f"  [ALERT] {ip} -> {count} failed attempts")
            found = True

    if not found:
        print("  None detected.")

    print("\nFiles generated:")
    print(f"  {SUSPICIOUS_FILE}")
    print(f"  {REPORT_FILE}")

    print("\nAnalysis completed successfully.")


if __name__ == "__main__":
    main()
