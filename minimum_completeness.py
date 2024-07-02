import os
import shutil

def count_sequences(file_path):
    """Count the number of sequences in a fasta file."""
    with open(file_path, 'r') as file:
        return sum(1 for line in file if line.startswith('>'))

def filter_fasta_files(min_sequences=107):
    """Filter fasta files in the current directory based on the number of sequences."""
    current_dir = os.path.dirname(os.path.abspath(__file__))
    output_dir = os.path.join(current_dir, 'minimum_completeness')
    
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    for file_name in os.listdir(current_dir):
        if file_name.endswith('.fas'):
            file_path = os.path.join(current_dir, file_name)
            num_sequences = count_sequences(file_path)
            if num_sequences >= min_sequences:
                shutil.copy(file_path, output_dir)
                print(f"Copied {file_name} with {num_sequences} sequences to {output_dir}")

if __name__ == "__main__":
    filter_fasta_files()
