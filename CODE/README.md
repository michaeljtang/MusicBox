### Project Name:
Programmable Music Box

### Hackster.io Page
https://www.hackster.io/michael-tang/programmable-music-box-1288ab

### How To Run:
1. Follow assembly instructions in above Hackster link to create physical music box
2. Use the latest PocketBeagle image from BeagleBoard.org
3. Download this project_01 folder from this repo, unzip, and then move into the Cloud9 IDE on your own PocketBeagle
4. Ensure you have Python as well as the Python AdaFruit_BBIO package installed locally. If not, the steps to execute are:
    - sudo apt-get install build-essential python-dev python-setuptools python-pip python-smbus-y
    - sudo apt-get install python-pip
    - sudo apt-get install python3-pip
    - sudo pip install Adafruit_BBIO
5. Change the permissions on the run script
    - chmod 755 run
6. Use Chron so that program will run on autoboot in the following steps
    - Navigate to your local cloud9 folder
    - Type "mkdir logs"
    - Type "sudo crontab -e"
    - Add to the end of the file "reboot sleep 30 && sh <full path to 'run'> > /var/lib/cloud9/logs/cronlog2>&1"
7. Reboot the PocketBeagle, and the code will auto-run after 30 seconds of waiting! 
8. Load in a hole punched paper in the music box, as demonstrated in the hackster.io above
9. Press the button to start!

Thanks to Erik Welsh for the ht16k33.py library included above!
