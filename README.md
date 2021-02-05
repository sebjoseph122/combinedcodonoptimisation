# combinedcodonoptimisation

main.py contains code to generate sequence from a given input protein sequences for multiple organisms.

rarecodons.py contains a function "get_rare_codons()" which returns the rare codons for a given organism obtained from the codon tables which we can generate. This function is used in main.

markovtable.py contains a function "get_codon_pair_freqs()" which return the freuquency of the every codon pair used
in the ribosomal proteins of a given organism.

indexes.py contains a function "get_index()", which returns the the index for each organism, which is being used to
generate a score for the sequences generate. This is generated using biopythons CAI.
