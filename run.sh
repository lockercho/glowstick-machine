#!/bin/bash
python /home/pi/glowstick-machine/app.py &
python /home/pi/glowstick-machine/RFID/MFRC522-python/rfid_read.py &