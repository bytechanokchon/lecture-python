# Python Interpreter
Python Interpreter คือโปรแกรมที่ทำหน้าที่อ่านคำสั่งภาษา Python แล้วประมวลผลคำสั่งเหล่านั้นให้คอมพิวเตอร์ทำงานตามที่เราต้องการ

## 2.1 การเรียกใช้งาน Python Interpreter (Invoking the Interpreter)
โดยทั่วไป เมื่อติดตั้ง Python เรียบร้อยแล้ว เราสามารถเปิดใช้งานผ่าน Terminal หรือ Command Prompt ได้

ตัวอย่างสำหรับ windows สามารถใช้งานคำสั่ง

    python

หรือ

    py

การออกจาก Python Interpreter สามารถกดปุ่ม `Ctrl + Z` หรือพิมพ์คำสั่ง `quit()`

#### การใช้งานคำสั่ง Python แบบอื่น ๆ
- `python -c` ใช้รันคำสั่ง Python ที่ระบุผ่าน Command Line โดยตรง
- `python -m` ใช้เรียกใช้งานโมดูล Python ในรูปแบบโปรแกรม
- `python -i` ใช้เปิดโหมด Interactive หลังจากรันไฟล์ Python เสร็จแล้ว

### 2.1.1 การส่งอาร์กิวเมนต์ (Argument Passing)
เมื่อเรียกใช้งาน Python พร้อมกับระบุชื่อไฟล์และอาร์กิวเมนต์เพิ่มเติม Python จะนำข้อมูลเหล่านั้นมาเก็บไว้ในตัวแปร sys.argv ซึ่งเป็นรายการ (List) ของข้อความ (String)

    import sys

    print(sys.argv)

ตัวแปรนี้ช่วยให้โปรแกรมสามารถรับข้อมูลจากผู้ใช้ผ่าน Command Line ได้

### 2.1.2 โหมด Interactive (Interactive Mode)
Interactive Mode คือโหมดที่เราสามารถพิมพ์คำสั่ง Python แล้วดูผลลัพธ์ได้ทันที โดยไม่จำเป็นต้องสร้างไฟล์โปรแกรมก่อน

เมื่อเปิด python จะพบเครื่องหมาย:

    >>>

เครื่องหมายนี้เรียกว่า Primary Prompt หมายถึง Python พร้อมรับคำสั่งใหม่แล้ว

หากต้องเขียนคำสั่งที่มีหลายบรรทัด Python จะใช้เครื่องหมาย:

    ...

ตัวอย่าง:

    >>> the_world_is_flat = True
    >>> if the_world_is_flat:
    ...     print("Be careful not to fall off!")
    ...
    Be careful not to fall off!

ผลลัพธ์คือ:

    Be careful not to fall off!

สังเกตว่าเมื่อเขียนคำสั่ง if เราต้องเยื้องบรรทัด (Indentation) ของคำสั่ง print() เข้าไปด้วย

## 2.2 Python Interpreter และสภาพแวดล้อมการทำงาน (The Interpreter and Its Environment)
หัวข้อนี้อธิบายเกี่ยวกับสภาพแวดล้อมที่ Python ใช้ในการอ่านและประมวลผลโปรแกรม รวมถึงวิธีจัดการไฟล์ต้นฉบับ

### 2.2.1 การเข้ารหัสไฟล์ต้นฉบับ (Source Code Encoding)
โดยค่าเริ่มต้น Python จะถือว่าไฟล์ Source Code ใช้การเข้ารหัสแบบ UTF-8

UTF-8 รองรับตัวอักษรจากภาษาต่าง ๆ ทั่วโลก ทำให้เราสามารถใช้ตัวอักษรหลายภาษาใน String, ชื่อตัวแปร และ Comment ได้

หากต้องการกำหนด Encoding แบบอื่น สามารถเขียนไว้ที่บรรทัดแรกของไฟล์ Python ได้ เช่น:

    # -*- coding: cp1252 -*-

ตัวอย่างนี้เป็นการกำหนดให้ไฟล์ใช้ Encoding แบบ Windows-1252
หากไฟล์มีบรรทัด Shebang อยู่แล้ว ให้เขียนบรรทัดกำหนด Encoding ไว้เป็นบรรทัดที่สองแทน:

    #!/usr/bin/env python3
    # -*- coding: cp1252 -*-