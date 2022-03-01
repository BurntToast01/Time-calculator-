def add_time(x, y, ):
    nums_OFx = ""
    nums_H = ""
    nums_M = ""
    nums_OFy = ""
    nums_OFy_H = ""
    nums_OFy_M = ""
    final_time = ""
    counter = 0
    timeOfday_counter = 0
    f = ""

    for i in x:
        if i.isdigit ():
            nums_OFx += i
    if len (nums_OFx) == 4:
        nums_H = nums_OFx[0:2]
        nums_M = nums_OFx[2::]
    else:
        if len (nums_OFx) == 3:
            nums_H = nums_OFx[0:1]
            nums_M = nums_OFx[1::]

    for n in y:
        if n.isdigit ():
            nums_OFy += n
    if len (nums_OFy) == 5:
        nums_OFy_H = nums_OFy[0:3]
        nums_OFy_M = nums_OFy[3::]
    if len (nums_OFy) == 4:
        nums_OFy_H = nums_OFy[0:2]
        nums_OFy_M = nums_OFy[2::]
    else:
        if len (nums_OFy) == 3:
            nums_OFy_H = nums_OFy[0:1]
            nums_OFy_M = nums_OFy[1::]

    a = int (nums_H) + int (nums_OFy_H)
    b = int (nums_OFy_M) + int (nums_M)
    c = a % 12
    d = b % 60
    e = c % 24
    counter += e
    # print(b)
    if b >= 60:
        a += 1
        c += 1
    if d < 10:
        d = str ("0") + str (d)
    # d = a % 12
    if "AM" in x:
        if a >= 12:
            f = "AM"
            final_time = (str (a) + ":" + str (d) + str (f))
            if a >= 13:
                f = "PM"
                final_time = (str (c) + ":" + str (d) + str (f))

    if "PM" in x:
        if a >= 12:

            if a >= 13:
                f = "AM"
                final_time = (str (c) + ":" + str (d) + str (f))
            f = "AM"
            final_time = (str (c) + ":" + str (d) + str (f))
        else:
            f = "PM"
            final_time = (str (c) + ":" + str (d) + str (f))

    print (final_time)


add_time ("3:00 PM", "3:10")
# Returns: 6:10 PM

add_time ("11:43 AM", "00:20")
# Returns: 12:03 PM

add_time ("10:10 PM", "3:30")
# Returns: 1:40 AM (next day)


add_time ("6:30 PM", "205:12")
# Returns: 7:42 AM (9 days later)

add_time ("11:50AM", "2:10")
add_time ("11:50AM", "21:00")

