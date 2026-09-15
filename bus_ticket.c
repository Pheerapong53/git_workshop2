#include <stdio.h>

int main() {
    int n;
    if (scanf("%d", &n) != 1) return 0;

    // ทำการบวกหลักไปเรื่อยๆ จนกว่าค่าจะเหลือหลักเดียว (< 10)
    while (n >= 10) {
        int sum = 0;
        while (n > 0) {
            sum += n % 10;
            n /= 10;
        }
        n = sum;
    }

    // พิมพ์ผลลัพธ์และขึ้นบรรทัดใหม่ตามข้อกำหนด
    printf("%d\n", n);

    return 0;
}