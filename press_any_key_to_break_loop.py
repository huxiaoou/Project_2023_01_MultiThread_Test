import time
import keyboard
from threading import Thread


def test_fun_for_press_any_key_to_continue():
    shared_break_tag = {"val": False}

    def main():
        content = "Press key 'q' to break .......... "
        while not shared_break_tag.get("val"):
            print("\r" + content, end="")
            time.sleep(0.05)
            content = content[1:] + content[0]
        return 0

    def rcv_break_signal():
        while True:
            if keyboard.is_pressed("q"):
                shared_break_tag["val"] = True
                break

        return 0

    t0 = Thread(target=rcv_break_signal)
    t1 = Thread(target=main)
    t0.start()
    t1.start()
    return 0


test_fun_for_press_any_key_to_continue()
