# Calculator Program

A simple Python calculator project for practicing **Python programming** and **Git/GitHub collaboration**.

## Project Objective

Students will work together to develop a Calculator Program. Each student or team is responsible for implementing an assigned calculator function in their own Git branch.

After development is completed, all branches will be merged into the `main` branch to create the complete Calculator Program.

## Calculator Menu

The program provides the following menu:

```text
***Calculator Program***

1. บวก
2. ลบ
3. คูณ
4. หาร
5. หาค่าเฉลี่ย
6. ยกกำลัง
7. หาค่าสูงสุด
8. หาค่าต่ำสุด
9. ปิดโปรแกรม
```

## Calculator Functions

| Menu | Function       | Description | Example              |
| ---- | -------------- | ----------- | -------------------- |
| 1    | Addition       | บวกตัวเลข   | `10 + 5 = 15`        |
| 2    | Subtraction    | ลบตัวเลข    | `10 - 5 = 5`         |
| 3    | Multiplication | คูณตัวเลข   | `10 × 5 = 50`        |
| 4    | Division       | หารตัวเลข   | `10 ÷ 5 = 2`         |
| 5    | Average        | หาค่าเฉลี่ย | `(10 + 20) / 2 = 15` |
| 6    | Power          | ยกกำลัง     | `2³ = 8`             |
| 7    | Maximum        | หาค่าสูงสุด | `max(10, 20) = 20`   |
| 8    | Minimum        | หาค่าต่ำสุด | `min(10, 20) = 10`   |
| 9    | Exit           | ปิดโปรแกรม  | `Exit`               |

## Student Assignment

แบ่งหน้าที่การพัฒนาฟังก์ชัน ดังนี้

| Function       | Student        |
| -------------- | -------------- |
| Addition       | Teacher   |
| Subtraction    | Student 1      |
| Multiplication | Student 2      |
| Division       | Student 3, 4   |
| Average        | Student 5, 6   |
| Power          | Student 7, 8   |
| Maximum        | Student 9, 10  |
| Minimum        | Student 11, 12 |

นักเรียนแต่ละคนหรือแต่ละทีมจะพัฒนาฟังก์ชันที่ได้รับมอบหมายบน Branch ของตนเอง

## Project Structure

```text
calculator/
│
├── main.py
├── addition.py
├── subtraction.py
├── multiplication.py
├── division.py
├── average.py
├── power.py
├── maximum.py
├── minimum.py
└── README.md
```

## Function Examples

### 1. Addition

```python
def add(a, b):
    return a + b
```

### 2. Subtraction

```python
def subtract(a, b):
    return a - b
```

### 3. Multiplication

```python
def multiply(a, b):
    return a * b
```

### 4. Division

```python
def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b
```

### 5. Average

```python
def average(a, b):
    return (a + b) / 2
```

### 6. Power

```python
def power(base, exponent):
    return base ** exponent
```

### 7. Maximum

```python
def maximum(a, b):
    return max(a, b)
```

### 8. Minimum

```python
def minimum(a, b):
    return min(a, b)
```

## Main Program

`main.py` ทำหน้าที่แสดงเมนู รับคำสั่งจากผู้ใช้งาน และเรียกใช้ฟังก์ชันที่เกี่ยวข้อง

ตัวอย่างโครงสร้างเมนู:

```python
while True:
    print("***Calculator Program***")
    print("1. บวก")
    print("2. ลบ")
    print("3. คูณ")
    print("4. หาร")
    print("5. หาค่าเฉลี่ย")
    print("6. ยกกำลัง")
    print("7. หาค่าสูงสุด")
    print("8. หาค่าต่ำสุด")
    print("9. ปิดโปรแกรม")

    choice = input("เลือกเมนู: ")

    if choice == "9":
        print("ปิดโปรแกรม")
        break
```

## Running the Program

ตรวจสอบว่าเครื่องมี Python ติดตั้งเรียบร้อยแล้ว จากนั้นรัน:

```bash
python main.py
```

## Git Workflow

### 1. Clone Repository

```bash
git clone <repository-url>
cd <repository-name>
```

### 2. Create Your Branch

นักเรียนแต่ละคนสร้าง Branch ของตนเอง

```bash
git checkout -b <your-name>
```

ตัวอย่าง:

```bash
git checkout -b siwat
```

### 3. Check Current Branch

```bash
git branch
```

ตัวอย่าง:

```text
  main
* siwat
```

เครื่องหมาย `*` แสดง Branch ที่กำลังทำงานอยู่

### 4. Develop Your Function

พัฒนาฟังก์ชันที่ได้รับมอบหมาย และทดสอบให้สามารถทำงานได้อย่างถูกต้อง

### 5. Check Changes

```bash
git status
```

### 6. Add Changes

```bash
git add .
```

### 7. Commit Changes

```bash
git commit -m "Add calculator function"
```

ควรเขียน Commit Message ให้สื่อความหมายกับสิ่งที่พัฒนา เช่น:

```bash
git commit -m "Add division function"
```

### 8. Push Your Branch

```bash
git push -u origin <your-name>
```

ตัวอย่าง:

```bash
git push -u origin siwat
```

## Important Rules

นักเรียน **ไม่ควรพัฒนาโดยตรงบน `main` branch**

ขั้นตอนการทำงาน:

1. สร้าง Branch ของตนเอง
2. พัฒนาฟังก์ชันที่ได้รับมอบหมาย
3. ทดสอบฟังก์ชัน
4. `git add`
5. `git commit`
6. `git push`
7. แจ้งผู้สอนเมื่อดำเนินการเสร็จ

หลังจากนั้นผู้สอนจะตรวจสอบและ Merge Branch ของนักเรียนแต่ละคนเข้าสู่ `main`

## Learning Outcomes

หลังจาก Workshop นักเรียนควรมีความเข้าใจเกี่ยวกับ:

* Python Functions
* Python Modules
* Modular Programming
* Git Repository
* Git Branch
* Git Commit
* Git Push / Pull
* Git Merge
* Merge Conflict
* การทำงานร่วมกันผ่าน Git/GitHub
