import time
import rtmidi
import RPi.GPIO as GPIO

#初期化とか
midi = rtmidi.midi()
midi.open_virtual_port("Elec_Garagara")
GPIO.setmode(GPIO.BCM)

#本体に貼ったアルミテープ
GPIO.setup(17, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(27, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(22, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(10, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(9, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(11, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(5, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(6, GPIO.IN, pull_up_down = GPIO.PUD_UP)

#手元のスイッチ
GPIO.setup(14, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(15, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(18, GPIO.IN, pull_up_down = GPIO.PUD_UP)

#球体が三つ繋がっているところはGND

#中でぶつかっているかどうかのフラグ
#ないと鳴り続けるけど実際ぶつかるのは一瞬
#これいります？
flag_17 = False
flag_27 = False
flag_22 = False
flag_10 = False
flag_9 = False
flag_11 = False
flag_5 = False
flag_6 = False

#スイッチを押しているかどうかのフラグ
#無限ループ内で状態を判定しているのでないと困るかもしれない
#一個は音程変えるものなので2つだけ
flag_15 = False
flag_18 = False

try:
    while True:
	#それぞれのアルミテープにぶつかったか判定するものがなんと8つもある素敵なコード
	#ボタンを押しながら鳴らすと1オクターブくらい高くなります
        if GPIO.input(17) == False:
            if flag_17 == False:
                if GPIO.input(14) == True:
                    note_on = [0x90, 61, 112]
                else:
                    note_on = [0x90, 74, 112]
                midi.send_message(note_on)
                flag_17 = True
        else:
            note_off = [0x80, 61, 0]
            note_off = [0x80, 74, 0]
            midi.send_message(note_off)
            flag_17 = False
    
        if GPIO.input(27) == False:
            if flag_27 == False:
                if GPIO.input(14) == True:
                    note_on = [0x90, 62, 112]
                else:
                    note_on = [0x90, 76, 112]
                midi.send_message(note_on)
                flag_27 = True
        else:
            note_off = [0x80, 62, 0]
            note_off = [0x80, 76, 0]
            midi.send_message(note_off)
            flag_27 = False
            
        if GPIO.input(22) == False:
            if flag_22 == False:
                if GPIO.input(14) == True:
                    note_on = [0x90, 64, 112]
                else:
                    note_on = [0x90, 78, 112]
                midi.send_message(note_on)
                flag_22 = True
        else:
            note_off = [0x80, 64, 0]
            note_off = [0x80, 78, 0]
            midi.send_message(note_off)
            flag_22 = False
            
        if GPIO.input(10) == False:
            if flag_10 == False:
                if GPIO.input(14) == True:
                    note_on = [0x90, 66, 112]
                else:
                    note_on = [0x90, 79, 112]
                midi.send_message(note_on)
                flag_10 = True
        else:
            note_off = [0x80, 66, 0]
            note_off = [0x80, 79, 0]
            midi.send_message(note_off)
            flag_10 = False
            
        if GPIO.input(9) == False:
            if flag_9 == False:
                if GPIO.input(14) == True:
                    note_on = [0x90, 67, 112]
                else:
                    note_on = [0x90, 81, 112]
                midi.send_message(note_on)
                flag_9 = True
        else:
            note_off = [0x80, 67, 0]
            note_off = [0x80, 81, 0]
            midi.send_message(note_off)
            flag_9 = False
            
        if GPIO.input(11) == False:
            if flag_11 == False:
                if GPIO.input(14) == True:
                    note_on = [0x90, 69, 112]
                else:
                    note_on = [0x90, 83, 112]
                midi.send_message(note_on)
                flag_11 = True
        else:
            note_off = [0x80, 69, 0]
            note_off = [0x80, 83, 0]
            midi.send_message(note_off)
            flag_11 = False
            
        if GPIO.input(5) == False:
            if flag_5 == False:
                if GPIO.input(14) == True:
                    note_on = [0x90, 71, 112]
                else:
                    note_on = [0x90, 85, 112]
                midi.send_message(note_on)
                flag_5 = True
        else:
            note_off = [0x80, 71, 0]
            note_off = [0x80, 85, 0]
            midi.send_message(note_off)
            flag_5 = False
            
        if GPIO.input(6) == False:
            if flag_6 == False:
                if GPIO.input(14) == True:
                    note_on = [0x90, 71, 112]
                else:
                    note_on = [0x90, 86, 112]
                midi.send_message(note_on)
                flag_6 = True
        else:
            note_off = [0x80, 73, 0]
            note_off = [0x80, 86, 0]
            midi.send_message(note_off)
            flag_6 = False
        
	#リバーブとかサスティーンもできる・・・はず
  #midiキーボードでできることはたぶんできる
        if GPIO.input(15) == False:
            if flag_15 == False:
                midi.send_message([0xb0, 64, 127])
                print("up")
                flag_15 = True
        else:
            midi.send_message([0xb0, 64, 0])
            flag_15 = False
            
        if GPIO.input(18) == False:
            if flag_18 == False:
                midi.send_message([0xb0, 91, 127])
                flag_18 = True
        else:
            midi.send_message([0xb0, 91, 0])
            flag_18 = False
            
        time.sleep(0.005)

except KeyboardInterrupt:
    pass

GPIO.cleanup()
