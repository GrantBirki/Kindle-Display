from BusData import BusHandler, Bus
import time
import optimage
from PIL import Image, ImageFont, ImageDraw
import subprocess
from datetime import datetime
from pstTime import get_pst_time, get_utc_time



def add_time(bus_list_input, bus_number):
        img = Image.open("blank.png")
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype("arial.ttf", 52)
        fontsmall = ImageFont.truetype("arial.ttf", 40)
        fontsmaller = ImageFont.truetype("arial.ttf", 36)

        if globaltimezone == 'pst':
            
            current_time_pst = get_pst_time('partial')
           
            print_time = "     Local Time: " + current_time_pst
            draw.text((50, 50), print_time, (0), font=fontsmall)

        else:
            current_time = get_utc_time()
            print_time = "     UTC Time: " + current_time
            draw.text((50, 50), print_time, (0), font=fontsmall)

        if len(bus_list_input) == 1:
            bus_dict_input0 = bus_list_input[0]
            arrival_time = '  Bus ' + bus_number[0] + ': ' + str(bus_dict_input0[0].arrival) + ' minutes'
            draw.text((50, 125), arrival_time, (0), font=font)

            if bus_dict_input0[0].predicted == True:
                schedule = '                 Real Time'
                draw.text((50, 185), schedule, (0), font=fontsmaller)

            else:
                schedule = '                 Scheduled'
                draw.text((50, 185), schedule, (0), font=fontsmaller)

            if len(bus_dict_input0) >= 2:
                arrival_time = '  Bus ' + bus_number[0] + ': ' + str(bus_dict_input0[1].arrival) + ' minutes'
                draw.text((50, 250), arrival_time, (0), font=font)
                if bus_dict_input0[1].predicted == True:
                    schedule2 = '                 Real Time'
                    draw.text((50, 310), schedule2, (0), font=fontsmaller)
                else:
                    schedule2 = '                 Scheduled'
                    draw.text((50, 310), schedule2, (0), font=fontsmaller)

            else:
                pass
            
            img.convert('L')
            img.save("out.png")


        elif len(bus_list_input) == 2:

            bus_dict_input0 = bus_list_input[0]
            arrival_time = '  Bus ' + bus_number[0] + ': ' + str(bus_dict_input0[0].arrival) + ' minutes'
            draw.text((50, 125), arrival_time, (0), font=font)

            if bus_dict_input0[0].predicted == True:
                schedule = '                 Real Time'
                draw.text((50, 185), schedule, (0), font=fontsmaller)

            else:
                schedule = '                 Scheduled'
                draw.text((50, 185), schedule, (0), font=fontsmaller)

            if len(bus_dict_input0) >= 2:
                arrival_time = '  Bus ' + bus_number[0] + ': ' + str(bus_dict_input0[1].arrival) + ' minutes'
                draw.text((50, 250), arrival_time, (0), font=font)
                if bus_dict_input0[1].predicted == True:
                    schedule2 = '                 Real Time'
                    draw.text((50, 310), schedule2, (0), font=fontsmaller)
                else:
                    schedule2 = '                 Scheduled'
                    draw.text((50, 310), schedule2, (0), font=fontsmaller)

            else:
                pass

            # Bus 2 print out starts here ------------------------------------------
            bus_dict_input1 = bus_list_input[1]
            arrival_time = '  Bus ' + bus_number[1] + ': ' + str(bus_dict_input1[0].arrival) + ' minutes'
            draw.text((50, 435), arrival_time, (0), font=font)

            if bus_dict_input1[0].predicted == True:
                schedule = '                 Real Time'
                draw.text((50, 495), schedule, (0), font=fontsmaller)

            else:
                schedule = '                 Scheduled'
                draw.text((50, 495), schedule, (0), font=fontsmaller)

            if len(bus_dict_input1) >= 2:
                arrival_time = '  Bus ' + bus_number[1] + ': ' + str(bus_dict_input1[1].arrival) + ' minutes'
                draw.text((50, 570), arrival_time, (0), font=font)
                if bus_dict_input1[1].predicted == True:
                    schedule2 = '                 Real Time'
                    draw.text((50, 630), schedule2, (0), font=fontsmaller)
                else:
                    schedule2 = '                 Scheduled'
                    draw.text((50, 630), schedule2, (0), font=fontsmaller)

            else:
                pass
            
            img.convert('L')
            img.save("out.png")


def scp_send():
    try:
        scp = subprocess.check_output(["scp", "-i", "/home/pi/keys/KindPi_ssh_key.pem", "out.png", "root@192.168.1.14:/var/tmp/root"])
        #for line in scp.splitlines():
            #pass
    except:
        time.sleep(30)
        scp = subprocess.check_output(["scp", "-i", "/home/pi/keys/KindPi_ssh_key.pem", "out.png", "root@192.168.1.14:/var/tmp/root"])
    return scp

def logging_data(bus_dict_log):
    with open('logs.txt', 'a') as f:
        log_time = get_pst_time('full')
        log_line = str(bus_dict_log[0].predicted) + ', ' + str(bus_dict_log[0].arrival) + ', ' + log_time + '\n'
        f.write(log_line)


def main(environment, timezone, bus_numbers, bus_urls):
    global globaltimezone
    globaltimezone = timezone

    if environment == 'prod':
        while True:
            bus_master_list = []
            len_of_bus_numbers = len(bus_numbers)
            for i in range(len_of_bus_numbers):
                if i == 0:
                    bh = BusHandler()
                    bus_dict_out0 = bh.update_buses(bus_urls[i])
                    bus_master_list.append(bus_dict_out0)

                elif i == 1:
                    bh = BusHandler()
                    bus_dict_out1 = bh.update_buses(bus_urls[i])
                    bus_master_list.append(bus_dict_out1)

            
            add_time(bus_master_list, bus_numbers)
            scp_send()
            time.sleep(30)

    
    elif environment == 'dev':
        bus_master_list = []
        len_of_bus_numbers = len(bus_numbers)
        for i in range(len_of_bus_numbers):
            if i == 0:
                bh = BusHandler()
                bus_dict_out0 = bh.update_buses(bus_urls[i])
                bus_master_list.append(bus_dict_out0)

            elif i == 1:
                bh = BusHandler()
                bus_dict_out1 = bh.update_buses(bus_urls[i])
                bus_master_list.append(bus_dict_out1)

            
        add_time(bus_master_list, bus_numbers)

        print(bus_master_list)
        

if __name__ == "__main__":
    timezone = 'pst'
    environment = 'prod'
    bus_numbers = ['62', '31']
    bus_urls = ['http://api.pugetsound.onebusaway.org/api/where/arrivals-and-departures-for-stop/1_18270.json?key=', 'http://api.pugetsound.onebusaway.org/api/where/arrivals-and-departures-for-stop/1_18250.json?key=']
    main(environment, timezone, bus_numbers, bus_urls)
