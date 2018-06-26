from extraction import *
from explore import *
import os

counts = open("../data/frames_counts.txt").read()

os.system('cls||clear')
name = input("Please enter your name ")

# Using path.join to ensure it can be used across all operating systems and platforms.
output_name = os.path.join("../data/output_" + name + ".txt")

output_file = open(output_name, 'w+')

i = 1

for line in counts.split('\n')[:100] :
    frame_name = line.split('\'')[1]
    frame_count = str(line.split('\'')[0][1:-2])
    print("frame " + str(i) + '/100')
    print(frame_name)
    display_frame_instances(frame_name)
    response = input("Is that frame relevant ? (y or n, then enter)")
<<<<<<< HEAD
    output.write(frame_name + " : " + response)
    # output.write(response)
    output.write('\n')
    print('\n')
    print('\n')
    print('\n')
    print('\n')
    print('\n')
    print('\n')
    print('\n')
=======
    output_file.write(response)
    output_file.write('\n')
    os.system('cls||clear')
>>>>>>> 50935468bc51dde72ee9e539ddcc5a35e6ceaf6b
    i += 1

output_file.close()

print("Tak !")
