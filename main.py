import sys
import xml.etree.ElementTree as ET


def main():
    test("C:\\Users\\aliug\\Desktop\\tcss455\\public-test-data\\profile\\profile.csv", "C:\\Users\\aliug\\Desktop\\tcss455") #change in vm


def test(file, output):
    male = 0
    female = 0
    age24 = 0
    age34 = 0
    age49 = 0
    age100 = 0
    highestAge = ""
    op = 0
    con = 0
    ex = 0
    agr = 0
    neu = 0
    fileIn = file  # sys.argv[1]
    training = "C:\\Users\\aliug\\Desktop\\tcss455\\training\\profile\\profile.csv" #"./tcss455/training/profile/profile.csv"
    #output = sys.argv[2]
    fileOut = ET.Element("user")

    with open(training, 'r') as train:
        lineNumber = 0
        for line in train:
            if lineNumber == 0:
                lineNumber += 1
                continue
            token = line.split(',')
            age = float(token[2])
            if age < 25:
                age24 += 1
            elif age < 35:
                age34 += 1
            elif age < 50:
                age49 += 1
            else:
                age100 += 1
            gender = float(token[3])
            if gender == 0:
                male += 1
            else:
                female += 1
            op += float(token[4])
            con += float(token[5])
            ex += float(token[6])
            agr += float(token[7])
            neu += float(token[8])
    with open(fileIn, 'r') as fpIn:
        for line in fpIn:
            token = line.split(",")
            user = token[1]
            maxAge = age24
            highestAge = "XX-24"
            if age34 > maxAge:
                maxAge = age34
                highestAge = "25-34"
            if age49 > maxAge:
                maxAge = age49
                highestAge = "35-49"
            if age100 > maxAge:
                maxAge = age34
                highestAge = "50-XX"
            if male > female:
                maxGen = "male"
            else:
                maxGen = "female"
            fileOut.set("id", user)
            fileOut.set("age_group", highestAge)
            fileOut.set("gender", maxGen)
            fileOut.set("extrovert", str(ex/9500))
            fileOut.set("neurotic", str(neu/9500))
            fileOut.set("agreeable", str(agr/9500))
            fileOut.set("conscientious", str(con/9500))
            fileOut.set("open", str(op/9500))
            tree = ET.ElementTree(fileOut)
            f = open(output+"\\"+user+".xml", "wb")
            tree.write(f)


main()
