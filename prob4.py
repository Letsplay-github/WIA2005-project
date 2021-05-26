import numpy as np
import os
import librosa
from fastdtw import fastdtw
from scipy.spatial.distance import euclidean
from scipy.io.wavfile import WavFileWarning, read
# **np.zeros
# **Return a new array of given shape and type, filled with zeros.


def dtw(s, t):
    y, x = len(s), len(t)
    dtw_matrix = np.zeros((y+1, x+1))
    for yindex in range(y+1):
        for xindex in range(x+1):
            dtw_matrix[yindex, xindex] = np.inf
    dtw_matrix[0, 0] = 0

    for yindex in range(1, y+1):
        for xindex in range(1, x+1):
            cost = abs(s[yindex-1] - t[xindex-1])

            last_min = np.min(
                [dtw_matrix[yindex-1, xindex],
                 dtw_matrix[yindex, xindex-1],
                 dtw_matrix[yindex-1, xindex-1]])

            dtw_matrix[yindex, xindex] = cost + last_min

    dtw_matrix = np.delete(dtw_matrix, 0, 0)
    dtw_matrix = np.delete(dtw_matrix, 0, 1)
    return dtw_matrix


# a = [1, 2, 3, 3, 5]
# b = [1, 2, 3, 3, 5, 2, 2, 4, 6, 8]
# print(a)
# print(b)

VOJandT = 'VoiceOver_J and T.wav'
VOmemohon = 'VoiceOver_memohon.wav'
VOmaaf = 'VoiceOver_maaf.wav'
JandTaudio = 'JandT.wav'
memohonaudio = 'memohon.wav'
maafaudio = 'maaf.wav'

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




# distance, path = fastdtw(a, b, dist=euclidean)

# print(distance)
# print(path)


# def dtwwithwindow(s, t, window):
#     n, m = len(s), len(t)
#     w = np.max([window, abs(n-m)])
#     dtw_matrix = np.zeros((n+1, m+1))

#     for i in range(n+1):
#         for j in range(m+1):
#             dtw_matrix[i, j] = np.inf
#     dtw_matrix[0, 0] = 0

#     for i in range(1, n+1):
#         for j in range(np.max([1, i-w]), np.min([m, i+w])+1):
#             dtw_matrix[i, j] = 0

#     for i in range(1, n+1):
#         for j in range(np.max([1, i-w]), np.min([m, i+w])+1):
#             cost = abs(s[i-1] - t[j-1])
#             # take last min from a square box
#             last_min = np.min(
#                 [dtw_matrix[i-1, j], dtw_matrix[i, j-1], dtw_matrix[i-1, j-1]])
#             dtw_matrix[i, j] = cost + last_min
#     return dtw_matrix


# c = [1, 2, 3, 3, 5]
# d = [1, 2, 2, 2, 2, 2, 2, 4]
# print(dtwwithwindow(c, d, 3))
