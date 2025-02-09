import cc_dat_utils

#Part 1
# input_dat_file = "data/pfgd_test.dat"
input_dat_file = "chips_tools\data\pfgd_test.dat"



#Use cc_dat_utils.make_cc_level_pack_from_dat() to load the file specified by input_dat_file
#print the resulting data

# load level
levelPack = cc_dat_utils.make_cc_level_pack_from_dat(input_dat_file)

# print output
output = str(levelPack)
print(output)

