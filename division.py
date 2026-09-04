def divide(a: float | int, b: float | int) -> float:
    """หารจำนวนสองจำนวน

    Args:
        a: ตัวตั้ง (Numerator)
        b: ตัวหาร (Denominator)

    Returns:
        ผลลัพธ์การหารเป็น float

    Raises:
        ValueError: เมื่อตัวหาร (b) มีค่าเป็น 0
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b