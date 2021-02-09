import ts_toolbox.PolyCreate as create

reload(create)
cheese = create.PolyCreate()
cheese.create()


"""import ts_toolbox.toolbox_window as window

reload(window)
tool = window.Window()
tool.create()"""
import ts_toolbox.toolbox_window as toolbox

reload(toolbox)
my_tool = toolbox.Window()
my_tool.create()