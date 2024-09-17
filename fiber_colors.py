# Module: fiber_colors.py

# Dictionary of color codes with their corresponding lists of colors
color_codes = {
    "[FR] FT": ("red", "blue", "green", "yellow", "purple", "white", "orange", "grey", "brown", "black", "turquoise", "pink"),
    "[FR] SFR": ("blue", "orange", "green", "brown", "grey", "yellow", "red", "purple", "white", "black", "pink", "turquoise"),
    "FOTAG": ("blue", "orange", "green", "brown", "grey", "white", "red", "black", "yellow", "purple", "pink", "turquoise"),
    "[CH] SWISSCOM CCM": ("red", "green", "yellow", "blue", "white", "purple", "orange", "black", "grey", "brown", "pink", "turquoise"),
    "DIN": ("red", "green", "blue", "yellow", "white", "grey", "brown", "purple", "turquoise", "black", "orange", "pink"),
    "TIA/EIA-589 (MPO)": ("blue", "orange", "green", "brown", "grey", "white", "red", "black", "yellow", "purple", "pink", "turquoise"),
    "IEC": ("blue", "yellow", "red", "white", "green", "purple", "orange", "grey", "turquoise", "black", "brown", "pink"),
    "[BE] FOTAG IEEE 802.8": ("blue", "orange", "green", "brown", "grey", "white", "red", "black", "yellow", "purple", "pink", "turquoise"),
    "IEC 60794-2": ("blue", "yellow", "red", "white", "green", "purple", "orange", "grey", "turquoise", "black", "brown", "pink"),
    "IEC 60304": ("red", "green", "blue", "yellow", "white", "grey", "brown", "purple", "turquoise", "black", "orange", "pink"),
    "TIA/EIA-598 EN 50174-1": ("blue", "orange", "green", "brown", "grey", "white", "red", "black", "yellow", "purple", "pink", "turquoise"),
    "ASF": ("red", "blue", "green", "yellow", "purple", "white", "orange", "grey", "brown", "black", "turquoise", "pink"),
    "BOUYGUES TELECOM": ("red", "blue", "green", "yellow", "purple", "white", "orange", "grey", "brown", "black", "turquoise", "pink"),
    "WORLDCOM": ("blue", "orange", "green", "brown", "grey", "yellow", "red", "purple", "white", "black", "pink", "turquoise"),
    "LD COM": ("blue", "orange", "green", "brown", "grey", "yellow", "red", "purple", "white", "black", "pink", "turquoise"),
    "VIATEL": ("blue", "orange", "green", "brown", "grey", "yellow", "red", "black", "yellow", "purple", "pink", "turquoise"),
    "[FR] SNCF": ("red", "blue", "green", "yellow", "purple", "white", "orange", "grey", "brown", "black", "turquoise", "pink")
}

# List of allowed modulos
allowed_modulos = [2, 4, 6, 12, 24, 36]

def color_all_fibers(capacity, modulo, color_code):
    """
    Returns a list of all fibers and tubes with their colors based on capacity, modulo, and color code.
    Includes the fiber number in the cable.
    """
    if color_code not in color_codes:
        possible_codes = ', '.join(color_codes.keys())
        return f"Unknown color code: '{color_code}'. Possible color codes are: {possible_codes}."
    
    if modulo not in allowed_modulos:
        possible_modulos = ', '.join(map(str, allowed_modulos))
        return f"Invalid modulo: '{modulo}'. Possible modulos are: {possible_modulos}."
    
    colors = color_codes[color_code]
    num_colors = len(colors)
    # Calculate the number of tubes needed
    number_of_tubes = -(-capacity // modulo)  # Ceiling division

    fibers_list = []

    fiber_num_in_cable = 1

    for tube_index in range(number_of_tubes):
        tube_number = tube_index + 1
        color_repeat_count = tube_index // num_colors
        tube_color_index = tube_index % num_colors
        tube_color = colors[tube_color_index]
        if color_repeat_count > 0:
            tube_color_display = f"{tube_color} ({color_repeat_count + 1} rings)"
        else:
            tube_color_display = tube_color

        fibers_in_this_tube = min(modulo, capacity - tube_index * modulo)

        for fiber_index in range(fibers_in_this_tube):
            fiber_number_in_tube = fiber_index + 1
            fiber_color_index = fiber_index % num_colors
            fiber_color = colors[fiber_color_index]

            fibers_list.append({
                'fiber_number': fiber_num_in_cable,
                'tube_number': tube_number,
                'tube_color': tube_color_display,
                'fiber_number_in_tube': fiber_number_in_tube,
                'fiber_color': fiber_color
            })

            fiber_num_in_cable += 1

    # Format the output
    output_lines = []
    header = f"{'Fiber':<6} {'Tube':<6} {'Tube Color':<20} {'Fiber in Tube':<13} {'Fiber Color'}"
    output_lines.append(header)
    output_lines.append('-' * len(header))
    for fiber in fibers_list:
        line = f"{fiber['fiber_number']:<6} {fiber['tube_number']:<6} {fiber['tube_color']:<20} {fiber['fiber_number_in_tube']:<13} {fiber['fiber_color']}"
        output_lines.append(line)

    output = '\n'.join(output_lines)
    return output

def color_one_fiber(capacity, modulo, color_code, fiber_num):
    """
    Returns the color of the fiber, its tube number, and the tube color based on capacity, modulo, and color code.
    Includes the fiber number in the cable.
    """
    if color_code not in color_codes:
        possible_codes = ', '.join(color_codes.keys())
        return f"Unknown color code: '{color_code}'. Possible color codes are: {possible_codes}."
    
    if modulo not in allowed_modulos:
        possible_modulos = ', '.join(map(str, allowed_modulos))
        return f"Invalid modulo: '{modulo}'. Possible modulos are: {possible_modulos}."
    
    if fiber_num < 1 or fiber_num > capacity:
        return f"Fiber number {fiber_num} out of range (1-{capacity})."
    
    colors = color_codes[color_code]
    num_colors = len(colors)
    number_of_tubes = -(-capacity // modulo)  # Ceiling division

    tube_index = (fiber_num - 1) // modulo
    tube_number = tube_index + 1
    fiber_index_in_tube = (fiber_num - 1) % modulo
    fiber_number_in_tube = fiber_index_in_tube + 1

    color_repeat_count = tube_index // num_colors
    tube_color_index = tube_index % num_colors
    tube_color = colors[tube_color_index]
    if color_repeat_count > 0:
        tube_color_display = f"{tube_color} ({color_repeat_count + 1} rings)"
    else:
        tube_color_display = tube_color

    fiber_color_index = fiber_index_in_tube % num_colors
    fiber_color = colors[fiber_color_index]

    output = f"Fiber number {fiber_num} in the cable:\n"
    output += f"  - Tube number {tube_number} ({tube_color_display})\n"
    output += f"  - Fiber number {fiber_number_in_tube} in the tube ({fiber_color})"

    return output
