"""
演示对表达式进行字符串格式化
"""
print("1 * 1 的结果是：%d" % (1 * 1))
print(f"1 * 2的结果是：{1 * 2}")
print("字符串在Python中的类型名是：%s" % type("字符串"))

class_num=57
avg_salary=10000.94
massage="本班级有%d个学生，平均工资是%7.5f元"%(class_num,avg_salary)
print(massage)