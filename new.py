import sys
import xml.etree.ElementTree as ET
import numpy as np
import pandas as pd
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression



def main():
    test("C:\\Users\\aliug\\Desktop\\tcss455\\public-test-data",
         "C:\\Users\\aliug\\Desktop\\tcss455")  # change in vm


def test(file, output):
    fileIn = file  # sys.argv[1]
    dfProfile = pd.read_csv(
        "C:\\Users\\aliug\\Desktop\\tcss455\\training\\profile\\profile.csv")  # "./tcss455/training/profile/profile.csv"
    dfLIWC = pd.read_csv(
        "C:\\Users\\aliug\\Desktop\\tcss455\\training\\LIWC\\LIWC.csv")  # "./tcss455/training/LIWC/LIWC.csv.csv"
    correct_df = dfLIWC.copy()
    correct_df.rename(columns={'userId': 'userid'}, inplace=True)
    df = pd.merge(dfProfile, correct_df, on="userid", how="outer")
    testDfProf = pd.read_csv(fileIn+"\\profile\\profile.csv")
    testDfLIWC = pd.read_csv(fileIn+"\\LIWC\\LIWC.csv")
    correct_testDf = testDfLIWC.copy()
    correct_testDf.rename(columns={'userId': 'userid'}, inplace=True)
    testDf = pd.merge(testDfProf, correct_testDf, on="userid", how="outer")

    feature_cols = df.columns.values.tolist()
    test_cols = testDf.columns.values.tolist()

    X = df[feature_cols[10:]]

    data_predict = df.gender

   # X_train, X_test, y_train, y_test = train_test_split(X, data_predict, test_size=0.2)
    linreg = LinearRegression()
    linreg.fit(X, data_predict)
   # print("\nCoefficients:", list(zip(feature_cols[10:], linreg.coef_)))
    #print("Intercept:", linreg.intercept_)

    y_pred = linreg.predict(testDf[test_cols[10:]])
    print(y_pred)
    pred_gender = []
    for index in y_pred:
        if index >= 0.5:
            pred_gender.append(1)
        else:
            pred_gender.append(0)
    #print("\nMAE:", metrics.mean_absolute_error(y_test, y_pred))
    #print("MSE:", metrics.mean_squared_error(y_test, y_pred))
    #print("RMSE:", np.sqrt(metrics.mean_squared_error(y_test, y_pred)))
    #print(metrics.accuracy_score(y_test,pred_gender))

    out = output


    fileOut = ET.Element("user")


    index = 0
    print(len(pred_gender))

    with open(fileIn+"\\profile\\profile.csv", 'r') as fpIn:
        des = 0
        for line in fpIn:
            if des == 0:
                des+=1
                continue
            token = line.split(",")
            user = token[1]
            if pred_gender[index] == 0:
                maxGen = "male"
                index+=1
            else:
                maxGen = "female"
                index+=1
            fileOut.set("id", user)
            fileOut.set("age_group", "")
            fileOut.set("gender", maxGen)
            fileOut.set("extrovert", "")
            fileOut.set("neurotic", "")
            fileOut.set("agreeable", "")
            fileOut.set("conscientious", "")
            fileOut.set("open", "")
            tree = ET.ElementTree(fileOut)
            f = open(output+"\\"+user+".xml", "wb")
            tree.write(f)


main()
