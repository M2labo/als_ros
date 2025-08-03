cmake_minimum_required(VERSION 3.8)
project(als_ros)

find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(sensor_msgs REQUIRED)
find_package(geometry_msgs REQUIRED)
find_package(visualization_msgs REQUIRED)

add_executable(scan2pc src/scan2pc.cpp)
ament_target_dependencies(scan2pc rclcpp sensor_msgs geometry_msgs)

add_executable(slamer src/slamer.cpp)
ament_target_dependencies(slamer rclcpp sensor_msgs geometry_msgs visualization_msgs)

install(TARGETS scan2pc
  DESTINATION lib/${PROJECT_NAME})

install(TARGETS slamer
  DESTINATION lib/${PROJECT_NAME})

ament_package()
