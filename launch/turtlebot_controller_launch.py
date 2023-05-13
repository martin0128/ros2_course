import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, DeclareLaunchArgument
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description():
    # Arguments
    world_file = DeclareLaunchArgument(
        'world_file',
        default_value=os.path.join(
            get_package_share_directory('turtlebot3_gazebo'),
            'worlds',
            'turtlebot3_house.world'),
        description='Path to world file')

    # Launch Gazebo
    gazebo_launch_file = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(os.path.join(
            get_package_share_directory('turtlebot3_gazebo'),
            'launch',
            'turtlebot3_house.launch.py')),
        launch_arguments=[('world', LaunchConfiguration('world_file'))])

    # Set the TurtleBot model type
    os.environ['TURTLEBOT3_MODEL'] = 'burger'

    # Launch turtlebot_controller.py
    controller_node = Node(
        package='ros2_course',
        executable='turtlebot_controller',
        output='screen'
    )

    # Combine launch description
    ld = LaunchDescription()
    ld.add_action(world_file)
    ld.add_action(gazebo_launch_file)
    ld.add_action(controller_node)

    return ld
