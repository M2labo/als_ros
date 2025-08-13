from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():
    pkg_dir = get_package_share_directory('als_ros')
    param_file = os.path.join(pkg_dir, 'config', 'mcl_params.yaml')
    map_file = os.path.join(pkg_dir, 'maps', 'map.yaml')

    mcl_node = Node(
        package='als_ros',
        executable='mcl',
        name='mcl',
        namespace='mcl',
        output='screen',
        parameters=[param_file]
    )

    map_server_node = Node(
        package='nav2_map_server',
        executable='map_server',
        name='map_server',
        namespace='map_server',
        output='screen',
        parameters=[
            param_file,
            {'yaml_filename': map_file}
        ]
    )

    base_to_lidar_tf = Node(
        package="tf2_ros",
        executable="static_transform_publisher",
        name="base_to_lidar_transform_node",
        output="screen",
        arguments=[
            "--x", "-0.22", "--y", "0", "--z", "0.975",
            "--roll", "0", "--pitch", "0", "--yaw", "0",
            "--frame-id", "base_link", "--child-frame-id", "laser"
        ]
    )

    return LaunchDescription([
        base_to_lidar_tf,
        map_server_node,
        mcl_node,
    ])
