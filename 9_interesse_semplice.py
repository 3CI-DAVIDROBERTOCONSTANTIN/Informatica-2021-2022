"""
Creare un programma che dato il capitale iniziale, il tasso di interesse e il numero di anni, calcoli automaticamente il capitale finale con tasso di interesse semplice;

@author David Roberto Constantin
@version 0.1 2021-09-25
variabili:  ci= capitale iniziale, tdi= tasso di interesse, nda= numero di anni, cf= capitale finale

ci=1000
tdi=2
nda=2
cf=1040
"""






print("Inserire capitale iniziale, tasso di interesse in percentuale, numero di anni, di cui si desidera calcolare il capitale finale, con tasso di interesse semplice: ")
ci=float(input("Capitale iniziale: "))
tdi=float(input("Tasso di interesse: "))
nda=float(input("Numero di anni: "))
cf=ci*(1+(tdi/100*nda))
print("Il capitale finale è pari a:" , cf)