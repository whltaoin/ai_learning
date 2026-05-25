# 7 自定义计算器
def calculator():
    try:
        num1 = float(input("输入第一个数字："))
        option = input("请输入符号[+ - * /]:")
        num2 = float(input("输入第二个数字："))
        if option == "+":
            print(f"结果：{num1+num2}")
        elif option == "-":
            print(f"结果：{num1 - num2}")
        elif option == "*":
            print(f"结果：{num1*num2}")
        elif option == "/":
            print(f"结果：{num1/num2}") if num1/num2 !=0 else print("除数不能为零！")
        else :
            print("输入了无效的运输符号")
    except ValueError:
        print("请输入有效的数字")


if __name__ == '__main__':

    # 1. 静态类型:java
    # int num = 10;
    # 2. 动态类型：python
    str1 =1
    print(type(str1))
    str2 = "1"
    print(type(str2))
    # 3. 列表(任意类型)
    str3 = [3,"33",[1]]
    print(str3[2][0])
    # 4. 元组(不可变)
    str4 = ("333",3232)
    print(type(str4))
    print(str4[0])
    # 5. 字典
    str5= {"name":"张三"}
    print(type(str5))
    print(str5.get("name"))
    # 6. set集合
    str6 = {33,23,2,2}
    print(type(str6))
    print(str6)
    # 8. 使用计算器
    calculator()
    # 第三部分：Python
    # 练习题
    # 基础练习：变量与运算符
    # 变量交换：定义两个变量
    # a = 5, b = 10，不使用中间变量，将它们的值交换。
    a = 5
    b=10
    a,b=b,a
    print(a,b)
    # 类型转换：用户输入一个年份（字符串），将其转换为整数，并计算距离
    # 2050
    # 年还有多少年。
    num3 = int(input("输入："))
    print(type(num3))
    print(2050-num3)
    # 进阶练习：容器与集合
    # 列表与去重：给定一个列表[1, 2, 2, 3, 4, 4, 5]，请利用集合(Set)
    # 的特性，输出一个去重后的列表。
    list1 =[1, 2, 2, 3, 4, 4, 5]
    list1 = list(set(list1))
    print(list1)












