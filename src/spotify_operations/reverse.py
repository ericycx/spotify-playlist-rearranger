import time
import reorder_playlist

def reverse_helper(sp, uid: str, length: int) -> None:
    new_order = list(range(length))
    positions = list(range(length))
    reorder_playlist.reorder_playlist(sp,uid, new_order,positions)
