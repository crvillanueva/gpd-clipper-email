import os
import geopandas as gpd
import fiona


def shp_clipper(input_folder: str, clipped_filename: str) -> None:
    """Clips ESRI shapefiles (.shp) in a given folder and move them to
    a new folder named 'clips' that is created inside the input folder

    Args:
        input_folder: Path to the folder that contains the shapes to be clipped
        clip_path: Path to the shape file that is used to clip
    """
    try:
        os.mkdir(os.path.join(input_folder, "clips"))
    except FileExistsError:
        print("Folder 'clips' already exists, be careful.")
        pass
    
    shapefiles = [file for file in os.listdir(input_folder) if file.split(".")[-1] == "shp"]
    print(shapefiles, "\n")
    
    try:
        read_clip = gpd.read_file(clipped_filename)
    except fiona.errors.DriverError: 
        raise Exception("Clip file doesn't exist or can't be found")
    clip_output_folder = os.path.join(input_folder, "clips")
    
    for file in shapefiles:
        print(f"Trying {file}")
        shp_to_clip_path = os.path.join(input_folder, file)
        try:
            gpd_to_clip = gpd.read_file(shp_to_clip_path)
        except:
            print(f"Couldn't read {file}")
        try:
            clip_file = gpd.clip(gpd_to_clip, read_clip)  # Clip
        except:
            print(f"Couldn't clip {file}")
        try:
            clipped_filename = f"{os.path.join(clip_output_folder, file[:-4])}_clip.shp"
            clip_file.to_file(clipped_filename)
            print(f"{file} clipped successfully.", "\n")
        except ValueError:
            print(f"Couldn't save {file}", "\n") 
        
