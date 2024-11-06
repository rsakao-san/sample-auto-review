from typing import List, Union

def calculate_average(numbers: List[Union[int, float]]) -> float:
    """数値のリストの平均値を計算します。

    Args:
        numbers (List[Union[int, float]]): 計算対象の数値リスト

    Returns:
        float: 平均値

    Raises:
        ValueError: リストが空の場合
        TypeError: リストに数値以外の要素が含まれる場合
    """
    if not numbers:
        raise ValueError("空のリストの平均値は計算できません")

    total = 0
    for number in numbers:
        if not isinstance(number, (int, float)):
            raise TypeError(f"数値以外の要素が含まれています: {number}")
        total += number

    return total / len(numbers)
