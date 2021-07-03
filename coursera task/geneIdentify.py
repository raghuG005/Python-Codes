gene = "AAATGCCCTAACTAGATTAAGAAACC"


isVaild = gene[gene.find("ATG"):gene.find("TAA")+3]

if len(isVaild) % 3 == 0:
    print("Vaild Gene")
else:
    print("No gene present")
