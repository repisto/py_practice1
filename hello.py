# hello.py
with open("한글파일.txt","w",encoding="utf-8") as f:
    f.write("안녕하세요, 파이썬!")

with open("한글파일.txt","r",encoding="utf-8") as f:
    content = f.read()
    print(content)
