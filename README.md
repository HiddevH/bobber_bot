# [bobber_bot]:
WoW (Classic) fishing bot.. for funzies. *Works in Retail too!

This bot is basically finished now! I achieved pretty solid tracking once HSV threshold of the bobber / tooltip is configured~
(The script will step you through configuration each time it runs -- you want only the bobber/parts of the bobber to be selected in white)
I've been bringing in bag fulls of fish each night and just kicking back making improvements. =]

The one tricky part is setting up the sound.. `audio_callback()` is using the speaker's output to detect the sound of the splash -- This takes some setup with Soundflower on OSX, or by creating a Sound Mixer on windows.. I've included the steps below to help set that up!

# [I've tested this A LOT]: xD
![menethil_harbor_fish](https://github.com/disarmyouwitha/bobber_bot/blob/master/logs/menethil_harbor_fish.png)
![lake_mennar_fish](https://github.com/disarmyouwitha/bobber_bot/blob/master/logs/lake_mennar_fish.png)
![wailing_caverns_fish](https://github.com/disarmyouwitha/bobber_bot/blob/master/logs/wailing_caverns_fish.png)

# [AT THE MOMENT]:
> The bot will start listening when started. This is the main loop -- when a SPLASH is detected, it will try to catch/recast 

> The bot will track the bobber by using the HSV threshold set during calibration.. this usually only takes a few gueses.

> It verifies that it has found the bobber by checking the location of the `Fishing Bobber Tooltip` when the bobber is moused-over.

> *If a number of baubles is given for _use_baubles=#, the bot will use `fishing baubles on "9"` on `fishing pole on "7"` when it starts, and every 10min until it thinks you are out of baubles.*

> *The bot will then use the `fishing skill on "8"` to cast the pole, and start tracking the bobber.*

> *Once the bobber (tooltip) is detected, the bot will wait until it "hears" the splash (or until the 30sec timer since pole was cast expires) and it will recast/try again.*

> *If the bot has "missed" 20 times in a row (timer has expired after 30sec) the bot thinks that it has disconnected, and will try to auto-reconnect*

> ^(Optionally, if you configure `login` it will have you SSIM your login box, with no password, so that it knows what a clear login screen looks like. The bot will ask you for your password, which is stored in `configs/pass.txt`, for attempting to relogin if disconnected.)

> ^(Optionally, if you configure `health` it will have you SSIM your (full) health bar, so that it knows what your health looks like full. It uses this to detect if you are dead on relogin.)

> ^(Optionally, you can enable `_use_mouse_mode=True` to only use the mouse for fishing actions and it will walk you through calibration -- allowing you to type to your guild, etc, if you are a chatter-bug like me =3)


# [Setting up audio_callback for OSX]:
> [0]: Install Soundflower:
>      https://github.com/mattingalls/Soundflower/releases/download/2.0b2/Soundflower-2.0b2.dmg
>      OR `install_files/Soundflower-2.0b2.dmg`

> [1]: Click your speaker from osx toolbar and select "Soundflower (2ch)" from the dropdown.
>       Check out: `img/soundflower_setup_osx` as an example

> [2]: And you should be done! Use `audio.py` to figure out what index your Soundflower device is!


# [Setting up audio_callback for WINDOWS]:
> [0]: Open Sound panel (Type "Sound" into system search)

> [1]: Select Speakers as the default playback device

> [2]: Go to the "Recording" tab

> [3]: Right click and enable "Show Disabled Devices"

> [4]: A recording device called "Wave Out Mix", "Mono Mix" or "Stereo Mix" (this was my case) should appear

> [5]: Right click on the new device and click "Enable"

> [6]: Right click on the new device and click "Set as Default Device"

> [7]: Double click on the new device to open the Properties window

> [8]: Go to the "Listen" tab

> [9]: Click on the "Listen to this device" checkbox

> [10]: Select your Speakers from the "Playback through this device" list

> And you should be done! Use `audio.py` to figure out what index your Sound Mixer device is!]


# [audio.py]:
> A small test script to make sure you are recording sound from your Input source. (Mic/Speakers)

> Used to figure out the indexes/threshold if the preset ones dont work for you!

# [thresh.py]:
> Running this script will start the "main loop" which will take you through calibration, then start the bot!

>

>

# [INSTALLING NOTES]:

# [OSX]:
> brew install python3

> brew install portaudio

> python -m pip install pyaudio

> install Soundflower-2.0b2.dmg from install_files (OR..)
> https://github.com/mattingalls/Soundflower/releases/download/2.0b2/Soundflower-2.0b2.dmg

# [WINDOWS]:
> install `python-3.7.5-amd64-webinstall.exe` from install_files

> install `PyAudio-0.2.11.win-amd64-py3.7.msi` from install_files

> python -m pip install `pyHook-1.5.1-cp37-cp37m-win_amd64.whl` from install_files

> python -m pip install mss


# [BOTH NEED]:
> python -m pip install numpy

> python -m pip install imageio

> python -m pip install playsound

> python -m pip install pyautogui

> python -m pip install PyUserInput

> python -m pip install scikit-image

> python -m pip install opencv-python

>

>

# [HIGHLY RECOMMENDED]:
> DLMS took care of most of my inventory problems.. I just add trashfish to my blacklist:
> `/dlms b_list add [item_link to trash fish]` in WoW

> DOWNLOAD ADDON: 
> https://www.warcrafttavern.com/addons/dlms-dynamic-loot-management-system/

> I use this, rather than autosell, to blacklist trash fish that would otherwise fill up my inventory.

# [LICENSE]:
> MIT License (open source) have fun / feel free to fork && submit Pull Requests with improvements! 
> https://choosealicense.com/licenses/mit/
