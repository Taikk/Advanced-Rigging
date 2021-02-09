import maya.cmds as cmds

def parent():
    selection = cmds.ls(s=True)
    cmds.group(selection, n='NewGroup')