from telethon import TelegramClient
import telethon.sync
import logging
import time

#logs
logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s', level=logging.WARNING)

#create file
timestr = time.strftime("%Y-%m-%d")
filename="telegramchatlist"+timestr+".html"
f= open(filename, "w+")
f.write("<html><head><style>table{font-family:arial,sans-serif;border-collapse:collapse;width:100%;}td,th{border:1px solid black;text-align:left;padding:8px;}tr:nth-child(even){background-color:#dddddd;}</style></head><body><h1>Date: "+timestr+"</h1>\n")

#credentials
api_id = 123456 #your id
api_hash = 'abc123' #your hash
name = 'anon' #your name

client = TelegramClient(name, api_id, api_hash)


async def main():
    dialogs = await client.get_dialogs(); #gets all chats
    for dialog in dialogs:
        if(dialog.is_group == True): #gets groups
            chatheader = "<h2>Group name: "+str(dialog.name)+"</h2><p>GroupID: "+str(dialog.id)+"</p>\n"
            f.write(chatheader)
            usercount=0
            f.write("<table><tr><td><b>ID</b></td><td><b>Phone</b></td><td><b>First Name</b></td><td><b>Last Name</b></td><td><b>Username</b></td></tr>\n")
            for user in await client.get_participants(dialog):	#gets list of users in chat
                usercount = usercount+1
                userentry = "<td>"+str(user.id)+"</td><td>"+str(user.phone)+"</td><td>"+str(user.first_name)+"<td>"+str(user.last_name)+"</td><td>"+str(user.username)+"</td></tr>\n"
                f.write(userentry)
            f.write("</table>\n")
            f.write("<b>members: "+ str(usercount) +"</b>\n")

with client:
    client.loop.run_until_complete(main())

f.write("</body></html>");

f.close()
