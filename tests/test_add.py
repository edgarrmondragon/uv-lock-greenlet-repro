from uv_lock_greenlet_repro import add


def test_add():
    assert add(1, 2) == 3
