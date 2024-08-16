def convert(amt):
    def towords(num):
        words=["","ONE","TWO","THREE","FOUR","FIVE","SIX","SEVEN","EIGHT","NINE","TEN",
               "ELEVEN","TWELVE","THIRTEEN","FOURTEEN","FIFTEEN","SIXTEEN","SEVENTEEN","EIGHTEEN","NINETEEN",
               "TWENTY "]*5
        words[30]="THIRTY "
        words[40]="FORTY "
        words[50]="FIFTY "
        words[60]="SIXTY "
        words[70]="SEVENTY "
        words[80]="EIGHTY "
        words[90]="NINETY "

        num=int(num)
        if(num<=20 or num==30 or num==40 or num==50 or num==60 or num==70 or num==80 or num==90):
            return words[num]
        else:
            return(towords(int(num/10)*10)+words[num%10])
    rupees,paise=amt.split('.')
    rupees=int(rupees)
    tens=rupees%100
    if tens !=0 :
        tens=towords(tens)
    else:
        tens=""

    rupees=int(rupees/100)
    huns=rupees%10
    if huns !=0 :
        huns=towords(huns)+" HUNDRED "
    else:
        huns=""
        
    rupees=int(rupees/10)
    ths=rupees%100
    if ths !=0 :
        ths=towords(ths)+" THOUSAND "
    else:
        ths=""

    rupees=int(rupees/100)
    laks=rupees%100
    if laks !=0 :
        laks=towords(laks)+" LAKHS "
    else:
        laks=""

    rupees=int(rupees/100)
    crs=rupees%100
    if crs !=0 :
        crs=towords(crs)+" CRORES "
    else:
        crs=""

    paise=towords(paise)
    if paise !="" :
        paise+=" PAISE"
    else:
        paise=""

    inwords=crs+laks+ths+huns+tens+" RUPEES "+paise+" ONLY"

    return inwords

    
