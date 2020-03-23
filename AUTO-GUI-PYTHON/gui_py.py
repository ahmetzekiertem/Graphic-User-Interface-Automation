#GUI Automation

import pyautogui

print(pyautogui.position())

pyautogui.size()
pyautogui.FAILSAFE = False
pyautogui.click()

'''pyautogui.moveTo(10,10)
pyautogui.moveTo(100,0, duration=1.5)
pyautogui.moveTo(0,-100, duration=1.5)'''
#pyautogui.moveRel(20,0)



#pyautogui.moveRel(200,0)

pyautogui.click()



#pyautogui.click(478,13)
#pyautogui.rightclick()

#pyautogui.doubleclick()

distance = 200

'''while distance > 0 :
    print(distance,0)
    pyautogui.dragRel(distance,0,duration=0.1) #move right
    distance = distance - 25
    print(0,distance)
    pyautogui.dragRel(0,distance,duration=0.1) #move down
    print(-distance,0)
    pyautogui.dragRel(-distance,0,duration=0.1) #move left
    distance = distance - 25
    pyautogui.dragRel(0,-distance,duration=0.1) #move up'''

pyautogui.click(pyautogui.position())

#pyautogui.typewrite('print("hello world")') # bayildigim bi python komutudur.

print("hello world") #

pyautogui.press('F1')

pyautogui.hotkey('command','A')

pyautogui.hotkey('command','C')

pyautogui.hotkey('command','V')
