#!/bin/bash
cd /home/pi/glowstick-machine/
python /home/pi/glowstick-machine/app.py &
python /home/pi/glowstick-machine/RFID/MFRC522-python/rfid_read.py &