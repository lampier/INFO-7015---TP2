import os
import time
import subprocess

print("Este experimento demora cerca de uma hora e meia para executar todas as janelas")

windows_size_vector={'500'}#'1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','22','24','26','28','30','40','50','65','70','85','90','100','108','123','132','178','186','190','200','220','300','450','500'}

for i in windows_size_vector:

	print("Experimento com window size = "+ i)
	
	cmd = "sed -i 's/unsigned int the_window_size =.*/unsigned int the_window_size = '"+i+"';/' aquecimentoA/datagrump/controller.cc"
	os.system(cmd)

	print("\n\n")
	print("Experimento com window size = "+ i)
	output = "./run-contest lampiao >'result/windowsize'"+i+"'.txt'"
	out = os.system("cd aquecimentoA \n make \n cd datagrump \n "+output)
	#time.sleep(160)
	print("\n\n")
	#result = subprocess.check_output("cd aquecimentoA \n make \n cd datagrump \n "+output, shell = True)
