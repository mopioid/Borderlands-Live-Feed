# Borderlands Chatbot
A Streamlabs Chatbot Script for providing live BL2 &amp; TPS data in response to !build &amp; !level.

![Command output examples](https://i.imgur.com/sVpDAik.png)

This is made possible thanks to [c0dycode's CommandInjector](https://github.com/c0dycode/BL-CommandInjector), via the [BLIO set of methods](https://github.com/mopioid/BLIO).

## Installation

### Installing CommandInjector
For Chatbot to be able to get its data from the game, you must add a few things to your game's Win32 folder. If you already have CommandInjector installed, you may skip ahead to [Installing Borderlands Chatbot](#installing-borderlands-chatbot).

1. Quit the game if it is running.
2. [Download the latest version of `ddraw.dll` (A.K.A. PluginLoader).](https://github.com/c0dycode/BorderlandsPluginLoader/releases)
3. Locate your game's `Win32` folder within your game's `Binaries` folder. ![Win32 folder](https://i.imgur.com/t6OI06l.png)

4. Copy `ddraw.dll` to the game's `Binaries\Win32` folder. ![ddrawl.dll](https://i.imgur.com/FHfiSqg.png)

5. In the `Win32` folder, create a folder called `Plugins`. ![Plugins folder](https://i.imgur.com/CDdoKDs.png)

7. [Download the latest version of CommandInjector.](https://github.com/c0dycode/BL-CommandInjector/blob/master/CommandInjector.zip)

6. Open the `CommandInjector.zip` file to view its contents. ![CommandInjector.zip](https://i.imgur.com/r1I3b26.png)

7. Copy `CommandInjector.dll` (BL2) or `CommandInjectorTPS.dll` (TPS) to the `Plugins` folder you created. ![CommandInjector.dll](https://i.imgur.com/U9OSqcV.png)

### Installing Borderlands Chatbot

1. [Download `BorderlandsChatbot.zip`.](https://github.com/mopioid/Borderlands-Chatbot/blob/master/BorderlandsChatbot.zip)
2. Launch Streamlabs Chatbot if it is not already running.
3. Navigate to the Scripts section in Streamlabs Chatbot's sidebar. If this is your first time using Streamlabs Chatbot scripts, it will walk you through how to prepare to use scripts, including installing Python. ![Scripts](https://i.imgur.com/be7rfSO.png)

4. Right-click in the scripts window and select "Open Script Folder." ![Open Script Folder](https://i.imgur.com/h09j7jM.png)

5. Open the `BorderlandsChatbot.zip` file to view its contents. ![BorderlandsChatbot.zip](https://i.imgur.com/9TW85Di.png)

6. Copy the `BorderlandsChatbot` folder to Streamlabs Chatbot's `Scripts` folder. ![Streamlabs Chatbot's `Scripts` folder](https://i.imgur.com/uPDdSag.png)

7. In Streamlabs Chatbot's Scripts window, click the circular Reload Scripts icon, and "Borderlands" should appear in the list.

8. Click the checkbox next to Borderlands to enable it ![Borderlands Script](https://i.imgur.com/gOWvMli.png)

You are now ready to run the !build and !level commands!
