rsync -avz --exclude "__history" --exclude "*~" --exclude "*.img" --exclude "home-pi-*" --exclude "dot*" --exclude "*.conf" --exclude "*.pyc" -e ssh . pi@198.0.0.234:/home/pi/atten
scp ../pi-vfd/vfd.py pi@198.0.0.234:/home/pi/atten
scp ../pi-encoder/encoder.py pi@198.0.0.234:/home/pi/atten
