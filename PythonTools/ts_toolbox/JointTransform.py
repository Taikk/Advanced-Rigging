import maya.cmds as cmds


class JointTransform:
    def __init__(self):
        self.my_window = 'tsJointWindow'

    def delete(self):
        if cmds.window(self.my_window, exists=True):
            cmds.deleteUI(self.my_window)

    def create(self):
        self.delete()

        self.my_window = cmds.window(self.my_window,
                                     title='Joint Transform Display',
                                     widthHeight=(200, 200))
        self.col_layout = cmds.columnLayout(parent=self.my_window,
                                            adjustableColumn=True)
        cmds.button(parent=self.col_layout,
                    label='JointDisplayOn',
                    c=lambda *x: self.setAxisDisplay(1, 1))
        cmds.button(parent=self.col_layout,
                    label='JointDisplayOFF',
                    c=lambda *x: self.setAxisDisplay(0, 0))
        cmds.showWindow(self.my_window)

    def setAxisDisplay(self, display=False, allObj=False):
        # if no joints are selected, do it for all the joints in the scene
        # if allObj flag is True then this will toggle the axis display for all objects in the scene, not just joints.
        if not allObj:
            if len(cmds.ls(sl=1, type="joint")) == 0:
                jnt_List = cmds.ls(type="joint")
            else:
                jnt_List = cmds.ls(sl=1, type="joint")
            # set the displayLocalAxis attribute to what the user specifies.
            for x in jnt_List:
                cmds.setAttr(x + ".displayLocalAxis", display)
        else:
            if len(cmds.ls(sl=1)) == 0:
                List = cmds.ls(transforms=1)
            else:
                List = cmds.ls(sl=1)
            # set the displayLocalAxis attribute to what the user specifies.
            for z in List:
                cmds.setAttr(z + ".displayLocalAxis", display)

    # turn off the Local Rotation Axis display for all transform nodes in the scene
    #setAxisDisplay(display=False, allObj=True)



my_window = JointTransform()
my_window.create()
