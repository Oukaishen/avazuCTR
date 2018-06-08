"""
This file is designed for sample the raw_data when the raw_data is too large.
The sample method is random.

@params
path : raw_data's path
sample_size : how many lines you want to sample
has_header : whether the raw_data has header

return:
nothing; the output file is here: /Users/kaishen/git_storage/avazuCTR/subsampled_data/random_subsample100m


"""


import random
random.seed(42)
import 	sys
from datetime import datetime


def random_subsample(path, sample_size = 10, has_header = False):

	t1 =  datetime.now()
	# first we calculate totally how many line are there in the input
	with open(path, "r") as f:
		for linecount, line in enumerate(f):
			if linecount == 0 and has_header:
				header = line
	if has_header:
		linecount -= 1	
	t2 = datetime.now()
	print("File has Header: {}, the header is {}".format(has_header,header))
	print("Time for counting lines is {} .".format(t2 - t1 ))
	print("Totally there are {} lines in the original file. ".format(linecount))


	t1 =  datetime.now()

	output_path = "/Users/kaishen/git_storage/avazuCTR/subsampled_data/random_subsample100m"
	random_list = random.sample(range(linecount), sample_size)
	random_list.sort()
	if has_header:
		random_list = [ x+1 for x in random_list]

	with open(output_path, "w+") as fout:
		with open(path,"r") as fin:
			temp = 0;
			for linecount_, line in enumerate(fin):
				if linecount_ == random_list[temp]:
					temp += 1
					fout.write(line)
				if temp >= sample_size:
					break
	t2 = datetime.now()
	print("Time for generating subsampled_data is {} .".format(t2 - t1 ))



if __name__ == "__main__":
	random_subsample(sys.argv[1], int(sys.argv[2]), sys.argv[3])