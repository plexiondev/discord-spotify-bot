## discord-spotify-bot

show off what you're listening to via discord - instead of using the spotify account linking.

## where

your now playing is shown on your bot's **listening game activity** and can also be shown using the new `/song` command.

![bot listening activity](https://user-images.githubusercontent.com/46572320/151660642-f6f8c822-49eb-4837-87b7-df60c460f203.png)
![using /song](https://user-images.githubusercontent.com/46572320/151660647-71796307-81d4-4bc2-be70-bd2d5ac75dbd.png)

## how

the bot grabs it's data from [snip](https://github.com/dlrudie/Snip) - a simple application that grabs your spotify/itunes now playing info. for info on setting up and installing snip, check the link provided.

spotify will randomly not update it's window title and will render snip useless in grabbing song info - pause and unpause to fix.

a time elapsed is also calculated since the script was ran and will count up every second. it will pause and unpause based on your music.

## install

### requirements

- installed `discord`
- installed `discord_slash`
- installed `colorama` (2022.0201 +)

### initial
1. download the latest release and extract wherever you want, this will be the working directory for running your bot.
2. head to the [discord dev portal](https://discord.com/developers/applications) and create an application
3. navigate straight to the **bot** tab and copy your token
4. paste this token into the `config.json` file in your bot's directory (in the "token" field)
5. navigate to **oauth2** then **url generator**, and tick these boxes:![firefox_5TjrboQzel](https://user-images.githubusercontent.com/46572320/151660843-aec5639c-d334-4190-8883-4ed47bb2e843.png)
6. generate the url and go to the link
7. select the server you want to use the bot in and continue through all the steps

### bot config

1. go into your discord **user settings**, **advanced** then enable `developer mode`:![Discord_2fXiKddp66](https://user-images.githubusercontent.com/46572320/151660885-db0e127a-00de-47da-a863-31405ea7b43a.png)
2. right click your server and **copy id**: ![image](https://user-images.githubusercontent.com/46572320/151660927-8cd92c92-1062-4f3e-9e9e-04315b0ca339.png)
3. paste this as one of the entries in the `config.json` "servers" (if you add the bot to more servers, repeat this step):![image](https://user-images.githubusercontent.com/46572320/151660981-b9ebf3ca-8e51-4a2d-ba2d-ebb966493089.png)
4. assuming you already have [**snip** set-up](https://github.com/dlrudie/Snip), put your bot's files into the same directory for ease of access
5. open `Snip.exe` then right-click, match the same options to ensure `/song` will work: ![image](https://user-images.githubusercontent.com/46572320/152219038-88400a6b-1c5b-4f66-9dd9-5f8034f2fbac.png)

6. then you should be able to run `main.py` and get everything working

to enable the time elapsed counter, head into the `config.json` and set `expose_listening` to `true`. restarting will apply the settings and show `Listening for x since x` when running `/song`

## issues

**error: `discord.errors.Forbidden: 403 Forbidden (error code: 50001): Missing Access`**

ensure you ticked `applications.commands` in the dev portal when adding your bot

---

**it won't update**
* try pausing and un-pausing to get snip to update
* close and re-open snip to re-authorise with spotify

---

**error: `discord.errors.NotFound: 404 Not Found (error code: 10062): Unknown interaction`**

check your computer is not running behind. either that or discord's servers may be dying - who knows.

---

**wrong cover art**

this is a known issue with local files that will need to be fixed on snip's end. the cover art will be cleared when pausing & unpausing though.

---

**still showing song title when paused**

this once again appears to be an issue with local files and is out of my control (lies on snip/spotify's end)

## last

any more issues contact **me first** before the creator of snip:

[send issues here](https://github.com/plexiondev/discord-spotify-bot/issues)
