def divide_advanced(a: float, b: float) -> dict:
    if b == 0:
        return {"error": "Cannot divide by zero"}

    return {
        "result": a / b,        # ผลหารทศนิยม
        "quotient": a // b,     # ผลหารจำนวนเต็ม
        "remainder": a % b      # เศษเหลือ
    }

# ส่วนรับค่าจาก Terminal และแสดงผล
try:
    num1 = float(input("กรอกตัวตั้ง (a): "))
    num2 = float(input("กรอกตัวหาร (b): "))
    
    result = divide_advanced(num1, num2)
    print("ผลลัพธ์:", result)

except ValueError:
    print("ข้อผิดพลาด: กรุณากรอกเฉพาะตัวเลขเท่านั้น")



    