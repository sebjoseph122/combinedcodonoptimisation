from Bio import SeqIO
import re

## Codon2AA Dictionary ##

Codon2AA = {"ttt":"F", "ttc":"F",
            "tta":"L", "ttg":"L","ctt":"L", "ctc":"L", "cta":"L", "ctg":"L",
            "tct":"S","tcc":"S", "tca":"S", "tcg":"S", "agt":"S", "agc":"S",
            "tat":"Y", "tac":"Y",
            "taa":"X", "tag":"X", "tga":"X",
            "tgt":"C", "tgc":"C",
            "tgg":"W",
            "cct":"P", "ccc":"P", "cca":"P", "ccg":"P",
            "cat":"H", "cac":"H",
            "caa":"Q", "cag":"Q",
            "cgt":"R", "cgc":"R", "cga":"R", "cgg":"R", "aga":"R", "agg":"R",
            "att":"I", "atc":"I", "ata":"I",
            "atg":"M",
            "act":"T", "acc":"T", "aca":"T", "acg":"T",
            "aat":"N", "aac":"N",
            "aaa":"K", "aag":"K",
            "gtt":"V", "gtc":"V", "gta":"V", "gtg":"V",
            "gct":"A", "gcc":"A", "gca":"A", "gcg":"A",
            "gat":"D", "gac":"D",
            "gaa":"E", "gag":"E",
            "ggt":"G", "ggc":"G", "gga":"G", "ggg":"G" 
}

## Codon Table Storing Number and Freq/1000 ##
## [Codon, Number, Fraction, Freq/1000] ##

CodonTable = [[["ttt",0],["ttc",0]], #Phe
              [["tta",0],["ttg",0],["ctt",0],["ctc",0],["cta",0],["ctg",0]], #Leu
              [["tct",0],["tcc",0],["tca",0],["tcg",0],["agt",0],["agc",0]], #Ser
              [["tat",0],["tac",0]], #Tyr
              [["taa",0],["tag",0],["tga",0]], #stop codon
              [["tgt",0],["tgc",0]], #Cys
              [["tgg",0]], #Trp
              [["cct",0],["ccc",0],["cca",0],["ccg",0]], #Pro
              [["cat",0],["cac",0]], #His
              [["caa",0],["cag",0]], #Gln
              [["cgt",0],["cgc",0],["cga",0],["cgg",0],["aga",0],["agg",0]], #Arg
              [["att",0],["atc",0],["ata",0]], #Ile
              [["atg",0]], #Met
              [["act",0],["acc",0],["aca",0],["acg",0]], #Thr
              [["aat",0],["aac",0]], #Asn
              [["aaa",0],["aag",0]], #Lys
              [["gtt",0],["gtc",0],["gta",0],["gtg",0]], #Val
              [["gct",0],["gcc",0],["gca",0],["gcg",0]], #Ala
              [["gat",0],["gac",0]], #Asp
              [["gaa",0],["gag",0]], #Glu
              [["ggt",0],["ggc",0],["gga",0],["ggg",0]] #Gly
] 


## Main ##



listofCodons = [*Codon2AA]  #Makes list of keys from dict
CodonCombinations = []      #Initiate list with form [2 codon seq, equivalent

for i in range(len(listofCodons)):
    for j in range(len(listofCodons)):
        CodonCombinations.append([listofCodons[i]+listofCodons[j], Codon2AA.get(listofCodons[i])+Codon2AA.get(listofCodons[j]) ,0])
    


for seq_record in SeqIO.parse("RhodosporidiumToruloidesRPGenes.fasta", "fasta"):            #change file name
    dnaSeq = str(seq_record.seq.lower())
    if re.match(r'^atg', dnaSeq):
        if len(dnaSeq)%3 == 0: 
            codonSeq = [dnaSeq[i:i+3] for i in range(0, len(dnaSeq)-2, 3)]
            for index,codon in enumerate(codonSeq):
                if(index+1<len(codonSeq)):
                    for combination in CodonCombinations:
                        if codon + codonSeq[index+1] == combination[0]:
                            combination[2] += 1
                        else:
                            pass
                else:
                    pass
##            for row in CodonTable:
##                for col in row:
##                    if col[0]==codon:
##                        col[1]+=1
    else:
        pass
##Total = sum(col[1] for row in CodonTable for col in row)
##for row in CodonTable:
##    Sum = sum(col[1] for col in row)
##    for col in row:
##        if Sum == 0:
##            col.append(0)
##            col.append(round((col[1]/Total)*1000,3))
##        else:
##            col.append(round(col[1]/Sum, 3))
##            col.append(round((col[1]/Total)*1000,3))

           
##print(Total)
##print(CodonCombinations[0])
##print(CodonCombinations[68])
print(CodonCombinations)

    
