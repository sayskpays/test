# LOG CHECK

from datetime import datetime
import fileinput
import glob


# Variable
read_file_path = "C:/dev/hello.txt"


def searchFile(interface_id):
    
    str_data = ""
    
    print("Input IF ID : %s" %interface_id.upper())
    with fileinput.input(glob.glob(read_file_path)) as f:
        for line in f:
            if line.find(interface_id.casefold()) !=-1 :
                str_data = line
                
                error_time = datetime.strptime(str_data[:24].replace(" ",""),'%Y%b%d%H:%M:%S:%f')
                print(error_time)
                print(type(error_time))
            
                print("Error Occurrence Time : %s " %str_data[:24])
                print("Error Data : %s " %line)
            else:
                pass
        
                    
searchFile(str(input("insert data: ")))
                


    