


img = loadImage("out.tiff")                   #carico l'immagine 
image(img, 0, 0)                              #la posiziono

loadPixels()                                  #funzione che converte la matrice img in vett di pixels


frase=[]                                      #dichiaro la lista frase
lato_pixel=50                                 #dichiaro la lunghezza del lato pixel
lato_img=500                                  #dichiaro la lunghezza del lato dell'immagine
size(500,500)


i=49                                          #metto l'indice del vettore a 49 perchè la matroce parte da 0
while pixels[i] != color(204,204,204):        #il ciclo continua finche non incontra il grigio di default del background
    if pixels[i] != color(204,204,204):
        r=int(red(pixels[i]))                 #carico in r il numero del rosso
    if pixels[i] != color(204,204,204):
        g=int(green(pixels[i]))               #carico in g il numero del verde
    if pixels[i] != color(204,204,204):
        b=int(blue(pixels[i]))                #carico in b il numero del blu
    if pixels[i] != color(204,204,204):
        i=i+lato_pixel                        #incremento i di 50 per passare al pixel successivo
    if(i%(lato_img-1)==0):                    #se l'indice é arrivato al bordo destro dell'immagine lo incremeto per endare ai pixel inferiori
        i=i+(lato_img*(lato_pixel-1))
    frase.append(chr(r))                      #aggiungo alla lista frase i numeri convertiti in lettere
    frase.append(chr(g))
    frase.append(chr(b))

stringa=""
for ele in frase:                             #converto la lista in una stringa e la stampo
    stringa += ele
print stringa
