#!/usr/bin/python3
import sys

# Loop starting from 1 to skip the script name (sys.argv[0])
for i in range(1, len(sys.argv)):
    print(sys.argv[i])  # Print each argument passed to the script

