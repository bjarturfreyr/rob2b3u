import yagmail
import socket
dangerdroneIP = [(s.connect(('8.8.8.8', 53)), s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1]

yag = yagmail.SMTP("bjarturogpalmiverkefni@gmail.com","danger123")
yag.send("bjarturogpalmiverkefni@gmail.com",dangerdroneIP," ")
print("IP mail sent.")
