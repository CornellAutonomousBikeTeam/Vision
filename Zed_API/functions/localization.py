########################################################################
#
# Copyright (c) 2017, STEREOLABS.
#
# All rights reserved.
########################################################################

"""
    Built off of StereoLabs position_example for localization
    Position sample shows the position of the ZED camera in a OpenGL window.
"""
from OpenGL.GLUT import *
import positional_tracking.tracking_viewer as tv
import pyzed.camera as zcam
import pyzed.types as tp
import pyzed.core as core
import pyzed.defines as sl
import threading

import csv
import time

class Localization:

    def test():
        print(sl.PyCOORDINATE_SYSTEM.PyCOORDINATE_SYSTEM_RIGHT_HANDED_Y_UP)

    def init(self, dim):
        self.data = []
        self.start(dim)

    def save(self):
        #write csv
        with open("data/data.csv", 'wb') as myfile:
            wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
            wr.writerow(self.data)

    def start(self, dim):
        init = zcam.PyInitParameters(camera_resolution=sl.PyRESOLUTION.PyRESOLUTION_HD720,
                                     depth_mode=sl.PyDEPTH_MODE.PyDEPTH_MODE_PERFORMANCE,
                                     coordinate_units=sl.PyUNIT.PyUNIT_METER,
                                     coordinate_system=sl.PyCOORDINATE_SYSTEM.PyCOORDINATE_SYSTEM_RIGHT_HANDED_Y_UP,
                                     sdk_verbose=True)
        cam = zcam.PyZEDCamera()
        status = cam.open(init)
        if status != tp.PyERROR_CODE.PySUCCESS:
            print(repr(status))
            exit()

        transform = core.PyTransform()
        tracking_params = zcam.PyTrackingParameters(transform)
        cam.enable_tracking(tracking_params)

        runtime = zcam.PyRuntimeParameters()
        camera_pose = zcam.PyPose()

        viewer = tv.PyTrackingViewer()
        viewer.init()

        py_translation = core.PyTranslation()

        if(dim=="2D"):
            start_zed_2D(cam, runtime, camera_pose, viewer, py_translation)
            viewer.exit()
        elif(dim=="3D"):
            start_zed_3D(cam, runtime, camera_pose, viewer, py_translation)

            viewer.exit()
            glutMainLoop()
        

    def start_zed_2D(self. cam, runtime, camera_pose, viewer, py_translation):
        zed_callback = threading.Thread(target=self.run2D, args=(cam, runtime, camera_pose, viewer, py_translation))
        zed_callback.start()

    def run2D(self, cam, runtime, camera_pose, viewer, py_translation):
        while True:
            if cam.grab(runtime) == tp.PyERROR_CODE.PySUCCESS:
                tracking_state = cam.get_position(camera_pose)
                text_translation = ""
                text_rotation = ""
                if tracking_state == sl.PyTRACKING_STATE.PyTRACKING_STATE_OK:
                    rotation = camera_pose.get_rotation_vector()
                    rx = round(rotation[0], 2)
                    ry = round(rotation[1], 2)

                    translation = camera_pose.get_translation(py_translation)
                    tx = round(translation.get()[0], 5)
                    ty = round(translation.get()[1], 5)

                    # store data point
                    data_point = [time.time(), rx, ry, tx, tz]
                    self.data.append(data_point)

                    text_translation = str((tx, ty))
                    text_rotation = str((rx, ry))
                    pose_data = camera_pose.pose_data(core.PyTransform())
                    viewer.update_zed_position(pose_data)

                print(text_translation)
            else:
                tp.c_sleep_ms(1)


def start_zed_3D(self, cam, runtime, camera_pose, viewer, py_translation):
    zed_callback = threading.Thread(target=run, args=(self, cam, runtime, camera_pose, viewer, py_translation))
    zed_callback.start()


def run(self, cam, runtime, camera_pose, viewer, py_translation):
    while True:
        if cam.grab(runtime) == tp.PyERROR_CODE.PySUCCESS:
            tracking_state = cam.get_position(camera_pose)
            text_translation = ""
            text_rotation = ""
            if tracking_state == sl.PyTRACKING_STATE.PyTRACKING_STATE_OK:
                rotation = camera_pose.get_rotation_vector()
                rx = round(rotation[0], 2)
                ry = round(rotation[1], 2)
                rz = round(rotation[2], 2)

                translation = camera_pose.get_translation(py_translation)
                tx = round(translation.get()[0], 2)
                ty = round(translation.get()[1], 2)
                tz = round(translation.get()[2], 2)

                text_translation = str((tx, ty, tz))
                text_rotation = str((rx, ry, rz))
                pose_data = camera_pose.pose_data(core.PyTransform())
                viewer.update_zed_position(pose_data)

            viewer.update_text(text_translation, text_rotation, tracking_state)
        else:
            tp.c_sleep_ms(1)

if __name__ == "__main__":
    l = Localization("2D")
    try:
        l.start()
    finally:
        l.save()
