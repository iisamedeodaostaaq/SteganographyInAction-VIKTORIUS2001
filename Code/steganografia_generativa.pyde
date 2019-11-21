i=0                            #indice dell'array frase
p=0                            #indice dell'arrey pixels
lato_pixel=50                  #lunghezza lato di un pixel
grandezza_img=lato_pixel*10    #grandezza lato immagine


def setup():
    global frase,i,p,lato_pixel
    i=0
    frase=[]
    size(grandezza_img,grandezza_img)      #grandezza immagine
    frase = input('scrivi una frase')      
    disegna()

#Questa funzione faccio uscire la finestra di imput della frase
def input(message=''):
    from javax.swing import JOptionPane
    return JOptionPane.showInputDialog(frame, message)

#questa fnzione ha il compito di disegnarmi l'immagine
def disegna():
    global i,p,lato_pixel
    loadPixels()           #trasforma l'immagine in un array pixels

    while i < (len(frase)):      #il while scorre i caratteri della frase
        if (i<len(frase)):       #finchè non li avrà scorsi tutti
            r=ord(frase[i])
        else:
            r=255                #se un colore nn è presente si 
        if (i+1<len(frase)):     #caricherà al suo interno 255
            g=ord(frase[i+1])
        else:
            g=255
        if (i+2<len(frase)):
            b=ord(frase[i+2])
        else:
            b=255
        i=i+3
        cont=0
        for x in range(lato_pixel):             #x=colonne
            for y in range (lato_pixel):        #y=righe
                pixels[p+y+(grandezza_img*x)] = color(r, g, b)   #inserisco ad ogni pixel il suo colore
        p=p+lato_pixel                                           #ripeto questo operazione per 50 volte
        if(p%grandezza_img==0):                
            p=p+(grandezza_img*(lato_pixel-1))    #se l'indice del vettore pixel è maggire
        print r                                   #del lato pixel vado avanti di lato immaggine per lato pixel - 1
        print g
        print b
    updatePixels()                 #carico i pixels
    save("out.tiff")               #salvo l'immagine col nome out.tiffss

    
        
        
    
    
    
