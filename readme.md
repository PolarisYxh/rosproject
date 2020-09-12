# Jackal's kinect package
before roslaunch iqr_4b_bringup iqr_bringup.launch,have to open all the devices such as kinova
roslaunch iqr_4b_moveit_config iqr_4b_moveit_execute.launch//manipulate kinova arm
roslaunch iqr_4b_navigation gmapping_demo.launch//open navigation algorithm

## only jackal model
sudo apt-get install ros-kinetic-jackal-simulator ros-kinetic-jackal-desktop ros-kinetic-jackal-navigation//下载jackal所有包
roslaunch jackal_gazebo jackal_world1.launch//打开gazebo的jackal机器人
roslaunch iqr_4b_bringup zhikete_mars.launch//打开智科特机器人和mars_plane的gazebo
roslaunch turtlebot3_teleop turtlebot3_teleop_key.launch//键盘控制机器人，需要turtlebot3的包
roslaunch jackal_viz view_robot.launch//rviz控制机器人
rosrun save_rgbd_from_kinect2 save_rgbd_from_kinect2//保存rgbd图
roslaunch iqr_4b_bringup zhikete_academy.launch  //打开智科特机器人和图书馆场景
## document
iqr_4b_robot-master/iqr_4b_description/urdf/iqr_4b_robot.urdf.xacro   //整体智科特组装机器人的文件

## 自己写的python通过socket传输从ros节点获取的rgbd图片
save_rgbd_from_kinect2里面的 trans_rgbd_from_kinect.py是服务器，获取ros rgbd传输到客户端
rosrun save_rgbd_from_kinect2 trans_rgbd_from_kinect.py
save_rgbd_from_kinect2里面的get_rgbd.py是客户端，获取rgbd并保存

## ros+unity
roslaunch iqr_4b_bringup zhikete_mars.launch//打开智科特机器人和mars_plane的gazebo
rosrun iqr_4b_bringup joy_to_twist.py  //打开unity控制机器人的节点
ros_unity_pro/Assets/RosSharp/Scenes/ZhiketeScene.unity    //打开对应的火星 unity场景，在unity场景运行以后，可以方向键控制机器人运动
ros_unity_pro/Assets/RosSharp/Scenes/3D SCENE/AVP_Interior_Vol.2.unity     //打开房间场景

## 502
roslaunch iqr_4b_bringup zhikete_mars.launch  //打开月面仿真环境+zhikete机器车(该车目前含有./interface.pdf中所述各个传感器的接口)
roslaunch iqr_4b_bringup 502_mars.launch    //打开月面仿真环境+502机器车(该车目前含有kinect,laser传感器，后续可以添加)
roslaunch 502_teleop turtlebot3_teleop.launch //打开键盘控制机器车运动程序，wasd控制运动