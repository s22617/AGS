import huffman
from bitstring import BitArray

if __name__ == "__main__":
    pathToInputFile = "input.txt"
    pathToOutputFile = "output"
    file = open(pathToInputFile, "r")

    inputText = file.read()
    countedLetters = huffman.countLetters(inputText)
    huffmanCodes = huffman.huffmanTree(countedLetters)
    file.close()

    file = open(pathToOutputFile + ".bin", "w")

    for code in huffmanCodes:
        file.write(code + ": " + huffmanCodes[code] + "\n")
    file.write("\n")
    file.close()

    message = BitArray(bin = huffman.encrypt(inputText, huffmanCodes))
    file = open(pathToOutputFile + ".bin", "ab")
    message.tofile(file)
    file.close()
