此代码包为gazebo+ros melodic+gazebo的kinect仿真并且点云重建的代码

roslaunch turtlebot3_gazebo kinect.launch
rosrun rviz rviz
//roslaunch turtlebot3_teleop turtlebot3_teleop_key.launch

保存gazebo-ros-openni-kinect插件传出的rgbd相片：
rosrun save_rgbd_from_kinect2 save_rgbd_from_kinect2

可以保存普通相片：rosrun image_view image_saver image:=/camera/depth/image_raw _encoding:=16UC1 
rosrun image_view image_view image:=/camera/depth/image_raw 右键保存depth图到终端路径，保存的是三通道的

rosrun image_view image_saver image:=/camera/rgb/image_raw

保存点云到pcd：
rosrun pcl_ros1 pointcloud_to_pcd cloud_topic:=/camera/depth/points


kinect仿真相关文件
src/turtlebot3/turtlebot3_description/urdf/turtlebot3_burger.urdf.xacro   小车

src/turtlebot3/turtlebot3_description/urdf/turtlebot3_burger.gazebo.xacro  小车

src/turtlebot3/turtlebot3_description/urdf/kinect.urdf.xacro  单独的kinect相机

src/turtlebot3/turtlebot3_description/urdf/kinect.gazebo.xacro  单独的kinect相机

src/turtlebot3_simulations/turtlebot3_gazebo/models/turtlebot3_worldmy   房子，调用了前两个
src/turtlebot3_simulations/turtlebot3_gazebo/worlds/turtlebot3_worldmy.world  调用了models/turtlebot3_worldmy   房子

src/turtlebot3_simulations/turtlebot3_gazebo/launch/turtlebot3_world.launch

src/turtlebot3_simulations/turtlebot3_gazebo/launch/kinect.launch


src文件夹下都是ros包：
turtlebot3* package is the ros turtlebot3 world and env
image_pipeline-melodic can view and save iamge
save_rgbd_from_kinect2 can save rgbd from kinect in gazebo
perception_pcl-melodic-devel can save and view pointcloud

Depth2point下是depth转点云的代码，还有点云拼接的代码：输入几对匹配好的rgbd图，不通过ros，输出拼接好的点云，cmake +make安装好后，可以./image2pcl直接运行。

目前阶段可以在gazebo固定位置放置kinect并且拍摄得到rgbd图像并保存，然后用rgbd图进行点云拼接。
下一步应实现gazebo下控制kinect拍摄动作的功能。




plus:roslaunch turtlebot3_gazebo man.launch 是人骑自行车的仿真。
