# Discord Cowsay

A Discord bot to run Cowsay, written in Python.

## Cowsay?

According to [Wikipedia](https://en.wikipedia.org/wiki/Cowsay), "cowsay is a program that generates ASCII pictures of a cow with a message. It can also generate pictures using pre-made images of other animals, such as Tux the Penguin, the Linux mascot. It is written in Perl. There is also a related program called cowthink, with cows with thought bubbles rather than speech bubbles. .cow files for cowsay exist which are able to produce different variants of "cows", with different kinds of "eyes", and so forth. It is sometimes used on IRC, desktop screenshots, and in software documentation. It is more or less a joke within hacker culture, but has been around long enough that its use is rather widespread. In 2007, it was highlighted as a Debian package of the day."

## Features

Supports a bunch of characters, such as beavis, cheese, cow, daemon, dragon, ghostbusters, kitty, meow, milk, pig, stegosaurus, stimpy, turkey, turtle, and tux.

The cowsay program is based off of [this implementation](https://github.com/VaasuDevanS/cowsay-python) and was modified to integrate into this program. The file `cowsay.py` is licensed under GPL-3.0, whereas the rest of the program is licensed under the MIT license.

## Running

There are two ways to run this program: with Docker, and without it (native). I recommend using the Docker image, as it is more portable. I won't reply to any bugs saying "this doesn't work on Windows / MacOS / Haiku".

### Docker

Download the provided `docker-compose.yml` file, and open it with your preferred text editor. Set the bot prefix to a character (default is `?`), and set the bot token. [Don't know how to get a token?](https://www.writebots.com/discord-bot-token/)

Install Docker Compose by following the instructions [here](https://docs.docker.com/compose/install/).

Start the bot with `docker-compose up -d`, and check to make sure that it's running with `docker ps`. If it isn't running, run `docker-compose up` to see debug output, and ensure that you've set all of the proper information in the `docker-compose.yml` file.

Invite your bot to the server(s) of your choice. [Don't know how?](https://discordjs.guide/preparations/adding-your-bot-to-servers.html).

### Native

Download and install the latest Python 3 from [here](https://www.python.org/downloads/). Download the source code of this program by going to the [releases page](https://github.com/sambhavsaggi/discord-cowsay-bot/releases) and downloading the .zip or .tar.gz file of the latest version. If you're not sure what to download, download the .zip file. Extract the file to somewhere you know.

Create a virtual environment with `python3 -m venv venv`, and activate it with `source venv/bin/activate`. If you are on Windows or just want to know more about virtual environments, check out the documentation [here](https://docs.python.org/3/tutorial/venv.html) on running a virtual environment.

Install the requirements with `pip3 install -r requirements.txt`.

Copy the file `sample.env` to a file called `.env`, and fill in the prefix and token. Read the section on Docker to learn how to get the token.

Run the program with `python3 discord-cowsay.py`, and have it run in the background.
