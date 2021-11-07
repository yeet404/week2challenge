# week2challenge

## Setup

You will need `Django` and `SQLite`

### Django

Simply `pip install Django` in your terminal or use the Mac or Linux `pip` equivalent

### SQLite (Windows Installation)

- based on [this tutorial](https://youtu.be/wXEZZ2JT3-k)

1. Go to the [SQLite download page](https://www.sqlite.org/download.html) and download `sqlite-tools-win32-x86-3360000` (under "Precompiled Binaries for Windows")
- There should be a folder of the same name inside the zip, and it should contain 3 `.exe` files
- Move this folder into your `C:\` drive, and you (probably should) rename it to `sqlite3`

2. Then search "Edit the system enviroment variables" in windows search (open windows search by pressing winkey)
- If for some reason the above does not work, open Control Panel and paste `Control Panel\System and Security\System` into address bar
- Then go to "Advanced system settings"

3. Click `Enviroment variables` > `System variables` > `Path` > `Edit` > `New`
- Enter path of your `sqlite3` folder (e.g. `C:\sqlite3`)
- Be sure to click on sys var's path **NOT** user var

To ensure that you have successfully installed SQLite, run `sqlite3` in your terminal

## Running the site

After cloning the repo, `cd` into `bank/`
- Be sure to `cd` into `.../week2challenge/bank/` and **NOT** `.../week2challenge/bank/bank/`

Enter `python manage.py runserver` to start the application
- The server will likely be at `http://127.0.0.1:8000/`
- Copy this into your browser

You should be greeted with a login/register page.

**If something goes wrong (when attempting to runserver)**:
- In `.../week2challenge/bank/`, try entering `python manage.py makemigrations` and then `python manage.py migrate`

Some user accounts are already premade (from when I was testing).
Here are their usernames and passwords, if you would like to log into them:

name2
- p: name21234567890

name4
- p: name41234567890

name5
- p: name51234567890

yeet
- p: yeet1234567890

I forgor to add a `.gitignore` 💀. 
I honestly have no clue what impact (if any) the pychache files have, and I figured that including my premade database saves you the hassle of running the migration commands anyways (assuming everything went well)
