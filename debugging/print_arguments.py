#!/usr/bin/python3
import sys

# Start the loop from index 1 to exclude the script name
for i in range(1, len(sys.argv)):
    print(sys.argv[i])
