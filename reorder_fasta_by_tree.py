import os
from Bio import Phylo

def get_taxa_order_from_tree(tree_file):
    """Extract taxa order from a rooted phylogenetic tree in Newick format, ignoring branch lengths."""
    tree = Phylo.read(tree_file, "newick")
    taxa = tree.get_terminals()
    return [taxon.name for taxon in taxa]

def reorder_fasta_sequences(folder_path, tree_file):
    # Get the priority list from the tree
    priority_list = get_taxa_order_from_tree(tree_file)
    
    # Process each .fas file in the folder
    for filename in os.listdir(folder_path):
        if filename.endswith('.fas'):
            file_path = os.path.join(folder_path, filename)
            
            # Read the file contents
            with open(file_path, 'r') as file:
                lines = file.readlines()
            
            # Dictionary to store sequences
            sequences = {}
            current_header = None
            
            # Parse the .fas file
            for line in lines:
                if line.startswith('>'):
                    current_header = line.strip()
                    sequences[current_header] = ''
                else:
                    sequences[current_header] += line.strip()
            
            # Reorder the sequences based on priority
            reordered_sequences = []
            for name in priority_list:
                for header in list(sequences.keys()):
                    if name in header:
                        reordered_sequences.append((header, sequences.pop(header)))
            
            # Add the remaining sequences that were not in the priority list
            reordered_sequences.extend(sequences.items())
            
            # Write the reordered sequences back to the file
            with open(file_path, 'w') as file:
                for header, sequence in reordered_sequences:
                    file.write(f"{header}\n")
                    file.write(f"{sequence}\n")
    
    print("Reordering complete.")

# Define the folder path and the tree file path
folder_path = os.getcwd()

# Find the .nwk file in the same folder
tree_file = None
for filename in os.listdir(folder_path):
    if filename.endswith('.nwk'):
        tree_file = os.path.join(folder_path, filename)
        break

if tree_file is None:
    print("No .nwk file found in the folder.")
else:
    # Run the reordering process
    reorder_fasta_sequences(folder_path, tree_file)
