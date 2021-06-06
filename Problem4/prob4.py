# first part
import numpy as np
from fastdtw import fastdtw
from scipy.spatial.distance import euclidean

import librosa
from scipy.io.wavfile import WavFileWarning, read



# def dtw(s, t):
#     y, x = len(s), len(t)
#     dtw_matrix = np.zeros((y+1, x+1))
#     # np.zerosReturn a new array of given shape and type, filled with zeros.

#     for yindex in range(y+1):
#         for xindex in range(x+1):
#             dtw_matrix[yindex, xindex] = np.inf
#     dtw_matrix[0, 0] = 0

#     for yindex in range(1, y+1):
#         for xindex in range(1, x+1):
#             cost = abs(s[yindex-1] - t[xindex-1])

#             last_min = np.min(
#                 [dtw_matrix[yindex-1, xindex],
#                  dtw_matrix[yindex, xindex-1],
#                  dtw_matrix[yindex-1, xindex-1]])

#             dtw_matrix[yindex, xindex] = cost + last_min

#     dtw_matrix = np.delete(dtw_matrix, 0, 0)
#     dtw_matrix = np.delete(dtw_matrix, 0, 1)
#     return dtw_matrix


# a = [1, 2, 3, 3, 5]
# b = [1, 2, 3, 3, 5, 2, 2, 4, 6, 8]
# print(a)
# print(b)
# print(dtw(a,b))

# # using fastdtw library
# distance, path = fastdtw(a, b, dist=euclidean)
# print(distance)
# print(path)

# --------------------------------------------------------


VOJandT = 'Problem4/VoiceOver_J and T.wav'
VOmemohon = 'Problem4/VoiceOver_memohon.wav'
VOmaaf = 'Problem4/VoiceOver_maaf.wav'
JandTaudio = 'Problem4/JandT.wav'
memohonaudio = 'Problem4/memohon.wav'
maafaudio = 'Problem4/maaf.wav'

# JandTaudioRATE, JandTaudioDATA = read(JandTaudio)
# VOJandTRATE, VOJandTDATA= read(VOJandT)
# memohonRATE, memohonaudioDATA = read(memohonaudio)

VOJandTDATA, VOJandTRATE = librosa.load(VOJandT)
VOmemohonDATA, VOmemohonRATE = librosa.load(VOmemohon)
VOmaafDATA, VOmaafRATE = librosa.load(VOmaaf)
JandTaudioDATA, JandTaudioRATE = librosa.load(JandTaudio)
memohonaudioDATA, memohonRATE = librosa.load(memohonaudio)
maafaudioDATA, maafRATE = librosa.load(maafaudio)

print("Rate of test audio'J&T':" + str(JandTaudioRATE) +
      ", Original: " + str(VOJandTRATE))

# data1 = np.amax(VOJandTDATA, axis=1)
# data2 = np.amax(JandTaudioDATA, axis=1)
# data3 = np.amax(memohonaudioDATA, axis=1)

# print(fastdtw(data1, data2)[0])
# print(fastdtw(data1, data3)[0])
print(fastdtw(VOJandTDATA, JandTaudioDATA)[0])
print(fastdtw(VOJandTDATA, memohonaudioDATA)[0])
print(fastdtw(VOJandTDATA, maafaudioDATA)[0])
print()
print(fastdtw(VOmemohonDATA, JandTaudioDATA)[0])
print(fastdtw(VOmemohonDATA, memohonaudioDATA)[0])
print(fastdtw(VOmemohonDATA, maafaudioDATA)[0])
print()
print(fastdtw(VOmaafDATA, JandTaudioDATA)[0])
print(fastdtw(VOmaafDATA, memohonaudioDATA)[0])
print(fastdtw(VOmaafDATA, maafaudioDATA)[0])
