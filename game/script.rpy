# odio programar

init:
    image black = "#000000"
    image white = "#FFFFFF"
    image somnium = "somnium.jpg"
    $ flash = Fade(.25, 0, .75, color="#fff")
# Declare characters used by this game. The color argument colorizes the
# name of the character.
define audio.spamton ="audio/Spamton.mp3"
define audio.explosion = "audio/explosion.mp3"
define audio.somnium_scan = "audio/somnium_scan.ogg"
define audio.mental_lock = "audio/mental_lock.ogg"
define audio.investigation = "audio/investigation.mp3"
define audio.psync_init = "audio/psync_init.mp3"
define m = Character("Mora")
define pancake = Character("Pantechi")
define spam = Character("SPAMTON", kind=nvl)
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
    scene black
    play sound psync_init
    pause(6)
    scene white
    with Dissolve(2)
    pause(0.5)
    play movie "video/somn_intro.mpeg"
    pause(1)
    scene black
    pause(6)
    #$ renpy.pause(6, hard=True)

    play music investigation
    scene somnium
    with Dissolve(1.5)

    show Mora naix

    # These display lines of dialogue.

    m "¿Eh? {w=1.0}¿Por qué estoy haciendo esto?"

    m "..."

    m "Siento que he visto este símbolo en algún lado..."

    m "En fin, eso no es importante ahora."

    "Junto a Mora os dedicáis a observar detenidamente la habitación."

    m "Esto tiene que ser un error...{w=0.75} No puede ser el Somnium de Shali."

    m "Es...{w=0.75} muy... {w=0.75}¿Blanco?"

    m "Algo me dice que no debería verse así..."

    m "..."

    m "No me gusta la sensación que transmite este sitio...{w=0.75} Cuanto antes averigüemos qué ha ocurrido, mejor."

    m "Démonos prisa."

    play sound somnium_scan
    m "SOMNIUM SCAN ACTIVATE!{p=11.0} {nw}" #Es bastante chufa, pero me ha dado dolores de cabeza hacer esto
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
label timies1:
        
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
                    jump timies1
                "Alzar":
                    m "¡DEVIL TRIGGER, ACTIVATE!"
                    play sound explosion
                    with flash
                    $ renpy.quit()
        "Contenedor de basura":
            play music spamton
            spam "HEY EVERY !! IT'S ME!!! EV3RY BUDDY 'S FAVORITE [[Number 1 Rated Salesman1997]] SPAMT SPAMTON G. SPAMTON!! WOAH!! IF IT ISN'T A... LIGHT nER! HEY-HE Y HEY!!! LOOKS LIKE YOU'RE{nw}" 
            spam "[[All Alone On A Late Night?]] ALL YOUR FRIENDS, [[Abandoned you for the slime]] YOU ARE? SALES, GONE DOWN THE [[Drain]] [[Drain]]?? LIVING IN A GODDAMN GARBAGE CAN???{nw}" 
            spam "WELL HAVE I GOT A [[Specil Deal]] FOR LONELY [[Hearts]] LIKE YOU!! IF YOU'VE [[Lost Control Of Your Life]] THEN YOU JUST GOTTA GRAB IT BY THE [[Silly Strings]] WHY BE THE [[Little Sponge]]{nw}" 
            spam "WHO HATES ITS [[$4.99]] LIFE WHEN YOU CAN BE A [[BIG SHOT!!!]] [[BIG SHOT!!!!]] [[BIG SHOT!!!!!]] THAT'S RIGHT!! NOW'S YOUR CHANCE TO BE A [[BIG SHOT]]!! AND I HAVE JUST. THE THING. YOU NEED.{nw}" 
            spam "THAT'S [[Hyperlink Blocked]] YOU WANT IT. YOU WANT [[Hyperlink Blocked]] DON'T YOU. WELL HAVE I GOT A DEAL FOR YOU!! ALL YOU HAVE TO DO IS SHOW ME. YOUR [[HeartShapedObject]].{nw}" 
            spam "YOU'RE LIGHT neR< AREN'T YOU? YOUVE GOT THE [[LIGHT.]] WHY DON'T YOU [[Show it off?]]"
            nvl clear
            stop music
            show mora spamton
            m ":o"
            play music investigation
            jump timies1
        "Teléfono Móvil":
            m "Es un smartphone, parece que está apagado." 
            menu:
                "Lanzarlo contra la pared":
                    m "Si creéis que la violencia es la solución a todos los problemas..."
                    m "No voy a cuestionaros."
                    m "Preparaos para presenciar mis dotes profesionales de lanzamiento."
                    m "¡HYYAAA!"
                    "Mora lanza el móvil contra la pared con una fuerza sobrehumana."
                    "Lo hace tan fuerte que la pared se agrieta."
                    "El móvil permanece ileso."
                    m "..."
                    m "Vaya, debe de ser un No-kian si ha conseguido agrietar la pared así..."
                    m "Huh... espero que esto no tenga ningún impacto negativo para la cognición de Shali..."
                    jump timies1
                "Cargarlo":
                    "Mora mira alrededor en buscar de un cargador y un enchufe. No parece haber nada en los alrededores que sea remotamente similar."
                    m "Sería una buena idea..."
                    m "Si no fuera porque no hay absolutamente nada con qué hacerlo..."
                    m "..."
                    m "(¿Acaso ha habido alguna vez un cargador y un enchufe juntos en un somnium?)"
                    jump timies1
                "Encenderlo":
                    "Mora mantiene pulsado el botón de encendido y la pantalla se ilumina."
                    m "¡Oh! Se ha encendido... pensé que no tendría batería... ¿Quién pensaría que la opción más obvia sería la correcta? Jeje."
                    m "¿No tiene contraseña? Con lo paranoica que es la gente hoy en día, pensaría que la gente no dejaría su información tan desprotegida."
                    m "Veamos a ver si hay algo de valor..."
                    m "..."
                    m "Qué raro...solo hay una app. TO-Witter - Bueno, Z..."
                    m "Este Jen Follet, desde que creó las Trollface Coins sólo toma malas decisiones."
                    #Aquí va la imagen del toweet, ya se peleará con ello la Silvia del futuro.
                    m "La última actividad digital de la víctima es un tweet que habla sobre un videojuego."
                    m "Parece que no era de su agrado."
                    m "Mmm...es bastante curioso que la diferencia de tiempo entre la publicación de este toweet y la hora de la muerte sea tan pequeña..."
                    m "¿Es posible que el asesino estuviera en la misma habitación que la víctima en el momento de la publicación?"
                    m "Pero...no había signos de que más de una persona haya estando en la casa..."
                    m "Mmm..."
                    m "Agentes, sigamos investigando, quizás encontremos más pistas."
        "Interactuable 4":
            "d"
    "Mora continúa moviéndose por el Somnium mediante vuestras indicaciones y tras poco tiempo se encuentra con más objetos."
    menu:
        "Interactuable 1":
            m "Ligma"
        "Figura misteriosa":
            m "balls"
        "Interactuable 3":
            m "who's Steve Jobs?"
    "Miráis alrededor de la sala, buscando más objetos, cuando de la nada, estos aparecen ante vosotros."
    menu:
        "Interactuable 1":
            m "Crotolamo"
        "Puerta":
            m "Padalustro"
        "Pankechi":
            m "Permatrago"
        "Interactuable 4":
            m "Trujo"
    "Mora y los demás os desplazáis hacia la última parte de la habitación donde encontráis los siguientes objetos."
    menu:
        "Interactuable 1":
            m "jaja"
        "Interactuable 2":
            m "jiji"
        "Figura hecha bolita agarrándose la cabeza":
            m "juju"
    m "Mierda, no nos queda tiempo ¡Tenemos que salir! ¡Tendréis que averiguar su identidad vosotros!"
    m "..."
    m "(Por mucho que me joda...)"
    stop music
    window hide
    scene black
    with Dissolve(1.0)
    pause(3.0)
    "Agentes, debereis repasar la información que se os ha otorgado y averiguar quién es esa figura amenazante."
    "¿Quién será? ¿Acaso podéis fiaros los unos de los otros?"
    "Sea cómo sea, deberéis llevarlo ante la justicia... Hacedlo por la agente Shali."
    # This ends the game.

    return
