season = 0  # 0: Summer, 1: Winter
frameCounter = 0
cloudX = 0  # Cloud movement position
birdX = 0  # Bird movement position
snowflakes = []  # Store snowflake positions

# Position variables for people
person1X, person2X = 200, 400  # Beach positions
snowballPlayer1X, snowballPlayer2X = 300, 600  # Snowball fight positions

# Color constants
SUMMER_SKY = color(135, 206, 235)
WINTER_SKY = color(176, 196, 222)
SEA_COLOR = color(0, 119, 190)
BEACH_COLOR = color(255, 223, 186)
SUN_COLOR = color(255, 223, 0)
SNOW_COLOR = color(240)
PROGRESS_BAR_COLOR = color(255, 69, 0)  # Orange color for progress bar

progressBarWidth = 200  # Width of the progress bar
progressLevel = 0  # Tracks the progress for season transition

def setup():
    size(800, 600)
    noStroke()
    textSize(32)
    global snowflakes
    # Initialize 100 snowflakes with random positions and fall speeds
    snowflakes = [[random(width), random(-50, height), random(1, 3)] for _ in range(100)]

def draw():
    global season, frameCounter, cloudX, birdX, progressLevel
    
    # Background sky color based on season
    background(SUMMER_SKY if season == 0 else WINTER_SKY)
    
    # Draw current season scene
    if season == 0:
        drawSummer()
    elif season == 1:
        drawWinter()

    # Display current season text and progress bar
    displaySeasonText()
    drawProgressBar()

# Display the current season's name
def displaySeasonText():
    fill(255)
    text("Summer" if season == 0 else "Winter", 20, 40)

# Draw Summer scene with moving people and beach umbrellas
def drawSummer():
    global cloudX, birdX, person1X, person2X
    
    # Sea and Beach
    fill(SEA_COLOR)
    rect(0, height / 2, width, height / 2)
    fill(BEACH_COLOR)
    rect(0, height / 1.5, width, height / 3)
    
    # Sun
    fill(SUN_COLOR)
    ellipse(width - 100, 100, 80, 80)
    
    # Beach Umbrellas
    drawBeachUmbrella(150, height / 1.6)
    drawBeachUmbrella(350, height / 1.6)
    drawBeachUmbrella(550, height / 1.6)
    
    # Moving people on the beach
    drawPeopleOnBeach(person1X, height / 1.4)
    drawPeopleOnBeach(person2X, height / 1.4)
    drawSwimmer(500, height / 1.8)

    # Animate people moving back and forth on the beach
    person1X += sin(frameCount * 0.05) * 1.5
    person2X += sin(frameCount * 0.05 + PI) * 1.5  # Move in opposite direction

    # Moving clouds
    drawCloud(cloudX, 150)
    drawCloud(cloudX + 300, 100)
    drawCloud(cloudX + 600, 130)
    cloudX = (cloudX + 1) % width
    
    # Flying birds
    drawBird(birdX, 200)
    drawBird(birdX + 100, 250)
    drawBird(birdX + 200, 220)
    birdX = (birdX + 2) % width

# Draw Winter scene with moving people and a cozy house
def drawWinter():
    global snowballPlayer1X, snowballPlayer2X
    
    fill(SNOW_COLOR)
    rect(0, height / 2, width, height / 2)
    
    # Snowman, Santa Claus, and Winter House
    drawSnowman(width / 2, height / 2 + 80)
    drawSantaClaus(width - 150, height / 2 + 80)  # Position Santa Claus
    drawHouse(100, height / 2 + 30)  # Position house
    
    # Moving people in a snowball fight
    drawSnowballFight(snowballPlayer1X, height / 2 + 50)
    drawSnowballFight(snowballPlayer2X, height / 2 + 50)
    
    # Animate snowball fight players moving back and forth
    snowballPlayer1X += cos(frameCount * 0.03) * 2  # Oscillating movement
    snowballPlayer2X += cos(frameCount * 0.03 + PI) * 2  # Opposite direction

    # Draw falling snowflakes
    drawSnowflakes()

# Draw people sitting or playing on the beach
def drawPeopleOnBeach(x, y):
    fill(255, 200, 150)  # Skin tone
    ellipse(x, y, 20, 20)  # Head
    rect(x - 10, y + 10, 20, 30)  # Body
    fill(255, 0, 0)  # Red for swimsuit
    rect(x - 10, y + 40, 10, 20)  # Legs

# Draw a beach umbrella
def drawBeachUmbrella(x, y):
    fill(255, 0, 0)  # Red umbrella top
    triangle(x - 25, y, x + 25, y, x, y - 40)  # Umbrella top
    fill(139, 69, 19)  # Brown for umbrella pole
    rect(x - 2, y, 4, 30)  # Umbrella pole

# Draw a swimmer in the sea
def drawSwimmer(x, y):
    fill(255, 200, 150)  # Skin tone
    ellipse(x, y, 20, 20)  # Head
    rect(x - 10, y + 10, 20, 10)  # Body
    fill(0, 119, 190)  # Sea color to blend lower body in water
    rect(x - 10, y + 20, 20, 10)  # Lower part hidden in water

# Draw a cozy house in the Winter scene
def drawHouse(x, y):
    fill(210, 105, 30)  # Brown color for house walls
    rect(x, y, 60, 40)  # House base
    fill(255, 0, 0)  # Red for roof
    triangle(x - 10, y, x + 70, y, x + 30, y - 40)  # Roof
    fill(255)  # White for windows
    rect(x + 10, y + 10, 10, 10)  # Left window
    rect(x + 40, y + 10, 10, 10)  # Right window
    fill(139, 69, 19)  # Darker brown for door
    rect(x + 25, y + 20, 10, 20)  # Door

# Draw a moving cloud
def drawCloud(x, y):
    fill(255)
    ellipse(x, y, 80, 50)
    ellipse(x + 40, y, 60, 40)
    ellipse(x - 40, y, 60, 40)

# Draw a flying bird
def drawBird(x, y):
    fill(0)
    arc(x, y, 40, 20, PI, TWO_PI)
    arc(x + 40, y, 40, 20, PI, TWO_PI)

# Draw a snowman
def drawSnowman(x, y):
    fill(255)
    ellipse(x, y, 80, 80)
    ellipse(x, y - 80, 60, 60)
    fill(0)
    ellipse(x - 10, y - 85, 10, 10)
    ellipse(x + 10, y - 85, 10, 10)
    fill(255, 165, 0)
    triangle(x, y - 75, x, y - 65, x + 15, y - 70)

# Draw full-body Santa Claus carrying a sack of presents
def drawSantaClaus(x, y):
    # Draw Santa's body and suit
    fill(255, 0, 0)  # Red for Santa's suit
    rect(x - 15, y, 30, 60)  # Body
    fill(255)  # White for fur trim
    rect(x - 15, y - 10, 30, 10)  # Fur trim on coat bottom
    rect(x - 15, y + 50, 30, 10)  # Fur trim on coat top
    ellipse(x, y - 25, 30, 30)  # Head

    # Draw Santa's face
    fill(255, 200, 150)  # Skin tone
    ellipse(x, y - 25, 25, 25)  # Face
    fill(0)  # Black for eyes
    ellipse(x - 5, y - 30, 5, 5)  # Left eye
    ellipse(x + 5, y - 30, 5, 5)  # Right eye
    fill(255)  # White for beard
    ellipse(x, y - 15, 20, 10)  # Beard
    
    # Santa's hat
    fill(255, 0, 0)  # Red for the hat
    triangle(x - 15, y - 45, x + 15, y - 45, x, y - 65)  # Hat shape
    fill(255)  # White pom-pom
    ellipse(x, y - 65, 10, 10)

    # Draw arms and legs
    fill(255, 0, 0)  # Red for sleeves and pants
    rect(x - 25, y + 10, 10, 20)  # Left arm
    rect(x + 15, y + 10, 10, 20)  # Right arm
    rect(x - 10, y + 60, 10, 20)  # Left leg
    rect(x + 10, y + 60, 10, 20)  # Right leg

    # Draw sack of presents
    fill(139, 69, 19)  # Brown for sack
    ellipse(x + 20, y - 10, 30, 40)  # Sack on Santa's back
    fill(255, 223, 0)  # Yellow for gift box
    rect(x + 15, y - 20, 10, 10)  # Gift box peeking out
    line(x + 20, y - 20, x + 20, y - 10)  # Ribbon line on gift
    line(x + 15, y - 15, x + 25, y - 15)  # Ribbon line on gift

# Draw people playing a snowball fight
def drawSnowballFight(x, y):
    fill(255, 200, 150)  # Skin tone
    ellipse(x, y, 20, 20)  # Head
    rect(x - 10, y + 10, 20, 30)  # Body
    fill(0)  # Black for snowball
    ellipse(x + 15, y - 5, 10, 10)  # Snowball in hand

# Generate and draw snowflakes with slight drift
def drawSnowflakes():
    global snowflakes
    
    fill(255)
    for flake in snowflakes:
        ellipse(flake[0], flake[1], 10, 10)
        flake[1] += flake[2]
        flake[0] += sin(radians(frameCounter % 360)) * 0.5
        if flake[1] > height:
            flake[1] = random(-50, 0)

# Draw an interactive progress bar to change season
def drawProgressBar():
    global progressLevel, season
    
    fill(200)  # Background of the progress bar
    rect(width - 220, height - 40, progressBarWidth, 20)
    fill(PROGRESS_BAR_COLOR)
    rect(width - 220, height - 40, progressLevel, 20)
    
    # Check if the progress bar is full to switch season
    if progressLevel >= progressBarWidth:
        season = (season + 1) % 2
        progressLevel = 0  # Reset progress level

# Handle mouse clicks on the progress bar to increase progress
def mousePressed():
    global progressLevel
    # Check if the mouse is within the bounds of the progress bar
    if width - 220 <= mouseX <= width - 20 and height - 40 <= mouseY <= height - 20:
        progressLevel += 20  # Increase progress level on click


                                                                
