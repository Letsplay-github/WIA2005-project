

import obo
import text_scrape
import plotly.graph_objects as go

headline = ["City-Link: CITY-LINK EXPRESS MAINTAINS ITS FAST & RELIABLE SERVICE WITH ISUZU",
            "City-Link: Company sets up collection centres for relief aid",
            "City-Link: Isuzu lorries = City-Link’s preferred choice",
            "Pos Laju: Poslaju customers urged to bear with longer waiting time",
            "Pos Laju: Pos Malaysia Introduces New Contactless System For Pos Laju Deliveries",
            "Pos Laju: Pos Malaysia’s SendParcel to hit record-breaking two million parcels monthly",
            "GDEX: After Indonesia, GD Express spreads wings to Vietnam",
            "GDEX: GDEX seen shielded from yield pressures",
            "GDEX: GDEX tightens collaboration with Yamato",
            "J&T Express: Courier firm apologises for workers’ rage against parcels",
            "J&T Express: J&T Express celebrates another milestone with Foton",
            "J&T Express: One master’s two apprentices: How Indonesia’s J&T Express rose in China on the back of Pinduoduo",
            "DHL: DHL Express delivers first batch of Covid-19 vaccines to Malaysia",
            "DHL: DHL temporarily suspends Chinese import shipments to India",
            "DHL: DHL hires hundreds of customs staff to prepare for no-deal Brexit"]

url = ["https://www.bigwheels.my/city-link-buys-isuzu-trucks/",
        "https://www.theborneopost.com/2015/01/07/company-sets-up-collection-centres-for-relief-aid/",
        "https://www.thesundaily.my/gear-up/isuzu-lorries--city-link-s-preferred-choice-AK729310",
        "https://www.theborneopost.com/2020/07/08/poslaju-customers-urged-to-bear-with-longer-waiting-time/",
        "https://www.lowyat.net/2021/231543/pos-malaysia-introduces-new-contactless-system-for-pos-laju-deliveries/",
        "https://www.thestar.com.my/news/nation/2020/09/08/pos-malaysias-sendparcel-to-hit-record-breaking-two-million-parcels-monthly",
        "https://www.thesundaily.my/business/after-indonesia-gd-express-spreads-wings-to-vietnam-XL1490000",
        "https://www.thesundaily.my/archive/gdex-seen-shielded-yield-pressures-NTARCH468919",
        "https://www.thesundaily.my/archive/1708651-BSARCH351610",
        "https://www.freemalaysiatoday.com/category/nation/2021/02/07/courier-firm-apologises-for-workers-rage-against-parcels/",
        "https://businessmirror.com.ph/2021/05/25/jt-express-celebrates-another-milestone-with-foton/",
        "https://kr-asia.com/one-masters-two-apprentices-how-indonesias-jt-express-rose-in-china-on-the-back-of-pinduoduo",
        "https://www.freightwaves.com/news/dhl-express-to-launch-new-cargo-airline-in-europe",
        "https://www.freemalaysiatoday.com/category/business/2020/07/01/dhl-temporarily-suspends-chinese-import-shipments-to-india/",
        "https://www.freemalaysiatoday.com/category/business/2019/02/12/dhl-hires-hundreds-of-customs-staff-to-prepare-for-no-deal-brexit/"]

article = dict(list(zip(headline, url)))

for x in article :

    title = x

    link = article[x]

    fullwordlist = text_scrape.extractWord(link)

    stopwordlist = obo.listStopwords(fullwordlist, obo.stopwords)
    positivewordlist = obo.listPositivewords(fullwordlist, obo.positivewords)
    negativewordlist = obo.listNegativewords(fullwordlist, obo.negativewords)
    neutralwordlist = obo.listNeutralwords(fullwordlist, obo.stopwords, obo.positivewords, obo.negativewords)

    swdictionary = obo.wordListToFreqDict(stopwordlist)
    pwdictionary = obo.wordListToFreqDict(positivewordlist)
    negwdictionary = obo.wordListToFreqDict(negativewordlist)
    neuwdictionary = obo.wordListToFreqDict(neutralwordlist)

    sortedswdict = obo.sortFreqDict(swdictionary)
    sortedpwdict = obo.sortFreqDict(pwdictionary)
    sortednegwdict = obo.sortFreqDict(negwdictionary)
    sortedneuwdict = obo.sortFreqDict(neuwdictionary)

    # print("Stopwords")
    # for s in sortedswdict: print(str(s))

    # print("Positivewords")
    # for s in sortedpwdict: print(str(s))

    # print("Negativewords")
    # for s in sortednegwdict: print(str(s))

    # print("Neutralwords")
    # for s in sortedneuwdict: print(str(s))

    totalpw = 0
    for key in pwdictionary: totalpw += pwdictionary[key]

    totalnegw = 0
    for key in negwdictionary: totalnegw += negwdictionary[key]

    fig = go.Figure([go.Bar(x=["Positive", "Negative"], y=[totalpw, totalnegw], marker_color=['rgb(87, 171, 255)', 'rgb(255, 87, 87)'])])
    fig.update_layout(title_text= title,
                    title_font_size=30)
    fig.show()