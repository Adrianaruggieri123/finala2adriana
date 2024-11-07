 


> Open this page at [https://adrianaruggieri123.github.io/finala2adriana/](https://adrianaruggieri123.github.io/finala2adriana/)

## Use as Extension

This repository can be added as an **extension** in MakeCode.

* open [https://arcade.makecode.com/](https://arcade.makecode.com/)
* click on **New Project**
* click on **Extensions** under the gearwheel menu
* search for **https://github.com/adrianaruggieri123/finala2adriana** and import

## Edit this project ![Build status badge](https://github.com/adrianaruggieri123/finala2adriana/workflows/MakeCode/badge.svg)

To edit this repository in MakeCode.

* open [https://arcade.makecode.com/](https://arcade.makecode.com/)
* click on **Import** then click on **Import URL**
* paste **https://github.com/adrianaruggieri123/finala2adriana** and click import

## Blocks preview

This image shows the blocks code from the last commit in master.
This image may take a few minutes to refresh.

![A rendered view of the blocks](https://github.com/adrianaruggieri123/finala2adriana/raw/master/.github/makecode/blocks.png)

#### Metadata (used for search, rendering)

* for PXT/arcade
<script src="https://makecode.com/gh-pages-embed.js"></script><script>makeCodeRender("{{ site.makecode.home_url }}", "{{ site.github.owner_name }}/{{ site.github.repository_name }}");</script>

Task Master
Task Master is a MakeCode Arcade game designed to teach players about task prioritisation and focus by collecting computer icons (tasks) and avoiding food icons (distractions). The player earns points by collecting task icons, but loses points for collecting distraction icons. The game is time-bound, reinforcing focus under a constraint.
Features
	• Timed Gameplay: The game runs for 30 seconds, encouraging players to focus on collecting tasks within a limited time.
	• Score System: Players gain points for collecting computer icons and lose points for collecting food icons, reinforcing the concept of prioritising tasks over distractions.
	• Dynamic Icon Creation: Computer and food icons appear at random intervals and positions, adding to the challenge and keeping gameplay engaging.
How to Play
	1. Move the player character with the arrow keys.
	2. Collect computer icons to gain points.
	3. Avoid food icons, as they deduct points from your score.
	4. The game ends after 30 seconds, with your final score displayed.
Code Overview
Key Components
	1. Game Timer: The game runs for a total of 30 seconds, checked via the on_update_interval function.
	2. Player Sprite: The player sprite is created with arrow-key movement and a boundary restriction to keep it on the screen.
	3. Icon Creation:
		○ create_computer_icon and create_food_icon functions generate icons at random positions on the screen.
		○ Computer icons are worth positive points, while food icons are distractions that deduct points.
	4. Collision Handling: Overlap functions check for collisions between the player and icons:
		○ on_on_overlap2 handles player-computer icon collisions, increasing the score.
		○ on_on_overlap manages player-food icon collisions, decreasing the score.
Installation
To play the game:
	1. Open MakeCode Arcade.
	2. Copy and paste the code into a new project.
	3. Click Run to start the game.
Acknowledgments
This project was developed using MakeCode Arcade and was inspired by the concept of task prioritisation.
![image](https://github.com/user-attachments/assets/6a1ced1f-eda5-45bc-9b08-d23701508364)
