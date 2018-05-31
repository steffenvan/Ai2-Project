from preprocess import *
import os

def convert(xml_file, txt_file) :
    preprocess(xml_file, txt_file)
    remove_empty_lines(txt_file)
    one_sentence_per_line(txt_file)
