from brightpi.brightpilib import BrightPi


bright_pi = BrightPi()
bright_pi.reset()
ir_leds = [5,6,7,8]


def ir_status():
    on_state = [0, 0, 0, 0, 5, 6, 7, 8]
    off_state = [0, 0, 0, 0, 0, 0, 0, 0]

    ir_statuses = bright_pi.get_led_on_off(ir_leds)
    if ir_statuses == on_state:
        status = 1
    elif ir_statuses == off_state:
        status = 0
    return status


def ir_switch(value):
    print('Set IR to {}.'.format(value))
    bright_pi.set_led_on_off(ir_leds, value)

