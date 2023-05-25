from sys import stdout
from time import sleep

CGREEN2 = "\033[32m"
CYELLOW2 = "\033[93m"
CCYAN2 = "\033[36m"


def show_banner():
    txt = f"""
{CYELLOW2} (                                        
{CYELLOW2} )\ )            )                       (                      )                      (                  
{CYELLOW2}(()/( (       ( /(   (     )       )     )\   (   (          ( /(      (  (  (       ) )\ )  (            
{CYELLOW2} /(_)))\  (   )\()) ))\   (     ( /(   (((_)  )(  )\  `  )   )\()) (   )\))( )(   ( /((()/(  )\   (   (   
{CYELLOW2}(_)) ((_) )\ (_))/ /((_)  )\  ' )(_))  )\___ (()\((_) /(/(  (_))/  )\ ((_))\(()\  )(_))/(_))((_)  )\  )\  
{CYELLOW2}/ __| (_)((_)| |_ (_))  _((_)) ((_)_  ((/ __| ((_)(_)((_)_\ | |_  ((_) (()(_)((_)((_)_(_) _| (_) ((_)((_) 
{CYELLOW2}\__ \ | |(_-<|  _|/ -_)| '  \()/ _` |  | (__ | '_|| || '_ \)|  _|/ _ \/ _` || '_|/ _` ||  _| | |/ _|/ _ \ 
{CYELLOW2}|___/ |_|/__/ \__|\___||_|_|_| \__,_|   \___||_|  |_|| .__/  \__|\___/\__, ||_|  \__,_||_|   |_|\__|\___/ 
{CYELLOW2}                                                     |_|              |___/                               
"""
    
    credit = f">{CCYAN2} Made by {CGREEN2}Jair Flores{CCYAN2} && {CGREEN2}Norberto Medellin{CCYAN2}\n\n"
    
    for col in txt:
        print(col, end="")
        stdout.flush()
        sleep(0.001)
    
    for col in credit:
        print(col, end="")
        stdout.flush()
        sleep(0.028)
