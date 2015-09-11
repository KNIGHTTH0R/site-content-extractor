__author__ = 'akhil'

import os
import argparse
from InputReader import InputReader
from FileProcessor import FileProcessor
from HTMLParser import HTMLParser
from nltk.tokenize import word_tokenize
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
    file = open(OUTPUT_PATH+filename, 'w', encoding='utf-8')
    for entry in content:
        tokens = word_tokenize(entry)
        for token in tokens:
            file.write(token + "\n")

    file.close()


def main():

    inputReader = InputReader(BASE_PATH)
    while inputReader.hasNextFile():
        fileName = inputReader.getNextFile()
        fileProcessor = FileProcessor(BASE_PATH, fileName)
        fileContent = fileProcessor._getFileContent()

        htmlParser = HTMLParser(fileContent)

        tagContent = htmlParser.getContentFromTags(args.tags)
        writeToFile(fileName, tagContent)

main()