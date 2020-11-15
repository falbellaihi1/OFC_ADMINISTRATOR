import difflib
import threading

import cv2 as cv
import numpy as np
import os
from time import time, sleep

import win32api
import win32con
import win32gui
from PIL import Image
import pyperclip
from windowcapture import WindowCapture
import pytesseract
from directkeys import PressKey, j, Enter
import pyautogui
from pywinauto.application import Application
from pywinauto.keyboard import SendKeys
import pydirectinput
from win32gui import GetWindowText, GetForegroundWindow
import re
import subprocess
import pyperclip
from  builtins import any as b_any
import sched
import PySimpleGUI as sg

layout = [[sg.Text('Some text on Row 1')],
          [sg.Text('Send message'), sg.InputText(key='global_message'), sg.Button('Send')],
          [sg.Button('Ok'), sg.Button('Cancel')],
          [sg.Checkbox('On', change_submits = True, enable_events=True, default='0', key='spam')],
          [sg.Multiline("", disabled=True, key="log")]

          ]

is_thead_active = False
# Change the working directory to the folder this script is in.
# Doing this because I'll be putting the files from each video in their own folder on GitHub
s = sched.scheduler(time, sleep)
rules_list = ["\n cheating\n spawnganking / running in the enemy grey zone\n fla flaming admin for keeping order"]
#helper to extract player name who is reporting another player
welcoming = "Welcome to the OFC community server"
server_info = "Visit our page  at ofcug.org   Discord: https://discord.gg/SA2Eht"
rules_empty = "No A nor C until 12 VS 12"
no_shotgun_rule = "No Shotgun TODAY!"
rules = "No Profanity, No Racism, No Whining, No Grey zone, No Spawn killing!"
join_ours = "Join our community servers we have OFCInfantery #81725  and Underground24-7 #32192"

def callback():
    if (GetWindowText(GetForegroundWindow()) == 'Battlefield™ V'):
        rect = win32gui.GetWindowRect(GetForegroundWindow())
        x = rect[0]
        y = rect[1]
        w = rect[2] - x
        h = rect[3] - y
        print("Window %s:" % win32gui.GetWindowText(GetForegroundWindow()))
        print("\tLocation: (%d, %d)" % (x, y))
        print("\t    Size: (%d, %d)" % (w, h))
        return [w,h]




def player_name_helper(player_name):
    player_name = player_name.split(':', 1)[0]
    return player_name
#helper to extract player name who is being reported
def reported_player_helper(reported_name):
    reported_player = reported_name.split("!", 1)[1]

def vote_counter(report, vote):

    current_vote_results = [{
        "player_reporting" :"",
        "player_reported":"",
        "report_reason":""
    }]
    player_reporting=''
    accept_vote = False
    if(len(current_vote_results) >0):
        for reporter in report:
            player_reporting = reporter['player_reporting']
        for reports in current_vote_results:
            if(player_reporting in current_vote_results['player_reporting']):
                print("you already voted")
        else:
            current_vote_results.append(report)
            print(current_vote_results)

def send_message(message):
    sleep(2)
    pydirectinput.press('j')

    pyperclip.copy(message)
    print(message)
    pydirectinput.keyDown('ctrl')
    pydirectinput.keyDown('v')
    pydirectinput.keyUp('ctrl')
    pydirectinput.keyUp('v')
    pydirectinput.press('Enter')
    sleep(5)

    # #sleep(10)
    # print(message)
    # pydirectinput.press('j')
    # # spam = pyperclip.copy(message)
    # # # pydirectinput.write(message, 0.00)
    # # pyperclip.paste()
    # pydirectinput.press('Enter')
def report_message(report_list):
    print(report_list)
    pydirectinput.keyDown('j')
    pydirectinput.keyUp('j')
    for info in report_list:
        pydirectinput.write(info)
    # pydirectinput.press('Enter')


def timer_clear_all():

    ##TODO CLEAR ALL ALISTS AFTER SOME TIME
    pass

def process_screen_shot(screenshot):
    num_image = Image.fromarray(screenshot, mode='RGB')

    num_image.save('bf1.png')
    image = cv.imread('bf1.png', 0)

    # image_proc = cv.cvtColor(image, cv.COLOR_BGR2RGB)
    x, y, w, h = 50, 180, 300, 20
    ROI = image[y:y + h, x:x + w]
    thresh = cv.threshold(ROI, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)[1]
    result = 255 - thresh
    data = pytesseract.image_to_string(result, config='--psm 1 --oem 3')
    cv.imshow('chat commands box', ROI)
    return data

def empty(a):
    pass

def process_menu_shot(screenshot):
    cv.createTrackbar("Threshold1", "Parameters", 102, 255, empty)
    num_image = Image.fromarray(screenshot, mode='RGB')
    num_image.save('menu.png')
    image = cv.imread('menu.png', 0)
    # image_proc = cv.cvtColor(image, cv.COLOR_BGR2RGB)
    x, y, w, h = 50, 180, 300, 600
    ROI = image[y:y + h, x:x + w]

    gray = cv.cvtColor(ROI, cv.COLOR_BGR2GRAY)
    blur = cv.GaussianBlur(gray, (3, 3), 0)
    thresh = cv.threshold(blur, 0, 255, cv.THRESH_BINARY_INV + cv.THRESH_OTSU)[1]

    # Morph open to remove noise and invert image
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (3, 3))
    opening = cv.morphologyEx(thresh, cv.MORPH_OPEN, kernel, iterations=1)
    invert = 255 - opening

    # thresh = cv.threshold(ROI, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)[1]
    # result = 255 - thresh
    data = pytesseract.image_to_string(invert, config='--psm 1 --oem 3')
    cv.imshow('menue box', kernel)
    return data






##############################################kil log test ###################################################











def empty(a):

        pass


def process_tickets(screenshot):

    #change colors to PROTANOPIA
    # SET BRIGHTNESS TO THE LEAST
    num_image = Image.fromarray(screenshot, mode='RGB')
    num_image.save('kill_log.png')
    image = cv.imread('kill_log.png', 0)
    # image_proc = cv.cvtColor(image, cv.COLOR_BGR2RGB)
    x, y, w, h = 700, 30, 50, 50
    ROI = image[y:y + h, x:x + w]
    thresh = cv.threshold(ROI, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)[1]
    result = 255 - thresh
    data = pytesseract.image_to_string(ROI, config='--psm 1 --oem 3')
    cv.imshow('tickets', ROI)
    return data

def process_scoreboard(screenshot):

    #change colors to PROTANOPIA
    # SET BRIGHTNESS TO THE LEAST
    num_image = Image.fromarray(screenshot, mode='RGB')
    num_image.save('score_board.png')
    image = cv.imread('score_board.png', 0)
    # image_proc = cv.cvtColor(image, cv.COLOR_BGR2RGB)
    x, y, w, h = 0, 30, 1200, 600
    ROI = image[y:y + h, x:x + w]
    thresh = cv.threshold(ROI, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)[1]
    result = 255 - thresh
    kernel = np.ones((3, 3))
    imgDil = cv.dilate(result, kernel, iterations=0)
    config = ('-l eng --oem 1 --psm 3')

    data = pytesseract.image_to_string(result, config='--psm 1 --oem 3')
    cv.imshow('scoreboard', imgDil)
    return data



melee_weapons = ["British Army Jack Knife","Club","Cricket Bat","Hatchet","Kukri","Pickaxe","Scout Knife","Shovel","Solveig Knife"]
shotguns_list = ["12g Automatic", "M30 Drilling", "Model 37", "M1897"]
guns_list = ["EMP" , "12g Automatic", "M30 Drilling", "Type 2A","KE7", "Kark98k", "Welgun", "M3 Grease Gun", "ZK-383", "Soumi KP/-31", "Boys AT Rifle", "M1911", "Panzerfaust"]
def process_kill_shot(screenshot):

    #change colors to PROTANOPIA
    # SET BRIGHTNESS TO THE LEAST
    num_image = Image.fromarray(screenshot, mode='RGB')
    num_image.save('kill_log.png')
    image = cv.imread('kill_log.png', 0)
    # image_proc = cv.cvtColor(image, cv.COLOR_BGR2RGB)
    x, y, w, h = 900, 30, 400, 150
    ROI = image[y:y + h, x:x + w]
    thresh = cv.threshold(ROI, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)[1]
    result = 255 - thresh
    kernel = np.ones((3, 3))
    imgDil = cv.dilate(result, kernel, iterations=0)
    config = ('-l eng --oem 1 --psm 3')
    data = pytesseract.image_to_string(result, config='--psm 1 --oem 3')
    cv.imshow('killbox', imgDil)
    return data

def ticket_data(feed):
    feeds = "".join(re.split("[^a-zA-Z:\[\]]*", feed))
    # if feeds >= 670:
    #     print(feeds)

## extracts text
def score_board_data(feed):
    feeds = "".join(re.split("[^a-zA-Z: ]*", feed))
    #print(feeds)


def kill_log(feed):

    feeds = "".join(re.split("[^a-zA-Z:\[\]]*", feed))
    #print(feeds, " the feed ")
    player_name = re.search(r"\]([A-Za-z0-9_]+)\[", feeds)#feeds[feeds.find("]") + 1:feeds.find("[")]
    if(player_name is not None):
        print("player name - ", player_name.group(1))
    #gun_name = feeds.split('[', 1)[1]
    gun_name = re.search(r"\[([A-Za-z0-9_ ]+)\]", feed) #feeds[feeds.find("[") + 1:feeds.find("]")]
    #No Shotgun TODAY
    #print(player_name)
    if(gun_name is not None):
        print(gun_name.group(1))
        if (gun_name.group(1) == "Boys AT Rifle"):
            send_message("AT Rifle camper killed a bot!")
        for guns in guns_list:
            if(gun_name.group(1) == guns):
                print(guns, " : ",gun_name.group(1))

        for knife in melee_weapons:
            if(gun_name.group(1) == knife):
                send_message("ops someone got chopped!")
                print("chooper", player_name.group(1))
        for shotgun in shotguns_list:
            #print(shotgun)
            if(gun_name.group(1) == shotgun):
                print("shotty being used ",gun_name , "|", player_name.group(1), " ")

    # if(b_any(gun_name in x for x in melee_weapons) ):
    #     print("found something")
    #     for gun in melee_weapons:
    #         if gun_name in gun:
    #             print("")


def commands(command):
    chat = []
    yes_votes = 0
    no_votes = 0
    report_list = []
    command = "".join(re.split("[^a-zA-Z:]*", command))
    # chat.append(command)
    # print(chat)
   # print("commands: ", command)
    if('play' in command.lower()):
        print('')

    # if ('report' in command):
    #
    #     player_name = command.split(':', 1)[0]
    #     player_name = player_name.lower()
    #     print('init report ', player_name)
    #
    #     # new = (''.join([i for i in hello if i.isalpha()]))
    #     reported_player = ""
    #     if ('/' in command):
    #         reported_player = command.split("/", 1)[1]
    #         reported_player = reported_player.lower()
    #         print('init player name', player_name_helper(reported_player))
    #
    #     # print("player reporting   :", player_name)
    #     # print(" reported player   :", reported_player)
    #     report_list = [{
    #         "player_reporting": player_name,
    #         "reported_player": reported_player,
    #         "report_reason": "cheating"
    #     }]
    #     print(report_list)
    #     for single_report in report_list:
    #         print('loopin')
    #         if(reported_player in single_report['reported_player']):
    #             print("")
    #         else:
    #             print('')
    #             # send_message("this is testing  "+(list(report_list)[0]['player_reporting'] + " \n is reporting " + list(report_list)[0][
    #             #     'reported_player'] + " \n  for " + list(report_list)[0]['report_reason']))
    #
    #     # send_message(report_list)
    #
    #     # print('report detected', hello)
    #
    # if (len(report_list) > 0):
    #     print('')
    #     # for report in report_list:
    #         # print('/')
    #         # print(
    #         #     "player : ", report['player_reporting'], "is reporting  :",
    #         #     report['reported_player'], " for cheating, vote will begain in 10 seconds"
    #         # )
    #
    # if ('!yes' in command):
    #     yes_votes = yes_votes + 1
    #     #print("count of yes votes is : ", yes_votes)
    # elif ('!no' in command):
    #     no_votes = no_votes + 1
    #     #print("count of no votes is : ", no_votes)
    elif ('rules' in command):
        print("request rules")
        send_message(rules)
        #send_message(rules_empty)
        send_message(no_shotgun_rule)
        # sleep(30)
        # send_message(rules_list[1])
        #
        # send_message(rules)
        # send_message(rules_list[1])
        # return 0
    elif('hack' in command):

        print("the irony of BF, guess what! someone is blaming players of hacking")

def welcome_threading():
    print("thread")
    threading.Timer(400, welcome_threading).start()

    #send_message(welcoming)
    # sleep(3)
    #send_message("OFC is starting an infantry only server from Friday and on. More info at ofcug.org/news")
    # sleep(3)
    # send_message(server_info)
    # sleep(3)
    # send_message(join_ours)
    #send_message(no_shotgun_rule)



subprocess.Popen(["C:\Program Files\AutoHotkey\AutoHotkey.exe", "copy-paste.ahk"])
def main():
    #if (GetWindowText(GetForegroundWindow()) == 'Battlefield™ V'):
    print("welcoming message coming")

    welcome_threading()






    # initialize the WindowCapture class
    wincap = WindowCapture('Battlefield™ V')




    loop_time = time()
    sg.theme('DarkAmber')  # Add a touch of color
    # All the stuff inside your window.


    # Create the Window
    window = sg.Window('OFC administrator', layout)
    # Event Loop to process "events" and get the "values" of the inputs
    while(True):

        event, values = window.read()
        if event == 'Send':
            print('ok')
            send_message(values['global_message'])
        print(sg.Checkbox.get)

        if event == sg.WIN_CLOSED or event == 'Cancel':  # if user closes window or clicks cancel
            break
        print('You entered ', values[0])

        window.close()
        if (GetWindowText(GetForegroundWindow()) == 'Battlefield™ V'):
            screenshot = wincap.get_screenshot()

            # data = process_screen_shot(screenshot)
            # kill_logs = process_kill_shot(screenshot)
            # #menue = process_menue_shot(screenshot)
            # commands(data)
            # kill_log(kill_logs)
            # proc_tick = process_tickets(screenshot)
            # ticket_data(proc_tick)
            # scoreboard = process_scoreboard(screenshot)
            # score_board_data(scoreboard)
            #commands(menue)
            #send_message(welcoming)


            # Button("QUIT", (100, 400), quit)
            #cv.imshow('Computer Vision', screenshot)


        # debug the loop rate
            #print('FPS {}'.format(1.0 / (time() - loop_time)))
        loop_time = time()


        # press 'q' with the output window focused to exit.
        # waits 1 ms every loop to process key presses
        if cv.waitKey(1) == ord('q'):
            pydirectinput.keyUp('ctrl')
            pydirectinput.keyUp('v')
            data =''
            cv.destroyAllWindows()
            break

    print('Done.')

run = main()
run.runall()

