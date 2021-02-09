import maya.cmds as cmds
import maya.mel as mel


def deleteHistory():
    mel.eval("DeleteAllHistory")
    print "History Deleted"
