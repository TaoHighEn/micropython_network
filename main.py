# 連線模式


import network, urequests, time

do_connect("ALNAP", "00000000")

# AP模式
#ap_model("ALNTest_AP", "abcd1234")
# 發送Line訊息
#token =  "u9wquIGn2NyOWv5nwYsJgXGfw05GdyMIjyr2tTi8QIg"
#token="r0UFXow4AayjDbsAirKATIWClcMtPJH9RMz1SGwqmK4"
#url = "https://notify-api.line.me/api/notify"
#headers = {
#        "Authorization": "Bearer " + token,
#        "Content-Type": "application/x-www-form-urlencoded"
#    }
#message = "Yeah！ Line Notify Connect Success  "
#message = "%E9%82%84%E6%95%A2%E4%B8%8B%E4%BE%86%E5%95%8A%E5%86%B0%E9%B3%A5%EF%BC%9F"
#print("send message:") 
#r = urequests.post(url, data="message="+ message+"&imageThumbnail=https://weixin123.neocities.org/6546464.jpg&imageFullsize=https://weixin123.neocities.org/6546464.jpg", headers=headers)
#print(r.status_code)  #200
#print(r.text)
# Line

# 閃爍燈
#from machine import Pin
#import time

# 右4腳位對應到GPIO15
#led = Pin(15, Pin.OUT)

#迴圈, 重覆執行
#while True:
#    #低電位, 不亮
#    led.value(0)
#    #暫停0.5秒
#    time.sleep(0.5)
#    #高電位, 亮
#    led.value(1)
#    time.sleep(0.5)
# 閃爍燈

# 計時器
#from machine import Pin, Timer
#
## LED當前的狀態
#lightup = False
#
## 閃爍函數
#def blink(self):
#    #宣告函式中會用到全域變數 lightup
#    global lightup 
#    if lightup:
#        #假如目前狀態是亮燈, 就改為低電位, 熄滅LED
#        led.value(0)
#    else:
#        #假如目前狀態是不亮, 就改為高電位, 點亮LED
#        led.value(1)
#    #變更LED狀態
#    lightup = not lightup
#
## 右4腳位對應到GPIO15
#led = Pin(15, Pin.OUT)
#
#"""
#ESP32 有4個硬體計時器, 分別是 0、1、2、3
#"""
#tim = Timer(0)
#"""
#mode: Timer.ONE_SHOT 執行一次
#      Timer.PERIODIC 持續執行  
#period: 周期,單位亳秒(ms) 
#callback: 執行的函數
#"""
#tim.init(mode = Timer.PERIODIC, period=500, callback=blink)
# 計時器

# 蜂鳴器
#from machine import Pin, PWM
#import time
#
## 右4腳位對應到GPIO15
#buzzer = PWM(Pin(15, Pin.OUT))
## 頻率
#buzzer.freq(0)
## 工作周期
#buzzer.duty(500)
#
##buzzer = PWM(Pin(15, Pin.OUT), freq = 0, duty = 500)
#
## 頻率設定 262Hz
#buzzer.freq(262)
## 持續 1 秒
#time.sleep(1)
##關閉
#buzzer.deinit()
# 蜂鳴器

#from machine import Pin, PWM
#import time
#
## 音階
#scale = [ 0 
#    , 262, 294, 330, 349, 392, 440, 494 
#    , 523, 587, 659, 698, 784, 880, 988 
#    ,1046,1175,1318,1397,1568,1760,1976]
#
## 右4腳位對應到GPIO15
#buzzer = PWM(Pin(15, Pin.OUT))
## 頻率
#buzzer.freq(0)
## 工作周期
#buzzer.duty(500)
#
##buzzer = PWM(Pin(15, Pin.OUT), freq = 0, duty = 500)
#
## 播放音階
#for i in range(0, len(scale)):
#    # 設定頻率
#    buzzer.freq(scale[i])
#    # 持續 0.5 秒
#    time.sleep(0.5)
#
##關閉
#buzzer.deinit()

#from machine import Pin, PWM
#import time
#
## 右4腳位對應到GPIO15
#buzzer = PWM(Pin(15, Pin.OUT))
## 頻率
#buzzer.freq(0)
## 工作周期
#buzzer.duty(500)
#
## 音階
#scale = [ 0 
#    , 262, 294, 330, 349, 392, 440, 494 
#    , 523, 587, 659, 698, 784, 880, 988 
#    ,1046,1175,1318,1397,1568,1760,1976]
#
## 播放簡譜
#def play(music):
#    global buzzer
#    for i in range(0, len(music)):
#        buzzer.freq(scale[music[i]])
#        time.sleep(0.5)
#
## 簡譜
#music1 = [1,1,5,5,6,6,5,0,4,4,3,3,2,2,1,5,5,4,4,3,3,2,5,5,4,4,3,3,2,1,1,5,5,6,6,5,4,4,3,3,2,2,1]
#play(music1)
#
##關閉
#buzzer.deinit()

#from machine import Pin, PWM
#import time
#
## 右4腳位對應到GPIO15
#buzzer = PWM(Pin(15, Pin.OUT))
## 頻率
#buzzer.freq(0)
## 工作周期
#buzzer.duty(500)
#
## 音階
#scale = [ 0 
#    , 130, 149, 165, 175, 196, 220, 247 , 0 , 0, 0
#    , 262, 294, 330, 349, 392, 440, 494 , 0 , 0, 0
#    , 523, 587, 659, 698, 784, 880, 988 , 0 , 0, 0
#    ,1046,1175,1318,1397,1568,1760,1976]
#
## 播放簡譜
#def play(music, beat):
#    global buzzer
#    for i in range(0, len(music)):
#        buzzer.freq(scale[music[i]])
#        time.sleep(beat[i])
## 簡譜
#music1 = [ 
#    23, 22, 21, 17,
#
#    16, 15, 16, 17,
#
#    13, 13, 11,
#    22, 17,
#
#    21, 21, 16,
#    17, 15,
#
#    16,16,14,
#    15, 13,
#    
#    16,16,21,
#    17,21,22,
#
#    23,22,23,24,
#    25,22,25,24,
#
#    23,26,25,24,
#    25,24,23,22,
#
#    21,16,26,27,
#    31,27,26,25,
#
#    24,23,22,26,
#    25,26,25,24
#    ]
##節拍
#beat1 = [
#    2, 2, 2, 2,
#
#    2, 2, 2, 2,
#
#    1, 0.5, 0.5,
#    1.5, 0.5, 
#
#    1, 0.5, 0.5,
#    1.5, 0.5,
#
#    1, 0.5, 0.5,
#    1.5, 0.5,
#
#    1, 0.5, 0.5,
#    1, 0.5, 0.5,
#
#    0.5, 0.5,0.5, 0.5,
#    0.5, 0.5,0.5, 0.5,
#
#    0.5, 0.5,0.5, 0.5,
#    0.5, 0.5,0.5, 0.5,
#
#    0.5, 0.5,0.5, 0.5,
#    0.5, 0.5,0.5, 0.5,
#
#    0.5, 0.5,0.5, 0.5,
#    0.5, 0.5,0.5, 0.5,
#]
#
#play(music1, beat1)
#
##關閉
#buzzer.deinit()

#from machine import Pin, SoftI2C
#import ssd1306
#
## 設定 I2C
#i2c = SoftI2C(scl=Pin(15), sda=Pin(2))
## SSD1306函式庫
#display = ssd1306.SSD1306_I2C(128, 64, i2c)
## 設定文字
#display.text('Hello, World!', 0, 0, 1)
## 顯示
#display.show()

#from machine import Pin, SoftI2C
#import ssd1306
#import framebuf
#
## 設定 I2C
#i2c = SoftI2C(scl=Pin(15), sda=Pin(2))
## SSD1306函式庫
#display = ssd1306.SSD1306_I2C(128, 64, i2c)
#
#"""
#http://dotmatrixtool.com/
#16px by 16px, row major, big endian.
#"""
#data = [0x00, 0x00, 0x00, 0x00, 0x10, 0x00, 0x00, 0x38, 0x00, 0x00, 0x6c, 0x00, 0x00, 0xc6, 0x00, 0x00, 0x83, 0x00, 0x01, 0x01, 0x80, 0x02, 0x00, 0xc0, 0x04, 0x00, 0x60, 0x0c, 0x10, 0x30, 0x18, 0x00, 0x10, 0x30, 0x00, 0x0c, 0x60, 0x00, 0x06, 0x7f, 0xff, 0xfe, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]
#pic_buffer = bytearray(data)
#
#"""
#https://docs.micropython.org/en/latest/library/framebuf.html
#framebuf.MONO_VLSB
#framebuf.MONO_HLSB
#framebuf.MONO_HMSB
#"""
##data = [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x3f, 0xfc, 0x01, 0x00, 0x01, 0x00, 0x01, 0x00, 0x01, 0x00, 0x0f, 0xf0, 0x01, 0x00, 0x01, 0x00, 0x01, 0x00, 0x01, 0x00, 0x7f, 0xfe, 0x00, 0x00, 0x00, 0x00]
##pic_buffer = bytearray(data)
##fbuf = framebuf.FrameBuffer(pic_buffer, 16, 16, framebuf.MONO_HLSB)
##display.blit(fbuf, 10, 10, 0) 
##
##data = [0x00, 0x00, 0x01, 0x00, 0x01, 0x00, 0x01, 0x00, 0x3f, 0xfe, 0x03, 0x00, 0x02, 0x00, 0x07, 0x00, 0x05, 0x80, 0x04, 0x80, 0x08, 0x40, 0x10, 0x30, 0x30, 0x18, 0x00, 0x04, 0x00, 0x00, 0x00, 0x00]
##pic_buffer = bytearray(data)
##fbuf = framebuf.FrameBuffer(pic_buffer, 16, 16, framebuf.MONO_HLSB)
##display.blit(fbuf, 26, 10, 0) 
#
#data = [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x04, 0x1e, 0x0c, 0x23, 0x94, 0x40, 0xd4, 0x50, 0x74, 0x40, 0x24, 0x40, 0x74, 0x4c, 0x4c, 0x78, 0x8c, 0x1f, 0x00, 0x00, 0x00, 0x00, 0x00]
#pic_buffer = bytearray(data)
#fbuf = framebuf.FrameBuffer(pic_buffer, 16, 16, framebuf.MONO_HLSB)
#display.blit(fbuf, 42, 10, 0)
#
#data = [0x00, 0x00, 0x00, 0x00, 0x18, 0x70, 0x3f, 0x90, 0x23, 0x10, 0x20, 0x10, 0x30, 0x20, 0x10, 0x40, 0x0c, 0xc0, 0x03, 0x80, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]
#pic_buffer = bytearray(data)
#fbuf = framebuf.FrameBuffer(pic_buffer, 16, 16, framebuf.MONO_HLSB)
#
#display.blit(fbuf, 58, 10, 0)
## 顯示
#display.show()

from machine import Pin, SoftI2C
import ssd1306
import framebuf

# 設定 I2C
i2c = SoftI2C(scl=Pin(15), sda=Pin(2))
# SSD1306函式庫
display = ssd1306.SSD1306_I2C(128, 64, i2c)

"""
http://dotmatrixtool.com/
16px by 16px, row major, big endian.
"""
data = [0x00, 0x00, 0x00, 0x00, 0x10, 0x00, 0x00, 0x38, 0x00, 0x00, 0x6c, 0x00, 0x00, 0xc6, 0x00, 0x00, 0x83, 0x00, 0x01, 0x01, 0x80, 0x02, 0x00, 0xc0, 0x04, 0x00, 0x60, 0x0c, 0x10, 0x30, 0x18, 0x00, 0x10, 0x30, 0x00, 0x0c, 0x60, 0x00, 0x06, 0x7f, 0xff, 0xfe, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]
pic_buffer = bytearray(data)

"""
https://docs.micropython.org/en/latest/library/framebuf.html
framebuf.MONO_VLSB
framebuf.MONO_HLSB
framebuf.MONO_HMSB
"""
x = 128
y = 10
shiftX = 3
while True:
    if x < -42 :
        x = 128
    x = x -shiftX
    display.fill(0)
    data = [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x3f, 0xfc, 0x01, 0x00, 0x01, 0x00, 0x01, 0x00, 0x01, 0x00, 0x0f, 0xf0, 0x01, 0x00, 0x01, 0x00, 0x01, 0x00, 0x01, 0x00, 0x7f, 0xfe, 0x00, 0x00, 0x00, 0x00]
    pic_buffer = bytearray(data)
    fbuf = framebuf.FrameBuffer(pic_buffer, 16, 16, framebuf.MONO_HLSB)
    display.blit(fbuf, x, y, 0) 

    data = [0x00, 0x00, 0x01, 0x00, 0x01, 0x00, 0x01, 0x00, 0x3f, 0xfe, 0x03, 0x00, 0x02, 0x00, 0x07, 0x00, 0x05, 0x80, 0x04, 0x80, 0x08, 0x40, 0x10, 0x30, 0x30, 0x18, 0x00, 0x04, 0x00, 0x00, 0x00, 0x00]
    pic_buffer = bytearray(data)
    fbuf = framebuf.FrameBuffer(pic_buffer, 16, 16, framebuf.MONO_HLSB)
    display.blit(fbuf, x + 16, y, 0) 

    data = [0x00, 0x00, 0x00, 0x00, 0x01, 0xfe, 0x01, 0x02, 0x00, 0x82, 0x7c, 0x82, 0x44, 0xfe, 0x44, 0x82, 0x7c, 0x82, 0x44, 0xfe, 0x44, 0x82, 0x78, 0x82, 0x00, 0x82, 0x01, 0x0a, 0x02, 0x06, 0x00, 0x00]
    pic_buffer = bytearray(data)
    fbuf = framebuf.FrameBuffer(pic_buffer, 16, 16, framebuf.MONO_HLSB)
    display.blit(fbuf, x + 32, y, 0) 
    # 顯示
    display.show()
