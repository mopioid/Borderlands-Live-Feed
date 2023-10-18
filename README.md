# Borderlands Live Feed
An [UnrealEngine PythonSDK](https://github.com/bl-sdk/PythonSDK) mod for Borderlands 2 and Borderlands: The Pre-Sequel! that provides access to continuously up-to-date information about the current game.

![Command output examples](https://i.imgur.com/e52SQLX.png)

Borderlands Live Feed outputs information on the current character and game mode instantly as they change in-game, outputting the raw information to a JSON file. This JSON file may be accessed by client applications for any desired application.

Included with Borderlands Live Feed is a script for Streamlabs Chatbot, which allows Twitch and YouTube streamers to provide information about their game via chat commands (see above image).

## Installation

Begin by [downloading the latest version of Borderlands Live Feed.](https://github.com/mopioid/Borderlands-Live-Feed/releases)

### Mod Installation (Required)

1. [Install UnrealEngine PythonSDK](https://github.com/bl-sdk/PythonSDK#installation) if you have not already.

2. Locate the SDK's `Mods` folder (located in the `Win32` folder of the `Binaries` folder of your BL2/TPS installation).

3. Copy the `LiveFeed` folder from the `Mods` folder in `BorderlandsLiveFeed.zip` to the SDK's `Mods` folder.

4. Launch the game, select "Mods" from the main menu, then select "Live Feed" to enable it.

### Streamlabs Chatbot Installation (Optional)

1. Launch Streamlabs Chatbot if it is not already running.

2. Navigate to the Scripts section in Streamlabs Chatbot's sidebar. If you have not done so previously, you must [configure Streamlabs Chatbot to be able to use scripts](https://streamlabs.com/content-hub/post/chatbot-scripts-desktop).

3. Right-click in the scripts window and select "Open Script Folder." ![Open Script Folder](https://i.imgur.com/otYQsbp.png)

4. Copy the `BorderlandsLiveFeed` folder from the `Chatbot` folder in `Borderlands-Live-Feed-master.zip` to Streamlabs Chatbot's `Scripts` folder.

5. In Streamlabs Chatbot's Scripts window, click the circular Reload Scripts icon, and "Borderlands" should appear in the list.

6. Click the checkbox next to Borderlands to enable it. ![Borderlands Script](https://i.imgur.com/ySmxeza.png)

7. See [Streamlabs Chatbot Usage](https://github.com/mopioid/Borderlands-Live-Feed#streamlabs-chatbot-usage) for details on setting up commands.

## Usage

### JSON Usage (Advanced)

Borderlands Live Feed outputs its information to `%APPDATA%\BorderlandsLiveFeed\Output.json`.

Example output:
```json
{
    "name": "Sniper Aurelia",
    "class": "Baroness",
    "head": "Aurelia",
    "skin": "Aurelia's Designer Ensemble",
    "level": 70,
    "OPLevel": null,
    "playthrough": 2,
    "currentPlaythrough": 1,
    "currentOPLevel": null,
    "map": "Eridian_slaughter_P",
    "weapons": ["Barking Rakehell", "Pacifying Wet Week", "Skookum Skullmasher", "Streamlined Omni-Cannon"],
    "shield": "Naught",
    "grenade": "Longbow Cryo Transfusion",
    "classMod": "Uninterested Sport Hunter Class Mod",
    "relic": "3DD1.E",
    "skills": [4,5,5,0,5,1,0,1,0,5,0,1,4,1,5,1,5,1,5,0,0,0,1,1,2,1,2,0,1,5,0,5,0,0,0,0,0]
}
```

Fields are assigned `null` if unavailable.

The `weapon` field will always be an array of a length of 4, with each member corresponding to a weapon slot (members corresponding to empty weapon slots are assigned `null`).

The `skills` field is an array of integers corresponding to the number of points spent in each skill. This corresponds to the URL formats of [bl2skills.com](https://bl2skills.com/vanilla.html) and [thepresequel.com](http://www.thepresequel.com/skill_calculator).

### Streamlabs Chatbot Usage

While the Borderlands Live Feed script is enabled in Chatbot, various parameters are available to be used in Commands:

| Parameter  | Description                  | Example output                                                                                                     |
|------------|------------------------------|--------------------------------------------------------------------------------------------------------------------|
| $blname    | Character class and name     | a Baroness named 'Sniper Aurelia'                                                                                  |
| $blskin    | Head and skin customizations | 'Aurelia' head with the 'Aurelia's Designer Ensemble' skin                                                         |
| $blbuild   | Skill tree URL               | http://thepresequel.com/Aurelia/4550510105014151515000112120150500000                                              |
| $bllevel   | Level and playthrough        | level 70 in UVHM, currently playing in TVHM                                                                        |
| $blweapons | Equipped weapons             | 'Barking Rakehell', 'Pacifying Wet Week', 'Skookum Skullmasher', and 'Streamlined Omni-Cannon'                     |
| $blgear    | Equipped gear                | 'Naught' shield, 'Longbow Cryo Transfusion' grenade mod, 'Uninterested Sport Hunter' class mod, and '3DD1.E' relic |

See screenshot for suggested usage of these parameters:

![Command syntax examples](https://i.imgur.com/dLx86Pg.png)
