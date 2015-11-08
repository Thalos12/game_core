# About this project

This project has as main aim to build the core of a simple rpg-like game.

# How to get and run game_core

Download with git (using <code>git clone https://github.com/Thalos12/game_core</code>),
navigate to the directory through the terminal then type <code>python main.py</code>.
There is no tutorial at the moment: you can only create a profile (soon we will add a
complete battle experience against bots).

# Choosing a name for the profile

The game will consider upper case letters as different from lower case letter.
Profiles named pippo, Pippo, PIPPO, PiPpO, etc… can all be assigned to different players.

# Details of the profile

Your profile has three main aspects for now:
<ul>
<li>character stats
<li>weapon stats
<li>armor stats
</ul>
Character stats are NAME, DESCRIPTION, LEVEL, EXP VIT, STR, RES, AGI, INT.
Weapon stats are NAME, KIND, DESCRIPTION and damage modifiers for pierce, slash, magic and
ranged attacks.
Armor stats are NAME, KIND, DESCRIPTION and damage reducers for pierce, slash, magic and
ranged attacks
More features will be available in the future, such as skills.
Probably another kind of attack, smash, will be added

# Main menu

From here you can see the stats of your profile (<code>i</code>), of your current weapon
(<code>w</code>) and current armor (<code>a</code>).
You can try to battle an AI enemy (<code>A</code>) but consider that this feature is still
in development and you may be in such a situation that nor you nor the AI can deal damage
(damage done is 0) so the fight just goes on endlessly.

# Damage

At the moment the damage done is calculated differently for each kind of attack:
pierce, slash depend on STR
magic depends on INT
ranged depends on AGI
The possible  maximum damage dealt is based on one of the stats and the damage modifier of
the currently equipped weapon.
The amount of damage prevented depends on RES and the damage reducer of the currently
equipper armor.

# Saving

At the moment saving is allowed only when a new profile is created.
This is intentional also because there is no way, for now, to modify it
(e.g. level up, change equipment, etc…).

# New updates

There will be many changes in the code, especially in the beginning.
Expect your profiles to be deleted in case of changes to the player class.

# Notice

The game_core code is distributed without any warranty: use it at your own risk.

# Copyright

Anybody can get the code and redistribute it (non commercially).
Nobody can claim ownership over the code, with the exception of the author(s).
Altering the code is allowed, within the limits defined above, but at your own risk: there
is no warranty on the modified code it.