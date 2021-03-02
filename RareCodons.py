##Rare Codons from Ribosomal Proteins at x threshold##

def get_rare_codons(organism):
    if (organism == "saccharomyces_cerevisiae"):
        ##rcs = ['ctt', 'ctc', 'cta', 'ctg', 'tca', 'tcg', 'agt', 'agc', 'tag', 'tga', 'ccc', 'ccg', 'cag', 'cgc', 'cga', 'cgg', 'agg', 'ata', 'aca', 'acg', 'gta', 'gtg', 'gca', 'gcg', 'gag', 'ggc', 'gga', 'ggg'] #0.1
        ##rcs = ['ctc', 'ctg', 'tcg', 'agt', 'agc', 'ccc', 'ccg', 'cag', 'cgc', 'cga', 'cgg', 'agg', 'ata', 'acg', 'gta', 'gtg', 'gca', 'gcg', 'gga', 'ggg'] #0.05
        rcs = ['ctc', 'ccg', 'cgc', 'cga', 'cgg', 'gcg', 'ggg']#0.01
    elif (organism == "yarrowia_lipolytica"):
        ##rcs = ['tta', 'ttg', 'cta', 'tca', 'tcg', 'agt', 'agc', 'tat', 'tag', 'tga', 'cca', 'ccg', 'cat', 'caa', 'cgt', 'cgc', 'cgg', 'aga', 'agg', 'ata', 'aca', 'acg', 'aat', 'aaa', 'gta', 'gtg', 'gca', 'gcg', 'gaa', 'ggg']#0.1
        ##rcs = ['tta', 'ttg', 'cta', 'tca', 'tcg', 'agt', 'agc', 'tat', 'tga', 'cca', 'ccg', 'caa', 'cgt', 'cgc', 'cgg', 'aga', 'agg', 'ata', 'aca', 'acg', 'aat', 'aaa', 'gta', 'gca', 'gcg', 'gaa', 'ggg']#0.05
        rcs = ['tta', 'ttg', 'cta', 'tca', 'agt', 'cca', 'ccg', 'cgc', 'agg', 'ata', 'aca', 'acg', 'aat', 'gta', 'gca', 'gcg', 'ggg']#0.01
    elif (organism == "aspergillus_niger"):
        ##rcs = ['ttt', 'tta', 'ttg', 'cta', 'tca', 'tcg', 'agt', 'tat', 'tga', 'cca', 'ccg', 'cat', 'caa', 'cga', 'cgg', 'aga', 'agg', 'ata', 'aca', 'acg', 'aat', 'aaa', 'gta', 'gtg', 'gca', 'gcg', 'gaa', 'gga', 'ggg']#0.1
        ##rcs = ['ttt', 'tta', 'ttg', 'cta', 'tca', 'agt', 'tga', 'cca', 'ccg', 'cat', 'cga', 'cgg', 'aga', 'agg', 'ata', 'aca', 'acg', 'aat', 'aaa', 'gta', 'gca', 'gcg', 'ggg']#0.05
        rcs = ['tta', 'cta', 'tca', 'tga', 'cga', 'ata', 'gta', 'ggg']#0.01
    elif (organism == "aspergillus_oryzae"):
        ##rcs = ['ttt', 'tta', 'ttg', 'cta', 'tca', 'tcg', 'agt', 'tat', 'tga', 'cca', 'ccg', 'cat', 'caa', 'cga', 'cgg', 'aga', 'agg', 'ata', 'aca', 'acg', 'aat', 'aaa', 'gta', 'gtg', 'gca', 'gcg', 'gaa', 'gga', 'ggg']#0.1
        ##rcs = ['tta', 'cta', 'tca', 'agt', 'tga', 'cca', 'ccg', 'cga', 'cgg', 'aga', 'agg', 'ata', 'aca', 'acg', 'aaa', 'gta', 'gca', 'gcg', 'ggg']#0.05
        rcs = ['tta', 'cta', 'ata', 'gta']#0.01
        
    elif (organism == "komagataella_pastoris"):
        ##rcs = ['tta', 'ctc', 'cta', 'tca', 'tcg', 'agt', 'agc', 'tga', 'ccc', 'ccg', 'cgc', 'cga', 'cgg', 'agg', 'ata', 'aca', 'acg', 'gta', 'gtg', 'gca', 'gcg', 'ggc', 'ggg']#0.1
        ##rcs = ['cta', 'tcg', 'agc', 'tga', 'ccc', 'ccg', 'cgc', 'cga', 'cgg', 'agg', 'ata', 'acg', 'gta', 'gca', 'gcg', 'ggc', 'ggg']#0.05
        rcs = ['ccg', 'cgg', 'acg', 'gcg', 'ggg']#0.01
    elif (organism == "escherichia_coli"):
        ##rcs = ['tta', 'ttg', 'ctt', 'ctc', 'cta', 'tca', 'tcg', 'agt', 'tag', 'ccc', 'cga', 'cgg', 'aga', 'agg', 'ata', 'aca', 'acg', 'gtc', 'gcc', 'gga', 'ggg']#0.1
        ##rcs = ['tta', 'ttg', 'ctt', 'ctc', 'cta', 'tca', 'tcg', 'agt', 'tag', 'ccc', 'cga', 'cgg', 'aga', 'agg', 'ata', 'aca', 'gga', 'ggg']#0.05
        rcs = ['cta', 'tag', 'cga', 'cgg', 'aga', 'agg', 'ata', 'gga']#0.01
    elif (organism == "bacillus_subtilis"):
        rcs = ['tga', 'cgg', 'agg']
    elif (organism == "komagataeibacter_rhaeticus"):
        rcs = ['tta', 'cta', 'tag', 'cga', 'aga', 'agg', 'ata']#0.01
    elif (organism == "rhodosporidium_toruloides"):
        rcs = ['tta', 'cta', 'aga', 'ata']#0.01
    return rcs
