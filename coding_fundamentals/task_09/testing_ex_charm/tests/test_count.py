from programs import count


def test_count():
    assert count.count([1, 2, 2, 3, 4], 2) == 2
