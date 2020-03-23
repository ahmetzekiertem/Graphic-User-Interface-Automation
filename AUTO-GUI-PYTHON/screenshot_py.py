import pyautogui

pyautogui.screenshot("/Users/mac/Desktop/examplescreen.png")


print(pyautogui.locateOnScreen("/Users/mac/Desktop/dosya_deg.png"))


print(pyautogui.locateCenterOnScreen("/Users/mac/Desktop/dosya_deg.png"))


pyautogui.moveTo(pyautogui.locateCenterOnScreen("/Users/mac/Desktop/dosya_deg.png"),duration=2)

pyautogui.click()
