

import obo
import text_scrape
import plotly.graph_objects as go
import time

# List of article headlines
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

# List of article links
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

# Compile headline and article link in a dictionary as tuple
article = dict(list(zip(headline, url)))

resultFile = open(r"Problem2\result.txt", "w")

for x in article :

    title = x

    link = article[x]

    resultFile.write(title + "\n\n")

# Scrape the article from websites using BeautifulSoup 4 module
    fullwordlist = text_scrape.extractWord(link)

# Filter, remove and create stop word list, positive word list and negative word list from original word list. 
# Remaining words in original word list is considered as neutral words.
    stopwordlist = obo.listStopwords(fullwordlist, obo.stopwords)
    positivewordlist = obo.listPositivewords(fullwordlist, obo.positivewords)
    negativewordlist = obo.listNegativewords(fullwordlist, obo.negativewords)
    neutralwordlist = obo.listNeutralwords(fullwordlist, obo.stopwords, obo.positivewords, obo.negativewords)

# Count and store word frequency for each word list in respective dictionary as (word, frequency) tuple
    swdictionary = obo.wordListToFreqDict(stopwordlist)
    pwdictionary = obo.wordListToFreqDict(positivewordlist)
    negwdictionary = obo.wordListToFreqDict(negativewordlist)
    neuwdictionary = obo.wordListToFreqDict(neutralwordlist)

# Sort dictionary items based on frequency in ascending order
    sortedswdict = obo.sortFreqDict(swdictionary)
    sortedpwdict = obo.sortFreqDict(pwdictionary)
    sortednegwdict = obo.sortFreqDict(negwdictionary)
    sortedneuwdict = obo.sortFreqDict(neuwdictionary)

# Print each dictionary content in result file
    resultFile.write("Stopwords")
    resultFile.write("\n")
    for s in sortedswdict: resultFile.write(str(s) + "\n")
    resultFile.write("\n")

    resultFile.write("Positivewords")
    resultFile.write("\n")
    for s in sortedpwdict: resultFile.write(str(s) + "\n")
    resultFile.write("\n")

    resultFile.write("Negativewords")
    resultFile.write("\n")
    for s in sortednegwdict: resultFile.write(str(s) + "\n")
    resultFile.write("\n")

    resultFile.write("Neutralwords")
    resultFile.write("\n")
    for s in sortedneuwdict: resultFile.write(str(s) + "\n")
    resultFile.write("\n")

# Sum up total positive word in article
    totalpw = 0
    for key in pwdictionary: totalpw += pwdictionary[key]

# Sum up total negative word in article
    totalnegw = 0
    for key in negwdictionary: totalnegw += negwdictionary[key]

    resultFile.write("Positive words:" + str(totalpw) + "\n")
    resultFile.write("Negative words:" + str(totalnegw) + "\n\n")


# Generate histogram to show article sentiment based on total positive word count and total negative word count
    fig = go.Figure([go.Bar(x=["Positive", "Negative"], y=[totalpw, totalnegw], marker_color=['rgb(87, 171, 255)', 'rgb(255, 87, 87)'])])
    fig.update_layout(title_text= title,
                    title_font_size=30)
    fig.show()

    time.sleep(1)