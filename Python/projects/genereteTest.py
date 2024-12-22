import numpy as np
import mrcfile
import os

# Parameters
output_directory = "mrc_files"
num_files = 10  # Number of MRC files to create
volume_size = (50, 50, 50)  # Dimensions of the 3D array in each file

# Create output directory if it doesn't exist
os.makedirs(output_directory, exist_ok=True)

# Generate mock MRC files
for i in range(1, num_files + 1):
    file_name = f"volume{i:03d}.mrc"
    file_path = os.path.join(output_directory, file_name)
    
    # Create a simple 3D array with increasing values
    data = np.random.random(volume_size) * (i / num_files)
    
    # Write the array to an MRC file
    with mrcfile.new(file_path, overwrite=True) as mrc:
        mrc.set_data(data.astype(np.float32))
        mrc.update_header_from_data()
    
    print(f"Created {file_path}")

print(f"Mock MRC files saved in '{output_directory}' directory.")
