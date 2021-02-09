# combinedcodonoptimisation

main.py contains function to generate sequence from a given input protein sequence, and list of multiple organisms. Optimisation still a work in progress.

rarecodons.py contains function "get_rare_codons()" which returns the rare codons for a given organism obtained from the codon tables which we can generate. This function is used in main.

markovtable.py contains a function "get_codon_pair_freqs()" which return the frequency of the every codon pair used
in the ribosomal proteins of a given organism.

indexes.py contains a function "get_index()", which returns the the CAI relative adaptiveness index for each organism, which is being used to
generate a score for the sequences generated. Uses Benjamin Lee's CAI module.

codon_combi_app.py use streamlit to run the program as a web app. (Work in progress)
