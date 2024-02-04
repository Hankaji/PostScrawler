# from WebScrapers import *
from WebScrapers import *
from globals import fileName
import sys


# everything start here
def webscrape(targetNumWeek=1):
    # reset
    with open(fileName, 'w') as file:
        file.flush()

    print(f'scraping weeks: {targetNumWeek}')

    # academy_binance.scrapeAcademyBinance(targetNumWeek)
    # chain_link.scrapeChainlink(targetNumWeek)
    # open_ai.scrapeOpenAI(targetNumWeek)
    # google_blog_ai.scrapeGoogleBlogAI(targetNumWeek)
    # developer_archives.scrapeDevelopersArchives(targetNumWeek)
    # alchemy_blog.scrapeAlchemyBlog(targetNumWeek)
    # decrypt.scrapeDecrypt(targetNumWeek)
    # cointelegraph.scrapeCointelegraph(targetNumWeek)
    # coin_desk.scrapeCoinDesk(targetNumWeek)
    # hak_research.scrapeHakResearch1(targetNumWeek)
    # ibm.scrapeIBM(targetNumWeek)
    # vng.scrapeVNG(targetNumWeek)
    # hugging_face.scrapeHuggingFace(targetNumWeek)
    # zkblab.scrapeZkblab(targetNumWeek)
    # google_lab.scrapeGoogleLab(targetNumWeek)
    # apple.scrapeApple(targetNumWeek)
    # forte_lab.scrapeForteLab(targetNumWeek)
    # ali_abdaal.scrapeAliAbdaal(targetNumWeek)
    # gfi.scrapeGfi(targetNumWeek)
    # bankless.scrapeBankless(targetNumWeek)
    # coin98.scrapeCoin98(targetNumWeek)
    # vitalik.scrapeVitalik(targetNumWeek)
    # hak_research.scrapeHakResearch(targetNumWeek)
    # hak_research.scrapeHakResearch1(targetNumWeek)
    
    # webflow.scrapeWebflow(targetNumWeek)
    # hackerrank.scrapeHackerrank(targetNumWeek)
    # atlassian.scrapeAtlassian(targetNumWeek)
    # cognizant.scrapeCognizant(targetNumWeek)
    # yc.scrapeYC(targetNumWeek)
    # accenture.scrapeAccenture(targetNumWeek)
    
    # mygreatlearning.scrapeMygreatlearning(targetNumWeek)
    # kdnugget.scrapeKdnugget(targetNumWeek)
    # analytic_vidhya.scrapeAnalytic_Vidhya(targetNumWeek)
    # hubspot.scrapeHubspot(targetNumWeek)
    
    theBlock1.startScrape(targetNumWeek)
    blockWork.startScrape(targetNumWeek)
    print('** Done **')


# start scraping
if __name__ == '__main__':
    inputWeek = 1

    if (len(sys.argv) > 1):
        inputWeek = int(sys.argv[1])

    webscrape(inputWeek)
