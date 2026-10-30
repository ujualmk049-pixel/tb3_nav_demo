Overview: TurtleBot3 (waffle) in Gazebo Classic with Nav2 on ROS 2 Humble.
Install:
  sudo apt install ros-humble-gazebo-ros-pkgs ros-humble-navigation2 \
    ros-humble-nav2-bringup ros-humble-turtlebot3 ros-humble-turtlebot3-simulations

Setup: 
  source /usr/share/gazebo/setup.bash
  export GAZEBO_MODEL_DATABASE_URI=""

Repo to be cloned in the src folder

Build and run:
  colcon build --symlink-install
  source install/setup.bash
  ros2 launch tb3_nav_demo nav_demo.launch.py

Usage: set the 2D Pose Estimate in RViz, send a Nav2 Goal, then insert a box in Gazebo to show replanning.

