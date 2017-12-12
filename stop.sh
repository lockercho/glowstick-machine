#!/bin/bash
ps uax | grep app.py | grep -v grep | awk '{print $2}' | xargs kill
ps uax | grep rfid_read | grep -v grep | awk '{print $2}' | xargs kill