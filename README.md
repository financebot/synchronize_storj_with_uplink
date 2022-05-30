# synchronize_storj_with_uplink
<br />
#documentation
<br />


This  script synchronizes local directory with storj directory with uplink
<br />
It does not add or remove any file from the local  directory
<br />
It  does not  remove any file from the remote directory .
<br />
It just copies new files from local directory to remote storj directory
<br />
It just check filename and filepath, not file size or file date creation 
<br />


#example
<br />
python3 ./synchronize_storj.py --local_dir /dir6565/dir773  --remote_dir sj://bucket_845/dir747/dir747 --mode_test_or_real real --show_new_files_yes_or_not not
