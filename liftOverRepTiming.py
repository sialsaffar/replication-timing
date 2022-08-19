#!/usr/bin/env python

"""
Script to lift over coordinates between two ref builds using UCSC
liftOver tool.
"""

import argparse
from liftover import get_lifter


if __name__=='__main__':
    parser = argparse.ArgumentParser(description='Takes 4 arguments')
    parser.add_argument('-i', '--input', required=True, help='input file with chromosome numbers as the 1st column and positions as the 2nd column')
    parser.add_argument('-o', '--output', required=True, help='Name for the output file')
    parser.add_argument('--frombuild', required=True, help='Version of the build we are lifting from')
    parser.add_argument('--tobuild', required=True, help='Version of the build we want')

    args = parser.parse_args()

    converter = get_lifter(args.frombuild, args.tobuild)
    with open(args.input, 'r') as infile, open(args.output, 'wt') as outfile:
        for line in infile:
            line = line.lstrip().split('\t')
            x = converter[int(line[0])][int(line[1])]
            outfile.write(f"{x[0][0]}\t{x[0][1]}\t{line[2]}")

