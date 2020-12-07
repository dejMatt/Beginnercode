x = input("How many measures are in the song (double the amount for repeated sections)")
x = int(x)
(y) = input("What is the tempo?")
y = int(y)
z = input("How many beats are in each bar?")
z = int(z)
e = input("How many bars have a rit?")
e = int(e)
x = e + x
a = x*z
b = y/60
c = a/b
d = c/60
c = str(c)
d = str(d)
d = float(d)
m = int(d)
c = float(c)
c = int(c)
m = int(m)
s = m*60
s = c-s
s = float (s)
s = int(s)
print("The total time it takes for this song is", +m,"minutes and",+s, "seconds")
h = input("Would you like to add to this? (Y/N)")
while h == "Y":
    j = input("How many measures are in the song (double the amount for repeated sections)")
    j = int(j)
    k = input("What is the tempo?")
    k = int(k)
    l = input("How many beats are in each bar?")
    l = int(l)
    p = input("How many bars have a rit?")
    p = int(p)
    j = p + j
    o = j*l
    k = k/60
    u = o/k
    t = u/60
    u = str(u)
    t = str(t)
    t = float(t)
    u = float(u)
    c = c + u 
    m = c/60
    m = float(m)
    m = int(m)
    s = m*60
    s = c-s
    s = int(s)
    print("The total time it takes for this song is", +m,"minutes and",+s, "seconds")
    h = input("Would you like to add to this? (Y/N)")
    if h == "N":
        break
print("Thanks and have a good day!")
print("Coded in python by Matt de Jager")