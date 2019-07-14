import random
import json
from ibm_watson import VisualRecognitionV3
from math import cos, sin, atan2, sqrt, radians, degrees

global distribution
distribution = []

class CenterPointFromListOfCoordinates:

    def center_geolocation(self, geolocations):
        """
        输入多个经纬度坐标，找出中心点
        :param geolocations: 集合
        :return:
        """
        x = 0
        y = 0
        z = 0
        length = len(geolocations)
        for lon, lat in geolocations:
            lon = radians(float(lon))
            lat = radians(float(lat))
            x += cos(lat) * cos(lon)
            y += cos(lat) * sin(lon)
            z += sin(lat)

        x = float(x / length)
        y = float(y / length)
        z = float(z / length)

        return (degrees(atan2(y, x)), degrees(atan2(z, sqrt(x * x + y * y))))


class person:
    id = 0
    age = 0
    relative = ""
    value = 0
    emo = ""
    time = 0
    x = 0
    y = 0
    pos = ()
    def __init__(self, id):
        self.id = id
        self.age = random.randint(1, 90)
        self.time = random.randint(1, 30)
        if self.id<=30:
            self.x = 30+random.randint(-10, 10)
            self.y = 20+random.randint(-10, 10)
        if self.id>30 and self.x<50:
            self.x = 80 + random.randint(-10, 10)
            self.y = 30 + random.randint(-10, 10)
        if self.id>=50:
            self.x = 60 + random.randint(-10, 10)
            self.y = 70 + random.randint(-10, 10)
        self.pos = (self.x, self.y)





people = []

data = open("C:\\Users\THINKPAD\Desktop\数据\out.txt", "w")
grade_relative = {"父亡":25, "母亡":25, "亡偶":25}
grade_emo = {"烦躁":30, "抑郁":30}
grade_age = {}
id = []
for i in range(0, 35):
    grade_age[i] = 20 - 0.571*i;
grade_age[35] = 0
for i in range(36, 91):
    grade_age[i] = -12.7 + 0.364*i;
relative = {0:"父亡",1:"母亡",2:"亡偶"}
emo = {0:"烦躁", 1:"抑郁", 2:"正常"}
value = {}

n = int(input("受灾人数:"))
m = int(input("志愿者人数："))

for num in range(n):
    data.write("{\n")
    p = person(num)
    p.id = num
    data.write("\t\"id\":\"")
    data.write(str(num))
    data.write("\",")
    data.write("\n\t\"亲属情况\":\"")
    for i in range(random.randint(0,2)):
        for j in range(i):
            x = random.randint(0,2)
            p.relative += relative[x]
            data.write(relative[x])
            p.value += grade_relative[relative[x]]
    data.write("\",")
    data.write("\n\t\"情绪\"：\"")
    emoj = random.randint(0, 2)
    if emoj<2:
        p.value += grade_emo[emo[emoj]]
    p.emo += emo[emoj]
    data.write(emo[emoj]+"\",")

    data.write("\n\t\"年龄\"：\"")
    data.write(str(p.age)+"\",")
    p.value += grade_age[p.age]

    data.write("\n\t\"x\"：\"")
    data.write(str(p.x)+'\",')
    data.write("\n\t\"y\"：\"")
    data.write(str(p.y)+"\",")
    distribution.append(p.pos)

    data.write("\n\t时间\"：\""+ str(p.time) +"\"")
    p.value *= p.time/30
    print(p.value)
    data.write("\n\t\"权值\"：\"")
    data.write(str(p.value) + "\",")
    data.write("\n}\n")

    people.append(p)



for day in range(30):
    day_data = open("C:\\Users\THINKPAD\Desktop\数据\\"+"day"+str(day)+".txt", "w")
    for i in range(n):
        people[i].value *= 30/people[i].time
        if people[i].time>1:
            people[i].time -= 1
            people[i].value *= people[i].time/30
    
        day_data.write("{\n")
        day_data.write("\t\"id\":\"")
        day_data.write(str(people[i].id))
        day_data.write("\",")
        day_data.write("\n\t\"亲属情况\":\"")
        day_data.write(people[i].relative)
        day_data.write("\",")
        day_data.write("\n\t\"情绪\"：\"")
        day_data.write(people[i].emo + "\",")

        day_data.write("\n\t\"年龄\"：\"")
        day_data.write(str(people[i].age) + "\",")

        day_data.write("\n\t\"x\"：\"")
        day_data.write(str(people[i].x) + '\",')
        day_data.write("\n\t\"y\"：\"")
        day_data.write(str(people[i].y) + "\",")

        day_data.write("\n\t时间\"：\"" + str(people[i].time) + "\"")
        day_data.write("\n\t\"权值\"：\"")
        day_data.write(str(people[i].value) + "\",")
        day_data.write("\n}\n")

    draw = []
    for per in people:
        draw.append([per.x, per.y, per.value])
    file = open("C:\\Users\THINKPAD\Desktop\画图\\file" + str(day) + ".txt", "w")
    file.write(str(draw))
    file.close()

    day_data.close()

print(distribution)
center = []
centerObj = CenterPointFromListOfCoordinates()
center.append(centerObj.center_geolocation(distribution[:30]))
center.append(centerObj.center_geolocation(distribution[30:50]))
center.append(centerObj.center_geolocation(distribution[50:]))

for per in center:
    print(per)

data.close()