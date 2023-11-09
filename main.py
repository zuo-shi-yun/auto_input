import keyboard
import pyperclip
from pynput.keyboard import Controller

print('欢迎使用!按下F8开始输入')

while True:  # 死循环
    # 等待快捷键
    keyboard.wait('f8')

    # 获取粘贴板上的内容
    clipboard_content = pyperclip.paste()

    # 模拟输入
    write = Controller()
    write.type(clipboard_content)
    print(f'完成输入:{clipboard_content}(按下F8再次输入)')
