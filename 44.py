def divide_advanced(a: float, b: float) -> dict:
    if b == 0:
        return {"error": "Cannot divide by zero"}
    
    return {
        "result": a / b,            # ผลหารทศนิยม
        "quotient": a // b,         # ผลหารจำนวนเต็ม
        "remainder": a % b,         # เศษที่เหลือ
    }

# ตัวอย่างการใช้งาน
print(divide_advanced(10, 3))
# Output: {'result': 3.3333333333333335, 'quotient': 3.0, 'remainder': 1.0}