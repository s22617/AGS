import numpy

def countLetters(input):
    countedLetters = {}
    for letter in input:
        if (letter in countedLetters):
            countedLetters[letter] = countedLetters.get(letter) + 1
        else:
            countedLetters[letter] = 1
    return countedLetters

def buildMinHeap(A):
    for i in range(int(len(A)//2 - 1), -1, -1):
        minHeapify(A, len(A), i)

def minHeapify(A, n, i):
    l = 2 * i + 1
    r = 2 * i + 2

    if (l < n and A[l][1] < A[i][1]):
        smallest = l
    else:
        smallest = i
    if (r < n and A[r][1] < A[smallest][1]):
        smallest = r
    if smallest != i:
        A[i], A[smallest] = A[smallest], A[i]
        minHeapify(A, n, smallest)

def huffmanTree(countedLetters):
    priorityQueueNumpy = []
    priorityQueue = []
    for x in countedLetters.items():
        priorityQueueNumpy.append(numpy.asarray(x))
    for i in priorityQueueNumpy:
        priorityQueue.append([i[0], int(i[1])])

    buildMinHeap(priorityQueue)
    huffTree = {}
    huffCodes = {}
    while len(priorityQueue) > 1:
        x = priorityQueue.pop(0)
        y = priorityQueue.pop(0)

        newString, newPriorityValue = x[0] + y[0], int(x[1]) + int(y[1])

        huffTree[newString] = [x[0], y[0]]
        #print("Huffman Tree: ", huffTree)
        priorityQueue.append([newString, newPriorityValue])
        #print("Priority Queue: ", priorityQueue)

        buildMinHeap(priorityQueue)

    for i in countedLetters.keys():
        for j in huffTree.values():
            previousCode = huffCodes.get(i, "")
            if i in j[0]:
                huffCodes[i] = "0" + previousCode
            elif i in j[1]:
                huffCodes[i] = "1" + previousCode

    return huffCodes

def get_key(val, dictionary):
    for key, value in dictionary.items():
         if val == value:
             return key
 
    return "key doesn't exist"

def decrypt(text, codes):
    text = list(text)
    tmp = ""
    decodedText = ""
    for i in range(len(text)):
        tmp += text[i]
        if tmp in codes.values():
            decodedText += get_key(tmp, codes)
            tmp = ""

    return decodedText

def encrypt(text, codes):
    encrypted = ""
    text = list(text)
    for i in range(len(text)):
        if text[i] in codes.keys():
            encrypted += codes[text[i]]
    return encrypted

# text = "Ala ma kota"
# countedLetters = countLetters(text)
# print(huffmanTree(test))
# print(decrypt("00000101101100011011110110111101", huffmanTree(countedLetters)))
# print(encrypt("Ala ma kota", huffmanTree(countedLetters)))