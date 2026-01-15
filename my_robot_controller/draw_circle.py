#!/usr/bin/env/ python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class DrawCircleNode(Node): #blueprint to create a node *blueprint

    def __init__(self): #constructor
        super().__init__("draw_circle")
        self.cmd_vel_pub_ = self.create_publisher(Twist, "/turtle1/cmd_vel", 10) #parameter : topic type, name, q size (creating topic)
        self.timer = self.create_timer(0.5, self.send_velocity_command) #every 0.5 sec, send_command_velocity will be called (this is what we call callback)
        self.get_logger().info("Draw circle node has been started")

    def send_velocity_command(self):
        msg = Twist()
        msg.linear.x = 2.0
        msg.angular.z = 1.0
        self.cmd_vel_pub_.publish(msg) #publish the message to topic

def main (args=None):
    rclpy.init(args = args)
    node = DrawCircleNode() #node created
    rclpy.spin(node) #spin the node (run the node) *loop
    rclpy.shutdown() #end looping
    #test
