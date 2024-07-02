import os
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord

# Directory containing sequence files
folder_path = r"C:\Users\fzs124\Desktop\Amblyo_AHE\2nd_paper\143taxa_Final_taxon_sampl\50p_loci\cleaning_in_prog\good_need_stopco"

# WARNING: Ensure you have backups of your original files before running this script.

# Iterate through each file in the directory
for filename in os.listdir(folder_path):
    if filename.endswith(".fas"):  # Assuming all files are in FASTA format
        file_path = os.path.join(folder_path, filename)
        
        try:
            # Load sequences
            sequences = list(SeqIO.parse(file_path, "fasta"))
            
            # List to hold modified records
            modified_records = []

            # Iterate through sequences and replace stop codons
            for record in sequences:
                seq = str(record.seq)
                
                # Find stop codons and replace them with NNN
                new_seq = ''.join(
                    "NNN" if seq[i:i+3] in ["TAG", "TGA", "TAA"] else seq[i:i+3]
                    for i in range(0, len(seq), 3)
                )
                
                # Create a new SeqRecord with modified sequence
                modified_record = SeqRecord(Seq(new_seq), id=record.id, description=record.description)
                modified_records.append(modified_record)
            
            # Define the output file path with 'mod_' prefix
            output_file_path = os.path.join(folder_path, f"mod_{filename}")
            with open(output_file_path, "w") as output_handle:
                SeqIO.write(modified_records, output_handle, "fasta")
            
            print(f"Modified alignment written to {output_file_path}")
        
        except Exception as e:
            print(f"Error processing {filename}: {e}")

# Reminder to users to check their backups
print("Reminder: Ensure you have backups of your original files.")
