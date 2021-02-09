import maya.cmds as cmds


def freeze():
    cmds.makeIdentity(apply=True, t=1, r=1, s=1, n=0)