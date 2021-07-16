import getpass
from pathlib import Path
from clipper_gpd import shp_clipper
from email_sender import send_email
from utilities import zip_folder

if __name__ == '__main__':
    folder_to_clip = input("Folder with shapefiles to clip: ")
    clip_path = input("Path to the file that clips: ")
    shp_clipper(folder_to_clip, clip_path) # Clip files
    print("Clips ended")
    
    # Zip clipped files
    zip_file_name = input("Insert the zipfile name of your clips: ")
    clips_folder = Path(folder_to_clip) / 'clips'
    zip_folder(clips_folder, zip_file_name)
    zip_file_path = Path(clips_folder) / zip_file_name
    print(f"Files zipped at {clips_folder} with name '{zip_file_name}'")
    
    # Send email
    email_account = input("Email account: ")
    password = getpass.getpass()
    receiver = input("To (email): ")
    subject = input("Insert email subject: ")
    msg = input("Email body message: ")
    
    send_email(email_account, password, receiver, subject, msg, [zip_file_path])
    print("Email sent!")
    
