from typing import Any


def assert_list_values(li: list[Any], values: list[Any]) -> None:
    if len(li) != len(values):
        raise AssertionError(f"list1 len {len(li)} != list2 len {len(values)}")

    invalid_values = [v2 for (v1, v2) in zip(sorted(li), sorted(values)) if v1 != v2]
    if invalid_values:
        raise AssertionError(f"{invalid_values} not found")

    assert True
