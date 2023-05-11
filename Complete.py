import pandas as pd
import numpy as np
from sklearn import linear_model

#py pip install -U scikit-learn

df = pd.read_csv('https://raw.githubusercontent.com/0Domlightning0/MachineLearningOffical/main/No_missing_OSSLT.csv')
df



#Removing All NaN Values within the CSV with the median value 


df.PercentageofGrade3StudentsAchievingtheProvincialStandardinReading.median()

df.PercentageofGrade3StudentsAchievingtheProvincialStandardinReading = df.PercentageofGrade3StudentsAchievingtheProvincialStandardinReading.fillna(df.PercentageofGrade3StudentsAchievingtheProvincialStandardinReading.median())
df


df.Longitude.median()

df.Longitude = df.Longitude.fillna(df.Longitude.median())
df

df.PercentageofStudentsWhoseFirstLanguageIsNotEnglish.median()

df.PercentageofStudentsWhoseFirstLanguageIsNotEnglish = df.PercentageofStudentsWhoseFirstLanguageIsNotEnglish.fillna(df.PercentageofStudentsWhoseFirstLanguageIsNotEnglish.median())
df

df.PercentageofStudentsWhoseFirstLanguageIsNotFrench.median()
df.PercentageofStudentsWhoseFirstLanguageIsNotFrench = df.PercentageofStudentsWhoseFirstLanguageIsNotFrench.fillna(df.PercentageofStudentsWhoseFirstLanguageIsNotFrench.median())
df

df.PercentageofStudentsWhoAreNewtoCanadafromaNonEnglishSpeakingCountry.median()
df.PercentageofStudentsWhoAreNewtoCanadafromaNonEnglishSpeakingCountry = df.PercentageofStudentsWhoAreNewtoCanadafromaNonEnglishSpeakingCountry.fillna(df.PercentageofStudentsWhoAreNewtoCanadafromaNonEnglishSpeakingCountry.median())
df

df.PercentageofStudentsWhoAreNewtoCanadafromaNonFrenchSpeakingCountry.median()
df.PercentageofStudentsWhoAreNewtoCanadafromaNonFrenchSpeakingCountry = df.PercentageofStudentsWhoAreNewtoCanadafromaNonFrenchSpeakingCountry.fillna(df.PercentageofStudentsWhoAreNewtoCanadafromaNonFrenchSpeakingCountry.median())
df

df.PercentageofStudentsReceivingSpecialEducationServices.median()
df.PercentageofStudentsReceivingSpecialEducationServices = df.PercentageofStudentsReceivingSpecialEducationServices.fillna(df.PercentageofStudentsReceivingSpecialEducationServices.median())
df

df.PercentageofStudentsIdentifiedasGifted.median()
df.PercentageofStudentsIdentifiedasGifted	 = df.PercentageofStudentsIdentifiedasGifted	.fillna(df.PercentageofStudentsIdentifiedasGifted	.median())
df

df.ChangeinGrade3ReadingAchievementOverThreeYears.median()
df.ChangeinGrade3ReadingAchievementOverThreeYears = df.ChangeinGrade3ReadingAchievementOverThreeYears.fillna(df.ChangeinGrade3ReadingAchievementOverThreeYears.median())
df

df.PercentageofGrade3StudentsAchievingtheProvincialStandardinWriting.median()
df.PercentageofGrade3StudentsAchievingtheProvincialStandardinWriting = df.PercentageofGrade3StudentsAchievingtheProvincialStandardinWriting.fillna(df.PercentageofGrade3StudentsAchievingtheProvincialStandardinWriting.median())
df


reg = linear_model.LinearRegression()
reg.fit(df[['Enrolment',"Latitude","Longitude","PercentageofStudentsWhoseFirstLanguageIsNotEnglish","PercentageofStudentsWhoseFirstLanguageIsNotFrench","PercentageofStudentsWhoAreNewtoCanadafromaNonEnglishSpeakingCountry","PercentageofStudentsWhoAreNewtoCanadafromaNonFrenchSpeakingCountry","PercentageofStudentsReceivingSpecialEducationServices","PercentageofStudentsIdentifiedasGifted","ChangeinGrade3ReadingAchievementOverThreeYears","PercentageofGrade3StudentsAchievingtheProvincialStandardinWriting","ChangeinGrade3WritingAchievementOverThreeYears","PercentageofGrade3StudentsAchievingtheProvincialStandardinMathematics","ChangeinGrade3MathematicsAchievementOverThreeYears","PercentageofGrade6StudentsAchievingtheProvincialStandardinReading","ChangeinGrade6ReadingAchievementOverThreeYears","PercentageofGrade6StudentsAchievingtheProvincialStandardinWriting","ChangeinGrade6WritingAchievementOverThreeYears","PercentageofGrade6StudentsAchievingtheProvincialStandardinMathematics","ChangeinGrade6MathematicsAchievementOverThreeYears"]].values, df.PercentageofGrade3StudentsAchievingtheProvincialStandardinReading)


res= [255, 46.56732, -84.3528, 0, 100, 0.1, 0.2, 10, 0.3, 73, 23, 62, -19, 54, 23.1, 78, 13, 84, 19, 47, 9]

Enrolment_Input = int(res[0])

Latitude_Input = int(res[1])

LongitudeInput = int(res[2])

PercentageofStudentsWhoseFirstLanguageIsNotEnglishInput = int(res[3])

PercentageofStudentsWhoseFirstLanguageIsNotFrenchInput = int(res[4])

PercentageofStudentsWhoAreNewtoCanadafromaNonEnglishSpeakingCountryInput = int(res[5])

PercentageofStudentsWhoAreNewtoCanadafromaNonFrenchSpeakingCountryInput = int(res[6])

PercentageofStudentsReceivingSpecialEducationServicesInput = int(res[7])

PercentageofStudentsIdentifiedasGiftedInput = int(res[8])

ChangeinGrade3ReadingAchievementOverThreeYearsInput = int(res[10])

PercentageofGrade3StudentsAchievingtheProvincialStandardinWritingInput = int(res[11])

ChangeinGrade3WritingAchievementOverThreeYearsInput = int(res[12])

PercentageofGrade3StudentsAchievingtheProvincialStandardinMathematicsInput = int(res[13])

ChangeinGrade3MathematicsAchievementOverThreeYearsInput = int(res[14])

PercentageofGrade6StudentsAchievingtheProvincialStandardinReadingInput = int(res[15])

ChangeinGrade6ReadingAchievementOverThreeYearsInput = int(res[16])

PercentageofGrade6StudentsAchievingtheProvincialStandardinWritingInput = int(res[17])

ChangeinGrade6WritingAchievementOverThreeYearsInput = int(res[18])

PercentageofGrade6StudentsAchievingtheProvincialStandardinMathematicsInput = int(res[19])

ChangeinGrade6MathematicsAchievementOverThreeYearsInput = int(res[20])

print(reg.intercept_)
print()
print( reg.coef_[0] * Enrolment_Input)
print( reg.coef_[1] * Latitude_Input)
print( LongitudeInput * reg.coef_[2])
print( PercentageofStudentsWhoseFirstLanguageIsNotEnglishInput * reg.coef_[3])
print(PercentageofStudentsWhoseFirstLanguageIsNotFrenchInput * reg.coef_[4])
print(PercentageofStudentsWhoAreNewtoCanadafromaNonEnglishSpeakingCountryInput + reg.coef_[5] )
print(PercentageofStudentsWhoAreNewtoCanadafromaNonFrenchSpeakingCountryInput * reg.coef_[6])
print(PercentageofStudentsReceivingSpecialEducationServicesInput * reg.coef_[7])
print(PercentageofStudentsIdentifiedasGiftedInput * reg.coef_[8] )
print(ChangeinGrade3ReadingAchievementOverThreeYearsInput * reg.coef_[9])
print(PercentageofGrade3StudentsAchievingtheProvincialStandardinWritingInput * reg.coef_[10])
print(ChangeinGrade3WritingAchievementOverThreeYearsInput * reg.coef_[11])
print(PercentageofGrade3StudentsAchievingtheProvincialStandardinMathematicsInput * reg.coef_[12])
print(ChangeinGrade3MathematicsAchievementOverThreeYearsInput * reg.coef_[13])
print(PercentageofGrade6StudentsAchievingtheProvincialStandardinReadingInput * reg.coef_[14])
print(ChangeinGrade6ReadingAchievementOverThreeYearsInput * reg.coef_[15])
print(PercentageofGrade6StudentsAchievingtheProvincialStandardinWritingInput * reg.coef_[16])
print(ChangeinGrade6WritingAchievementOverThreeYearsInput * reg.coef_[17])
print(PercentageofGrade6StudentsAchievingtheProvincialStandardinMathematicsInput * reg.coef_[18])
print(ChangeinGrade6MathematicsAchievementOverThreeYearsInput * reg.coef_[19])






print(reg.predict([ [255, 46.56732, -84.3528, 0, 100, 0.1, 0.2, 10, 0.3, 23, 62, -19, 54, 23.1, 78, 13, 84, 19, 47, 9] ]))

print(reg.intercept_ + reg.coef_[0] * Enrolment_Input + reg.coef_[1] * Latitude_Input + LongitudeInput * reg.coef_[2] + PercentageofStudentsWhoseFirstLanguageIsNotEnglishInput * reg.coef_[3] + PercentageofStudentsWhoseFirstLanguageIsNotFrenchInput * reg.coef_[4] + PercentageofStudentsWhoAreNewtoCanadafromaNonEnglishSpeakingCountryInput + reg.coef_[5] + PercentageofStudentsWhoAreNewtoCanadafromaNonFrenchSpeakingCountryInput * reg.coef_[6] + PercentageofStudentsReceivingSpecialEducationServicesInput * reg.coef_[7] + PercentageofStudentsIdentifiedasGiftedInput * reg.coef_[8] + ChangeinGrade3ReadingAchievementOverThreeYearsInput * reg.coef_[9] + PercentageofGrade3StudentsAchievingtheProvincialStandardinWritingInput * reg.coef_[10] + ChangeinGrade3WritingAchievementOverThreeYearsInput * reg.coef_[11] + PercentageofGrade3StudentsAchievingtheProvincialStandardinMathematicsInput * reg.coef_[12] + ChangeinGrade3MathematicsAchievementOverThreeYearsInput * reg.coef_[13] + PercentageofGrade6StudentsAchievingtheProvincialStandardinReadingInput * reg.coef_[14] + ChangeinGrade6ReadingAchievementOverThreeYearsInput * reg.coef_[15] + PercentageofGrade6StudentsAchievingtheProvincialStandardinWritingInput * reg.coef_[16] + ChangeinGrade6WritingAchievementOverThreeYearsInput * reg.coef_[17] + PercentageofGrade6StudentsAchievingtheProvincialStandardinMathematicsInput * reg.coef_[18] + ChangeinGrade6MathematicsAchievementOverThreeYearsInput * reg.coef_[19])

print("Actual answer:")

print(res[9])

