# synchronize_storj_with_uplink
#documentation


This  script synchronizes local directory with storj directory with uplink
It does not add or remove any file from the local  directory
It  does not  remove any file from the remote directory .
It just copies new files from local directory to remote storj directory
It just check filename and filepath, not file size or file date creation 


#example
python3 ./synchronize_storj.py --local_dir ./rootdir002  --remote_dir sj://rootdir001 --mode_test_or_real real --show_new_files_yes_or_not not
