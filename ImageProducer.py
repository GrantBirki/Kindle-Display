from BusData import BusHandler, Bus
import time
import optimage
from PIL import Image, ImageFont, ImageDraw
import subprocess


def add_time(bus_dict_input):
        img = Image.open("blank.png")
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype("arial.ttf", 52)

        arrival_time = 'Next Bus: ' + str(bus_dict_input[0].arrival) + ' minutes'
        draw.text((50, 50), arrival_time, (0), font=font)

        if len(bus_dict_input) >= 2:
            arrival_time = 'Next Bus: ' + str(bus_dict_input[1].arrival) + ' minutes'
            draw.text((50, 125), arrival_time, (0), font=font)

        else:
            pass
        
        img.convert('L')
        img.save("out.png")


def scp_send():
    scp = subprocess.check_output(["scp", "-i", "/home/pi/keys/KindPi_ssh_key.pem", "out.png", "root@192.168.1.14:/var/tmp/root"])
    #for line in scp.splitlines():
        #pass
    return scp


def main():

    #Environment Type
    environment = 'prod'

    if environment == 'prod':
        bh = BusHandler()
        bus_dict_out = bh.update_buses()
        add_time(bus_dict_out)
        scp_send()

    
    elif environment == 'dev':
        bh = BusHandler()
        bus_dict_out = bh.update_buses()
        print(bus_dict_out[0].arrival)
        add_time(bus_dict_out)

if __name__ == "__main__":
    main()

