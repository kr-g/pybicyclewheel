import time

from pybicyclewheel.xls_calc import wheel_calc

# your data here - the index is the line number in the xls sheet

rim_idx = 3  # a719_3
hub_idx = 5  # deore_t610_36

cross = 3
spoke = 2.0

# same crossing pattern on both sides

cross_l = cross
cross_r = cross

# wheel_calc - new in v0.0.5

spoke_lr, wheel, rim_dims, rim_info, hub_dims, hub_info = wheel_calc(rim_idx, hub_idx)

rim = wheel.rim
hub = wheel.hub

print("rim", rim_dims)
print("rim", rim_info)
print()

print("hub", hub_dims)
print("hub", hub_info)
print()

print("spoke length (left, right) mm", spoke_lr)
print("rim", rim)
print("hub", hub)
# print("wheel", wheel)
print("---", time.asctime(time.localtime(time.time())), "---")
