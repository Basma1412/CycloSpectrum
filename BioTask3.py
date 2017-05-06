
def massSpectrum(input):
    peptideMass = {'G': 57, 'A': 71, 'S':87,'P': 97, 'V': 99,
    'T':101, 'C':103,'I':113,'L':113,'N':114,'D':115,'K':128,
    'Q':128,'E':129,'H':137,'F':147,'R':156,'Y':163,'W':186,'0':0};
    return peptideMass[input]



def subPeptides(input):
    subpeptides=['0']
    i = 0
    length = len(input)
    while i <length-1:
        j=0
        while j<(length-i):
            sub=input[j:j+i+1]
            subpeptides.append(sub)
            j = j+1

        k= length-i-1
        if i<length-1:
             if k<length:
                sub=input[k:k+i+1]
                sub=input[0]+sub
                subpeptides.append(sub)
                k=k+1
        i=i+1
    return subpeptides



def subpeptidesLength(protein):
    subpeptides=subPeptides(protein)
    masses =[]
    for subpeptid in subpeptides:
        mass=0
        for c in subpeptid:
            mass = mass+massSpectrum(c)
        masses.append(mass)
    return masses







print("Enter Protein Sequence")
protein = input()
print(subpeptidesLength(protein))