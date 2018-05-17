from preprocess import preprocess, remove_empty_lines
import os

xml_path = "../data/A00_xml/"
txt_path = "../data/A00_txt/"



for filename in os.listdir(xml_path):
    preprocess(xml_path + filename, txt_path + filename[:-4] + ".txt" )
    remove_empty_lines(txt_path + filename[:-4] + ".txt")
