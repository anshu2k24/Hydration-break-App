from plyer import notification as nt
import time as t
import pandas as pd
import sys

sys.stdout.reconfigure(encoding='utf-8')    #used this cause we have special emojis in our msg

if __name__ == '__main__':
    df = pd.read_csv('titles_msgs.csv')
    i=0
    while True:
            if i==len(df):
                i=0
            else:
                nt.notify(
                    title = df.iloc[i]['Title'],
                    message = df.iloc[i]['Message'],
                    app_icon = "rest_water.ico",
                    timeout = 5
                )
                #notification every 30 mins
                t.sleep(60*30)
                i+=1  