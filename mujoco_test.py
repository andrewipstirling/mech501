# add path
import sys
import mujoco
import mujoco_viewer
import numpy as np
path = sys.path[0]
model = mujoco.MjModel.from_xml_path('./xml/inverted_pendulum.xml')
data = mujoco.MjData(model)
viewer = mujoco_viewer.MujocoViewer(model, data)
while data.time < 40:
    if viewer.is_alive:
        viewer.render()
    else:
        break
viewer.close()