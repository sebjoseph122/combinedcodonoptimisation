import streamlit as st
from PIL import Image
from main import get_nucleotide_seq


user_organisms = []

############
#Page Title#
############

##image = Image.open('translation_logo.jpeg')
##
##st.image(image, use_column_width=True)

st.write("""
# CodonCombi

Codon Optimisation for Multiple Organisms

***
""")

st.header("Select Organisms")

if st.checkbox("Saccharomyces Cerevisae"):
    user_organisms.append("saccharomyces_cerevisiae")
if st.checkbox("Yarrowia Lipolytica"):
    user_organisms.append("yarrowia_lipolytica")
if st.checkbox("Escherichia Coli"):
    user_organisms.append("escherichia_coli")
if st.checkbox("Aspergillus Niger"):
    user_organisms.append("aspergillus_niger")
if st.checkbox("Aspergillus Oryzae"):
    user_organisms.append("aspergillus_oryzae")
if st.checkbox("Bacillus Subtilis"):
    user_organisms.append("bacillus_subtilis")
if st.checkbox("Komagataella(Pichia) Pastoris"):
    user_organisms.append("komagataella_pastoris")
if st.checkbox("Rhodosporidium(Rhodotorula) Toruloides"):
    user_organisms.append("rhodosporidium_toruloides")
if st.checkbox("Komagataeibacter Rhaeticus"):
    user_organisms.append("komagataeibacter_rhaeticus")

    




################
#Input Text Box#
################

st.header('Enter Amino Acid Sequence (X for STOP Codon)')

example_input = "e.g.MSKGEELFTGVVPILVELDGDVNGHKFSVRGEGEGDA\
TNGKLTLKFICTTGKLPVPWPTLVTTLTYGVQCFSRYPDHMKRHDFFKSAMPEGYVQERTISFKDD\
GTYKTRAEVKFEGDTLVNRIELKGIDFKEDGNILGHKLEYNFNSHNVYITADKQKNGIKANFKIRHNV\
EDGSVQLADHYQQNTPIGDGPVLLPDNHYLSTQSRLSKDPNEKRDHMVLLEFVTAAGITHGMDELYKX"

user_seq = st.text_area("Protein Sequence Input", example_input, height=250)
user_seq = user_seq.splitlines()
user_seq = ''.join(user_seq)
user_seq = user_seq.upper()

user_organisms

if st.button("Run"):
    st.write("""
    ***
    """)

    st.header('OUTPUT')
    nuc_seq, cai_val = get_nucleotide_seq(user_organisms, user_seq)
    st.text(nuc_seq)
    st.text("CAI Value = " + str(cai_val))

