import os
import csv
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--output-dir", default="/data")
args = parser.parse_args()

output_dir = args.output_dir
os.makedirs(output_dir, exist_ok=True)

text_file = os.path.join(output_dir, "output.txt")
with open(text_file, "w") as f:
    f.write("Batch process executed successfully.\n")

csv_file = os.path.join(output_dir, "output.csv")
with open(csv_file, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["id","name"])
    writer.writerow([1,"Alice"])
    writer.writerow([2,"Bob"])

print(f"Text output: {text_file}")
print(f"CSV output: {csv_file}")
print("Batch process completed.")