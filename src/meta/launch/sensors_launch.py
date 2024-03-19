import os

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch_ros.actions import Node
from launch.launch_description_sources import PythonLaunchDescriptionSource


def generate_launch_description():
   lidar = IncludeLaunchDescription(
      PythonLaunchDescriptionSource([os.path.join(
         get_package_share_directory('livox_ros_driver2'), 'launch_ROS2'),
         '/rviz_MID360_launch.py'])
      )
   
   camera = IncludeLaunchDescription(
      PythonLaunchDescriptionSource([os.path.join(
         get_package_share_directory('realsense2_camera'), 'launch'),
         '/rs_launch.py'])
      )

   teraranger = LaunchDescription([
        Node(
            package='teraranger_ros2',
            executable='teraranger_ros2_node',
            name='teraranger_node',
            parameters=[{'portname': '/dev/ttyACM1'}],  # Specify your port name here
            arguments=['--ros-args', '-p', 'portname:=/dev/ttyACM0']
        )
    ])

   return LaunchDescription([
      lidar, 
      camera, 
      teraranger
   ])