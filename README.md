# glowstick-machine

This is an MVP glow stick rental machine prototype.
The machine is simulated by an ipad as the display + camera, and an RPi used as web server and RFID reader.
Software implemented using Python, Flask, Websocket.

This machine implements a whole process of rental:
1. User scans their concert ticket by the iPad camera.
2. User scans their easy card.
3. The RFID reader on the RPi will notify the website and automatically guide the user to the next step.
4. User gets their glow stick for this concert.

## Hardware Environment
- iPad
- Raspberry Pi 3
- RFID reader

## Software dependencies
- Python
- Flask
- Socket.io

#### The private key in this REPO is used only for self-sign so no security hole.
