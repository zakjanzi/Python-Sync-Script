import os
import sys
import shutil
import hashlib

# A function to calculate the md5. To be used in the synchronize_folders function.
def calculate_md5(filename, chunk_size=8192):
    md5_hash = hashlib.md5()
    with open(filename, "rb") as f:
        while chunk := f.read(chunk_size):
            md5_hash.update(chunk)
    return md5_hash.hexdigest()

# The synchronization function.
def synchronize_folders(source_folder, destination_folder, log_file):
    try:
        # Creates the directory if it does not exist.
        if not os.path.exists(destination_folder):
            os.makedirs(destination_folder)
        
        # Opens the log file
        with open(log_file, "a") as log:
            for root, _, files in os.walk(source_folder):
                for file_name in files:
                    source_path = os.path.join(root, file_name)
                    destination_path = os.path.join(destination_folder, os.path.relpath(source_path, source_folder))
                    
                    # If either condition is true (file does not exist in path OR the MD5 is different), the file will be copied.
                    if not os.path.exists(destination_path) or calculate_md5(source_path) != calculate_md5(destination_path):
                        shutil.copy2(source_path, destination_path)
                        log.write(f"Copied: {source_path} -> {destination_path}\n")
                        print(f"Copied: {source_path} -> {destination_path}")
            
            # Check path of files in destination, and remove them if they don't exist in source.
            for root, _, files in os.walk(destination_folder):
                for file_name in files:
                    destination_path = os.path.join(root, file_name)
                    source_path = os.path.join(source_folder, os.path.relpath(destination_path, destination_folder))
                    # If the file was removed from source, it will be removed from destination.
                    if not os.path.exists(source_path):
                        os.remove(destination_path)
                        log.write(f"Removed: {destination_path}\n")
                        print(f"Removed: {destination_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Allow script to run directly (and check # of arguments passed)
if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Missing argument. Usage: python OneWaySync.py <source_folder> <destination_folder> <log_file>. Do not wrap the path with quotes or <>.")
        sys.exit(1)
    
    source_folder = sys.argv[1]
    destination_folder = sys.argv[2]
    log_file = sys.argv[3]
    
    synchronize_folders(source_folder, destination_folder, log_file)
