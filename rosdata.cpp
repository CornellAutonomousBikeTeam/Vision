#include <ros/ros.h>
#include <sensor_msgs/Image.h>


void confidence(const sensor_msgs::Image::ConstPtr& msg) {

    // Get a pointer to the depth values casting the data
    // pointer to floating point
    float* depths = (float*)(&msg->data[0]);

    // Image coordinates of the center pixel
    int u = msg->width / 2;
    int v = msg->height / 2;

    // Linear index of the center pixel
    int centerIdx = u + msg->width * v;

    // Output the measure
    ROS_INFO("Center distance : %g m", depths[centerIdx]);
}

int main(int argc, char** argv) {

    ros::init(argc, argv, "zed_confidence_map");

    ros::NodeHandle n;

    ros::Subscriber cmap = n.subscribe("/zed/zed_node/confidence/confidence_map", 10, confidence);


    ros::spin();

    return 0;
}

