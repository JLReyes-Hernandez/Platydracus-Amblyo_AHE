import csv
import re

# Function to create taxon partition matrix
def create_taxon_partition_matrix(alignment_file, partition_file, output_file):
    # Read partition file to get gene positions
    gene_partitions = {}
    with open(partition_file, 'r') as part_file:
        for line in part_file:
            line = line.strip()
            if line.startswith("charset"):
                match = re.match(r'charset\s+(\S+)\s+=\s+(\d+)-(\d+);', line)
                if match:
                    gene = match.group(1)
                    start = int(match.group(2))
                    end = int(match.group(3))
                    gene_partitions[gene] = (start, end)
                else:
                    print(f"Error parsing positions in line: {line}")

    # Initialize matrix to store taxon-partition presence
    taxon_partition_matrix = {}

    # Read alignment file
    with open(alignment_file, 'r') as align_file:
        next(align_file)  # Skip the first line
        for line in align_file:
            line = line.strip()
            if line:  # Skip empty lines
                taxon, sequence = line.split()
                taxon_partition_matrix[taxon] = {}
                for gene, (start, end) in gene_partitions.items():
                    if any(base not in ['?', 'X'] for base in sequence[start-1:end]):
                        taxon_partition_matrix[taxon][gene] = 1
                    else:
                        taxon_partition_matrix[taxon][gene] = 0

    # Write results to CSV file
    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)

        # Add "Total" column right after "Taxon"
        header = ['Taxon', 'Total'] + list(gene_partitions.keys())
        writer.writerow(header)

        # Write taxon data with total count per species
        for taxon, partition_presence in taxon_partition_matrix.items():
            gene_counts = [1 if presence else 0 for presence in partition_presence.values()]
            total_genes = sum(gene_counts)  # Sum presence across all genes
            writer.writerow([taxon, total_genes] + gene_counts)

    print("Matrix written to", output_file)

# Call function with your alignment and partition files
alignment_file = '50P_NT_MC.phy'
partition_file = '50P_NT_MC_partitions.nex'
output_file = '50P_NT_MC_taxon_loci_matrix.csv'
create_taxon_partition_matrix(alignment_file, partition_file, output_file)
