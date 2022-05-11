# Arctis-7-battery-percentage
Python script to get battery level from Steelseries Arctis 7 headset and create and icon in the system tray. The backgound color of the icon is adapted according to the power level.
    - 100 to 50% => Green
    - 49 to 20% => Orange
    - 20 to 0% => Red

When the headset is not connected : 
![image](https://user-images.githubusercontent.com/37587774/167914432-5c0915a1-e8e1-41ba-b62c-e0ccc3c25d13.png)

When the headset is connected :
![image](https://user-images.githubusercontent.com/37587774/167915031-9667ba9c-ea4d-4007-a6d9-3b26c14046b8.png)


### Usage
```     
    pip3 install -r requirements.txt
    python3 ./arctis7.py
```


