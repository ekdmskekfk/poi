score = 0
TM1650.on()
TM1650.show_number(score)

def on_forever():
    global score
    if ModuleWorld_Digatal.IR(ModuleWorld_Digatal.mwDigitalNum.P2P3,
        ModuleWorld_Digatal.enObstacle.OBSTACLE):
        score = score + 1
        music.start_melody(music.built_in_melody(Melodies.BA_DING), MelodyOptions.ONCE)
        TM1650.show_number(score)
        basic.pause(100)
basic.forever(on_forever)

