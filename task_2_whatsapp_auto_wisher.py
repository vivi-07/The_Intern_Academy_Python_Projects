import pywhatkit as kit

try:
    kit.sendwhatmsg("+91xxxxxxxxxx","Wishing you a magical birthday filled with wonderful surprises!",18,13)
    print("Birthday wishes sent successfully")

except:
    print("Error! Birthday wishes not sent")