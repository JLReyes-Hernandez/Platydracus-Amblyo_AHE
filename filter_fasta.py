import os
from Bio import SeqIO

def filter_sequences(input_folder):
    # Create a new folder for output files
    output_folder = os.path.join(os.getcwd(), 'filtered_sequences')
    os.makedirs(output_folder, exist_ok=True)
    
    # Loop through all files in the current directory
    for filename in os.listdir(input_folder):
        if filename.endswith(".fas"):
            input_file = os.path.join(input_folder, filename)
            output_file = os.path.join(output_folder, f'filt_{filename}')
            with open(output_file, 'w') as out_f:
                for record in SeqIO.parse(input_file, 'fasta'):
                    # Check if the sequence contains only missing data or gaps
                    if set(str(record.seq)) - {'?', '-'}:
                        SeqIO.write(record, out_f, 'fasta')

if __name__ == "__main__":
    input_folder = os.getcwd()  # Use the current directory as input folder

    filter_sequences(input_folder)
    print("Filtered sequences have been written to 'filtered_sequences' folder")
