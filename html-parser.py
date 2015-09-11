__author__ = 'akhil'

import os
import argparse
from InputReader import InputReader
from FileReader import FileReader
from HTMLParser import HTMLParser
import nltk.data

# initialize argument parser
parser = argparse.ArgumentParser()
parser.add_argument('--input', '-i', default=os.getcwd() + '/../data', help='absolute path of input directory')
parser.add_argument('--tags', '-t', nargs=3, action='append', help='tags in the form of "tagname attributename value"')
parser.add_argument('--output', '-o', default=os.getcwd() + '/../htmlparsed', help='absolute path of output directory')
args = parser.parse_args()

BASE_PATH = args.input
OUTPUT_PATH = args.output + '/'

def writeToFile(filename, content):
    if not content:
        return
    sent_detector = nltk.data.load('tokenizers/punkt/english.pickle')
    file = open(OUTPUT_PATH+filename, 'w', encoding='utf-8')
    for entry in content:
        file.write("\n".join(sent_detector.tokenize(entry.strip())))
        file.write('\n')
    file.close()


def main():

    inputReader = InputReader(BASE_PATH)
    while inputReader.hasNextFile():
        fileName = inputReader.getNextFile()
        fileProcessor = FileReader(BASE_PATH, fileName)
        fileContent = fileProcessor._getFileContent()

        htmlParser = HTMLParser(fileContent)

        tagContent = htmlParser.getContentFromTags(args.tags)
        writeToFile(fileName, tagContent)
main()