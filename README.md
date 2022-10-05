# Lineage 2 OpenCV Fishing bot
The pixel bot works on computer vision technology and is not injected into the game process.
The script uses the [PyDirectInput](https://pypi.org/project/PyDirectInput/) library to emulate key input -- This library aims to replicate the functionality of the PyAutoGUI mouse and keyboard inputs, but by utilizing DirectInput scan codes and the more modern SendInput() win32 function.
More details can be found in the documentation https://pypi.org/project/PyDirectInput/

## Installation
Install the dependencies from requirements.txt

```sh
python -m pip install -r requirements.txt
or
pip install -r requirements.txt
```

## Libraries

Dillinger is currently extended with the following plugins.
Instructions on how to use them in your own application are linked below.

| libs | links |
| ------ | ------ |
| OpenCV | https://opencv.org/ |
| PyDirectInput | https://pypi.org/project/PyDirectInput/ |
| PyWin32 |https://pypi.org/project/pywin32/ |

# Usage

- Launch Terminal or Code editor to run script via admin rights
- You need to set the window resolution to 1024*768 32bit
- Select the frequency of your monitor in Hz
- Click in the Reset Window Location settings while the fishing window is active in order to reset the fishing window for sure
- It is desirable, but not necessary, to hide all unnecessary visualization settings: 
Settings > Game and Settings > Damage Text
Hide the names of monsters, players, cancel trades, duels, group invites, and so on

# Keybinding
The bot uses the following keys. You must assign the following skills/macros in the game bar to these keys:
- F1 -- Pumping skill
- F2 -- Reeling skill
- F4 -- Fishing skill
- F5, F6, F7 -- Macros for pet/summon kill mobs
- 2 -- Pet/Summoner attack skill

- You have to create three macros to kill mobs via pet/sumon and put f5, f6, f7 buttons on the game panel:
- /target Caught Homunculus
/useshortcut 2 2
- /target Caught Flava
/useshortcut 2 2
- /target Caught Gigantic Eye
/useshortcut 2 2
