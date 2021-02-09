import maya.cmds as cmds

def parentConstrain():
    sel = cmds.ls(s=True)
    for x in sel:
        cmds.parentConstraint(mo=True, w=True)