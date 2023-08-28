# The script of the game goes in this file.

init:
    image black = "#000000"
# Declare characters used by this game. The color argument colorizes the
# name of the character.
define audio.mental_lock = "audio/mental_lock.ogg"
define audio.investigation = "audio/investigation.mp3"
define m = Character("Mora")
define pancake = Character("Pantechi")
define spam = Character("SPAMTON")
define nerd = Character("Silvia")

# The game starts here.

label start:

    stop music fadeout 0.5

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene black
    with Dissolve(1.0)

    pause(5.0)
    "Recordad Agentes, sólo os podéis quedar en Somnium por 6 minutos"

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    play music investigation
    scene somnium
    with Dissolve(1.0)

    show Mora naix

    # These display lines of dialogue.

    m "¿Eh? ¿por qué estoy haciendo esto?"

    m "..."

    m "Siento que he visto este símbolo en algún lado..."

    m "En fin, eso no es importante ahora."

    "Junto a Mora os dedicáis a observar detenidamente la habitación"

    m "Esto tiene que ser un error... No puede ser el Somnium de Shali."

    m "Es...muy...¿blanco?"

    m "Algo me dice que no debería verse así..."

    m "..."

    m "No me gusta la sensación que transmite este sitio... Cuanto antes averigüemos qué ha ocurrido,mejor."

    m "Démonos prisa"

    m "SOMNIUM SCAN ACTIVATE!"

    hide Mora naix
    pause(1.0)

    play sound mental_lock
    show movil

    pause(1.0)

    hide movil
    play sound mental_lock
    show figura

    pause(1.0)

    hide figura
    play sound mental_lock
    show polea

    pause(1.0)

    hide polea
    play sound mental_lock
    show bolita

    pause(1.0)

    m "Allé voy"
    # This ends the game.

    return
