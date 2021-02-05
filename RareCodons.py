##Lists of Organism and Respective Rare Codons##

#0.1 Threshold#



def get_rare_codons(organism):
    if (organism == "saccharomyces_cerevisiae"):
        rcs = ['ctc', 'tcg', 'cgc', 'cga', 'cgg']
        rcs = ['ctt', 'ctc', 'cta', 'ctg', 'tca', 'tcg', 'agt', 'agc', 'tag', 'tga', 'ccc', 'ccg', 'cag', 'cgc', 'cga', 'cgg', 'agg', 'ata', 'aca', 'acg', 'gta', 'gtg', 'gca', 'gcg', 'gag', 'ggc', 'gga', 'ggg']
        #rare codons from rps
        #['cgc'] @0.05 threshold
    elif (organism == "yarrowia_lipolytica"):
        rcs = ['tta', 'cta', 'tca', 'agt', 'cgc', 'agg', 'ata', 'gta', 'ggg']
        #['tta', 'agg', 'ata'] @0.05
    elif (organism == "aspergillus_niger"):
        rcs = ['tta', 'cta']
        #['tta']@0.05
    elif (organism == "aspergillus_oryzae"):
        rcs = ['tta']
        #['tta']@0.05
    elif (organism == "komagataella_pastoris"):
        rcs = ['ctc', 'tcg', 'cgc', 'cgg', 'gcg']
        #[]@0.05
    elif (organism == "escherichia_coli"):
        rcs = ['cta', 'tag', 'cga', 'cgg', 'aga', 'agg', 'ata']
        #['cta', 'aga', 'agg']
    elif (organism == "bacillus_subtilis"):
        rcs = ['cta', 'tcg', 'ccc', 'cga', 'agg']
        #['cta']@0.05
    elif (organism == "komagataeibacter_rhaeticus"):
        rcs = ['ctc', 'tcg', 'cgc', 'cgg', 'gcg']
        #[]@0.05
    elif (organism == "rhodosporidium_toruloides"):
        rcs = ['tta', 'cta', 'tct', 'tca', 'agt', 'cgt', 'aga', 'ata', 'gta']
        #['tta', 'cta', 'agt', 'aga', 'ata', 'gta'] @0.05
    return rcs


        
        
        
    

## removes duplicates rarecodons = list(set(saccharomyces_cerevisiae+yarrowia_lipolytica))

