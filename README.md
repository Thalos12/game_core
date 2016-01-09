# About this project
This project has as main aim to build a simple rpg-like game.

# How to get and run game_core
Download with git (<code>git clone https://github.com/Thalos12/game_core</code>) then
navigate to the directory through the terminal and type <code>python ChildrenOfTheGoddess.py</code>.

# How to play
At the moment you can only create a temporary profile which cannot be saved, but we expect to be able
to add the possibility to save and a battle-mode against bots in a few updates.

# Choosing a name for the profile
The game will consider upper case letters as different from lower case letter.
Profiles named pippo, Pippo, PIPPO, PiPpO, etc… can all be assigned to different players.
No two players can have the same name.

# Structure of the profile
Your profile has four main aspects for now:
<ul>
<li>character informations
<li>weapon stats
<li>armor stats
<li>skill stats (under testing)
</ul>
Character informations are NAME LEVEL, EXP, MONEY, VIT, STR, RES, AGI, INT.
Weapon stats are NAME, KIND, DESCRIPTION and damage modifiers for pierce, slash, impact
magic and ranged attacks.
Armor stats are NAME, KIND, DESCRIPTION and damage reducers for pierce, slash, impact,
magic and ranged attacks.
Skills will be available in the future.

# Damage
The estimate of the damage dealt is based on different stats for each kind of attack
as follows:
<ul>
<li>pierce, slash depend on STR
<li>magic depends on INT
<li>ranged depends on AGI
</ul>
The possible maximum damage dealt is based on the damage modifier of the currently
equipped weapon for the kind of attack you use.
The amount of damage prevented depends on RES and the damage reducer of the currently
equipper armor for the kind of attack you receive.
More details may be added in the future.

# Saving
<in developement>

# New updates
There will be many changes in the code, especially in the beginning.
Expect your profiles to be unusable every update.

# Notice
The game_core code is distributed without any warranty: use it at your own risk.

# Copyright
Anybody can download the code and redistribute it (non commercially).
Nobody can claim ownership over the code, the artwork, the music and thesound with the
exception of the author(s).
Altering the code is allowed, within the limits defined above, but at your own risk: there
is no warranty on the modified code (in the future this will not be allowed anymore).
