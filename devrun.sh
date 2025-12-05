#!/bin/bash

# Build bookrobot_gazebo package
echo "Building bookrobot_gazebo..."
colcon build --packages-select bookrobot_gazebo --allow-overriding bookrobot_gazebo

# Source the workspace
echo "Sourcing workspace..."
source install/setup.bash

# Launch Gazebo with library world
echo "Launching library world in Gazebo..."
ros2 launch bookrobot_gazebo bringup_gazebo.launch.py world_name:=library.sdf
