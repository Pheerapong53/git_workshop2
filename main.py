from addition import add

def main():
    print("***Calculator Program***")
    print("1. บวก") 
    print("2. ลบ") #1
    print("3. คูณ") #2
    print("4. หาร") #3,4
    print("5. หาค่าเฉลี่ย") #5,6
    print("6. ยกกำลัง") #7,8
    print("7. หาค่าสูงสุด") #9,10
    print("8. หาค่าต่ำสุด") #11,12
    print("9. ปิดโปรแกรม")

while True:
    choice = input("เลือกรายการ: ")

    if choice == "9":
        print("ปิดโปรแกรม")
        break

    if choice not in ["1", "2", "3", "4", "5", "6","7","8"]:
        print("เลือกเมนูไม่ถูกต้อง")
        continue

    num1 = float(input("Enter num1: "))
    num2 = float(input("Enter num2: "))

    if choice == "1":
        result = add(num1, num2)
    elif choice == "2":
        result = num1 - num2
    else:
        print("อยู่ระหว่างการพัฒนา")

    print("Result: ", result)
    