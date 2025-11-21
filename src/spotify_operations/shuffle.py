import random
import time
import reorder_playlist

def shuffle_helper(sp, uid: str, length: int) -> None:
    new_order = list(range(length))
    random.shuffle(new_order)
    positions = list(range(length))
    reorder_playlist.reorder_playlist(sp,uid, new_order,positions)
