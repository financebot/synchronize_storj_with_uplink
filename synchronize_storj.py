import os
import subprocess
import codecs  
import re
import argparse
import time


#PART1. INTRODUCTION
print('\n\n')



#tutorial. example. usage.
example1='python3 /home/user6565/synchronize_storj.py --local_dir /home/user6565/local_directory_67565  --remote_dir sj://remote_bucket_5643/directory_5665 --mode_test_or_real real --show_new_files_yes_or_not yes'



#define argument
parser = argparse.ArgumentParser(description='synchronize local directory with storj directory')
parser.add_argument('--local_dir', default="", required=True, type=str, help='--local_dir /homea/user545/directory_85686/')
parser.add_argument('--remote_dir', default="", required=True, type=str, help='--remote_dir sj://directory_543254')
parser.add_argument('--mode_test_or_real', default="real", required=True, type=str, help='--mode_test_or_real test--mode_test_or_real')
parser.add_argument('--show_new_files_yes_or_not', default="yes", required=True, type=str, help='--show_new_files_yes_or_not yes ')




#parse arguments
args = parser.parse_args()


#define utility variables
mode_test_or_real=args.mode_test_or_real
show_new_files_yes_or_not=args.show_new_files_yes_or_not




#define directory varibles
local_dir=os.path.abspath(args.local_dir)
remote_dir=args.remote_dir

print('local_dir: ', local_dir)
print('remote_dir:', remote_dir)
print('\n\n')



#in the case, ask to the user to remove last slash of the directory names
if local_dir[len(local_dir)-1]=='/': 
	print('please remove last slash character from the local dir name')
	os._exit(0)


#local_dir=local_dir[0:len(local_dir)-1] 
#print(local_dir)


if remote_dir[len(remote_dir)-1]=='/': 
	print('please remove last slash character from the remote dir name')
	os._exit(0)

#remote_dir=remote_dir[0:len(remote_dir)-1] 
#print(remote_dir)


#check if local_dir exist
local_dir_exist = os.path.isdir(local_dir) 
if local_dir_exist==False:  
	print(local_dir, ' does not exist')
	os._exit(0)



#check arguments
if show_new_files_yes_or_not!='yes' and show_new_files_yes_or_not!='not':
	print('the option show_new_files_yes_or_not accepts as values only: yes or not')
	print('current show_new_files_yes_or_not: ', show_new_files_yes_or_not)
	print('\n\n')
	print('Example: ')
	print(example1)
	os._exit(1)





if mode_test_or_real!='test' and mode_test_or_real!='real':
	print('the option mode_test_or_real accepts as values only: test or real')
	print('current option mode_test_or_real: ', mode_test_or_real)
	print('\n\n')
	print('Example: ')
	print(example1)
	os._exit(1)



#show_new_files_yes_or_not
#os._exit(0)


#PART2 REMOTE FILES
#get all files infos from the storj servers
#equivalent bash command: "uplink ls -r sj://directory_23334
#process = subprocess.Popen(["uplink", "ls", "-r", args.remote_dir], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
process = subprocess.Popen(["uplink", "ls", "-r", args.remote_dir], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#os._exit(0)


#copy the output and the errors from the subprocess pipe
process_communicate=process.communicate()

#print(process_communicate[0])
#print(process_communicate[1])


#copy output, this is the files list
list_files=''
list_files_2=''
if list_files!=None:
	list_files=process_communicate[0]
	list_files_2 = list_files.decode('UTF-8')
else:
	print('Files list from the server None')
	os._exit(1)




#handle error from the server
subprocess_error=process_communicate[1]
subprocess_error_2=''
if subprocess_error!=None:
        subprocess_error=process_communicate[1]
        subprocess_error_2 = subprocess_error.decode('UTF-8')



#print error message from server
print('\n\n')
if len(subprocess_error_2)>0:
	print('ERROR MESSAGE FROM SERVER')
	print(subprocess_error_2)
	os._exit(0)

#os._exit(0)
#print(list_files_2)


#parse server data
#split string on newline
#every line is the infos of one file on the server storj
list_files_3 = list_files_2.split("\n")

#print(list_files_3)



#get array which start with OBJ
#this is array with info about one file on the server storj
list_files_4=[]
for current_file in list_files_3:
	#print(current_file)
	current_file_2=current_file.split(" ")
	current_file_2_0=current_file_2[0]
	#print(current_file_v2_0)
	if current_file_2_0=='OBJ': 
		list_files_4.append(current_file)


#In the case, the storj server return a list with zero file
if len(list_files_4)==0:
	print('The storj server return a list with zero file. Maybe the remote directory is missing')
	print('If the remote directory is not missing, create at least one file inside it')
	print('remote_dir: ', remote_dir)
	os._exit(0)




#the file size  is a string with only number characters.
#search it, use it as marker, and extract the remote file path

#define regex which match numbers
num_regex="^\d+$"

#define same temporary variables
list_remote_files_5=[]
index_size=0
index_filepath_remote=0
flag1=True
flag2=True

for current_file in list_files_4:
	current_file_2=current_file.split(" ")
	index=-1
	index2=-1
	index_size=0
	index_filepath_remote=0
	flag1=True
	flag2=True
	for current_part in current_file_2:
		index=index+1
		number_check=False
		number_check=re.match(num_regex, current_part)
		#print(number_check)
		if number_check:
			if flag1==True:
				index_size=index
				flag1=False
			#print(index)
			#print(current_part)
			current_file_slice1=current_file_2[(index_size+1):len(current_file)]
			#print(current_file_slice1)
			for current_part_2 in current_file_slice1:
				index2=index2+1
				if current_part_2!='':
					if flag2==True:
						index_filepath_remote=index2
						#print(current_part_2)
						flag2=False
						current_filepath_remote=current_file_slice1[(index_filepath_remote):len(current_file_slice1)]
						current_filepath_remote_v2=' '.join(current_filepath_remote)
						#print(current_filepath_remote_v2)
						list_remote_files_5.append(current_filepath_remote_v2)


#print remote files path
#for current_filepath_remote_5 in list_remote_files_5:
#	print(current_filepath_remote_5)

#os._exit(0)




#PART3. LOCAL FILES
#get local files list 

process = subprocess.Popen(["find", local_dir], stdout=subprocess.PIPE)
list_files_local=process.communicate()[0]
list_files_local_2 = list_files_local.decode('UTF-8')  




#parse local data
#split string on newline
#every line is the infos of one file on the local storage
list_files_local_3 = list_files_local_2.split("\n")



local_dir_as_array=local_dir.split("/")
lenght_path_local_folder=len(local_dir_as_array)
#print(local_dir_as_array)
#print(list_files_local_3[10])
#os._exit(0)


#parse local file again
#get filepath without root local_dir
list_partial_filepath_local_5=[]
for current_full_filepath_local in list_files_local_3:
	current_full_filepath_local_3 = current_full_filepath_local.split("/")
	current_partial_filepath_local_4=[]
	current_partial_filepath_local_5=[]
	#if(current_file_local_3[0]=='.'):  current_file_local_4=current_file_local_3[2:len(current_file_local_3)]
	current_partial_filepath_local_4=current_full_filepath_local_3[lenght_path_local_folder:len(current_full_filepath_local_3)]
	current_partial_filepath_local_5='/'.join(current_partial_filepath_local_4)
	#print(current_partial_filepath_local_5)
	#print(current_full_filepath_local)
	if os.path.isfile(current_full_filepath_local)==True:
		list_partial_filepath_local_5.append(current_partial_filepath_local_5)
		#print('isfile: ', current_full_filepath_local)


#print('list_partial_filepath_local:')
#print(list_partial_filepath_local)

#os._exit(0)

#PART4. COMPARE LOCAL FILES AND REMOTE FILES
#here the script create 3 arraies
#array list_of_files_to_copy_from_local_dir_to_remote_dir_case_partial_path
#array list_of_files_to_copy_from_local_dir_to_remote_dir_case_full_path_remote
#array list_of_files_to_copy_from_local_dir_to_remote_dir_case_full_path_local



yes_found=False

list_of_files_to_copy_from_local_dir_to_remote_dir_case_partial_path=[]
list_of_files_to_copy_from_local_dir_to_remote_dir_case_full_path_remote=[]
list_of_files_to_copy_from_local_dir_to_remote_dir_case_full_path_local=[]



#print('list_partial_filepath_local_5: ', len(list_partial_filepath_local_5))
#print('list_remote_files_5:', len(list_remote_files_5))


for current_partial_filepath_local_5 in list_partial_filepath_local_5:
	yes_found=False
	for current_partial_filepath_remote_5 in list_remote_files_5:
		if current_partial_filepath_remote_5==current_partial_filepath_local_5:
			yes_found=True
			#print('remote: ', current_partial_filepath_remote_5)
			#print('local: ', current_partial_filepath_local_5)
	if yes_found==False:
		#print('local555: ', current_partial_filepath_local_5)
		list_of_files_to_copy_from_local_dir_to_remote_dir_case_partial_path.append(current_partial_filepath_local_5)


#print('list_partial_filepath_local:')
#print(list_partial_filepath_local)
#os._exit(1)


#print(list_of_files_to_copy_from_local_dir_to_remote_dir_case_partial_path)
#print('tets64646')


#os._exit(1)



#copy files from local directory to remote directory


number_of_new_files=len(list_of_files_to_copy_from_local_dir_to_remote_dir_case_partial_path)
if show_new_files_yes_or_not=='yes':
	print('\n\n')
	print('Number of new files to copy: ', number_of_new_files)
	print('\n\n')


if show_new_files_yes_or_not=='yes' and number_of_new_files==0:
	print('\n\n')
	print('Maybe there is not new files in the local directory')
	print('\n\n')




for current_new_partial_filepath in list_of_files_to_copy_from_local_dir_to_remote_dir_case_partial_path: 
	current_local_fullpath=os.path.join(local_dir, current_new_partial_filepath)
	#list_of_files_to_copy_from_local_dir_to_remote_dir_case_full_path_local.append(current_local_fullpath)

	current_remote_fullpath=os.path.join(remote_dir, current_new_partial_filepath)
	#list_of_files_to_copy_from_local_dir_to_remote_dir_case_full_path_remote.append(current_remote_fullpath)    

	if show_new_files_yes_or_not=='yes':
		print('\n\n')
		print('upload files')
		print(current_local_fullpath)
		print(current_remote_fullpath)
		print('\n\n')

	#copy files from local directory to remote directory
	if mode_test_or_real=='real':
		print('\n\n')
		#equivalent shell command: uplink cp /dir441/file34344.txt sj://bucket001/dir3434
		#process = subprocess.Popen(["uplink", "cp", current_local_fullpath, current_remote_fullpath], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
		process = subprocess.Popen(["uplink", "cp", current_local_fullpath, current_remote_fullpath])
		process.wait()
		print('\n\n')
		time.sleep(1)
	elif show_new_files_yes_or_not=='yes':
		print('Copy commad skipped. This is the Test mode.')
		print('subprocess.Popen(["uplink", "cp", current_local_fullpath, current_remote_fullpath], stdout=subprocess.PIPE, stderr=subprocess.PIPE')








os._exit(0)





#documentation
'''
This  script synchronizes local directory with storj directory with uplink
It does not add or remove any file from the local  directory
It  does not  remove any file from the remote directory .
It just copies new files from local directory to remote storj directory
It just check filename and filepath, not file size or file date creation 


#example
python3 ./synchronize_storj.py --local_dir /dir6565/dir773  --remote_dir sj://bucket_845/dir747/dir5567 --mode_test_or_real real --show_new_files_yes_or_not not

'''
