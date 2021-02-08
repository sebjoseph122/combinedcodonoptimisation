from RareCodons import get_rare_codons
from markovtable import get_codon_pair_freqs
from CAI import CAI
from indexesforCAI import get_index
import random

##Function to produce DNAseq##

def seq_construction(codon_pair_possibilities, nucleotide_seq):
    codon_pairs = []
    codon_pair_weights = []
    for possibility in codon_pair_possibilities:
        codon_pairs.append(possibility[0])
        codon_pair_weights.append(possibility[2])
    option = random.choices(codon_pairs, weights=codon_pair_weights,k=1)   #weights=codon_pair_weights
    if nucleotide_seq == "":
        temp = str(option[0])
        return temp
    else:
        temp = str(option[0])
        return temp[-3:]


##Main##

#These can be changed#
user_organisms = ["saccharomyces_cerevisiae", "escherichia_coli"]

#Get rare codons for chosen organisms and put in list, removing duplicates#
rarecodons = [] 

for organism in user_organisms:
    rarecodons += get_rare_codons(organism)

rarecodons = list(set(rarecodons))

#Get the codon pair frequencies for chosen organisms and add#
for i in range(len(user_organisms)):
    if (i==0):
        codonCombinations = get_codon_pair_freqs(user_organisms[i])
    else:
        temp = get_codon_pair_freqs(user_organisms[i])
        for j in range(len(temp)):
            codonCombinations[j][2] += temp[j][2]

#Cleans up the list of codon pairs, removing pairs with rare codons and setting 0 to 1#
finalCodonCombinations = []
for combination in codonCombinations:
    if (combination[2]==0):
        combination[2]=1
    else:
        pass
    for i in range(len(rarecodons)):
        if (i+1<len(rarecodons)):
            if ((combination[0][0:3]==rarecodons[i]) or (combination[0][-3:]==rarecodons[i])):
                break
            else:
                pass
        elif (i+1==len(rarecodons)):
            if ((combination[0][0:3]==rarecodons[i]) or (combination[0][-3:]==rarecodons[i])):
                break
            else:
                finalCodonCombinations.append(combination)

#This will be the user input#
user_seq = "MVSKGEELFTGVVPILVELDGDVNGHKFSVSGEGEGDATYGKLTLKFICTTGKLPVPWPT\
LVTTLTYGVQCFSRYPDHMKQHDFFKSAMPEGYVQERTIFFKDDGNYKTRAEVKFEGDTL\
VNRIELKGIDFKEDGNILGHKLEYNYNSHNVYIMADKQKNGIKVNFKIRHNIEDGSVQLA\
DHYQQNTPIGDGPVLLPDNHYLSTQSALSKDPNEKRDHMVLLEFVTAAGITLGMDELYKX"

#Splits the user input into codon pairs#
seq_couples = []
for i in range(len(user_seq)-1):
    seq_couples.append(user_seq[i]+user_seq[i+1])


count=0

#Generate 20 different sequences.
while(count<=20):    
    nucleotide_solution = ""
    CAI_Value = 0
    for i in range(len(seq_couples)):
        pair_possibilities = []
        if i==0:
            for combination in finalCodonCombinations:
                if combination[1]==seq_couples[i]:
                    pair_possibilities.append(combination)
            nucleotide_solution = seq_construction(pair_possibilities, nucleotide_solution)
        else:
            for combination in finalCodonCombinations:
                if combination[1]==seq_couples[i]:
                    if combination[0][0:3]==nucleotide_solution[-3:]:
                        pair_possibilities.append(combination)
            nucleotide_solution += seq_construction(pair_possibilities, nucleotide_solution)
    for organism in user_organisms:
        CAI_Value += CAI(nucleotide_solution, weights = get_index(organism))
    print(CAI_Value/len(user_organisms))  #generates average of cai values
    print("\n")
    print(nucleotide_solution)
    print("\n")
    count= count +1



