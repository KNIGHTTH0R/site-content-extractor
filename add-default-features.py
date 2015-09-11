__author__ = 'akhil'

import os
import argparse
import nltk
import nltk.data
from InputReader import InputReader
from FileReader import FileReader
from FileWriter import FileWriter
from nltk.tokenize import word_tokenize

# initialize argument parser
parser = argparse.ArgumentParser()
parser.add_argument('--input', '-i', default=os.getcwd() + '/../htmlparsed', help='absolute path of input directory')
parser.add_argument('--output', '-o', default=os.getcwd() + '/../htmlparsed', help='absolute path of output directory')
args = parser.parse_args()

INPUT_PATH = args.input
OUTPUT_PATH = args.output

def getSentences(content):
    sent_detector = nltk.data.load('tokenizers/punkt/english.pickle')
    sentences = sent_detector.tokenize(content.strip())
    sentences = list(filter(lambda x: not x == '\n', sentences))
    return sentences

def writeFeaturesToFile(sentence, filename):
    fileWriter = FileWriter(OUTPUT_PATH, filename)
    tagged = nltk.pos_tag(word_tokenize(sentence))
    for i in range(len(tagged)):
        feature = 'I\tcw={} ct={}'.format(tagged[i][0], tagged[i][1])
        if i == 0:
            feature = feature + ' pw=BOS pt=BOS'
        else:
            feature = feature + ' pw={} pt={}'.format(tagged[i-1][0], tagged[i-1][1])
        if i == len(tagged)-1:
            feature = feature + ' nw=EOS nt=EOS'
        else:
            feature = feature + ' nw={} nt={}'.format(tagged[i+1][0], tagged[i+1][1])

        fileWriter.writeToFile(feature)
    fileWriter.writeToFile("\n")

    print(tagged)

def main():

    inputReader = InputReader(INPUT_PATH)
    while inputReader.hasNextFile():
        fileName = inputReader.getNextFile()
        fileProcessor = FileReader(INPUT_PATH, fileName)
        fileContent = fileProcessor._getFileContent()

        sentences = getSentences(fileContent)
        for sentence in sentences:
            writeFeaturesToFile(sentence, fileName)

        break
main()