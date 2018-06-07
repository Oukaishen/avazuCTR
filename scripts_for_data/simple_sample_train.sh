#!/bin/bash

# This scripts is to extract 100M lines from the raw train data.
train_path=~/git_storage/avazuCTR/raw_data/train

subsampled_data_path=~/git_storage/avazuCTR/subsampled_data/simple_train_100m

# create the file if it does not exist
touch -a $subsampled_data_path

# do the cmd but this will contain the header
# (head -n 500000 $train_path && tail -n 500000 $train_path) > $subsampled_data_path


#revise version
tail -n +2 $train_path | head -n 500000 > $subsampled_data_path
tail -n 500000 $train_path >> $subsampled_data_path