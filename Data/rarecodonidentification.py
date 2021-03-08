from CUTforRPs import komagataella_pastoris

rareCodons = []

for row in komagataella_pastoris:
    for col in row:
        if col[2]<=0.01:
            rareCodons.append(col[0])
print(rareCodons)

