age = int(input("请输入你的年龄: "))
if age < 18:
    print("你还未成年！")
elif age >= 18 and age < 60:
    print("你成年了！")
else:
    print("你是老年人！")