def reverse_and_complement( dna_strand ):
    Comp = {“a”:”t”, “c”:”g”, “g”:”c”,”t”:”a”}
    comp_strand = “”
    for base in dna_strand:
        comp_strand = comp_strand + Comp[base.lower()]
    return comp_strand 
        
