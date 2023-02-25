import win32gui
import pyautogui

# Get the handle of the window to focus
hwnd = win32gui.FindWindow(None, "Roblox")

# Bring the window to the front and give it focus
win32gui.SetForegroundWindow(hwnd)

pyautogui.press('/')

pyautogui.typewrite("chat bot python made by crazyj455")

pyautogui.press('enter')
