cmake_minimum_required(VERSION 3.8)
project(als_ros)

# ROS 2 packages
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(sensor_msgs REQUIRED)
find_package(geometry_msgs REQUIRED)
find_package(nav_msgs REQUIRED)
find_package(tf2 REQUIRED)
find_package(tf2_ros REQUIRED)
find_package(tf2_geometry_msgs REQUIRED)
find_package(visualization_msgs REQUIRED)

# System libraries
find_package(OpenCV REQUIRED)
find_package(yaml-cpp REQUIRED)

include_directories(include)

add_executable(mcl src/mcl.cpp)
target_include_directories(mcl PUBLIC include ${OpenCV_INCLUDE_DIRS})
target_link_libraries(mcl ${OpenCV_LIBRARIES} yaml-cpp)

ament_target_dependencies(mcl
  rclcpp
  sensor_msgs
  geometry_msgs
  nav_msgs
  tf2
  tf2_ros
  tf2_geometry_msgs
  visualization_msgs
)

install(TARGETS mcl
  RUNTIME DESTINATION lib/${PROJECT_NAME}
)

install(
  DIRECTORY
  launch 
  config
  map
  DESTINATION share/${PROJECT_NAME}/
)

ament_package()
