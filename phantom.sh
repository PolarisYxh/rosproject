gnome-terminal -x -c "roslaunch kinova_gazebo robot_launch.launch kinova_robotType:=j2n6s300 use_trajectory_controller:=true"&
gnome-terminal -x -c "roslaunch j2n6s300_moveit_config j2n6s300_gazebo_demo.launch"&
gnome-terminal -x -c "roslaunch kinova_arm_moveit_demo phantomPoseTarget.launch"
