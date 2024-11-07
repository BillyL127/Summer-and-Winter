# Summer and Winter Interactive Coding Project
A dynamic interactive project illustrating seasonal changes between summer and winter through animations and user interactions, created in Processing. 

## Table of Contents
* [General Info](#general-information)
* [Technologies Used](#technologies-used)
* [Features](#features)
* [Screenshots](#screenshots)
* [Setup](#setup)
* [Usage](#usage)
* [Project Status](#project-status)
* [Room for Improvement](#room-for-improvement)
* [Acknowledgements](#acknowledgements)
* [Contact](#contact)
<!-- * [License](#license) -->


## General Information
This project, "Summer and Winter," is an interactive visual experience designed to illustrate the beauty of seasonal transitions. Through animations and interactive elements, users can switch between summer and winter scenes, engaging with each season's unique visual elements, like moving clouds, snowflakes, and characters.

Problem & Purpose
Problem: Interactive visuals can often lack the depth to create a truly immersive experience of seasonal changes.
Purpose: This project allows users to explore and control seasonal transitions, enhancing engagement and visual storytelling through creative coding.
Reason: This project was undertaken to combine coding with artistic design principles, exploring the possibilities of Processing.py for creating dynamic, interactive scenes.


## Technologies Used
Processing.py - Python mode for Processing
Python - version 3.x


## Features
Seasonal Transitions: Toggle between summer and winter scenes through an interactive progress bar.
Custom Animations: Includes elements like moving clouds, birds, and falling snowflakes to bring each season to life.
User Interaction: The progress bar allows users to control seasonal changes, creating a personalized experience.
Distinct Color Palettes: Custom colors for summer and winter scenes, reflecting the mood of each season.


## Screenshots
<img width="797" alt="Summer Screenshot" src="https://github.com/user-attachments/assets/10c769e6-f278-43b9-b5c0-c616ddce8069">
Description: A bright, sunny beach scene with moving clouds and birds.

<img width="793" alt="Winter Screenshot" src="https://github.com/user-attachments/assets/7bf1f84f-3319-41dc-b171-c11054ad0cda">
Description: A snowy winter scene with falling snowflakes, a snowman, and characters having a snowball fight


## Setup
What are the project requirements/dependencies? Where are they listed? A requirements.txt or a Pipfile.lock file perhaps? Where is it located?

Proceed to describe how to install / setup one's local environment / get started with the project.


## Usage
This project allows users to experience a seamless transition between summer and winter scenes using an interactive progress bar. Below are specific use cases and code examples for customizing elements.

1. Starting the Program
Open the summer_and_winter.pyde file in Processing (Python mode).
Press the Run button in Processing to launch the program.
The project opens with a summer scene by default.
2. Interacting with the Progress Bar
The interactive progress bar at the bottom allows users to toggle between summer and winter scenes.
To switch seasons, click within the progress bar area. Each click increases the bar’s progress level.
When the bar is full, the scene transitions from summer to winter (or vice versa), resetting the progress bar.
3. Code Customization Examples
Changing the Speed of Cloud Movement

To adjust the speed of the clouds in the summer scene:
`# Inside the drawSummer() function
cloudX += 2  # Default speed is 2; increase or decrease this value for different speeds`

Adjusting Snowflake Size and Speed
To customize snowflake appearance in the winter scene:
`# Inside the setup() function, where snowflakes are initialized
snowflakes = [[random(width), random(-50, height), random(1, 5)] for _ in range(100)]
# Modify the range in random(1, 5) to increase or decrease the fall speed of snowflakes
`

Changing Colors of Seasonal Elements
You can modify the colors used for different seasons by updating the color constants:
`# Modify these constants to adjust sky and element colors
SUMMER_SKY = color(135, 206, 235)
WINTER_SKY = color(176, 196, 222)
SEA_COLOR = color(0, 119, 190)
BEACH_COLOR = color(255, 223, 186)
SUN_COLOR = color(255, 223, 0)
SNOW_COLOR = color(240)
`
4. Use Case Examples
Switching Seasons: Explore the visual changes in each season by repeatedly clicking the progress bar. Watch how colors, animations, and character actions adapt to each season’s theme.
Editing Character Movement: You can adjust the movement of characters (such as beachgoers or snowball players) by modifying their x coordinates in each frame to change their animation patterns.
By interacting with the progress bar, customizing speeds, colors, and character actions, you can personalize the experience and explore different seasonal dynamics within this project.

## Project Status
Project is: _complete_ 


## Room for Improvement

Room for improvement:
- Enhanced interaction: Allow users to control more elements, like changing weather or time of day.
- Improved animations: Add more detailed and physics-based animations for greater realism.

To do:
- Physics-based interactions for elements like snowflakes and waves.
- Additional seasonal scenes, such as spring and autumn, to expand the project’s scope.


## Acknowledgements
Inspired by the YouTube video "Creative Coding for Beginners - Full Course!" by Dan.
Resources used:
Programming 101 by Meyer
Coding Art: A Guide to Creativity with Processing and p5.js by Funk
Geometric Computation: Foundations for Design by Ko
Processing Cheat Sheet by Openlab


## Contact
Created by [@BillyL127](https://www.flynerd.pl/) - feel free to contact me!
