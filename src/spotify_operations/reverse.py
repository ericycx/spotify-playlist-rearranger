import time

def reverse_helper(sp, uid: str, length: int) -> None:
    new_order = list(range(length))
    positions = list(range(length))
    for orig_idx in new_order:
        current_pos = positions.index(orig_idx)
        print(f"Moving track at current_pos={current_pos}")
        sp.playlist_reorder_items(uid, range_start=current_pos, insert_before=0)
        moved = positions.pop(current_pos)
        positions.insert(0, moved)
        time.sleep(0.1)
