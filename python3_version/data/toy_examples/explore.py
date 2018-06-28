import json

filename = "E09-1005-parscit.130908-11.49.59"

text_list = open(filename + '.txt', 'r').read().split("\n")

json_list = json.load(open(filename + '.json','r'))

neg_file = open(filename[:-16] + '.neg').read().split("\n")


sents = []
for line in neg_file :
    if line.startswith("1	") :
        sents.append(line)

for i in range(min(len(sents), len(text_list))) :
    print(sents[i])
    print(text_list[i])
    print("***********************")



# print(len(text_list))
# 
# print(len(json_list))

# number_of_frames = 0
# 
# for i in range(len(text_list)) :
#     print("************************************************************************************")
#     print(text_list[i])
#     print('\n')
#     number_of_frames += len(json_list[i]["frames"])
#     for elt in json_list[i]["frames"] :
#         print(elt)
#         print("\n")
#     print("************************************************************************************\n")
#     print("\n")
# 
# print("Total number of frames in the article : %d. Average number of frames per sentence : %d." %(number_of_frames,number_of_frames/len(text_list)))