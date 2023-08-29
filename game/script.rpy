﻿# odio programar

init:
    image black = "#000000"
    image white = "#FFFFFF"
    image somnium = "somnium.jpg"
    $ flash = Fade(.25, 0, .75, color="#fff")
    default pankechi = False
# Declare characters used by this game. The color argument colorizes the
# name of the character.
define audio.spamton ="audio/Spamton.mp3"
define audio.explosion = "audio/explosion.mp3"
define audio.somnium_scan = "audio/somnium_scan.ogg"
define audio.mental_lock = "audio/mental_lock.ogg"
define audio.investigation = "audio/investigation.mp3"
define audio.psync_init = "audio/psync_init.mp3"
define m = Character("Mora")
define pancake = Character("Pankechi")
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
                "Seppuku":
                    m "Bueno...si así lo habéis decidido... ¡Allá voy!"
                    "Mora se hace el seppuku y cae al suelo"
                    #Aquí va la animación de fallar en el somnium        
            return
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
label timies2:
    menu:
        "Interactuable 1":
            m "Ligma"
        "Figura misteriosa y amenazante":
            "Mora se acerca a la figura, cuando de repente, la atrapa e intenta dejarla inconsciente"
            menu:
                "Súplex alemán":
                    "Sin rechistar, Mora intenta hacer un súplex alemán a la figura, fallando en el intento, de tal forma que se hace el súplex a sí misma."
                    m "¿Espera qué-? AAAAAAAAAAAAAAAA"
                    m "¡Uf-!"
                    m "Auch... ¿Cómo ha-?"
                    m "..."
                    m "Todos mis años cómo luchadora profesional se han ido por el desagüe..."
                    jump timies2
                "¿Quién eres?":
                    m "¿Quién eres?"
                    m "..."
                    m "..."
                    m "Me imaginaba que no iba a ser tan sencillo pero, joder tío, podrías al menos decir algo."
                    jump timies2
                "Intentar liberarse":
                    "Mora forcejea con la figura y en el proceso es capaz de fijarse en que la figura lleva una bandolera negra"
                    "Consigue soltarse, pero no parece que nada cambie realmente"
                    m "¿QUÉ NARICES? ¿PERO QUÉ TE PASA?"
                    m "UGH"
                    m "No sé quién eres, pero cómo me vuelvas a tocar, te hago ASÍN y te quedas sin riñón."
                    jump timies2
                "Gritar":
                    "Antes de poder preguntar nada sobre qué gritar, Mora se queda congelada y habla en esperanto por un momento. Tras esto, la figura desaparece."
                    m "texto esperanto placeholder, son las 2 y media de la mañana y no estoy para carácteres especiales, no me jodas"
                    m "..."
                    m "Jijiji" #ya veremos si aquí hay audio, aunque lo dudo
                    m "más texto en esperanto, de verdad que ya lo haré"
                    m "..."
                    m "¿Qué me ha pasado?... En cuanto me habéis dicho que grite..."
                    m "¡OH! No sé qué habréis visto, pero ¡es probable que tenga relación con lo ocurrido tras que me desactivaran!"
                    m "...Tiene toda la pinta de que esa figura fue quién lo hizo"
                    m "Y por ende..."
                    m "Es muy probable que también sea el asesino y el culpable de que Shali esté así..."
                    m "Llevaba una bandolera negra...Mmm, no es que sea un detalle muy identificativo... pero puede ayudarnos en algún momento."
                    m "..."
                    m "¡Continuemos! Aún hay mucho que averigüar." 
        "Interactuable 3":
            m "who's Steve Jobs?"
    "Miráis alrededor de la sala, buscando más objetos, cuando de la nada, estos aparecen ante vosotros."
label timies3:    
    menu:
        "Interactuable 1":
            m "Crotolamo"
        "Puerta":
            menu:
                "Investigar":
                    m "Parece que esta puerta está atada a un complejo sistema de poleas..."
                    m "Hay un ladrillo cómicamente grande, colocado para que al abrir la puerta, este golpee a la persona en la cabeza y lance una cuerda que atrape su torso."
                    m "Tras esto, parece que el sistema de poleas se encargaría de arrastrar a la víctima, fuera de la ventana hacia ¿una obra?..."
                    m "Mmmm...la cuerda continua hasta...la viga ligeramente oxidada..."
                    m "Es la misma que la de la escena del crimen..."
                    m "..."
                    m "(Esto debe de ser cómo se produjo el asesinato...)"
                    m "(...)"
                    jump timies3
                "Desarmar":
                    m "Ummm...dudo mucho que pueda desarmar esto...No hay ninguna herramienta y no conozco cómo o en qué orden se han ido colocando todos los elementos..."
                    m "No creo que sea la opción correcta."
                "Abrir":
                    "Mora abre la puerta"
                    "Miguel aparece, y todo el sistema de poleas repite el mismo proceso que en la realidad. En cuanto abre la puerta, un ladrillo cómicamente grande le golpea en la cabeza dejándolo K.O"
                    "De mientras cae al suelo, una cuerda se engancha a su torso, atrapándolo. Las poleas comienzan a moverse y arrastran el cuerpo por el suelo hasta llegar a una ventana."
                    "La cuerda tira del cuerpo y lo saca de la casa por la ventana para seguir arrastrándolo por la calle hasta la obra más cercana."
                    "Una vez colocado en posición, sobre este cae una viga, ligeramente oxidada, dejando su cadáver en la misma posición y en las mismas condiciones en las que se había encontra el cuerpo."
                    m "Shali...¿Cómo sabes...?...No..."
                    m "¡Esto no tiene sentido! ¡No ha podido ser ella!"
                    m "Si hubiese sido ella, ¿por qué aquella figura me desactivó y la atacó?"
                    m "Si bien es cierto que para cuando me pude reiniciar, ya había concluido todo el crimen, no me cuadra que estuviera en su estado atual de shock si ella fuera la asesina."
                    m "Agentes, ¿vosotros pensáis lo mismo, verdad?"
                    m "Quizás...simplemente ha estado en la escena del crimen...y ha visto el mecanismo...o puede que el asesino la obligara a mirar de mientras se producía el asesinato..."
                    m "..."
                    m "Estoy muy preocupada...todo esto tiene muy mala pinta...Shali... ¿Qué te ha hecho?"
                    m "Ugh. Tenemos que llegar a la conclusión de esto."
                    m "Solo nos queda un neurocandado. ¡Podemos hacerlo! ¡Saquemos la verdad a la luz!"
        "Pankechi" if not pankechi:
            menu:
                "Darle tortitas":
                    "Mora obtiene unas tortitas y se las ofrece"
                    "Pankechi las coloca en su cabeza mientras se aleja"
                    "Crees escucharle decir..."
                    #delicious pancakes.ogg
                    "Delicious pancakes"
                    m "... ¿Creo que le gustan las tortitas?"
                    $ pankechi = True
                    jump timies3
                "Oh dios mío, Pankechi del famoso videojuego People 5":
                    "Al momento de decir esto, Pankechi mira a Mora y comienza a gritar:"
                    pancake "Ueghhh.. (o^▽^o) i'm getting a wawm tingwy f-feewing fwom all this power!"
                    m "... ¿Qwé? O_O"
                    "Justo después de decir eso, Pankechi desaparece espontáneamente y no vuelve a aparecer."
                    $ pankechi = True
                    jump timies3
                "Disparar en la cabeza":
                    "Mora saca un arma que aparece de Dios sabe dónde"
                    m "¡Persona!"
                    "Mora aprieta el gatillo y le dispara"
                    "Pankechi se muere"
                    m "..."
                    m "Ups, creo que ese era del People 3"
                    $ pankechi = True
                    jump timies3
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
