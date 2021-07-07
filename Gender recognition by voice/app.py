import numpy as np
import scipy.io.wavfile
import scipy.signal
import scipy.fft
import sys
import warnings

warnings.filterwarnings('ignore')


w, array = scipy.io.wavfile.read(sys.argv[1])


#if there are two channels, take only the first one
if(isinstance(array[0],np.ndarray)): array = [s[0] for s in array]


n=len(array)

signalKaiser=array*np.kaiser(len(array),100)
signalKaiser_fft=np.abs(scipy.fft.fft(signalKaiser))

freqs = np.arange(len(array))/(len(array)/w)

for i in range(len(signalKaiser_fft)):
    if(freqs[i]<80): signalKaiser_fft[i]=0

hps=np.copy(signalKaiser_fft)

for i in np.arange(2,6):
    d=scipy.signal.decimate(signalKaiser_fft,int(i))
    hps[:len(d)]*=d


maximum=max(hps)
res=[]
for i in range(len(hps)):
    if maximum==hps[i]: 
        res.append(freqs[i])
        break

sex=''
if(res[0]<170):sex='M'
else: sex='K'

print(sex,end='')