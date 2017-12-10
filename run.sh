#!/bin/bash
FLASK_APP=app.py flask run --host=0.0.0.0 &
python ./RFID/MFRC522-python/rfid_read.py &