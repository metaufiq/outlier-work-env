from chimerax.core.commands import run

# Assuming 'session' is passed correctly to this script from ChimeraX

N = 10  # Number of volumes
isosurface_level = 0.05  # Adjust this value as needed
color = "cornflowerblue"

# Load all MRC files and track model IDs
model_ids = []
for i in range(1, N + 1):
    open_command = f"open volume{i:03d}.mrc"
    run(session, open_command)
    model_ids.append(i)  # Assuming sequential assignment; verify in practice.

# Set isosurface level and color
for model_id in model_ids:
    run(session, f"volume #{model_id} color {color}")
    run(session, f"volume #{model_id} level {isosurface_level}")

# Set a known orientation
run(session, "view orient")

# Start recording a movie
run(session, "movie record movie.mp4 width 1080 height 1080 supersample 3")

# Cycle through images and rotate them
def cycle_and_rotate(session, model_ids):
    for frame in model_ids:
        run(session, "hide models")
        run(session, f"show models #{frame}")
        run(session, "wait 30")  # Wait for 30 frames

    run(session, "turn y 90")  # Rotate by 90 degrees around the Y-axis
    run(session, "wait 60")  # Wait for 60 frames

    for frame in model_ids:
        run(session, "hide models")
        run(session, f"show models #{frame}")
        run(session, "wait 30")  # Wait for 30 frames

# Execute the cycle and rotate function
cycle_and_rotate(session, model_ids)

# Stop recording the movie
run(session, "movie stop")
