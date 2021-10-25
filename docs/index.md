# Welcome to pydmdll

### 前言
Python模拟鼠标键盘的包有很多，它们的文档也很全，功能也很人性化，最后实在没有办法了再使用大漠。    
推荐结合使用：比如：大漠没有监听键盘的功能，你完全可以再开一个线程，使用`Keyboard`进行监听。

* `Pyautogui`侧重于鼠标，键盘，截图，消息框的功能  
* `Pywinauto`侧重对CS的操作，对进程，窗体进行操作  
* `Keyboard`侧重于键盘，监听键盘，设置热键，键盘记录等功能

### 简介

`pydmdll`**仅支持32位Python3**，实现了大漠插件免费功能部分，内部封装的是`V3.1233`版本的`dm.dll`.初衷是为了解决鼠标在游戏内部无法拖拽的问题。

### 项目

* [Github](https://github.com/Gaoyongxian666/pydmdll)
* [在线文档](https://pydmdll.readthedocs.io/zh/latest/)

### 功能  

* 模拟键盘：输入，输出，按键，点击等
* 窗口功能：最小化，激活，移动，获取窗口句柄等
* 基本功能：剪贴板，蜂鸣器等

### 安装

    pip install pydmdll

### 开始
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

### 注意
    在线程里面使用dm，要注意初始化pythoncom，否则每次都要注册DM，单线程情况下不用设置。

    import pythoncom
    pythoncom.CoInitialize()
    dm = DM()


    管理员运行cmd命令，/C代表打开执行之后直接关闭
    注意cmd会直接运行你传入的命令，如果你使用/K 参数保留命令行，不会显示你传入的命令，但确实已经执行了，如果有回显你才会看到
    
    ctypes.windll.shell32.ShellExecuteW(None, "runas", "cmd.exe", "/C %s" % self.cmd_un_dll, None, 1)

    管理员运行本程序代码，通常在最开始执行，即整个代码以管理员运行

    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)

### 其他

`pydmdll`可以直接使用，默认使用的是内部封装的是`V3.1233`版本的`dm.dll`，也可以指定本地的`dm.dll`。

`大漠插件`是用vb语言写的一个闭源且收费的的`dll`，`V3.1233`是其最后一个免费的版本，当然也仅是免费使用部分功能。  


### 键盘代码

| key_str   | 虚拟键码 |
| --------- | -------- |
| "1",      | 49       |
| "2",      | 50       |
| "3",      | 51       |
| "4",      | 52       |
| "5",      | 53       |
| "6",      | 54       |
| "7",      | 55       |
| "8",      | 56       |
| "9",      | 57       |
| "0",      | 48       |
| "-",      | 189      |
| "=",      | 187      |
| "back",   | 8        |
| "a",      | 65       |
| "b",      | 66       |
| "c",      | 67       |
| "d",      | 68       |
| "e",      | 69       |
| "f",      | 70       |
| "g",      | 71       |
| "h",      | 72       |
| "i",      | 73       |
| "j",      | 74       |
| "k",      | 75       |
| "l",      | 76       |
| "m",      | 77       |
| "n",      | 78       |
| "o",      | 79       |
| "p",      | 80       |
| "q",      | 81       |
| "r",      | 82       |
| "s",      | 83       |
| "t",      | 84       |
| "u",      | 85       |
| "v",      | 86       |
| "w",      | 87       |
| "x",      | 88       |
| "y",      | 89       |
| "z",      | 90       |
| "ctrl",   | 17       |
| "alt",    | 18       |
| "shift",  | 16       |
| "win",    | 91       |
| "space",  | 32       |
| "cap",    | 20       |
| "tab",    | 9        |
| "~",      | 192      |
| "esc",    | 27       |
| "enter",  | 13       |
| "up",     | 38       |
| "down",   | 40       |
| "left",   | 37       |
| "right",  | 39       |
| "option", | 93       |
| "print",  | 44       |
| "delete", | 46       |
| "home",   | 36       |
| "end",    | 35       |
| "pgup",   | 33       |
| "pgdn",   | 34       |
| "f1",     | 112      |
| "f2",     | 113      |
| "f3",     | 114      |
| "f4",     | 115      |
| "f5",     | 116      |
| "f6",     | 117      |
| "f7",     | 118      |
| "f8",     | 119      |
| "f9",     | 120      |
| "f10",    | 121      |
| "f11",    | 122      |
| "f12",    | 123      |
| "[",      | 219      |
| "]",      | 221      |
| "\\",     | 220      |
| ";",      | 186      |
| "'",      | 222      |
| ",",      | 188      |
| ".",      | 190      |
| "/",      | 191      |

