cmake_minimum_required(VERSION 3.8)
project(als_ros)

find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(sensor_msgs REQUIRED)
find_package(geometry_msgs REQUIRED)
find_package(nav_msgs REQUIRED)
find_package(tf2 REQUIRED)
find_package(tf2_ros REQUIRED)
find_package(tf2_geometry_msgs REQUIRED)
find_package(visualization_msgs REQUIRED)

add_executable(mcl src/mcl.cpp)
ament_target_dependencies(mcl rclcpp sensor_msgs geometry_msgs nav_msgs tf2 tf2_ros tf2_geometry_msgs visualization_msgs)

install(TARGETS mcl
  DESTINATION lib/${PROJECT_NAME})

ament_package()
