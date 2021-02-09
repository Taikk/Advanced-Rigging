import maya.cmds as cmds


class Renamer:
    def __init__(self):
        self.my_window = 'WindowUI'

    def delete(self):
        if cmds.window(self.my_window, exists=True):
            cmds.deleteUI(self.my_window)

    def create(self):
        self.delete()

        self.my_window = cmds.window(self.my_window,
                                     title='Rename',
                                     widthHeight=(200, 200))
        self.col_layout = cmds.columnLayout(parent=self.my_window,
                                            adjustableColumn=True)
        self.input = cmds.textField(parent=self.col_layout,
                                    placeholderText='Enter new Name...')
        cmds.button(parent=self.col_layout, label='Rename', c=lambda *x: self.SequentialRenamer())
        cmds.showWindow(self.my_window)

    def SequentialRenamer(self):
        sel = cmds.ls(selection=True)
        selection_count = 1

        for _ in sel:
            field_val = cmds.textField(self.input, q=True, text=True)
            selection_input = field_val.count("#")
            string_parts = field_val.partition("#" * selection_input)
            sequential_numbering = str(selection_count)

            if string_parts[1]:
                print "Characters are sequential."
                sequential_numbering = sequential_numbering.zfill(3)
                cmds.rename(string_parts[0] + sequential_numbering + string_parts[2])

            else:
                cmds.error("Characters are not sequential. Input another.")

            selection_count += 1


my_window = Renamer()
my_window.create()
