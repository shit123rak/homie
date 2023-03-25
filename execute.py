import os
import random

from packs.img_to_text import __text, __google
from pynput.keyboard import Key, Controller
import keyboard as _keyboard
import time
import num2words as n2w

keyboard = Controller()

imp = {
    'What is Team 3 composition?': 'Neji, Tenten, Lee',
    'How many tails does Chōmei have?': '7',
    'What is Team Ebisu composition?': 'Konohamaru, Moegi, Udon',
    'What weapon does Sasuke use?': 'Katana',
    "What is Naruto's summoning jutsu?": 'Toad',
    'What weapon does Sai use?': 'Scroll',
    'What is Team 8 composition?': 'Hinata, Kiba, Shino',
    "What is Minatos's nickname?": 'Yellow Flash',
    "What is Team Minato composition?": 'Kakashi, Obito, Rin',
    "What is the Eight Tails' real name?": 'Gyuki',
    'What Jiraiya/Orochimaru/Tsunade known as?': 'The Sannin',
    'Who is the One-Tail jinchūriki?': 'Gaara',
    'What is Team 10 composition?': 'Shikamaru, Choji, Ino',
    'What weapon does Kankuro use?': 'Puppet',
    'What did Naruto wear before he got his headband?': 'Goggles',
    'Which Hokage sealed the nine-tailed fox inside Naruto?': '4th Hokage',
    'How many tails does Kokuō have?': '5',
    'How many ninjas from Konoha passed first chunnin exam?': '1',
    'How many tails does Chōmei have?': '7'
}


def _to_names(number):
    if number.isnumeric():
        num_name = n2w.num2words(int(number))
        return num_name
    else:
        return number


def send_nm(msg):
    words = str(msg)
    for _i in range(0, len(words)):
        keyboard.press(words[_i])
        keyboard.release(words[_i])

    keyboard.press(Key.enter)
    keyboard.release(Key.enter)


def organize_msg(msg):
    msg.replace("\n", " ")
    msg_arr = msg.split(" ")
    msg_arr.reverse()
    print(msg_arr)
    if 'spuckhafte.\n' in msg_arr or 'spuckhafte.\n\n' in msg_arr and msg_arr[0] == 'spuckhafte.\n' or msg_arr[0] == 'spuckhafte.\n\n':
        return 'Wait'
    else:
        msg_arr.reverse()
        msg = ' '.join(msg_arr)
        if 'A rank' in msg:
            msg_arr = msg.split("A rank")
        if 'B rank' in msg:
            msg_arr = msg.split("B rank")
        if 'C rank' in msg:
            msg_arr = msg.split("C rank")
        if 'S rank' in msg:
            msg_arr = msg.split("S rank")
        if len(msg_arr) == 2:
            msg_arr = msg_arr[1]
        else:
            msg_arr = msg_arr[0]
        msg_arr = msg_arr.split("\n")
        msg_arr = [i for i in msg_arr if i != '']
        msg_arr.pop(0)

        _question = msg_arr[0]
        _options = [msg_arr[1], msg_arr[2], msg_arr[3]]
        return [_question, _options]


def search_google(questionG, optionsG):
    optionsG = [i.lower() for i in optionsG]
    optionsG = [_to_names(i) for i in optionsG]
    searched = __google(questionG)
    _keyboard.press_and_release('ctrl+w')
    searched = searched.split("\n")
    searched = ' '.join(searched).lower()
    print(optionsG)
    for option in optionsG:
        option = option
        if option in searched:
            print(searched)
            print(option)
            print(optionsG.index(option) + 1)
            return str(optionsG.index(option) + 1)
    return str(random.randint(1, 3))


def main():
    while True:
        discord_path = 'C:/Users/Rakshit/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Discord Inc/Discord'
        os.startfile(discord_path)
        os.startfile(discord_path)
        try:
            print('Start')
            time.sleep(2)
            send_nm('<@770100332998295572> m')
            time.sleep(1)
            text = __text()
            text = organize_msg(text)
            time.sleep(0.5)
            if text != 'Wait':
                question = text[0]
                options = text[1]
                if question in imp.keys():
                    ans = imp[question]
                    ans = str(options.index(ans) + 1)
                    send_nm(ans)
                else:
                    ans = search_google(question, options)
                    time.sleep(2)
                    send_nm(ans)
                time.sleep(0.8)
                # _keyboard.press_and_release('win+d')
                time.sleep(50)
            else:
                send_nm('Wait...')
                time.sleep(2)
        except:
            print('err')
            # _keyboard.press_and_release('win+d')
            ans = random.randint(1, 3)
            send_nm(ans)
            time.sleep(51)


if __name__ == '__main__':
    main()

