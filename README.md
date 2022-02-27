# Stereo-Vision

## Implementation of Stereo Vision/Triangulation with IMX 219-83 Stereo Camera

To calculate the depth of an object, an IMX 219-83 stereo camera, mounted on the head of the humanoid platform, is used keeping in mind the consideration of the height of an average human being. Hence, the depth obtained is the same as compared to human vision.

Major parameters of  IMX 219-83 Stereo camera taken into consideration:
* Field of view (FOV) - 60 deg
* Resolution of the camera - 640*480
* Distance of separation of two cameras  - 6cm

##### Representation of Stereo Camera and image

![img](https://github.com/MAYA-1-0/Stereo-Vision/blob/main/images/Screenshot%20from%202022-02-27%2021-45-11.png)


The main application of Stereo vision implemented here is face attention,
This module detects a face and continously looks at the detected face in real time through humanoid's neck (Roll, Pitch, Yaw), which has 3 dynamixel motors.

Usage and Requirements:

1. Pull docker image for dynamixel motor control.
```
docker pull mayakle/maya_head:latest
```

2. Clone this repository to your ROS Workspace and put it under a package created by you with name stereo_vision (otherwise existing package.xml and cmakelists.txt file can be deleted and new package can be built with any other name)

3. Clone the opencv repository for using haarcascade classifier
```
git clone https://github.com/opencv/opencv.git
```
