from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import IncludeLaunchDescription, DeclareLaunchArgument
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration, PythonExpression, PathJoinSubstitution, TextSubstitution

def generate_launch_description():
    ld = LaunchDescription()
    
    host_arg = DeclareLaunchArgument(
        "host", default_value=TextSubstitution(text="10.4.25.99")
    )
    ld.add_action(host_arg)
    port_arg = DeclareLaunchArgument(
        "port", default_value=TextSubstitution(text="'9100'")
    )
    ld.add_action(port_arg)
    odometry_timeout_arg = DeclareLaunchArgument(
        "odometry_timeout", default_value=TextSubstitution(text="1.0")
    )
    ld.add_action(odometry_timeout_arg)
    threshold_linear_slow_arg = DeclareLaunchArgument(
        "threshold_linear_slow", default_value=TextSubstitution(text="0.4")
    )
    ld.add_action(threshold_linear_slow_arg)
    threshold_linear_fast_arg = DeclareLaunchArgument(
        "threshold_linear_fast", default_value=TextSubstitution(text="0.9")
    )
    ld.add_action(threshold_linear_fast_arg)
    threshold_angular_fast_arg = DeclareLaunchArgument(
        "threshold_angular_fast", default_value=TextSubstitution(text="1.0")
    )
    ld.add_action(threshold_angular_fast_arg)
    marker_type_arg = DeclareLaunchArgument(
        "marker_type", default_value=TextSubstitution(text="11")
    )
    ld.add_action(marker_type_arg)
    scale_x_arg = DeclareLaunchArgument(
        "scale_x", default_value=TextSubstitution(text="1.0")
    )
    ld.add_action(scale_x_arg)
    scale_y_arg = DeclareLaunchArgument(
        "scale_y", default_value=TextSubstitution(text="1.0")
    )
    ld.add_action(scale_y_arg)
    scale_z_arg = DeclareLaunchArgument(
        "scale_z", default_value=TextSubstitution(text="1.0")
    )
    ld.add_action(scale_z_arg)
    has_wireless_emstop_arg = DeclareLaunchArgument(
        "has_wireless_emstop", default_value=TextSubstitution(text="false")
    )
    ld.add_action(has_wireless_emstop_arg)
    warn_for_laser_bridged_arg = DeclareLaunchArgument(
        "warn_for_laser_bridged", default_value=TextSubstitution(text="false")
    )
    ld.add_action(warn_for_laser_bridged_arg)
    warn_for_wireless_bridged_arg = DeclareLaunchArgument(
        "warn_for_wireless_bridged", default_value=TextSubstitution(text="false")
    )
    ld.add_action(warn_for_wireless_bridged_arg)
    reconnect_attempts_arg = DeclareLaunchArgument(
        "reconnect_attempts", default_value=TextSubstitution(text="5")
    )
    ld.add_action(reconnect_attempts_arg)
    reconnect_duration_arg = DeclareLaunchArgument(
        "reconnect_duration", default_value=TextSubstitution(text="5.0")
    )
    ld.add_action(reconnect_duration_arg)
    footprint_angular_slow_arg = DeclareLaunchArgument(
        "footprint_angular_slow", default_value=TextSubstitution(text="[[0.4, 0.4], [-0.4, 0.4], [-0.4, -0.4], [0.4, -0.4]]")
    )
    ld.add_action(footprint_angular_slow_arg)
    footprint_angular_fast_arg = DeclareLaunchArgument(
        "footprint_angular_fast", default_value=TextSubstitution(text="[[0.5, 0.5], [-0.5, 0.5], [-0.5, -0.5], [0.5, -0.5]]")
    )
    ld.add_action(footprint_angular_fast_arg)
    footprint_linear_slow_arg = DeclareLaunchArgument(
        "footprint_linear_slow", default_value=TextSubstitution(text="[[0.6, 0.4], [-0.4, 0.4], [-0.4, -0.4], [0.6, -0.4]]")
    )
    ld.add_action(footprint_linear_slow_arg)
    footprint_linear_fast_arg = DeclareLaunchArgument(
        "footprint_linear_fast", default_value=TextSubstitution(text="[[0.8, 0.4], [-0.4, 0.4], [-0.4, -0.4], [0.8, -0.4]]")
    )
    ld.add_action(footprint_linear_fast_arg)

    safety_controller = Node(
        package="cob_safety_controller",
        namespace="safety_controller",
        executable="safety_controller",
        prefix = 'xterm -e',
        output='screen',
        name="safety_controller",
        parameters=[{
        "host": LaunchConfiguration("host"),
        "port": LaunchConfiguration("port"),
        "odometry_timeout": LaunchConfiguration("odometry_timeout"),
        "threshold_linear_slow": LaunchConfiguration("threshold_linear_slow"),
        "threshold_linear_fast": LaunchConfiguration("threshold_linear_fast"),
        "threshold_linear_fast": LaunchConfiguration("threshold_angular_fast"),
        "marker_type": LaunchConfiguration("marker_type"),
        "scale_x": LaunchConfiguration("scale_x"),
        "scale_y": LaunchConfiguration("scale_y"),
        "scale_z": LaunchConfiguration("scale_z"),
        "has_wireless_emstop": LaunchConfiguration("has_wireless_emstop"),
        "warn_for_laser_bridged": LaunchConfiguration("warn_for_laser_bridged"),
        "warn_for_wireless_bridged": LaunchConfiguration("warn_for_wireless_bridged"),
        "reconnect_attempts": LaunchConfiguration("reconnect_attempts"),
        "reconnect_duration": LaunchConfiguration("reconnect_duration"),
        "footprint_angular_slow": LaunchConfiguration("footprint_angular_slow"),
        "footprint_angular_fast": LaunchConfiguration("footprint_angular_fast"),
        "footprint_linear_slow": LaunchConfiguration("footprint_linear_slow"),
        "footprint_linear_fast": LaunchConfiguration("footprint_linear_fast"),}]
    )

    ld.add_action(safety_controller)

    return ld
