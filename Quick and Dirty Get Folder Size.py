# Quick and Dirty code for looping through files in a folder to get total size

import os
import argparse



def get_total_size_of_folder(folder_path):
    tot = 0

    for f in os.listdir(folder_path):
        # Get full filepath of f
        FILE = os.path.join(folder_path, f)

        # what type is f?
        if os.path.isfile(FILE):    
            # if file get size
            tot += os.path.getsize(FILE)
        elif os.path.isdir(FILE):
            # if folder, recurse
            tot += get_total_size_of_folder(FILE)
        else:
            # note if its type is neither file nor folder
            print(f"Skipping {FILE}, not a file or directory")
    return tot

def get_good_units(size_in_bytes):
    # translate bytevalue into the right size units (KB, MB, GB, etc.)
    if size_in_bytes == 0:
        return 0,'bytes'
    if size_in_bytes < 0:
        raise ValueError("Total size value cannot be negative")

    for unit in ['B', 'kb', 'Mb', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB']:
        if size_in_bytes < 1024:
            return size_in_bytes,unit
        size_in_bytes /= 1024

def get_folders_list():
    # use argparse to get folder path from command line
    parser = argparse.ArgumentParser(description="Get total size of a folder")
        
    parser.add_argument("folders",  
                        type=str, 
                        nargs="*",
                        metavar="FOLDER",
                        help="One or more folder paths.  Optional.\nCurrent directory if not specified."
                        )
    
    args = parser.parse_args()
    FOLDERS = args.folders
    
    if not FOLDERS:
        FOLDERS = [os.getcwd()]
    return FOLDERS

def process_folders(FoldersList):
    for F in FoldersList:
        process_folder(F)

def process_folder(folder1):
    # process a single folder
    if os.path.exists(folder1) and os.path.isdir(folder1):
        # get folder size in bytes
        total_size = get_total_size_of_folder(folder1)
        # translate to appropriate units
        total_size, unit = get_good_units(total_size)

        print(f"Total size of [{folder1:<20}]: {total_size:10,.1f} {unit}")
    else:
        print(f"Error: '{folder1}' is not a valid directory.")



if __name__ == "__main__":

    FoldersList = get_folders_list()
    process_folders(FoldersList)

    # END MAIN #
