import os



#reading the configuration
config_file = open("./sorter.config", "r")
config_data = config_file.readlines()
folders = config_data[0].replace('\n','').split(" ")
folders_str = config_data[0]
print(f"loaded folders: {folders}")
extentions = [x.replace('\n','').split(" ") for x in config_data[1:]]
print(f"extensions are : {extentions}") 
extension_dic = {}
basePath = "."

for i in range(len(extentions)):
    for j in range(len(extentions[i])):
        extension_dic[extentions[i][j]] = folders[i]



#function for creating files for testing
def create_test_files():
    for i in range(len(extentions)):
        for j in range(len(extentions[i])):
            filename = str.format("{nombre}.{extension}", nombre = "archivo", extension = extentions[i][j])
            
            file = open(filename,"w")
            file.write("something")
            file.close()


#Folder creation method
def create_folders():
    try:
        command = f" md  {basePath}{os.sep}{folders_str}"
        os.system(command) 
    except:
        print("Directory was already created")

def moveDir(foldername, filename):
    command = f"Move {filename} {foldername}"
    os.system(command)


#Get Files Method
def get_dir_list():
    return os.listdir()



#sort files by configuration directives
def sort():
    items = get_dir_list()
    for i in range(len(items)):
        if os.path.isfile(items[i]):
            item_extention = items[i].split(".")[1]
            if item_extention in extension_dic:
                destination_folder = f"{basePath}{os.sep}{extension_dic[item_extention]}"
                try:
                    print(destination_folder)
                    moveDir(f"{destination_folder}",items[i])
                except:
                    print("Error transportando los archivos")


#Main process
def main():
    create_test_files()
    create_folders()
    sort()

#create_test_files()

#excecution
main()
