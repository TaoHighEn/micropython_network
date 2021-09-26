import micropython, network
micropython.alloc_emergency_exception_buf( 100 )

def do_connect(ssid, pw):
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect(ssid, pw)
        while not sta_if.isconnected():
            pass
    print('network config:', sta_if.ifconfig())

def ap_model(ssid, pw, channel = 11):
    ap_if = network.WLAN(network.AP_IF)
    ap_if.active(True)  #啟用AP網路
    ap_if.config(essid=ssid, channel=11)  #設定SSID
    ap_if.config(authmode=3, password=pw)  #設定加密模式與密碼
    print('ap config:', ap_if.ifconfig())
 
