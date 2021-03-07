import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
from sklearn import preprocessing
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import re
import os

codon2AA = {"ttt":"Phe", "ttc":"Phe",
            "tta":"Leu", "ttg":"Leu",
            "tct":"Ser","tcc":"Ser", "tca":"Ser", "tcg":"Ser", "agt":"Ser", "agc":"Ser",
            "tat":"Tyr", "tac":"Tyr",
            "taa":"Stop", "tag":"Stop", "tga":"Stop",
            "tgt":"Cys", "tgc":"Cys",
            "tgg":"Trp",
            "ctt":"Leu", "ctc":"Leu", "cta":"Leu", "ctg":"Leu",
            "cct":"Pro", "ccc":"Pro", "cca":"Pro", "ccg":"Pro",
            "cat":"His", "cac":"His",
            "caa":"Gln", "cag":"Gln",
            "cgt":"Arg", "cgc":"Arg", "cga":"Arg", "cgg":"Arg", "aga":"Arg", "agg":"Arg",
            "att":"Ile", "atc":"Ile", "ata":"Ile",
            "atg":"Met",
            "act":"Thr", "acc":"Thr", "aca":"Thr", "acg":"Thr",
            "aat": "Asn", "aac":"Asn",
            "aaa":"Lys", "aag":"Lys",
            "gtt":"Val", "gtc":"Val", "gta":"Val", "gtg":"Val",
            "gct":"Ala", "gcc":"Ala", "gca":"Ala", "gcg":"Ala",
            "gat":"Asp", "gac":"Asp",
            "gaa":"Glu", "gag":"Glu",
            "ggt":"Gly", "ggc":"Gly", "gga":"Gly", "ggg":"Gly" 
            }

listOfCodons = [*codon2AA]                  #creates a list of all the keys of the codon dictionary
listOfLists = []
listOfGenes = []
listOfDIR = []


def CodonBias2(fileName):

    dnaSeq = ""

    dnaFile = open(fileName, "r")
    dnaLine = dnaFile.readline()
    while dnaLine != "":
        dnaLine = dnaFile.readline()
        dnaSeq += dnaLine
    dnaFile.close()

    Codons = [dnaSeq[i:i+3] for i in range(0, len(dnaSeq)-2, 3)]

    codonCount = len(Codons)                                                                                             
    occurrences = []                                                                                                   #list of the occurrences of each codon
    listOfFractions = []
    for item in listOfCodons:
        count = 0
        for codon in Codons:                                                                                             #iterates through inputed gene looking for matching codon
            if item == codon:
                count+=1
            else:
                count=count
        occurrences.append(count)
##    print("\t\tCodon" + "\t\tAmino Acid" + "\t\tFraction")
##    for i in range(len(listOfCodons)):
##        print("\t\t", listOfCodons[i], "\t\t", codon2AA.get(listOfCodons[i]), "\t\t\t", occurrences[i]/codonCount)      #outputs fraction occurrences/total number of codons (including start and stop codons)
    for i in range(len(listOfCodons)):
        listOfFractions.append(occurrences[i]/codonCount)
    return listOfFractions

def pureCodonBias(fileName, folderName):
    AA = []
    occurrences = []
    dnaSeq = ""
    listOfFractions = []
    Codons =[]

    dnaFile = open(fileName, "r")
    dnaLine = dnaFile.readline()
    while dnaLine != "":
        dnaLine = dnaFile.readline()
        dnaSeq += dnaLine
    dnaFile.close()
    dnaseq = dnaSeq.lower()

    if re.match(r'^atg', dnaseq):
        Codons = [dnaseq[i:i+3] for i in range(0, len(dnaseq)-2, 3)]
        for codon in Codons:                                                                                                 #creating list of translated codons to amino acids
            aa = codon2AA.get(codon,"not found")
            AA.append(aa)
        for item in listOfCodons:
            count=0;
            for codon in Codons:
                if item == codon:
                    count +=1
                else:
                    count=count
            occurrences.append(count)

        for i in range(len(listOfCodons)):
            denominator = AA.count(codon2AA.get(listOfCodons[i]))
            if denominator==0:                                                                                              #can't divide by zero, so this is a quick fix
                denominator=1
            else:
                denominator = denominator
##        print("\t\t", listOfCodons[i], "\t\t", codon2AA.get(listOfCodons[i]), "\t\t\t", occurrences[i]/denominator)
            listOfFractions.append(occurrences[i]/denominator)
        listOfLists.append(listOfFractions)
        listOfGenes.append(fileName)
        listOfDIR.append(folderName)
    else:
        pass
        
#main




dir = [ "RPSC", "RPAN", "RPYL", "RPPP", "RPAO", "RPKR", "RPEC", "RPBS", "RPRT"]

for folder in dir:
    directory = r'C:\Users\Me\Documents\Year3\Group Project\Autumn\stress_genes' + "\\" + folder       #change to read another folder
    for fastafile in os.listdir(directory):
        pureCodonBias(os.path.join(directory, fastafile), folder)
        
        


GDTable = pd.DataFrame({"Gene Group":listOfDIR})


##COpied from Youtube
data = pd.DataFrame(listOfLists, columns=[listOfCodons], index=listOfGenes)        #constructing panda

##data.to_csv(r'ResultsYeastGenome.csv')     #convert panda to csv to compare
print(data.shape)

##scaled_data = preprocessing.scale(data.T) #Average value for each gene = 0 and sd = 1 T= transpose of data required because function requires data in columns
scaled_data = StandardScaler().fit_transform(data)


pca = PCA(n_components=2)

principal_components = pca.fit_transform(scaled_data)
principal_db = pd.DataFrame(data = principal_components, columns =['PC1', 'PC2'])
print(principal_db.shape)


finalfreq = pd.concat([principal_db, GDTable], axis=1)

fig= plt.figure(figsize= (8,8))
ax = fig.add_subplot(1,1,1)
ax.set_xlabel('Principal Component 1', fontsize=15)
ax.set_ylabel('Principal Component 2', fontsize=15)
ax.set_title('2 Component PCA', fontsize=20)

colours = ['r', 'g', 'b', 'k', 'c', 'm', 'y', 'darkorange', 'darkgrey']
for target, colour in zip(dir, colours):
    indicesToKeep = finalfreq["Gene Group"] == target
    ax.scatter(finalfreq.loc[indicesToKeep, 'PC1'], finalfreq.loc[indicesToKeep, 'PC2'], c=colour, s=50)

ax.legend(dir)

ax.grid()

plt.savefig("RPs for organisms.jpg", dpi=300)




    
