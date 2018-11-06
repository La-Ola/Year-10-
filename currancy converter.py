#Currancy Converter

GBP = int(input("How many GreatBritishPounds do you wish to convert?"))
er = int(input("Convertion to 1)UnitedStatesDollar 2)Euro 3)AustrallianDollar 4)CanadianDollar 5)SwissFranc 6)HongKongDollar 7)JapaneseYen 8)MexicanPeso 9)IndianRupee 10)NewZealandDollar"))

if er == 1:
    USD = 1.6117 * GBP
    if GBP < 500:
        USD = USD / 100 * 5
    elif GBP > 500:
        USD = USD / 100 * 3
    print ("Your money has been exchanged to $", (round(USD,2)) ,", with the service charge subtracted.")
elif er == 2:
    E = 1.2216 * GBP
    if GBP < 500:
        E = E / 100 * 5
    elif GBP > 500:
        E = E / 100 * 3
    print ("Your money has been exchanged to €", (round(E,2)) ,", with the service charge subtracted.")
elif er == 3:
    AD = 1.5578 * GBP
    if GBP < 500:
        AD = AD / 100 * 5
    elif GBP > 500:
        AD = AD / 100 * 3
    print ("Your money has been exchanged to $", (round(AD,2)) ,", with the service charge subtracted.")
elif er == 4:
    CD = 1.5985 * GBP
    if GBP < 500:
        CD = CD / 100 * 5
    elif GBP > 500:
        CD = CD / 100 * 3
    print ("Your money has been exchanged to $", (round(CD,2)) ,", with the service charge subtracted.")
elif er == 5:
    SF = 1.4681 * GBP
    if GBP < 500:
        SF = SF / 100 * 5
    elif GBP > 500:
        SF = SF / 100 * 3
    print ("Your money has been exchanged to ", (round(SF,2)) ,"Fr, with the service charge subtracted.")
elif er == 6:
    HKD = 1.2501 * GBP
    if GBP < 500:
        HKD = HKD / 100 * 5
    elif GBP > 500:
        HKD = HKD / 100 * 3
    print ("Your money has been exchanged to $", (round(HKD,2)) ,", with the service charge subtracted.")
elif er == 7:
    JY = 1.3173 * GBP
    if GBP < 500:
        JY = JY / 100 * 5
    elif GBP > 500:
        JY = JY / 100 * 3
    print ("Your money has been exchanged to ", (round(JY,2)) ,"Yen, with the service charge subtracted.")
elif er == 8:
    MP = 2.1207 * GBP
    if GBP < 500:
        MP = MP / 100 * 5
    elif GBP > 500:
        MP = MP / 100 * 3
    print ("Your money has been exchanged to $", (round(MP,2)) ,", with the service charge subtracted.")
elif er == 9:
    IR = 8.3961 * GBP
    if GBP < 500:
        IR = IR / 100 * 5
    elif GBP > 500:
        IR = IR / 100 * 3
    print ("Your money has been exchanged to ", (round(IR,2)) ,"Rupees, with the service charge subtracted.")
elif er == 10:
    NZD = 1.6117 * GBP
    if GBP < 500:
        NZD = NZD / 100 * 5
    elif GBP > 500:
        NZD = NZD / 100 * 3
    print ("Your money has been exchanged to $", (round(NZD,2)) ,", with the service charge subtracted.")