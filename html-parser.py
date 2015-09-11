__author__ = 'akhil'

import os
import argparse
from InputReader import InputReader
from FileProcessor import FileProcessor
from HTMLParser import HTMLParser
from nltk.tokenize import word_tokenize
import nltk
# nltk.download()

# initialize argument parser
parser = argparse.ArgumentParser()
parser.add_argument('--input', '-i', default=os.getcwd() + '/../data', help='absolute path of input directory')
parser.add_argument('--tags', '-t', nargs=3, action='append', help='tags in the form of "tagname attributename value"')
parser.add_argument('--output', '-o', default=os.getcwd() + '/../htmlparsed', help='absolute path of output directory')
args = parser.parse_args()

BASE_PATH = args.input
OUTPUT_PATH = os.getcwd() + ''

def main():

    inputReader = InputReader(BASE_PATH)
    fileProcessor = FileProcessor(BASE_PATH, "")
    while inputReader.hasNextFile():
        fileProcessor.setFileName(inputReader.getNextFile())
        fileContent = fileProcessor._getFileContent()

        htmlParser = HTMLParser(fileContent)

        tagContent = htmlParser.getContentFromTags(args.tags)

        print(word_tokenize(tagContent[0]))
        print(tagContent)
        break

main()