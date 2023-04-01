import xmind

def gen_my_xmind_file():  
    # 1、如果指定的XMind文件存在，则加载，否则创建一个新的
    workbook = xmind.load("my.xmind")

    # 2、获取第一个画布（Sheet），默认新建一个XMind文件时，自动创建一个空白的画布
    sheet1 = workbook.getPrimarySheet()
    # 对第一个画布进行设计完善，具体参照下一个函数
    design_sheet1(sheet1)

    # 3、创建第二个画布
    gen_sheet2(workbook, sheet1)

    # 4、保存（如果指定path参数，另存为该文件名）
    xmind.save(workbook, path='test.xmind')

