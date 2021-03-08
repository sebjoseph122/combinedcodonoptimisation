from Bio import SeqIO
from CAI import CAI, RSCU, relative_adaptiveness

sequences = []

for seq_record in SeqIO.parse("RhodosporidiumToruloidesRPGenes.fasta", "fasta"):        #change file name       #Change File Name depending on organism
    dnaSeq = str(seq_record.seq.lower())
    if len(dnaSeq)%3 !=0:
        print(seq_record.id)
    else:
        sequences.append(dnaSeq)


weights = relative_adaptiveness(sequences=sequences)
print(weights)



for seq_record in SeqIO.parse("RhodosporidiumToruloidesRPGenes.fasta", "fasta"):     #changw file name depending on organism
    dnaSeq = str(seq_record.seq.lower())
    if len(dnaSeq)%3 !=0:
        print(seq_record.id)
    else:
       print(CAI(dnaSeq,weights=weights))


