import os
from ament_index_python.packages import get_package_share_directory as pkg
from launch import LaunchDescription
from launch.actions import (IncludeLaunchDescription, SetEnvironmentVariable,
                            TimerAction)
from launch.launch_description_sources import PythonLaunchDescriptionSource as Src


def generate_launch_description():
    gz = pkg('turtlebot3_gazebo')
    nav = pkg('turtlebot3_navigation2')
    me = pkg('tb3_nav_demo')

    gazebo = IncludeLaunchDescription(
        Src(os.path.join(gz, 'launch', 'turtlebot3_world.launch.py')))

    navigation = IncludeLaunchDescription(
        Src(os.path.join(nav, 'launch', 'navigation2.launch.py')),
        launch_arguments={
            'use_sim_time': 'True',
            'map': os.path.join(me, 'maps', 'map.yaml'),
            'params_file': os.path.join(nav, 'param', 'humble', 'waffle.yaml'),
        }.items())

    return LaunchDescription([
        SetEnvironmentVariable('TURTLEBOT3_MODEL', 'waffle'),
        SetEnvironmentVariable('GAZEBO_MODEL_DATABASE_URI', ''),
        gazebo,
        TimerAction(period=8.0, actions=[navigation]),
    ])
