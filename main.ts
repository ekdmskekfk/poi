TM1650.on()
let score = 0
TM1650.showNumber(score)
basic.forever(function () {
    if (ModuleWorld_Digatal.IR(ModuleWorld_Digatal.mwDigitalNum.P2P3, ModuleWorld_Digatal.enObstacle.Obstacle)) {
        score = score + 1
        music.startMelody(music.builtInMelody(Melodies.BaDing), MelodyOptions.Once)
        TM1650.showNumber(score)
        basic.pause(100)
    }
})
