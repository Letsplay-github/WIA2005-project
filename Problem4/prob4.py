# first part
import numpy as np
from fastdtw import fastdtw
from scipy.spatial.distance import euclidean

import librosa
from scipy.io.wavfile import WavFileWarning, read

# declare variables
VOJandT = 'Problem4/VoiceOver_J and T.wav'
VOmemohon = 'Problem4/VoiceOver_memohon.wav'
VOmaaf = 'Problem4/VoiceOver_maaf.wav'
JandTaudio = 'Problem4/JandT.wav'
memohonaudio = 'Problem4/memohon.wav'
maafaudio = 'Problem4/maaf.wav'

# use librosa library to have both RATE and DATA for each audio
VOJandTDATA, VOJandTRATE = librosa.load(VOJandT)
VOmemohonDATA, VOmemohonRATE = librosa.load(VOmemohon)
VOmaafDATA, VOmaafRATE = librosa.load(VOmaaf)
JandTaudioDATA, JandTaudioRATE = librosa.load(JandTaudio)
memohonaudioDATA, memohonRATE = librosa.load(memohonaudio)
maafaudioDATA, maafRATE = librosa.load(maafaudio)

# print("Rate of test audio'J&T':" + str(JandTaudioRATE) +
#       ", Original: " + str(VOJandTRATE))
# print ((maafRATE))

# print(fastdtw(data1, data2)[0])
# print(fastdtw(data1, data3)[0])

print("Shortest path for VoiceOver J&T: ")
print("with J&T: " + str(fastdtw(VOJandTDATA, JandTaudioDATA)[0]) + " and the Cost matrix is: " + str(len(VOJandTDATA)*len(JandTaudioDATA)))
print("with memohon: " + str(fastdtw(VOJandTDATA, memohonaudioDATA)[0]) + " and the Cost matrix is: " + str(len(VOJandTDATA)*len(memohonaudioDATA)))
print("with maaf: " + str(fastdtw(VOJandTDATA, maafaudioDATA)[0])  + " and the Cost matrix is: " + str(len(VOJandTDATA)*len(maafaudioDATA)))
print()
print("Shortest path for VoiceOver memohon: ")
print("with J&T: " + str(fastdtw(VOmemohonDATA, JandTaudioDATA)[0]))
print("with memohon: " + str(fastdtw(VOmemohonDATA, memohonaudioDATA)[0]))
print("with maaf: " + str(fastdtw(VOmemohonDATA, maafaudioDATA)[0]))
print()
print("Shortest path for VoiceOver maaf: ")
print("with J&T: " + str(fastdtw(VOmaafDATA, JandTaudioDATA)[0]))
print("with memohon: " + str(fastdtw(VOmaafDATA, memohonaudioDATA)[0]))
print("with maaf: " + str(fastdtw(VOmaafDATA, maafaudioDATA)[0]))