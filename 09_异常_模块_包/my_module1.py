def info_print1():
    print("my_module1")

def substr(s,x,y):
    '''
    功能是按照指定的下标范围截取字符串
    :param s: 字符串
    :param x: 开始下标
    :param y: 结束下标
    :return: 截取后的字符串
    '''
    return s[x:y]

def print_filr_info(file_name):
    '''
    功能是将给定路径的文件内容输出到控制台，如果文件不存在捕获异常并打印提示信息
    :param file_name: 文件路径
    :return: None
    '''
    f=None
    try:
        with open(file_name, "r", encoding="utf-8") as f:
            print(f.read())
    except Exception as e:
        print("文件不存在", e)
    finally:
        if f:        # 如果f不为空，说明文件打开成功
            f.close()



if __name__ == '__main__':
    print_filr_info("D:/sr.txt")