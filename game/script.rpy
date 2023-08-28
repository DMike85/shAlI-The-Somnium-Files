# The script of the game goes in this file.

init:
    image black = "#000000"
    $ flash = Fade(.25, 0, .75, color="#fff")
# Declare characters used by this game. The color argument colorizes the
# name of the character.
define audio.explosion = "audio/explosion.mp3"
define audio.somnium_scan = "audio/somnium_scan.ogg"
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
    "Recordad Agentes, sólo os podéis quedar en Somnium por 6 minutos."

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.
    play movie "video/somn_intro.mpeg"
    #$ renpy.pause(6, hard=True)
    play music investigation
    scene somnium
    with Dissolve(1.0)

    show Mora naix

    # These display lines of dialogue.

    m "¿Eh? ¿Por qué estoy haciendo esto?"

    m "..."

    m "Siento que he visto este símbolo en algún lado..."

    m "En fin, eso no es importante ahora."

    "Junto a Mora os dedicáis a observar detenidamente la habitación."

    m "Esto tiene que ser un error... No puede ser el Somnium de Shali."

    m "Es...muy...¿Blanco?"

    m "Algo me dice que no debería verse así..."

    m "..."

    m "No me gusta la sensación que transmite este sitio... Cuanto antes averigüemos qué ha ocurrido, mejor."

    m "Démonos prisa."

    play sound somnium_scan
    m "SOMNIUM SCAN ACTIVATE!{p=11.0} {nw}" 
    hide Mora naix
    window hide
    pause(1.0)

    play sound mental_lock
    show movil

    pause(3.0)

    hide movil
    play sound mental_lock
    show figura

    pause(3.0)

    hide figura
    play sound mental_lock
    show polea

    pause(3.0)

    hide polea
    play sound mental_lock
    show bolita

    pause(3.0)

    m "¡Vamos a ello!"

    "Mora avanza un poco hasta que se encuentra con 4 objetos."
label espada:
        
    menu:
        "Espada legendaria":
            m "Parece una espada, está muy decorada."
            menu:
                m "Parece una espada, está muy decorada.{fast}"
                "Investigar":
                    m "Según internet, esta espada es la Rebellion, la espada principal de Dante, el protagonista de la saga de juegos Devil May Cry ¿Me pregunto qué hará aquí?"
                    nerd "Uhmmmm, de hecho..."
                    nerd "Rebellion técnicamente se la dan a Dante, pero no era suya, era de su padre Sparda, que se la dió cómo recuerdo. Aunque ya no importa porque en Devil May Cry 5..."
                    m "..."
                    m "Ugh..."
                    jump espada
                "Alzar":
                    m "¡DEVIL TRIGGER, ACTIVATE!"
                    play sound explosion
                    with flash
                
        "Contenedor de basura":
            "b"
        "Teléfono Móvil":
            "c"
        "Interactuable 4":
            "d"
    
    # This ends the game.

    return
