import requests,json
import random
from optparse import OptionParser as OPTp
from stem.control import Controller
from flask import Flask
from requests.packages.urllib3.exceptions import InsecureRequestWarning 
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


class CREATOR_MESSAGE():
    def MAIN_PRINT():
        return """
                  
 _________        .---"""      """---.              
:______.-':      :  .--------------.  :             
| ______  |      | :                : |             
|:______I:|      | |  # SUDO        | |             
|:______I:|      | |                | |             
|:______P:|      | |  Privacy is    | |             
|         |      | |  a human right | |             
|:_____:  |      | |                | |             
|    ==   |      | :                : |             
|       V |      :  '--------------'  :             
|       + |      :'---...______...---'              
|       + |-._.-i___/'             \._              
|'-.____+_|   '-.   '-...______...-'  `-._          
:_________:      `.____________________   `-.___.-. 
                 .'.000000000000000000.'.      :___:
    IIPV      .'.111111111111111111111111.'.         
                 010001100011010001000110
              :____________________________:"""
              
    def SIDE_PRINT():
        return """
    You can use this e-mail to receive disposable messages."""
    
    def SHOW_INFO():
        try:
            print("""
                  
                  
             IIIIIIIIIIIIIIIIIIII        PPPPPPPPPPPPPPPPP        VVVVVVVV           VVVVVVVV
             I::::::::II::::::::I        P::::::::::::::::P       V::::::V           V::::::V
             I::::::::II::::::::I        P::::::PPPPPP:::::P      V::::::V           V::::::V
             II::::::IIII::::::II        PP:::::P     P:::::P     V::::::V           V::::::V
               I::::I    I::::I            P::::P     P:::::P      V:::::V           V:::::V 
               I::::I    I::::I            P::::P     P:::::P       V:::::V         V:::::V  
               I::::I    I::::I            P::::PPPPPP:::::P         V:::::V       V:::::V   
               I::::I    I::::I            P:::::::::::::PP           V:::::V     V:::::V    
               I::::I    I::::I            P::::PPPPPPPPP              V:::::V   V:::::V     
               I::::I    I::::I            P::::P                       V:::::V V:::::V      
               I::::I    I::::I            P::::P                        V:::::V:::::V       
               I::::I    I::::I            P::::P                         V:::::::::V        
             II::::::IIII::::::II        PP::::::PP                        V:::::::V         
             I::::::::II::::::::I ...... P::::::::P                         V:::::V          
             I01000110II00110100I .::::. P01000110P                          V:::V     --> CREATED FOR FREE NET
             IIIIIIIIIIIIIIIIIIII ...... PPPPPPPPPP                           VVV      --> open-source culture
                                                                                       --> ANTI-SPY
                  
                 -------------------------------------------------------------------------------------
                 ############################################################################################################
                 ############################################################################################################
                  
                  python IIPV_MAPR.py -g
                  python IIPV_MAPR.py --get
                 
                  python IIPV_MAPR.py -r [target_mail]
                  python IIPV_MAPR.py --read [target_mail]
                  
                  python IIPV_MAPR.py -T [target_mail]
                  python IIPV_MAPR.py --readwithtor [target_mail]
                  
                  ####   -h    --help             how to use   ####
                  
                  [ -g ]  --get                       -> GET NEW DISPOSABLE MAIL
                  [ -r ]  --read                      -> READ MESSAGE
                  [ -T ]  --readwithtor               -> READ MESSAGE WITH TOR CONNECTION
                  
                  <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
                  -------------------------------------------------------------------------------------
                  [NOTED - IMPORTANT]
                  + USE VPN AND PROXIES
                  + Stem Project must be installed to read messages with TOR link
                  + To use the TOR function, you must first run the TOR browser and get the relay
                  -------------------------------------------------------------------------------------
                  >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                  
                  
                  """)
        except:
            pass
                                                                                       

class GET_DOCUMENT():
    def GET_USER_AGENT():
        try:
            list_tar = []
            f_op = open("C:\\Users\\Asus\\Desktop\\user_agent_all.json")
            j_op = json.loads(f_op.read())
            for x_value in j_op["user_agents"]:
                for ix_values in j_op["user_agents"][x_value]:
                    for ixl_values in j_op["user_agents"][x_value][ix_values]:
                        for ixlp_values in j_op["user_agents"][x_value][ix_values][ixl_values]:
                            list_tar.append(ixlp_values)
            return list_tar
        except:
            pass
        
    def READING_FILE(file_name=str):
        try:
            with open(file_name,"r",errors="replace") as file_tar:
                x_file = []
                for line_x in file_tar:
                    try:
                        ext_tar = line_x.strip()
                        x_file.append(ext_tar)
                    except:
                        pass
            return x_file
        except:
            pass
        
    def GET_HEADER():
        try:
            list_agent = GET_DOCUMENT.GET_USER_AGENT()
            random_agent = random.choice(list_agent)
            ref_ex_list = GET_DOCUMENT.READING_FILE("C:\\Users\\Asus\\Desktop\\ref_list.txt")
            ref_all = random.choice(ref_ex_list)
            date_day = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
            date_month = ["Jan","Feb","Mar","Apr","Aug","Sep","Oct","Nov","Dec"]
            date_day_number = random.randint(1,30)
            date_year = random.randint(2000,2021)
            date_time_x = random.randint(10,23)
            date_time_y = random.randint(10,50)
            date_time_z = random.randint(10,55)
            keep_alive_rate = random.randint(100,155)
            main_header = {"User-Agent":str(random_agent),
                          "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                          "Connection":"Keep-Alive",
                          "Keep-Alive":str(keep_alive_rate),
                          "Content-Type":"text/html",
                          "Accept-Encoding":"gzip,deflate",
                          "Accept-Language":"en-us,en;q=0.5",
                          "Accept-Charset":"ISO-8859-1,utf-8;q=0.7,*;q=0.7",
                          "Referer":str(ref_all),
                          "Date":f"{random.choice(date_day)}, {date_day_number} {random.choice(date_month)} {date_year} {date_time_x}:{date_time_y}:{date_time_z} GMT"}
            return main_header
        except:
            pass


class SEND_REQUESTS():
    def GET_MAIL():
        try:
            req_url = "http://api.guerrillamail.com/ajax.php?f=get_email_address&ip=127.0.0.1&lang=en"
            header_target = GET_DOCUMENT.GET_HEADER()
            r_q = requests.Session()
            get_mail = json.loads(r_q.get(req_url,headers=header_target).text)
            mail_address = get_mail["email_addr"]
            r_q.close()
            return mail_address
        except:
            pass


class TOR_CONNECTION():
    def RUN_TOR(from_use,subject_use,body_use):
        html_main = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta name="viewport" content="width=device-width">
<style>
/* BODY CSS */
body {
background-color: white;
text-align: left;
line-height: 1.5;
letter-spacing: 0.4px;
color: #363636;
font-family: Monaco, sans-serif;
font-size: 15px;
padding-right: 20px;
padding-left: 20px;
}
/* H2 H3 CSS */
h2, h3 {
color: #a30000;
font-family: Verdana, sans-serif;
font-size: 18px;
letter-spacing: 5px;
text-align: left;
padding-top: 4px;
padding-right: 20px;
padding-left: 20px;
margin-left: 20px;
margin-right: 20px;
overflow: auto;
}
h4 {
color: black;
font-family: Verdana, sans-serif;
font-size: 14px;
letter-spacing: 5px;
text-align: left;
padding-top: 4px;
padding-left: 20px;
padding-right: 20px;
margin-left: 20px;
margin-right: 20px;
overflow: auto;
}
/* P CSS */
p {
padding-left: 20px;
padding-right: 20px;
margin-left: 20px;
margin-right: 20px;
overflow: auto;
}
</style>
<title>IIPV</title>
</head>
<body>
<h2>DISPOSABLE MAIL PRIVACY</h2>
<h4>FROM: %s</h4>
<h4>SUBJECT: %s</h4>
%s
</body>
</html>
"""%(from_use,subject_use,body_use)
        app = Flask(__name__,template_folder='template')
        @app.route('/')
        def index():
          return html_main
        print("\n")
        print('[  CONNECTING TO TOR BASE  ]')
        with Controller.from_port() as controller:
              controller.authenticate()
              response = controller.create_ephemeral_hidden_service({80: 5000}, await_publication = True)
              print("\n")
              print("SERVICE IS AVAILABLE: [--> %s.onion ]" % response.service_id)
              print("PLEASE USE TOR BROWSER TO CHECK YOUR MESSAGE")
              print("\n")
              try:
                  app.run(debug=False)
              finally:
                  print("\n")
                  print("[SHUTTING DOWN BY USER]")

class DEFINE_PROCESS():
    def GET_NEW_MAIL():
        try:
            print(CREATOR_MESSAGE.MAIN_PRINT())
            new_mail = SEND_REQUESTS.GET_MAIL()
            print("\n")
            print("[+] COMPLETED")
            print(f"[ {new_mail} ]")
            print(CREATOR_MESSAGE.SIDE_PRINT())
            print("\n")
            mess_tx = "[>] Remember that message will be deleted when you read"
            mess_tx += "\n"
            mess_tx += "[>] Transmission of the message may take time"
            print(mess_tx)
            print("\n")
        except:
            pass
    
    def GET_MESSAGE_FROM(user_input):
        try:
            cont_before_mail = f"http://api.guerrillamail.com/ajax.php?f=set_email_user&email_user={str(user_input)}"
            check_mail = "http://api.guerrillamail.com/ajax.php?f=check_email&seq=1"
            header_target = GET_DOCUMENT.GET_HEADER()
            r_q = requests.Session()
            r_q.get(cont_before_mail,
                    headers=header_target)
            get_mail = json.loads(r_q.get(check_mail,headers=header_target).text)
            mail_id = get_mail['list'][0]['mail_id']
            fetch_mail_on = f"http://api.guerrillamail.com/ajax.php?f=fetch_email&email_id={mail_id}"
            fetch_get = r_q.get(fetch_mail_on,
                                headers=header_target)
            fetch_json = json.loads(fetch_get.text)
            print("\n")
            print("[>] Be sure to save the message before closing or refreshing the page")
            print("\n")
            print("[>] COMPLETED")
            print("\n")
            print("[>] IGNORE FORMATS OF HTML")
            print(f"MAIL FROM: {fetch_json['mail_from']}")
            print(f"MAIL SUBJECT: {fetch_json['mail_subject']}")
            print("\n")
            print(fetch_json["mail_body"])
            delete_mail = f"http://api.guerrillamail.com/ajax.php?f=del_email&email_ids[]={mail_id}"
            r_q.get(delete_mail)
            print("\n")
            print("MAIL HAS BEEN DELETED")
            print("\n")
            r_q.close()
        except:
            print("\n")
            print("MAIL MAY BE DELETED OR NOT YET AVAILABLE, CHECK LATER")
            print("\n")
    
    def GET_MESSAGE_WITH_TOR(user_input):
        try:
            cont_before_mail = f"http://api.guerrillamail.com/ajax.php?f=set_email_user&email_user={str(user_input)}"
            check_mail = "http://api.guerrillamail.com/ajax.php?f=check_email&seq=1"
            header_target = GET_DOCUMENT.GET_HEADER()
            r_q = requests.Session()
            r_q.get(cont_before_mail,
                    headers=header_target)
            get_mail = json.loads(r_q.get(check_mail,headers=header_target).text)
            mail_id = get_mail['list'][0]['mail_id']
            fetch_mail_on = f"http://api.guerrillamail.com/ajax.php?f=fetch_email&email_id={mail_id}"
            fetch_get = r_q.get(fetch_mail_on,
                                headers=header_target)
            fetch_json = json.loads(fetch_get.text)
            print("\n")
            print("[>] Be sure to save the message before closing or refreshing the page")
            print("\n")
            print("[>] MESSAGE WILL BE DELETED AFTER SHUTDOWN")
            print("[>] SITE WILL BE BLOCKED WHEN YOU TURN OFF THE CONNECTION")
            print("[>] CONNECTIVITY MAY BE SLOW DEPENDING ON YOUR INTERNET, PLEASE WAIT")
            print("[>] STARTING...")
            print("\n")
            TOR_CONNECTION.RUN_TOR(fetch_json['mail_from'],
                                   fetch_json['mail_subject'],
                                   fetch_json["mail_body"])
            delete_mail = f"http://api.guerrillamail.com/ajax.php?f=del_email&email_ids[]={mail_id}"
            r_q.get(delete_mail)
            print("\n")
            print("[>] MAIL HAS BEEN DELETED")
            print("\n")
            r_q.close()
        except:
            print("\n")
            print("MAIL MAY BE DELETED OR NOT YET AVAILABLE, CHECK LATER")
            print("\n")
        
class RUN_MAIN():
    def START_PROCESS():
        run_args = OPTp(add_help_option=False,epilog="SITE INFO")
        run_args.add_option("-h",
                            "--help",
                            action="store_true",
                            dest="x_help",
                            help="HOW TO USE")
        run_args.add_option("-g",
                            "--get",
                            action="store_true",
                            dest="x_get",
                            help="GET NEW DISPOSABLE MAIL")
        run_args.add_option("-r",
                            "--read",
                            type="string",
                            dest="x_read",
                            help="READ MESSAGE")
        run_args.add_option("-T",
                            "--readwithtor",
                            type="string",
                            dest="x_tor",
                            help="READ MESSAGE WITH TOR CONNECTION")
        run_ops,arq_ops = run_args.parse_args()
        if run_ops.x_help:
            CREATOR_MESSAGE.SHOW_INFO()
            pass
        elif run_ops.x_get:
            DEFINE_PROCESS.GET_NEW_MAIL()
        elif run_ops.x_read:
            mail_target = str(run_ops.x_read).replace(" ","")
            DEFINE_PROCESS.GET_MESSAGE_FROM(mail_target)
        elif run_ops.x_tor:
            mail_target = str(run_ops.x_tor).replace(" ","")
            DEFINE_PROCESS.GET_MESSAGE_WITH_TOR(mail_target)
        else:
            CREATOR_MESSAGE.SHOW_INFO()
            pass

if __name__ == "__main__":
    try:
        RUN_MAIN.START_PROCESS()
    except:
        CREATOR_MESSAGE.SHOW_INFO()
        pass
