from datetime import datetime
from pprint import pprint

import matplotlib.pyplot as plt
import numpy as np

from pysteps import io, rcparams
from pysteps.feature import tstorm as tstorm_detect
from pysteps.tracking import tdating as tstorm_dating
from pysteps.utils import to_reflectivity
from pysteps.visualization import plot_precip_field, plot_track, plot_cart_contour
import serial
import time as tm  # Rename the time module to avoid conflict

ser = serial.Serial('COM2', 9600, timeout=1)

# Select the input data
date = datetime.strptime("201607112100", "%Y%m%d%H%M")
data_source = rcparams.data_sources["mch"]

# Extract corresponding settings
root_path = data_source["root_path"]
path_fmt = data_source["path_fmt"]
fn_pattern = data_source["fn_pattern"]
fn_ext = data_source["fn_ext"]
importer_name = data_source["importer"]
importer_kwargs = data_source["importer_kwargs"]
timestep = data_source["timestep"]

# Load the data from the archive
fns = io.archive.find_by_date(
    date, root_path, path_fmt, fn_pattern, fn_ext, timestep, num_next_files=20
)
importer = io.get_method(importer_name, "importer")
R, _, metadata = io.read_timeseries(fns, importer, **importer_kwargs)

# Convert to reflectivity (it is possible to give the a- and b- parameters of the
# Marshall-Palmer relationship here: zr_a = and zr_b =).
Z, metadata = to_reflectivity(R, metadata)

# Extract the list of timestamps
timelist = metadata["timestamps"]

pprint(metadata)

input_image = Z[2, :, :].copy()
timestamp = timelist[2]  # Rename the variable to avoid conflict
cells_id, labels = tstorm_detect.detection(input_image, time=timestamp)

print(cells_id.iloc[0])

# Plot precipitation field
plot_precip_field(Z[2, :, :], geodata=metadata, units=metadata["unit"])
plt.xlabel("Swiss easting [m]")
plt.ylabel("Swiss northing [m]")

# Add the identified cells
plot_cart_contour(cells_id.cont, geodata=metadata)

# Filter the tracks to only contain cells existing in this timestep
IDs = cells_id.ID.values
track_filt = []
# for track in track_list:
#     if np.unique(track.ID) in IDs:
#         track_filt.append(track)

# Add their tracks
plot_track(track_filt, geodata=metadata)
plt.show()

# Define Z-R relationship constants
a = 200  # Z-R relationship constant
b = 1.6  # Z-R relationship exponent

# Convert reflectivity (Z) to precipitation intensity (R)
precip_intensity = a * (Z ** b)

# Print precipitation intensity for the specific frame
print("Precipitation intensity (mm/h) at the specific frame:")
print(precip_intensity[2, :, :])

# Plot the precipitation intensity for the specific frame
# plt.figure()
# plt.imshow(precip_intensity[2, :, :], cmap='viridis', origin='upper')
# plt.colorbar(label='Precipitation intensity (mm/h)')
# plt.title(f'Precipitation intensity at {timelist[2]}')
# plt.xlabel("Swiss easting [m]")
# plt.ylabel("Swiss northing [m]")
# plt.show()

print(metadata)

# Print the entire precipitation intensity array if needed
print("Precipitation intensity (mm/h) for all frames:")
print(precip_intensity)

# Print the maximal dBZ value recorded
max_dbz = np.nanmax(Z)
print("Maximal dBZ value recorded:", max_dbz)

if max_dbz > 25:
    for _ in range(10):  # Send 10 times
        ser.write(b'T')
        tm.sleep(0.5)  # Use the renamed time module
