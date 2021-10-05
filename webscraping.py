import requests
from bs4 import BeautifulSoup
import pandas
import argparse
import connect

parser = argparse.ArgumentParser()
parser.add_argument("--page_num_max", help="enter the no.of pages" , type=int)
parser.add_argument("--dbname", help="enter the dbanme" , type=str)
args = parser.parse_args()

connect.create_table(args.dbname)

website="https://www.flipkart.com/search?q=flip+flops&sid=osp%2Ccil%2Ce1r&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_4_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_4_na_na_na&as-pos=1&as-type=RECENT&suggestionId=flip+flops%7CMen&page="
page_num_Max = args.page_num_max
scrapped_info_list=[]
for page_num in range(1, page_num_Max):

    req = requests.get(website + str(page_num))
    content = req.content
    soup = BeautifulSoup(content,"html.parser")
    all_slippers=soup.find_all("div",{"class":"_2B099V"})
    for slipper in all_slippers:
        slipper_dict={}
        slipper_dict["name"] = slipper.find("div",{"class":"_2WkVRV"}).text
        slipper_dict["cost"] = slipper.find("div",{"class" : "_30jeq3"}).text
        try:
            slipper_dict["original_price"]=slipper.find("div",{"class" : "_3I9_wc"}).text
        except AttributeError:
            slipper_dict["original_price"]=None
        scrapped_info_list.append(slipper_dict)
        connect.insert_into_table(args.dbname,tuple(slipper_dict.values()))


dataframe=pandas.DataFrame(scrapped_info_list)
dataframe.to_csv("flipkart.csv")
connect.get_the_info(args.dbname)
