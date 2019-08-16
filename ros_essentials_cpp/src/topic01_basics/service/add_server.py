#!/usr/bin/env python

from ros_essentials_cpp.srv import AddTwoInts
from ros_essentials_cpp.srv import AddTwoIntsRequest
from ros_essentials_cpp.srv import AddTwoIntsResponse

import rospy

def handle_add_two_ints(req):
    print "Returning [%s + %s = %s]"%(req.a, req.b, (req.a + req.b))
    return AddTwoIntsResponse(req.a + req.b)
    #return to response

def add_two_ints_server():
    rospy.init_node('add_two_ints_server')#initialize the node
    s = rospy.Service('add_two_ints', AddTwoInts, handle_add_two_ints)
    #create a server listen to incoming request 
    #'add_two_ints' is the name of the service
    #AddTwoInts is the type of message
    #handle_add_two_ints is the function be called everytime a new request comming
    print "Ready to add two ints."
    rospy.spin()
    
if __name__ == "__main__":
    add_two_ints_server()