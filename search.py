import subprocess
import apt



cache = apt.Cache()
if cache['mlocate'].is_installed:
    print ("package mlocate is installed")
else:
    command=['sudo apt install mlocate']
    output = subprocess.Popen(command, stdout=subprocess.PIPE).communicate()[0]
    output = output.decode()


def find_files(file_name):
	command = ['locate', file_name]

	output = subprocess.Popen(command, stdout=subprocess.PIPE).communicate()[0]
	output = output.decode()

	x = output.split('\n')
	results =[]
	for i in range(len(x)):
		if file_name in x[i].split('/'):
			results.append(x[i])
	
	return results


