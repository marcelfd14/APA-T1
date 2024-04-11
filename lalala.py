""" 
Sonia Sahuquillo Guillén
Marcel Farelo de la Orden

 EXERCICI 1 

""" 

import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf
T= 2.5  
fm=8000
fx=440
A=4
pi=np.pi
L=int(fm*T)
Tm=1/fm
t=Tm*np.arange(L)
x=A*np.cos(2*pi*fx*t)
sf.write('so_exemple2.wav',x,fm)

Tx=1/fx                                   # Període del senyal
Ls=int(fm*5*Tx)                           # Nombre de mostres corresponents a 5 períodes de la sinusoide

plt.figure(0)                             # Nova figura
plt.plot(t[0:Ls], x[0:Ls])                # Representació del senyal en funció del temps
plt.xlabel('t en segons')                 # Etiqueta eix temporal
plt.title('5 periodes de la sinusoide')   # Títol del gràfic
plt.show()                                # Visualització de l'objecte gràfic. 



import sounddevice as sd      # Importem el mòdul sounddevice per accedir a la tarja de so
sd.play(x, fm)                # Reproducció d'àudio

from numpy.fft import fft     # Importem la funció fft
N=5000                        # Dimensió de la transformada discreta
X=fft(x[0 : Ls], N)           # Càlcul de la transformada de 5 períodes de la sinusoide

k=np.arange(N)                        # Vector amb els valors 0≤  k<N

plt.figure(1)                         # Nova figura
plt.subplot(211)                      # Espai per representar el mòdul
plt.plot(k,abs(X))                    # Representació del mòdul de la transformada
plt.title(f'Transformada del senyal de Ls={Ls} mostres amb DFT de N={N}')   # Etiqueta del títol
plt.ylabel('|X[k]|')                  # Etiqueta de mòdul
plt.subplot(212)                      # Espai per representar la fase
plt.plot(k,np.unwrap(np.angle(X)))    # Representació de la fase de la transformad, desenroscada
plt.xlabel('Index k')                 # Etiqueta de l'eix d'abscisses 
plt.ylabel('$\phi_x[k]$')             # Etiqueta de la fase en Latex
plt.show()

"""
 EXERCICI 2
""" 
x_r, fm = sf.read('so_exemple2.wav')


plt.figure(2)                             # Nova figura
plt.plot(t[0:Ls], x_r[0:Ls])              # Representació del senyal en funció del temps
plt.xlabel('t en segons')                 # Etiqueta eix temporal
plt.title('5 periodes de la sinusoide')   # Títol del gràfic
plt.show() 

N=5000                     # Dimensió de la transformada discreta
X=fft(x_r[0 : Ls], N)      # Càlcul de la transformada de 5 períodes de la sinusoide

k=np.arange(N)                        # Vector amb els valors 0≤  k<N

plt.figure(3)                         # Nova figura
plt.subplot(211)                      # Espai per representar el mòdul
plt.plot(k,abs(X))                    # Representació del mòdul de la transformada
plt.title(f'Transformada del senyal de Ls={Ls} mostres amb DFT de N={N}')   # Etiqueta del títol
plt.ylabel('|X[k]|')                  # Etiqueta de mòdul
plt.subplot(212)                      # Espai per representar la fase
plt.plot(k,np.unwrap(np.angle(X)))    # Representació de la fase de la transformad, desenroscada
plt.xlabel('Index k')                 # Etiqueta de l'eix d'abscisses 
plt.ylabel('$\phi_x[k]$')             # Etiqueta de la fase en Latex
plt.show()

"""
# EXERCICI 3
"""
T= 2.5  
fm=8000
fx=440
A=4
pi=np.pi
L=int(fm*T)
Tm=1/fm
t=Tm*np.arange(L)
x=A*np.cos(2*pi*fx*t)
N=5000                        # Dimensió de la transformada discreta
X=fft(x[0 : Ls], N)           # Càlcul de la transformada de 5 períodes de la sinusoide
k=np.arange(N)

plt.figure(4)  

Y_dB = 20*np.log10(np.abs(X)/(max(np.abs(X))))   # Fórmula que ens proporciona l'enunciat
X_fk = (k/N) * fm  #    de 0 a fm/2 ho aplicarem al mostrar-la
plt.subplot(211)
plt.plot(X_fk[0:int(fm/2)],Y_dB[0:int(fm/2)])   # si no posem el int --> slice indices must be integers or None or have an __index__ method
plt.title(f'Transformada del senyal de Ls={Ls} mostres amb DFT de N={N}')   # Etiqueta del títol 
plt.ylabel('dB')
plt.subplot(212)
plt.plot(X_fk[0:int(fm/2)],np.unwrap(np.angle(X[0:int(fm/2)])) )
plt.xlabel('Hz')    
plt.ylabel('$\phi_x[k]$')    
plt.show()

# Busquem fx:
espectre = plt.magnitude_spectrum(x, fm) 
fx = espectre[1][np.argmax(espectre[0])] 
print(f'Freqüència del senyal: {fx} Hz')

# Busquem amplitud
Amp = 10**int(max(Y_dB)/20)
print(f'Amplitud del senyal: {Amp}')


""" 
EXERCICI 4

 """
audiomono,fm = sf.read('/Users/marcelf/Desktop/APA/P1/directwave-instrument-pack-demo-a.wav') 

T= 0.025 # l'enunciat ens diu que seleccionem només 25ms
L=int(fm*T) # 25 ms equivalen a L mostres
Tm=1/fm 
t=Tm*np.arange(L)
plt.figure(5)  
plt.plot(t[0:L],audiomono[0:L])
plt.title(f'25 ms de la cançó')   # Etiqueta del títol 
plt.ylabel('amplitud')
plt.xlabel('temps en segons')      
plt.show()

print(f'Freqüència de mostratge de la cançó: {fm}')
print(f'Nombre de mostres del senyal: {L}')

# copiem el mateix codi del ex3
X=fft(audiomono[0 : L], N)          
k=np.arange(N)
plt.figure(6)  
Y_dB = 20*np.log10(np.abs(X)/(max(np.abs(X))))   # Fórmula que ens proporciona l'enunciat
X_fk = (k/N) * fm  #    de 0 a fm/2 ho aplicarem al mostrar-la
plt.subplot(211)
plt.plot(X_fk[0:int(fm/2)],Y_dB[0:int(fm/2)])   # si no posem el int --> slice indices must be integers or None or have an __index__ method
plt.title(f'Transformada del senyal de Ls={L} mostres amb DFT de N={N}')   # Etiqueta del títol 
plt.ylabel('dB')
plt.subplot(212)
plt.plot(X_fk[0:int(fm/2)],np.unwrap(np.angle(X[0:int(fm/2)])) )
plt.xlabel('Hz')    
plt.ylabel('$\phi_x[k]$')    
plt.show()