#Jackal's kinect package  
before roslaunch iqr_4b_bringup iqr_bringup.launch,have to open all the devices such as kinova  
roslaunch iqr_4b_moveit_config iqr_4b_moveit_execute.launch//manipulate kinova arm  
roslaunch iqr_4b_navigation gmapping_demo.launch//open navigation algorithm  

## only jackal model
sudo apt-get install ros-kinetic-jackal-simulator ros-kinetic-jackal-desktop ros-kinetic-jackal-navigation//下载jackal所有包
roslaunch jackal_gazebo jackal_world1.launch//打开gazebo的jackal机器人  
roslaunch iqr_4b_bringup zhikete_mars.launch//打开智科特机器人和mars_plane的gazebo
roslaunch turtlebot3_teleop turtlebot3_teleop_key.launch//键盘控制机器人，需要turtlebot3的包
roslaunch jackal_viz view_robot.launch//rviz控制机器人
rosrun rosrun save_rgbd_from_kinect2 save_rgbd_from_kinect2//保存rgbd图
## document
iqr_4b_robot-master/iqr_4b_description/urdf/iqr_4b_robot.urdf.xacro   //整体智科特组装机器人的文件

