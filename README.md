# About this project

This project has as main aim to build a simple rpg-like game.

# How to get and run game_core

Download with git (<code>git clone https://github.com/Thalos12/game_core</code>) then
navigate to the directory through the terminal and type <code>python main.py</code>.

# How to play

At the moment you can only create a profile, but we expect to be able to add a complete
battle against bots in a few updates.
Update: added battle mode against ai, needs to be balanced.

# Choosing a name for the profile

The game will consider upper case letters as different from lower case letter.
Profiles named pippo, Pippo, PIPPO, PiPpO, etc… can all be assigned to different players.
No two players can have the same name.

# Structure of the profile

Your profile has four main aspects for now:
<ul>
<li>character stats
<li>weapon stats
<li>armor stats
<li>skill (under testing)
</ul>
Character stats are NAME, DESCRIPTION, LEVEL, EXP VIT, STR, RES, AGI, INT.
Weapon stats are NAME, KIND, DESCRIPTION and damage modifiers for pierce, slash, magic and
ranged attacks.
Armor stats are NAME, KIND, DESCRIPTION and damage reducers for pierce, slash, magic and
ranged attacks.
More features will be available in the future, such as skills.
Probably another kind of attack, smash, will be added, to include weapons like maces.
Update: added smash and skill, testing.

# Main menu

From here you can see the stats of your profile (<code>i</code>), current weapon
(<code>w</code>) and current armor (<code>a</code>).
You can try to battle an AI enemy (<code>A</code>) but consider that this feature is still
in development and you may be in such a situation that nor you nor the AI can deal damage
(damage done is 0) so the fight just goes on endlessly. Future updates should correct
this.

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

At the moment saving is allowed only when a new profile is created.
This is intentional also because there is no way, for now, to modify it
(e.g. level up, change equipment, etc…).

# New updates

There will be many changes in the code, especially in the beginning.
Expect your profiles to be deleted (or be unusable) in case of changes to the player 
class or to the profile modile.

# Notice

The game_core code is distributed without any warranty: use it at your own risk.

# Copyright

Anybody can download the code and redistribute it (non commercially).
Nobody can claim ownership over the code, with the exception of the author(s).
Altering the code is allowed, within the limits defined above, but at your own risk: there
is no warranty on the modified code it (in the future this will not be allowed anymore).
