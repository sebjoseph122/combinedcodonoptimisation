def get_RP_index(organism):
    if(organism == "saccharomyces_cerevisiae"):
        ix = {'TTT': 0.3451202263083451, 'TTC': 1.0, 'TTA': 0.26464507236388696, 'TTG': 1.0, 'TCT': 1.0, 'TCC': 0.6768507638072856, 'TCA': 0.10223266745005875, 'TCG': 0.03290246768507638, 'TAT': 0.17746913580246912, 'TAC': 1.0, 'TGT': 1.0, 'TGC': 0.13513513513513514, 'TGG': 1.0, 'CTT': 0.07512060647829083, 'CTC': 0.008270158511371467, 'CTA': 0.10062026188835285, 'CTG': 0.018607856650585803, 'CCT': 0.16147635524798154, 'CCC': 0.020761245674740483, 'CCA': 1.0, 'CCG': 0.006920415224913495, 'CAT': 0.3737373737373737, 'CAC': 1.0, 'CAA': 1.0, 'CAG': 0.026262626262626262, 'CGT': 0.22699386503067487, 'CGC': 0.005521472392638037, 'CGA': 0.0006134969325153374, 'CGG': 0.0024539877300613494, 'ATT': 0.8303571428571428, 'ATC': 1.0, 'ATA': 0.05484693877551021, 'ATG': 1.0, 'ACT': 1.0, 'ACC': 0.9143258426966293, 'ACA': 0.11938202247191011, 'ACG': 0.028089887640449437, 'AAT': 0.23973362930077693, 'AAC': 1.0, 'AAA': 0.24875396465790667, 'AAG': 1.0, 'AGT': 0.0846063454759107, 'AGC': 0.08813160987074031, 'AGA': 1.0, 'AGG': 0.027607361963190184, 'GTT': 1.0, 'GTC': 0.6844229217110573, 'GTA': 0.05407586763518967, 'GTG': 0.04358353510895884, 'GCT': 1.0, 'GCC': 0.3490172721858249, 'GCA': 0.04466944609886837, 'GCG': 0.01012507444907683, 'GAT': 0.8209677419354839, 'GAC': 1.0, 'GAA': 1.0, 'GAG': 0.06078431372549019, 'GGT': 1.0, 'GGC': 0.05740740740740741, 'GGA': 0.030246913580246913, 'GGG': 0.01111111111111111}
    elif(organism == "aspergillus_niger"):
        ix = {'TTT': 0.0226628895184136, 'TTC': 1.0, 'TTA': 0.0020790020790020787, 'TTG': 0.07900207900207899, 'TCT': 0.2899728997289973, 'TCC': 1.0, 'TCA': 0.016260162601626018, 'TCG': 0.14363143631436315, 'TAT': 0.05604719764011799, 'TAC': 1.0, 'TGT': 0.11428571428571428, 'TGC': 1.0, 'TGG': 1.0, 'CTT': 0.3118503118503118, 'CTC': 1.0, 'CTA': 0.008316008316008315, 'CTG': 0.48440748440748443, 'CCT': 0.30221130221130216, 'CCC': 1.0, 'CCA': 0.01474201474201474, 'CCG': 0.06388206388206387, 'CAT': 0.01824817518248175, 'CAC': 1.0, 'CAA': 0.06636155606407323, 'CAG': 1.0, 'CGT': 0.8986866791744841, 'CGC': 1.0, 'CGA': 0.011257035647279551, 'CGG': 0.07879924953095685, 'ATT': 0.17481203007518797, 'ATC': 1.0, 'ATA': 0.0009398496240601502, 'ATG': 1.0, 'ACT': 0.2200392927308448, 'ACC': 1.0, 'ACA': 0.01964636542239686, 'ACG': 0.060903732809430254, 'AAT': 0.03614457831325301, 'AAC': 1.0, 'AAA': 0.012195121951219513, 'AAG': 1.0, 'AGT': 0.02710027100271003, 'AGC': 0.3739837398373984, 'AGA': 0.09943714821763602, 'AGG': 0.03564727954971857, 'GTT': 0.39171974522292996, 'GTC': 1.0, 'GTA': 0.0015923566878980893, 'GTG': 0.11942675159235669, 'GCT': 0.7766497461928933, 'GCC': 1.0, 'GCA': 0.021996615905245348, 'GCG': 0.07783417935702198, 'GAT': 0.2958904109589041, 'GAC': 1.0, 'GAA': 0.08862629246676514, 'GAG': 1.0, 'GGT': 1.0, 'GGC': 0.5172413793103449, 'GGA': 0.1234119782214156, 'GGG': 0.01633393829401089}
    elif(organism == "aspergillus_oryzae"):
        ix = {'TTT': 0.053968253968253964, 'TTC': 1.0, 'TTA': 0.010893246187363833, 'TTG': 0.13507625272331153, 'TCT': 0.447457627118644, 'TCC': 1.0, 'TCA': 0.02711864406779661, 'TCG': 0.1423728813559322, 'TAT': 0.1013986013986014, 'TAC': 1.0, 'TGT': 0.32307692307692304, 'TGC': 1.0, 'TGG': 1.0, 'CTT': 0.4008714596949891, 'CTC': 1.0, 'CTA': 0.006535947712418301, 'CTG': 0.355119825708061, 'CCT': 0.4823151125401929, 'CCC': 1.0, 'CCA': 0.028938906752411574, 'CCG': 0.03858520900321543, 'CAT': 0.07264957264957266, 'CAC': 1.0, 'CAA': 0.07323232323232323, 'CAG': 1.0, 'CGT': 1.0, 'CGC': 0.8787878787878788, 'CGA': 0.032467532467532464, 'CGG': 0.07792207792207792, 'ATT': 0.2260127931769723, 'ATC': 1.0, 'ATA': 0.0021321961620469083, 'ATG': 1.0, 'ACT': 0.2933985330073349, 'ACC': 1.0, 'ACA': 0.039119804400977995, 'ACG': 0.06356968215158924, 'AAT': 0.07816711590296495, 'AAC': 1.0, 'AAA': 0.018467220683287166, 'AAG': 1.0, 'AGT': 0.06779661016949153, 'AGC': 0.4305084745762712, 'AGA': 0.10389610389610389, 'AGG': 0.07792207792207792, 'GTT': 0.4861660079051383, 'GTC': 1.0, 'GTA': 0.003952569169960474, 'GTG': 0.16403162055335968, 'GCT': 0.7855750487329435, 'GCC': 1.0, 'GCA': 0.04288499025341131, 'GCG': 0.07797270955165693, 'GAT': 0.3987730061349693, 'GAC': 1.0, 'GAA': 0.1059390048154093, 'GAG': 1.0, 'GGT': 1.0, 'GGC': 0.6291390728476821, 'GGA': 0.1479028697571744, 'GGG': 0.019867549668874173}
    elif(organism == "bacillus_subtilis"):
        ix = {'TTT': 0.4838709677419355, 'TTC': 1.0, 'TTA': 0.5555555555555555, 'TTG': 0.24786324786324784, 'TCT': 1.0, 'TCC': 0.08854166666666667, 'TCA': 0.421875, 'TCG': 0.03125, 'TAT': 0.4107142857142857, 'TAC': 1.0, 'TGT': 0.5, 'TGC': 1.0, 'TGG': 1.0, 'CTT': 1.0, 'CTC': 0.0641025641025641, 'CTA': 0.1752136752136752, 'CTG': 0.14957264957264957, 'CCT': 1.0, 'CCC': 0.03571428571428571, 'CCA': 0.9732142857142857, 'CCG': 0.3571428571428571, 'CAT': 0.8378378378378379, 'CAC': 1.0, 'CAA': 1.0, 'CAG': 0.29411764705882354, 'CGT': 1.0, 'CGC': 0.5060606060606061, 'CGA': 0.030303030303030304, 'CGG': 0.006060606060606061, 'ATT': 0.7845528455284553, 'ATC': 1.0, 'ATA': 0.020325203252032523, 'ATG': 1.0, 'ACT': 1.0, 'ACC': 0.04712041884816754, 'ACA': 0.7277486910994764, 'ACG': 0.2984293193717278, 'AAT': 0.38181818181818183, 'AAC': 1.0, 'AAA': 1.0, 'AAG': 0.21745788667687593, 'AGT': 0.15625, 'AGC': 0.3020833333333333, 'AGA': 0.1515151515151515, 'AGG': 0.012121212121212121, 'GTT': 1.0, 'GTC': 0.17307692307692304, 'GTA': 0.717948717948718, 'GTG': 0.2467948717948718, 'GCT': 1.0, 'GCC': 0.0790273556231003, 'GCA': 0.4802431610942249, 'GCG': 0.23708206686930092, 'GAT': 1.0, 'GAC': 0.9038461538461537, 'GAA': 1.0, 'GAG': 0.30861244019138756, 'GGT': 1.0, 'GGC': 0.45692883895131087, 'GGA': 0.7153558052434458, 'GGG': 0.0599250936329588}
    elif(organism == "komagataeibacter_rhaeticus"):
        ix = {'TTT': 0.1895424836601307, 'TTC': 1.0, 'TTA': 0.0012048192771084338, 'TTG': 0.03132530120481928, 'TCT': 0.14285714285714285, 'TCC': 1.0, 'TCA': 0.045454545454545456, 'TCG': 0.5909090909090909, 'TAT': 0.7901234567901234, 'TAC': 1.0, 'TGT': 0.13793103448275862, 'TGC': 1.0, 'TGG': 1.0, 'CTT': 0.14457831325301204, 'CTC': 0.14698795180722893, 'CTA': 0.004819277108433735, 'CTG': 1.0, 'CCT': 0.096045197740113, 'CCC': 0.5084745762711865, 'CCA': 0.028248587570621472, 'CCG': 1.0, 'CAT': 0.8831168831168832, 'CAC': 1.0, 'CAA': 0.017467248908296942, 'CAG': 1.0, 'CGT': 0.6873385012919897, 'CGC': 1.0, 'CGA': 0.007751937984496124, 'CGG': 0.16020671834625322, 'ATT': 0.22012578616352202, 'ATC': 1.0, 'ATA': 0.0015723270440251573, 'ATG': 1.0, 'ACT': 0.056074766355140186, 'ACC': 1.0, 'ACA': 0.12149532710280375, 'ACG': 0.6074766355140188, 'AAT': 0.18877551020408162, 'AAC': 1.0, 'AAA': 0.09289617486338798, 'AAG': 1.0, 'AGT': 0.05844155844155844, 'AGC': 0.4480519480519481, 'AGA': 0.010335917312661497, 'AGG': 0.007751937984496124, 'GTT': 0.5018181818181818, 'GTC': 0.8218181818181818, 'GTA': 0.06909090909090909, 'GTG': 1.0, 'GCT': 0.2195767195767196, 'GCC': 1.0, 'GCA': 0.2380952380952381, 'GCG': 0.6825396825396826, 'GAT': 0.6584158415841584, 'GAC': 1.0, 'GAA': 1.0, 'GAG': 0.8049792531120332, 'GGT': 0.5628415300546449, 'GGC': 1.0, 'GGA': 0.06010928961748634, 'GGG': 0.14754098360655737}
    elif(organism == "komagataella_pastoris"):
        ix = {'TTT': 0.4136904761904762, 'TTC': 1.0, 'TTA': 0.16347826086956524, 'TTG': 1.0, 'TCT': 1.0, 'TCC': 0.858974358974359, 'TCA': 0.1794871794871795, 'TCG': 0.03333333333333333, 'TAT': 0.1391304347826087, 'TAC': 1.0, 'TGT': 1.0, 'TGC': 0.625, 'TGG': 1.0, 'CTT': 0.23478260869565218, 'CTC': 0.12173913043478261, 'CTA': 0.053913043478260876, 'CTG': 0.3252173913043478, 'CCT': 0.4854651162790698, 'CCC': 0.055232558139534885, 'CCA': 1.0, 'CCG': 0.00872093023255814, 'CAT': 0.2520325203252033, 'CAC': 1.0, 'CAA': 1.0, 'CAG': 0.5027777777777778, 'CGT': 0.2715311004784689, 'CGC': 0.01674641148325359, 'CGA': 0.014354066985645935, 'CGG': 0.004784688995215311, 'ATT': 0.8454545454545453, 'ATC': 1.0, 'ATA': 0.024999999999999998, 'ATG': 1.0, 'ACT': 0.8705234159779615, 'ACC': 1.0, 'ACA': 0.11294765840220385, 'ACG': 0.01928374655647383, 'AAT': 0.13026052104208416, 'AAC': 1.0, 'AAA': 0.16790736145574855, 'AAG': 1.0, 'AGT': 0.12564102564102564, 'AGC': 0.06923076923076922, 'AGA': 1.0, 'AGG': 0.025119617224880382, 'GTT': 1.0, 'GTC': 0.7398230088495574, 'GTA': 0.0831858407079646, 'GTG': 0.12566371681415928, 'GCT': 1.0, 'GCC': 0.5925394548063128, 'GCA': 0.07604017216642754, 'GCG': 0.012912482065997129, 'GAT': 0.501240694789082, 'GAC': 1.0, 'GAA': 0.4621451104100946, 'GAG': 1.0, 'GGT': 1.0, 'GGC': 0.047879616963064295, 'GGA': 0.24623803009575926, 'GGG': 0.009575923392612859}
    elif(organism == "rhodosporidium_toruloides"):
        ix = {'TTT': 0.18309859154929578, 'TTC': 1.0, 'TTA': 0.004016064257028112, 'TTG': 0.157429718875502, 'TCT': 0.14393939393939392, 'TCC': 0.3977272727272727, 'TCA': 0.07575757575757576, 'TCG': 1.0, 'TAT': 0.05466970387243736, 'TAC': 1.0, 'TGT': 0.09883720930232558, 'TGC': 1.0, 'TGG': 1.0, 'CTT': 0.1285140562248996, 'CTC': 1.0, 'CTA': 0.00963855421686747, 'CTG': 0.18714859437751005, 'CCT': 0.3073322932917316, 'CCC': 1.0, 'CCA': 0.15912636505460218, 'CCG': 0.5288611544461779, 'CAT': 0.09649122807017543, 'CAC': 1.0, 'CAA': 0.12779973649538867, 'CAG': 1.0, 'CGT': 0.21940163191296463, 'CGC': 1.0, 'CGA': 0.16047144152311876, 'CGG': 0.2511332728921124, 'ATT': 0.12663185378590078, 'ATC': 1.0, 'ATA': 0.00783289817232376, 'ATG': 1.0, 'ACT': 0.2030769230769231, 'ACC': 1.0, 'ACA': 0.1430769230769231, 'ACG': 0.5323076923076924, 'AAT': 0.05627009646302251, 'AAC': 1.0, 'AAA': 0.038526912181303115, 'AAG': 1.0, 'AGT': 0.050505050505050504, 'AGC': 0.21843434343434343, 'AGA': 0.011786038077969173, 'AGG': 0.22030825022665457, 'GTT': 0.161106590724166, 'GTC': 1.0, 'GTA': 0.025223759153783568, 'GTG': 0.1627339300244101, 'GCT': 0.34353405725567615, 'GCC': 1.0, 'GCA': 0.33366238894373146, 'GCG': 0.7156959526159922, 'GAT': 0.12332439678284182, 'GAC': 1.0, 'GAA': 0.09147424511545293, 'GAG': 1.0, 'GGT': 0.36283185840707965, 'GGC': 1.0, 'GGA': 0.3223767383059418, 'GGG': 0.16308470290771176}
    elif(organism == "yarrowia_lipolytica"):
        ix = {'TTT': 0.16573033707865167, 'TTC': 1.0, 'TTA': 0.0018726591760299626, 'TTG': 0.016853932584269662, 'TCT': 0.7807228915662651, 'TCC': 1.0, 'TCA': 0.014457831325301205, 'TCG': 0.02891566265060241, 'TAT': 0.013477088948787063, 'TAC': 1.0, 'TGT': 0.3333333333333333, 'TGC': 1.0, 'TGG': 1.0, 'CTT': 0.36329588014981273, 'CTC': 1.0, 'CTA': 0.0009363295880149813, 'CTG': 0.4644194756554307, 'CCT': 0.2926208651399491, 'CCC': 1.0, 'CCA': 0.005089058524173028, 'CCG': 0.010178117048346057, 'CAT': 0.10344827586206896, 'CAC': 1.0, 'CAA': 0.02336448598130841, 'CAG': 1.0, 'CGT': 0.02995169082125604, 'CGC': 0.0019323671497584538, 'CGA': 1.0, 'CGG': 0.017391304347826087, 'ATT': 0.37807183364839314, 'ATC': 1.0, 'ATA': 0.0009451795841209828, 'ATG': 1.0, 'ACT': 0.3088235294117647, 'ACC': 1.0, 'ACA': 0.011029411764705881, 'ACG': 0.005514705882352941, 'AAT': 0.005747126436781609, 'AAC': 1.0, 'AAA': 0.016, 'AAG': 1.0, 'AGT': 0.007228915662650603, 'AGC': 0.06265060240963856, 'AGA': 0.03188405797101449, 'AGG': 0.0009661835748792269, 'GTT': 0.6151260504201681, 'GTC': 1.0, 'GTA': 0.0033613445378151263, 'GTG': 0.14621848739495796, 'GCT': 0.645293315143247, 'GCC': 1.0, 'GCA': 0.013642564802182811, 'GCG': 0.004092769440654843, 'GAT': 0.33980582524271846, 'GAC': 1.0, 'GAA': 0.033200531208499334, 'GAG': 1.0, 'GGT': 1.0, 'GGC': 0.6020618556701031, 'GGA': 0.27010309278350514, 'GGG': 0.0020618556701030924}
    elif(organism == "escherichia_coli"):
        ix = {'TTT': 0.3435582822085889, 'TTC': 1.0, 'TTA': 0.035629453681710214, 'TTG': 0.0498812351543943, 'TCT': 1.0, 'TCC': 0.6640624999999999, 'TCA': 0.0703125, 'TCG': 0.04687499999999999, 'TAT': 0.35714285714285715, 'TAC': 1.0, 'TGT': 0.40740740740740744, 'TGC': 1.0, 'TGG': 1.0, 'CTT': 0.05938242280285035, 'CTC': 0.047505938242280284, 'CTA': 0.004750593824228028, 'CTG': 1.0, 'CCT': 0.2236024844720497, 'CCC': 0.018633540372670808, 'CCA': 0.2111801242236025, 'CCG': 1.0, 'CAT': 0.3783783783783784, 'CAC': 1.0, 'CAA': 0.3111111111111111, 'CAG': 1.0, 'CGT': 1.0, 'CGC': 0.455607476635514, 'CGA': 0.009345794392523364, 'CGG': 0.009345794392523364, 'ATT': 0.3525423728813559, 'ATC': 1.0, 'ATA': 0.003389830508474576, 'ATG': 1.0, 'ACT': 1.0, 'ACC': 0.9039548022598871, 'ACA': 0.1016949152542373, 'ACG': 0.11299435028248589, 'AAT': 0.16818181818181818, 'AAC': 1.0, 'AAA': 1.0, 'AAG': 0.4233128834355828, 'AGT': 0.125, 'AGC': 0.6562499999999999, 'AGA': 0.011682242990654207, 'AGG': 0.0011682242990654205, 'GTT': 1.0, 'GTC': 0.18233618233618235, 'GTA': 0.5099715099715101, 'GTG': 0.25925925925925924, 'GCT': 1.0, 'GCC': 0.19060773480662982, 'GCA': 0.5883977900552486, 'GCG': 0.356353591160221, 'GAT': 0.628140703517588, 'GAC': 1.0, 'GAA': 1.0, 'GAG': 0.34571428571428575, 'GGT': 1.0, 'GGC': 0.6387283236994219, 'GGA': 0.017341040462427744, 'GGG': 0.02601156069364162}
    
    return ix
        