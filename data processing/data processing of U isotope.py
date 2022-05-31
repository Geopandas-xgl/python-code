
import pandas as pd
import math 
df = pd.read_excel("C:\\Users\\19328\\Desktop\\南海U同位素文章\\NK-1 data_python.xlsx",
                     sheet_name = "NK-1", header = 0, index_col= 0)
df["beta"] = df[["233U","236U"]].apply(lambda x:math.log((x["233U"]/x["236U"])/1.01882)/
                                       math.log(233.0396352/236.045568), axis=1)

m238 = 238.0507882
m236 = 236.045568
m235 = 235.0439299
m234 = 234.0409521
m233 = 233.0396352

r86 = 0.00023481
r56 = 0.00004548
r46 = 0.00036606
r85 = r86/r56

df["238U/236U True"] = df[["238U","236U","beta"]].apply(lambda x:((x["238U"]/x["236U"])-
                                r86*(m238/m236)**x["beta"])/(m238/m236)**x["beta"],axis=1)
df["235U/236U True"] = df[["235U","236U","beta"]].apply(lambda x:((x["235U"]/x["236U"])-
                                r56*(m235/m236)**x["beta"])/(m235/m236)**x["beta"],axis=1)
df["234U/236U True"] = df[["234U","236U","beta"]].apply(lambda x:((x["234U"]/x["236U"])-
                                r46*(m234/m236)**x["beta"])/(m234/m236)**x["beta"],axis=1)
df["238U/235U True"] = df[["238U/236U True","235U/236U True"]].apply(lambda x:x["238U/236U True"]/x["235U/236U True"], axis=1)
df["234U/238U True"] = df[["238U/236U True","234U/236U True"]].apply(lambda x:x["234U/236U True"]/x["238U/236U True"], axis=1)

''''df["p"] = df[["238U","235U","238U/235U True","beta"]].apply(lambda x:((x["238U"]/x["235U"])/(m238/m235)**x["beta"]-x["238U/235U True"])/(r86/r56-x["238U/235U True"]), axis=1)'''

with pd.ExcelWriter("C:\\Users\\19328\\Desktop\\南海U同位素文章\\NK-1 data_python.xlsx", mode ="a", engine = "openpyxl") as writer:
    df.to_excel(writer, sheet_name="NK-1_1" )



