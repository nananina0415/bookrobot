#!/usr/bin/env python3
import trimesh
import numpy as np

# Bookshelf dimensions
num_levels = 6  # Number of shelves
cube_height = 0.300  # Bookcube height
cube_width = 0.350  # Bookcube width
cube_depth = 0.330  # Bookcube depth
pole_vertical_spacing = 0.350  # 35cm vertical distance between pole pairs
first_pole_offset = 0.015  # 1.5cm above support upper plane

# Frame dimensions
back_plate_thickness = 0.010  # 10mm back plate
base_support_thickness = 0.010  # 10mm base plate
pole_diameter = 0.018  # 18mm poles (slightly smaller than 20mm holes)
pole_x_offset = 0.155  # ±155mm from center (matching bookcube holes)

# Calculate total dimensions
# Height = base + first_pole_offset + (num_levels-1) * spacing + cube_height
total_height = base_support_thickness + first_pole_offset + (num_levels - 1) * pole_vertical_spacing + cube_height
total_width = cube_width
total_depth = cube_depth + back_plate_thickness

# Create back plate
back_plate = trimesh.creation.box(
    extents=[total_width, back_plate_thickness, total_height],
    transform=trimesh.transformations.translation_matrix([
        0,
        -cube_depth/2,
        total_height/2
    ])
)

# Create base support
base_support = trimesh.creation.box(
    extents=[total_width, cube_depth, base_support_thickness],
    transform=trimesh.transformations.translation_matrix([
        0,
        0,
        base_support_thickness/2
    ])
)

# Start with back plate and base
parts = [back_plate, base_support]

# Create horizontal pole pairs for each level
for level in range(num_levels):
    # Calculate Z position for this level
    # First pole at base + 1.5cm, then 35cm spacing
    z_pos = base_support_thickness + first_pole_offset + level * pole_vertical_spacing

    # Left pole (Y-axis aligned, horizontal)
    rotation_x = trimesh.transformations.rotation_matrix(np.pi/2, [1, 0, 0])
    translation_left = trimesh.transformations.translation_matrix([
        -pole_x_offset,
        0,
        z_pos
    ])
    left_pole = trimesh.creation.cylinder(
        radius=pole_diameter/2,
        height=cube_depth,
        transform=translation_left @ rotation_x
    )
    parts.append(left_pole)

    # Right pole (Y-axis aligned, horizontal)
    translation_right = trimesh.transformations.translation_matrix([
        pole_x_offset,
        0,
        z_pos
    ])
    right_pole = trimesh.creation.cylinder(
        radius=pole_diameter/2,
        height=cube_depth,
        transform=translation_right @ rotation_x
    )
    parts.append(right_pole)

# Combine all parts
bookshelf_frame = trimesh.util.concatenate(parts)

# Export frame to STL
frame_output = '/home/roplming/rpmws/src/bookrobot/bookrobot_gazebo/models/bookshelf/bookshelf_frame.stl'
bookshelf_frame.export(frame_output)
print(f"Bookshelf frame STL exported to: {frame_output}")
print(f"Frame vertices: {len(bookshelf_frame.vertices)}, Faces: {len(bookshelf_frame.faces)}")
print(f"Frame dimensions: {total_width}m(W) x {total_depth}m(D) x {total_height}m(H)")
print(f"Number of levels: {num_levels}")
print(f"Pole pairs: {num_levels}")
