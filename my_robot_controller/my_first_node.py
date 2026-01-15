#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

class MyNode(Node):

    def __init__(self):
        super().__init__("first_node") #our node
        self.counter_ = 0 #start counter
        self.create_timer(1.0, self.timer_callback) #timerfunction in ROS

    def timer_callback(self):
        self.get_logger().info("Hello" + str(self.counter_)) #print function in ROS
        self.counter_ += 1 #update counter

def main(args=None):
    rclpy.init(args=args) #initialized ros2 communication
    node = MyNode() #start your node here
    rclpy.spin(node)
    rclpy.shutdown() #last line which is mandatory

if __name__== '__main__':
    main()