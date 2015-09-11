__author__ = 'akhil'

import os
import argparse

# initialize argument parser
parser = argparse.ArgumentParser()
parser.add_argument('--input', '-i', default=os.getcwd() + '/../htmlparsed', help='absolute path of input directory')
parser.add_argument('--tags', '-t', nargs=3, action='append', help='tags in the form of "tagname attributename value"')
parser.add_argument('--output', '-o', default=os.getcwd() + '/../htmlparsed', help='absolute path of output directory')
args = parser.parse_args()