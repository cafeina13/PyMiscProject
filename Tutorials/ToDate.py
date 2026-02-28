import os
import time as t


pitonOlmayan = os.getcwd()
mrPiton = "C:/Users/ZERO/Desktop/Mr.Piton"
os.chdir(mrPiton)
anaKlasor = os.listdir()

for i in anaKlasor:
    if os.path.isdir(i):
        os.chdir(os.path.join(mrPiton,i))
        gezelienKlasor = os.listdir()
        for j in gezelienKlasor:
            degistirmeTarihiTuple = t.localtime(os.stat(j)[8])
            dTarihiSTR = t.strftime("%d %B %Y %A, %H.%M", degistirmeTarihiTuple)
            klasor = os.path.join(mrPiton,dTarihiSTR)
            yeniYol = os.path.join(klasor,j)
            if not os.path.exists(klasor):
                os.mkdir(klasor)
            os.rename(j,yeniYol)
        os.chdir(mrPiton)

        """
        %Y  Year with century as a decimal number.
        %m  Month as a decimal number [01,12].
        %d  Day of the month as a decimal number [01,31].
        %H  Hour (24-hour clock) as a decimal number [00,23].
        %M  Minute as a decimal number [00,59].
        %S  Second as a decimal number [00,61].
        %z  Time zone offset from UTC.
        %a  Locale's abbreviated weekday name.
        %A  Locale's full weekday name.
        %b  Locale's abbreviated month name.
        %B  Locale's full month name.
        %c  Locale's appropriate date and time representation.
        %I  Hour (12-hour clock) as a decimal number [01,12].
        %p  Locale's equivalent of either AM or PM.
        """




os.chdir(pitonOlmayan)