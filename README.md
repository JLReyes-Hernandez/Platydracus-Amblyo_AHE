Description of python scripts.

'filter_fasta.py': Removes empty sequences from .fas files.

'replace!byN.py': Replace the ! symbol by N in .fas files.

'reorder_fasta_by_tree.py': Sorts the sequences in phylogenetic order using a tree as a guide.

 'reorder_fasta_bymybest.py': Places at the beginning of all .fas files the specified taxa that may be the outgroup and pairs of species that have good sequence quality and are known to be related.

'stop_codons_masking_folder_path.py': Replaces the stop codons of the standard code with NNN.

 'check_alignment_lengths.py': Check that the alignments are divisible by 3.

'minimum_completeness.py': Places the alignments with a specific number of sequences in a new folder.

'gene_count_total_for_each_taxon.py': This script generates a taxon-gene presence matrix from an alignment and partition file. It extracts gene positions, checks for gene presence per taxon (ignoring ? and X), and outputs a CSV where each row represents a taxon and columns indicate gene presence (1 or 0). A "Total" column is added to count the number of genes present per taxon.
