# Iterative approach to searching for a key in nested boxes

def look_for_key(main_box):
    pile = main_box.make_a_pile_to_look_through()
    while pile is not empty():
        box = pile.grab_a_box()
        for item in box:
            if item.is_a_box():
                pile.append(item)
            elif item.is_a_key():
                print("Found the key!")

# Use of recursion

def look_for_key(box):
    for item in box:
        if item.is_a_box():
            look_for_key(item)
        elif item.is_a_key():
            print("Found the key!")
# Note: The recursive approach is often more elegant and easier to read,
# especially when dealing with nested structures like boxes within boxes.

        