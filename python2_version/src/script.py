from explore import *
import os
from extraction import *
import json



ai2_path = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
print('ai2 :' + ai2_path)
root = os.path.abspath(os.path.join(ai2_path, os.pardir))

xml_path = ai2_path + "/data/xml/"
abs_json_path = ai2_path + "/data/json_abs/"
txt_path = ai2_path + "/data/txt/"
path = ai2_path + "/data/"

d ={}

for abstract in os.listdir(abs_json_path)[2:3] :
    if abstract.endswith(".json") :
        print(abstract)
        json_file = json.load(open(abs_json_path+abstract))
        for sentence in json_file :
            for frame in sentence["frames"] :
                print(extract_text(frame)) 
        print(count_frames(abs_json_path+abstract))


