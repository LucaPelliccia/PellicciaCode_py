larg=500                                                                #larghezza disegno
altz=500                                                                #altezza disegno
img=createImage(larg,altz,RGB)                                         
img.loadPixels()                                                     
lineaf=0                                                                #linea alla fine
numquadrati=0                                                           #numero dei quadrati all'interno della stessa riga
 
def setup():
    size(larg,altz)                                                     
    creazionefigura()                                                           
        
def creazionefigura():
    global pospix,y,x,larg,altz,lineaf,numquadrati,k
    input=createInput("Input")                                           #apre il file 
    content=""                                       
    pospix=0                                                             #indica la posizione del pixel
    while numquadrati<=10:                                               #ciclo che impone il limite di 10 quadrati per riga
        decfrz1 = input.read()                                           #decifrazione valore 1
        decfrz2 = input.read()                                           #decifrazione valore 2
        decfrz3 = input.read()                                           #decifrazione valore 3
        if decfrz2==-1:                                                  #controlli per vedere se ci sono vuoti
            decfrz2=255                                                    
        if decfrz3==-1:                                                    
            decfrz3=255                                                    
        if decfrz1==-1:                                                    
            if numquadrati==0:
                break
            else:
                for k in range (10-numquadrati):
                    for x in range (50):
                        for y in range (50):
                            img.pixels[pospix+y+(larg*x)]=color(0,0,0)        #colora il pixel di nero
                            lineaf=1
        else:                                                            #crea il quadrato con le componenti rgb rispettive ai valori ricavati dai 3 caratteri
            numquadrati+=1
            for x in range (50):
                for y in range (50):
                    img.pixels[pospix+y+(larg*x)]=color(decfrz1,decfrz2,decfrz3)        #colora pixel
        pospix=pospix+50                                                                #spostamento di un quadrato
        if(pospix%larg==0):
            pospix=pospix+larg*49                                                       
            numquadrati=0                                                             #azzera l'indice del numero dei quadrati
            if lineaf==1:                                                       
                break
    img.updatePixels()                                                        #aggiorna i pixels
    image(img,0,0)                                                            #stampa la figura
    save("Mistery.tiff")                                                      #salva
    
