from .importLinks import get_saved_links
from .download import download_reels
from .csv2Lst import LCConvert,CLConvert,clean
def download_saved(username:str,password:str):
    linksCSV='./links.csv'
    videoLib='../videoLib'
    links=get_saved_links(username,password)
    LCConvert(linksCSV,links)
    mlinks=CLConvert(linksCSV)
    download_reels(videoLib,mlinks,0)
    clean(linksCSV)