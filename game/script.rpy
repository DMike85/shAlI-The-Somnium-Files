# The script of the game goes in this file.

init:
    image black = "#000000"

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define m = Character("Mora")
define pancake = Character("Pantechi")
define spam = Character("SPAMTON")
define nerd = Character("Silvia")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene black
    with Dissolve(1.0)

    pause(0.5)
    "Recordad Agentes, sólo os podéis quedar en Somnium por 6 minutos"

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

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

    show Mora happy

    m "Did you know i'm circumcised?"

    # This ends the game.

    return
