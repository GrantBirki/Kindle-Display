from BusData import BusHandler, Bus
import time
import optimage
from PIL import Image, ImageFont, ImageDraw
import subprocess
from datetime import datetime
from pstTime import get_pst_time, get_utc_time



def add_time(bus_dict_input):
        img = Image.open("blank.png")
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype("arial.ttf", 52)
        fontsmall = ImageFont.truetype("arial.ttf", 40)
        fontsmaller = ImageFont.truetype("arial.ttf", 36)

        if timezone == 'pst':
            
            current_time_pst = get_pst_time('partial')
           
            print_time = "     Local Time: " + current_time_pst
            draw.text((50, 50), print_time, (0), font=fontsmall)

        else:
            current_time = get_utc_time()
            print_time = "     UTC Time: " + current_time
            draw.text((50, 50), print_time, (0), font=fontsmall)


        arrival_time = 'Next Bus: ' + str(bus_dict_input[0].arrival) + ' minutes'
        draw.text((50, 125), arrival_time, (0), font=font)

        if bus_dict_input[0].predicted == True:
            schedule = '                Real Time'
            draw.text((50, 185), schedule, (0), font=fontsmaller)

        else:
            schedule = '                Scheduled'
            draw.text((50, 185), schedule, (0), font=fontsmaller)

        if len(bus_dict_input) >= 2:
            arrival_time = 'Next Bus: ' + str(bus_dict_input[1].arrival) + ' minutes'
            draw.text((50, 250), arrival_time, (0), font=font)
            if bus_dict_input[1].predicted == True:
                schedule2 = '                Real Time'
                draw.text((50, 285), schedule2, (0), font=fontsmaller)
            else:
                schedule2 = '                Scheduled'
                draw.text((50, 285), schedule2, (0), font=fontsmaller)

        else:
            pass
        
        img.convert('L')
        img.save("out.png")


def scp_send():
    scp = subprocess.check_output(["scp", "-i", "/home/pi/keys/KindPi_ssh_key.pem", "out.png", "root@192.168.1.14:/var/tmp/root"])
    #for line in scp.splitlines():
        #pass
    return scp

def logging_data(bus_dict_log):
    with open('logs.txt', 'a') as f:
        log_time = get_pst_time('full')
        log_line = str(bus_dict_log[0].predicted) + ', ' + str(bus_dict_log[0].arrival) + ', ' + log_time + '\n'
        f.write(log_line)


def main():

    #Environment Type
    environment = 'prod'
    global timezone
    timezone = 'pst'

    if environment == 'prod':
        while True:
            bh = BusHandler()
            bus_dict_out = bh.update_buses()
            add_time(bus_dict_out)
            logging_data(bus_dict_out)
            scp_send()
            time.sleep(30)

    
    elif environment == 'dev':
        bh = BusHandler()
        bus_dict_out = bh.update_buses()
        print(bus_dict_out[0].arrival)
        add_time(bus_dict_out)

if __name__ == "__main__":
    main()

