import maya.cmds as cmds
import random


class Generator:
    def __init__(self):
        self.my_window = 'ranWin'

    def delete(self):
        if cmds.window(self.my_window, exists=True):
            cmds.deleteUI(self.my_window)

    def create(self):
        self.delete()

        self.my_window = cmds.window(self.my_window,
                                     title='Randomizer',
                                     widthHeight=(200, 200))
        self.col_layout = cmds.columnLayout(parent=self.my_window,
                                            adjustableColumn=True)

        self.amnt = cmds.intField(parent=self.col_layout, minValue=0, maxValue=10, value=0)

        # X Min and Max Input Values
        self.minXInput = cmds.intField(parent=self.col_layout, minValue=-10, maxValue=10, value=0)
        self.maxXInput = cmds.intField(parent=self.col_layout, minValue=-10, maxValue=10, value=0)
        # Y Min and Max Input Values
        self.minYInput = cmds.intField(parent=self.col_layout, minValue=-10, maxValue=10, value=0)
        self.maxYInput = cmds.intField(parent=self.col_layout, minValue=-10, maxValue=10, value=0)
        # Z Min and Max Input Values
        self.minZInput = cmds.intField(parent=self.col_layout, minValue=-10, maxValue=10, value=0)
        self.maxZInput = cmds.intField(parent=self.col_layout, minValue=-10, maxValue=10, value=0)

        cmds.button(parent=self.col_layout, label='Apply', c=lambda *x: self.main(amnt=self.amnt,
                                                                                  minX=self.minXInput,
                                                                                  maxX=self.maxXInput,
                                                                                  minY=self.minYInput,
                                                                                  maxY=self.maxYInput,
                                                                                  minZ=self.minZInput,
                                                                                  maxZ=self.maxZInput))

        cmds.showWindow(self.my_window)

    def main(self, amnt, minX, maxX, minY, maxY, minZ, maxZ):
        myList = []
        selection = cmds.ls(s=True)

        amnt = cmds.intField(self.amnt, q=True, value=True)

        # X Values
        minX = cmds.intField(self.minXInput, q=True, value=True)
        maxX = cmds.intField(self.minXInput, q=True, value=True)
        # Y Values
        minY = cmds.intField(self.minXInput, q=True, value=True)
        maxY = cmds.intField(self.minXInput, q=True, value=True)
        # Z Values
        minZ = cmds.intField(self.minXInput, q=True, value=True)
        maxZ = cmds.intField(self.minXInput, q=True, value=True)

        for x in selection:
            for z in range(0, amnt):
                myList = cmds.duplicate(x)
                cmds.xform(myList, ws=True, t=(random.uniform(minX, maxX), random.uniform(minY, maxY),
                                               random.uniform(minZ, maxZ)))


my_window = Generator()
my_window.create()
