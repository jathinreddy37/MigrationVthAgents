import csv
import os

def write_csv(filepath, headers, rows):
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(rows)

def generate_source_csv(output_dir="data"):
    headers = [
        "cust_id",
        "cust_name",
        "email",
        "age",
        "signup_date",
        "country"
    ]

    rows = [
        [1, "Aarav Sharma", "aarav@example.com", 28, "2024-01-10", "India"],
        [2, "Meera Patel", "meera@example.com", 31, "2024-02-15", "India"],
        [3, "John Doe", "john@example.com", 35, "2024-03-20", "USA"],
        [4, "Sara Khan", "sara@example.com", 26, "2024-04-05", "UAE"]
    ]

    filepath = os.path.join(output_dir, "source_customers.csv")
    write_csv(filepath, headers, rows)
    print(f"Created: {filepath}")

if __name__ == "__main__":
    generate_source_csv()