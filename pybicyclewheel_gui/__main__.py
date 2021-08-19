from pybicyclewheel.xls_calc import *
from pybicyclewheel_gui import *

from tile import *

"""

sample gui for ui control testing

"""

t1 = TileLabel(caption="Sample Label")
t1_0 = TileButton(commandtext="Sample Button")
t2 = TileEntry(caption="Name")
t3 = TileLabel(caption="label text test")
t4 = TileEntryButton(caption="Long long text", commandtext="do-it")
t5 = TileLabel(caption="label sample text test")
t6 = TileLabel(text="ending text label alt spec")
t6_1 = TileLabel()  # caption not set

t_rim_file = TileFileSelect(caption="Rim file", commandtext="...")
t_hub_file = TileFileSelect(caption="Hub file", path="~/repo/pybicyclewheel/")


def gen():
    """generator for combo values"""
    for i in range(0, 4):
        yield i


t_hub = TileEntryCombo(caption="Hub", values=[1, 2, 3, 4])
t_rim = TileEntryCombo(caption="Rim", values=gen())

t_reload = TileLabelButton(caption="reload all rim and hub data files")

t_1 = TileLabel(caption="Sample Label 1")
t_2 = TileLabel(caption="Sample Label 2")
t_3 = TileLabel(caption="Sample Label 3")

t_tab = TileTab(
    source=[
        (
            "first",
            TileRows(
                source=[
                    t_1,
                    TileEntrySpinbox(
                        caption="turn me", spin_opts={"values": [1, 2, 3, 4, 5, 6]}
                    ),
                ]
            ),
        ),
        (
            "second",
            TileRows(
                source=[
                    t_2,
                    TileEntryListbox(
                        caption="select one", values=[5, 6, 7, 8, 9, 10, 11, 12]
                    ),
                ]
            ),
        ),
        ("third", TileRows(source=[t_3])),
        (
            "rims",
            TileRows(
                source=[
                    t_rim_file,
                ]
            ),
        ),
        (
            "hubs",
            TileRows(
                source=[
                    t_hub_file,
                    TileEntryCombo(caption="whatever", values=[11, 21, 31, 41]),
                ]
            ),
        ),
    ]
)


mainframe = Tile(Tile.tk)
# mainframe.title("pyBicycleWheel")

t_close = TileLabelButton(caption="close app", command=mainframe.quit)

l7 = TileRows(
    source=[t1, t1_0, t2, t3, t4, t5, t6, t6_1, t_hub, t_rim, t_reload, t_close, t_tab]
)

mainframe.add(l7)
mainframe.layout()

mainframe.geometry("+100+100")
mainframe.resize_grip()

mainframe.mainloop()
