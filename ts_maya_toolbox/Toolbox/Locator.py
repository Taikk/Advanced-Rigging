import maya.cmds as cmds


def create_locator():
    # Create a locator at the center of the current selection
    # first make selection in scene
    # get selection and assign variable
    # Find center point of selection
    # create a locator
    # assign locator position

    sels = cmds.ls(sl=True)

    bbox = cmds.exactWorldBoundingBox(sels)
    x_pos = (bbox[0] + bbox[3]) / 2
    y_pos = (bbox[1] + bbox[4]) / 2
    z_pos = (bbox[2] + bbox[5]) / 2

    locator = cmds.spaceLocator(p=[0, 0, 0])
    cmds.xform(locator, worldSpace=True, translation=[x_pos, y_pos, z_pos])

    cmds.select(locator, r=True)

    return locator
create_locator()