import Website
import Tries

citylink = ['https://postandparcel.info/73872/news/big-can-be-beautiful-carriers-learn-lessons-from-city-link-collapse/',
            'http://autoworld.com.my/news/2020/09/25/city-link-express-takes-delivery-of-277-new-isuzu-trucks/',
            'https://www.thestar.com.my/business/business-news/2015/01/05/citylink-mulls-main-market-listing-in-three-years']

poslaju = ['https://www.theborneopost.com/2020/07/08/poslaju-customers-urged-to-bear-with-longer-waiting-time/',
            'https://www.prnewswire.com/news-releases/pos-laju-recognized-by-frost--sullivan-for-dominating-the-delivery-service-market-in-malaysia-on-the-strength-of-its-vast-channel-network-301194852.html',
            'https://soyacincau.com/2020/06/23/pos-malaysia-is-asking-customers-for-their-patience-due-to-unexpected-delays/']

gdex = ['https://www.thestar.com.my/business/business-news/2020/05/30/brisk-business-for-gdex',
        'https://www.theedgemarkets.com/article/surviving-impact-covid19-unexpected-catalyst-logistics-competition-heating',
        'https://www.thestar.com.my/business/business-news/2021/05/01/surge-in-demand-for-logistics-e-commerce']

jt = ['https://www.malaymail.com/news/malaysia/2021/02/07/courier-company-jt-express-explains-staffs-violent-handling-of-parcels-caug/1947791',
        'https://juiceonline.com/jt-apologises-for-violent-sorting-of-packages-incident-says-it-was-a-misunderstanding-about-pro-rated-bonuses/',
        'https://www.thestar.com.my/aseanplus/aseanplus-news/2021/04/02/indonesias-jt-express-weighing-us1bil-plus-ipo']

dhl = ['https://postandparcel.info/137533/news/e-commerce/dhl-express-we-strongly-believe-that-the-future-of-last-mile-logistics-is-electric/',
        'https://www.theceomagazine.com/executive-interviews/transportation-logistics/christopher-ong/',
        'https://www.taiwannews.com.tw/en/news/4050136']


def calcRatio(arr):  # positive ratio out of 5(put array)
    total = 0
    posiNum = 0
    negNum = 0
    for i in range(len(arr)):
        posiNum += len(arr[i].positive)
        negNum += len(arr[i].negative)

    total = posiNum + negNum

    star = posiNum * 1.0 / total * 5
    return star


if __name__ == '__main__':
    print("CITYLINK")
    CityLink = []
    for i in range(len(citylink)):
        CityLink.append(Website.Website(citylink[i]))
        CityLink[i].read()
        CityLink[i].PosiNeg()
        CityLink[i].Print()

    print("POSLAJU")
    Poslaju = []
    for i in range(len(poslaju)):
        Poslaju.append(Website.Website(poslaju[i]))
        Poslaju[i].read()
        Poslaju[i].PosiNeg()
        Poslaju[i].Print()

    print("GDEX")
    GDEX = []
    for i in range(len(poslaju)):
        GDEX.append(Website.Website(gdex[i]))
        GDEX[i].read()
        GDEX[i].PosiNeg()
        GDEX[i].Print()

    print("J&T")
    JT = []
    for i in range(len(poslaju)):
        JT.append(Website.Website(jt[i]))
        JT[i].read()
        JT[i].PosiNeg()
        JT[i].Print()

    print("DHL")
    DHL = []
    for i in range(len(poslaju)):
        DHL.append(Website.Website(dhl[i]))
        DHL[i].read()
        DHL[i].PosiNeg()
        DHL[i].Print()
    print(calcRatio(DHL), "star")





