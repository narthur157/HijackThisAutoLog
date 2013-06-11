from twill.commands import *
import os
import sys

go("http://www.hijackthis.de")
f = open("hijackthis.log")
x=f.read()
formvalue(1, "logfile", x)
submit(6)
f.close()
f = open("hijacklog.html", "w+")
f.write(show())
f.close()
