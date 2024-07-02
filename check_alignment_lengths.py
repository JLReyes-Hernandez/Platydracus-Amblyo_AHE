import os
from Bio import SeqIO

# Get the directory of the script itself
folder_path = os.path.dirname(os.path.abspath(__file__))
report_file_path = os.path.join(folder_path, "alignment_length_report.txt")

# Function to check if sequence lengths are divisible by 3
def check_sequence_lengths(filename):
    non_divisible_by_3 = []
    with open(os.path.join(folder_path, filename), "r") as handle:
        for record in SeqIO.parse(handle, "fasta"):
            if len(record.seq) % 3 != 0:
                non_divisible_by_3.append(record.id)
    return non_divisible_by_3

# List to hold files with sequences not divisible by 3
files_with_issues = []

# Iterate through each file in the directory
for filename in os.listdir(folder_path):
    if filename.endswith(".fas"):  # Assuming all files are in FASTA format
        non_divisible_by_3 = check_sequence_lengths(filename)
        if non_divisible_by_3:
            files_with_issues.append((filename, non_divisible_by_3))

# Write report
with open(report_file_path, "w") as report_file:
    if files_with_issues:
        for filename, ids in files_with_issues:
            report_file.write(f"{filename} has sequences not divisible by 3:\n")
            for seq_id in ids:
                report_file.write(f"  - {seq_id}\n")
        print(f"Report written to {report_file_path}")
    else:
        report_file.write("All alignments have sequences with lengths divisible by 3.\n")
        print("All alignments have sequences with lengths divisible by 3.")

print("Script completed.")
