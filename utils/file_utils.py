import tempfile
import os
from uuid import uuid4


TMP_FOLDER_NAME= "project_midterm"
# create folder if not exist

def create_if_not_exists(path:str):
    if not os.path.exists(path):
        os.makedirs(path)


def get_tmp_folder_path():
    path=tempfile.gettempdir()
    path=os.path.join(path,TMP_FOLDER_NAME)
    create_if_not_exists(path)
    return path

# return file path to return local audio file path
def get_unique_tmp_file_path():
    file_path = os.path.join(get_tmp_folder_path(), str(uuid4()))
    return file_path

# here we will create a unique path for file and append its suffiz
def create_unique_tmp_file(file_suffix:str):
    return f'{get_unique_tmp_file_path()}_{file_suffix}'


# write binary file data on the file created

def persist_binary_file_locally (data:bytes,file_suffix:str)->str:
    if data is not None:
        file_path= create_unique_tmp_file(file_suffix)
        with open(file_path,'wb') as f:
            f.write(data)

        return file_path

if __name__=="__main__":
    print(get_tmp_folder_path())