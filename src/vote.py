from extraction import *
from explore import *
import os


def readFile(filename):
    filehandle = open(filename).read
    filehandle.close()

counts = readFile("../data/frames_counts.txt")

name = input("Please enter your name ")

# Using path.join to ensure it can be used across all operating systems and platforms.
filename = os.path.join("../data/output_" + name + ".txt")

output = open(filename, 'w+')

i = 1

for line in counts.split('\n')[:100] :
    frame_name = line.split('\'')[1]
    frame_count = str(line.split('\'')[0][1:-2])
    print("frame " + str(i) + '/100')
    print(frame_name)
    (display_frame_instances(frame_name))
    response = input("Is that frame relevant ? (y or n, then enter)")
    output.write(response)
    output.write('\n')
    print('\n')
    print('\n')
    print('\n')
    print('\n')
    print('\n')
    print('\n')
    print('\n')
    i += 1

output.close()

print("Tak !")
