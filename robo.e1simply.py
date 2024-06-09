# robo.r2
while True:
    hi = input("Hi my name is Robot 😊👋 ")
    if hi !="":
        break

print("")

while True:
    how = input("How are you?😜 ")
    if how !="":
        break
    
    
print("Wow glad to hear 😚")
print("")

while True:
    name = input("Just enter your name🙃: ")
    if name !="":
        break
    
print("Wow nice to meet you " + name )
print("")

while True:
    where = input("Where are you from?😝😙: ")
    if where !="":
        break

print("Wow Nice country 😘" + where)
print("")

print("And im from Erick 😊, he's my Owner!😊, He created me!😊, I LOVE HIM 😘")

while True:
    did = input("did you understand me?👌: ")
    if did !="":
        break

print("good🙃 ")
print("")
while True:
    what = input("What's your favorite color? ")
    if what !="":
        break
print("woow really? great 😚😚😚 ")
print("")

while True:
    what1 = input("and what's your favorite car?? ")
    if what1 !="":
        break
print("well 😊")
print("")

while True:
    lang = input("How many languages can you speak? ")
    if lang !="":
        break
print("Really? ")

while True:
    langu = input("can you tell me which languages? ")
    if langu !="":
        break

print("")
print("Woow you are so smart :)>> " + langu)
print("")

while True:
    bythe = input("Whats your job or profession? ")
    if bythe !="":
        break
print( bythe + "Oh great :) ")
print()

while True:
    prog = input("DO YOU WANT TO KNOW ABOUT PROGRAMMING AND CODING? ")
    if prog !="":
        break
print("Ok wait i will explain you :) ")
input("ready???: ")
print()

print("Computer programming or coding is the composition of sequences of instructions, called programs,that computers can follow to perform tasks.  It involves designing and implementing algorithms,step-by-step specifications of procedures, by writing code in one or more programming languages. Programmers typically use high-level programming languages that are more easily intelligible to humans than machine code, which is directly executed by the central processing unit. Proficient programming usually requires expertise in several different subjects, including knowledge of the application domain, details of programming languages and generic code libraries, specialized algorithms, and formal logic.")
print("")
input("")
print("here's programming and coding information")
input()



while True:
    hackwifi = input("i will hack your wifi network and other networks: ")
    if hackwifi !="":
        break

#Wifi hack

import subprocess

data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8', errors="backslashreplace").split('\n')

profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]

for i in profiles:
    try:
        results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8', errors="backslashreplace").split('\n')
        results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
        try:
            print ("{:<30}|  {:<}".format(i, results[0]))
        except IndexError:
            print ("{:<30}|  {:<}".format(i, ""))
    except subprocess.CalledProcessError:
        print ("{:<30}|  {:<}".format(i, "ENCODING ERROR"))

input("")
print("i hacked your wifi networks you can see your wifi passwords")
print("")
input("soooooo: ")
print("")

while True:
    e = input("I will show you bmw logo if you want?: ")
    if e !="":
        break
print("")
while True:
    f = input("Readyyyyyy?: ")
    if f !="":
        break

#BMW LOGO

import turtle as t

# t.setup(600, 600)

t.setpos(0,-250)
t.pensize(8)
t.fillcolor('black')
t.begin_fill()
t.pencolor('gray')
t.circle(250)
t.end_fill()

t.pensize(3)
t.up()
t.setpos(0,-150)
t.down()
t.fillcolor('white')
t.begin_fill()
t.circle(150)
t.end_fill()

t.fillcolor('deepskyblue')
t.begin_fill()
t.circle(150, 90)
t.left(90)
t.pensize(2)
t.pencolor('black')
t.forward(150)
t.left(90)
t.forward(150)
t.end_fill()
t.up()
t.setpos(-150,0)
t.down()
t.begin_fill()
t.pensize(3)
t.pencolor('gray')
t.circle(150, -90)
t.left(90)
t.pensize(2)
t.pencolor('black')
t.forward(150)
t.right(90)
t.forward(150)
t.end_fill()

# letters:

t.pensize(12)
t.pencolor('white')

# B
t.up()
t.setpos(0,0)
t.right(35)
t.forward(165)
t.right(5.2)
t.down()
t.forward(64)
t.right(90)
t.forward(35)
t.circle(-16,180)
t.forward(35)
t.right(180)
t.forward(35)
t.circle(-16,180)
t.forward(35)

# M
t.up()
t.setpos(-32,165)
t.setheading(90)
t.down()
t.forward(62)
t.setpos(0,180)
t.setpos(32,227)
t.right(180)
t.forward(62)

# W
t.up()
t.setpos(0,0)
t.setheading(52)
t.forward(228)
t.down()
t.right(170)
t.forward(65)
t.left(142)
t.forward(50)
t.right(142)
t.forward(50)
t.left(142)
t.forward(65)

t.hideturtle()
t.done()
input()
print("")
bmw = input("did you see bmw logo?:): ")
print(bmw + "Good")
print("")

while True:
    h = input("first erick's favorite car is BMW;): ")
    if h !="":
        break

while True:
    r = input("Do you you want to get some information about me?: ")
    if r !="":
        break
    
input("Naah you can not get information about me becouse it is so dangerous. we are anonymous. you can know only our names")
print("")

input()


#add here


while True:
    site = input("if you want to get news about US?: ")
    if site !="":
        break
print()
print("Great 🙃")

while True:
    site1 = input("YOU HAVE TO SUBSCRIBE TO MY YOUTUBE CHANNEL😜 ")
    if site1 !="":
        break
    print()
    
while True:
    site2 = input("Search:>> ' RICH_nsm ' on YouTube: ")
    if site2 !="":
        break
input()

print("And my instagram name: ' erick_coder7 '")

while True:
    insata11 = input("you can search on instagram too: ")
    if insata11 !="":
        break
input()







