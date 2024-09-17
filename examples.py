from fiber_colors import color_one_fiber, color_all_fibers


result = color_all_fibers(36, 12, "[FR] FT")
print(result)

result = color_all_fibers(432, 12, "[FR] FT")
print(result)

fiber_info = color_one_fiber(24, 12, "[FR] FT", 13)
print(fiber_info)