import time

from pybicyclewheel.dataloader import RimDataLoader, HubDataLoader

from pybicyclewheel.rim import Rim
from pybicyclewheel.hub import Hub
from pybicyclewheel.wheel import Wheel

# your data here

rim_idx = 3  # a719_3
hub_idx = 5  # deore_t610_36

cross = 3
spoke = 2.0

# same crossing pattern on both sides

cross_l = cross
cross_r = cross

# calc

rdl = RimDataLoader("./rims.xls").load_xls()

xls_off = -2

rim_dims = rdl.get_dims(rim_idx + xls_off)
print("rim", rim_dims)
print("rim", rdl.get_row(rim_idx + xls_off))
print()

hdl = HubDataLoader("./hubs.xls").load_xls()

hub_dims = hdl.get_dims(hub_idx + xls_off)
print("hub", hub_dims)
print("hub", hdl.get_row(hub_idx + xls_off))
print()

if rim_dims.holes != hub_dims.holes:
    raise Exception("holes different")

rim = Rim(rim_dims.erd)

hub = Hub(
    hub_dims.holes,
    diameter_l=hub_dims.flange_diameter_left,
    diameter_r=hub_dims.flange_diameter_right,
    distance_l=-hub_dims.flange_distance_left,
    distance_r=hub_dims.flange_distance_right,
    spoke_hole=hub_dims.spoke_hole,
)

wheel = Wheel(hub=hub, rim=rim, cross_l=cross_l, cross_r=cross_r, spoke=spoke)

print("spoke length (left, right) mm", wheel.spoke_lr())
print("rim", rim)
print("hub", hub)
# print("wheel", wheel)
print("---", time.asctime(time.localtime(time.time())), "---")
