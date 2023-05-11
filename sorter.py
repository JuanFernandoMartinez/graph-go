import os

images = ["jpg","JPG", "PNG", "png", "gif", "GIF", "svg", "SVG"]
documents = ["doc","docx","pdf", "DOC","DOCX","PDF"]
xls = ["csv","xls","xlsx","CSV","XLS","XLSX"]
videos = ["mp4","MP4"]
musica = ["mp3","mp3"]

list_de_tipos = [images,documents, xls, videos, musica]

#function for creating files for testing
def create_test_files():
    for i in range(len(list_de_tipos)):
        for j in range(len(list_de_tipos[i])):
            filename = str.format("{nombre}.{extension}", nombre = "archivo", extension = list_de_tipos[i][j])
            
            file = open(filename,"w")
            file.write("something")
            file.close()


#funciona perfecto
def create_folders():
    os.system("md images videos musica xls documents other")    

def moveDir(foldername, filename):
    comand = str.format('Move "{file}" {folder}"',file = filename, folder = foldername)
    os.system(comand)
    
    #print(comand)


def get_dir_list():
    items = os.listdir()
    return items
def sort():
    items = get_dir_list()
    for i in range(len(items)):
        if os.path.isfile(items[i]):
            aux_list = items[i].split(".")
            if aux_list[1] in images:
                moveDir("images",items[i])
            elif aux_list[1] in documents:
               moveDir("documents", items[i])
            elif aux_list[1] in videos:
                moveDir("videos", items[i])
            elif aux_list[1] in musica:
                moveDir("musica", items[i])
            elif aux_list[1] in xls:
                moveDir("xls", items[i])
            #elif aux_list[1] != "ink" and items[i] != "sorter.py":
            #    moveDir("other", items[i])


def main():
    create_folders()
    sort()

#create_test_files()

#main()
main()
