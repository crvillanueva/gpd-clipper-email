import os
import zipfile
from pathlib import Path

def zip_folder(folder_to_zip: str, zip_f_name: str) -> None:
    """Compress as '.zip' all the files inside a given folder

    Args:
        folder_to_zip: Path to the folder with the files to zip.
        zip_f_name: Filename of the zip to return

    Returns:
        None
    """
    os.chdir(folder_to_zip)
    
    with zipfile.ZipFile(zip_f_name, "w", compression=zipfile.ZIP_DEFLATED) as my_zip:
        for file in os.listdir():
            if file != zip_f_name:
                my_zip.write(file)
