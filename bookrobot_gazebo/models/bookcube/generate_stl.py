#!/usr/bin/env python3
import trimesh
import numpy as np

# Dimensions in meters (matching .scad file)
width = 0.350
depth = 0.330
height = 0.300
bottom_thickness = 0.030
wall_thickness = 0.010

# Hole parameters
hole_diameter = 0.020  # 20mm (2cm)
hole_x_offset = 0.155  # ±155mm from center (total distance 310mm = 31cm)

# Create bottom plate
bottom_plate = trimesh.creation.box(
    extents=[width, depth, bottom_thickness],
    transform=trimesh.transformations.translation_matrix([0, 0, bottom_thickness/2])
)

# Create left wall
left_wall = trimesh.creation.box(
    extents=[wall_thickness, depth, height],
    transform=trimesh.transformations.translation_matrix([
        -width/2 + wall_thickness/2,
        0,
        bottom_thickness + height/2
    ])
)

# Create right wall
right_wall = trimesh.creation.box(
    extents=[wall_thickness, depth, height],
    transform=trimesh.transformations.translation_matrix([
        width/2 - wall_thickness/2,
        0,
        bottom_thickness + height/2
    ])
)

# Create back wall
back_wall = trimesh.creation.box(
    extents=[width - 2*wall_thickness, wall_thickness, height],
    transform=trimesh.transformations.translation_matrix([
        0,
        -depth/2 + wall_thickness/2,
        bottom_thickness + height/2
    ])
)

# Combine all parts
bookcube = trimesh.util.concatenate([bottom_plate, left_wall, right_wall, back_wall])

# Create left hole (cylinder along Y-axis)
# Rotate cylinder 90 degrees around X-axis to align with Y-axis
rotation_x = trimesh.transformations.rotation_matrix(np.pi/2, [1, 0, 0])
translation_left = trimesh.transformations.translation_matrix([
    -hole_x_offset,
    0,
    bottom_thickness/2
])
left_hole = trimesh.creation.cylinder(
    radius=hole_diameter/2,
    height=depth + 0.002,  # along Y-axis (depth direction)
    transform=translation_left @ rotation_x
)

# Create right hole (cylinder along Y-axis)
translation_right = trimesh.transformations.translation_matrix([
    hole_x_offset,
    0,
    bottom_thickness/2
])
right_hole = trimesh.creation.cylinder(
    radius=hole_diameter/2,
    height=depth + 0.002,
    transform=translation_right @ rotation_x
)

# Subtract holes from bookcube
try:
    bookcube = bookcube.difference([left_hole, right_hole])
    print("Boolean difference successful!")
except Exception as e:
    print(f"Boolean difference failed: {e}")
    print("Attempting to merge meshes without boolean operation...")

# Export to STL
output_path = '/home/roplming/rpmws/src/bookrobot/bookrobot_gazebo/models/bookcube/bookcube.stl'
bookcube.export(output_path)
print(f"STL exported to: {output_path}")
print(f"Vertices: {len(bookcube.vertices)}, Faces: {len(bookcube.faces)}")
