from assert_list import assert_list_values


def test_assert_values() -> None:
    li = [[], [1], [2], [2, 3], [1, 2, 3]]
    values = [[], [1], [2], [2, 3], [1, 2, 3]]
    assert_list_values(li, values)

    try:
        assert_list_values(li, [1, 2, 3])
    except AssertionError as _:
        pass
