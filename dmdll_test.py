# -*- coding: UTF-8 -*-
"""
@Project ：pydmdll
@File ：dmdll_test.py
@Author ：Gao yongxian
@Date ：2021/10/25 10:19
@contact: g1695698547@163.com
"""
import os
import time


from pydmdll import DM

if __name__ == '__main__':
    dm = DM()
    # dm = DM(dm_dll_path="你自己的版本路径")

    # 取消注册
    # dm.Un_reg()

    # 打开记事本
    os.system("start notepad.exe")
    time.sleep(1)

    # 窗口句柄就是一个int类型的数字
    txt_hwnd = dm.FindWindow("", "记事本")
    print(txt_hwnd)

    # 最大化指定窗口,同时激活窗口.
    f = dm.SetWindowState(txt_hwnd, 1)
    # print(f)

    # 使记事本窗口移动
    dm.MoveWindow(txt_hwnd, 10, 10)

    # 打印注册路径
    path = dm.GetBasePath()
    print(path)

    # 获取剪贴板
    print(dm.GetClipboard())

    # 获取标题还有.py的所有句柄
    # 注意：返回的是str，但句柄必须是int类型，要强行转化
    # hwnd_str_list=dm.EnumWindow(0,".py","",1+2+4+8).split(",")
    # print(hwnd_str_list)
    # for hwnd in hwnd_str_list:
    #     print(dm.GetWindowClass(int(hwnd)))
    #     print(dm.GetWindowProcessPath(int(hwnd)))
    #     print(dm.GetWindowTitle(int(hwnd)))
    #     dm.MoveWindow(int(hwnd),100,100)

    # 推荐相对移动
    dm.MoveR(40, 10)