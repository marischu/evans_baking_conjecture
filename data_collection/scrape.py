import csv
import numpy as np
#from selenium_scraper.get_recipes import print_json, FILE_NAME, extract_links_to_file, get_recipe
import yaml
from recipe_scrapers import scrape_me
import re


def load_configurations():
    with open("config.yaml", "r") as file:
        cfg = yaml.safe_load(file)
    return cfg

def extract_links(cfg,site,links_file,verb=True):
    # get links
    raise NotImplementedError

# converts to US if metric
def extract_amounts(item_str):
    raise NotImplementedError
    parts = item_str.split(" ")

def containsNumber(value):
    return any([char.isdigit() for char in value])

def containsLetter(value):
    return any(remove_numbers(value))

def remove_numbers(value):
    return re.sub('[0-9]','', value)

def convert_to_amounts(ingr_dict,cfg):
    units = cfg["units"]

    for ingr_str in ingr_dict:
        parts = ingr_str.split("")
        
        # search for number
        amount = None
        for part in parts:
            if containsNumber(part):
                print(part)

"""
        # search for unit
        unit = None
        for part in parts:
            if part in units:
                unit = part
        if unit == None:
            for part in parts:
                if part.containsNumber(part):
"""


def reduce_ingredients(cfg, ingredients):
    ingr_dict = dict.fromkeys(cfg['ingredients'])

    for search in ingr_dict:
        ingr_dict[search] = None
        for item in ingredients:
            if search in item: 
                if ingr_dict[search] == None:
                    ingr_dict[search] = item
                else:
                    temp = ingr_dict[search]
                    if type(temp) == str: # if a string
                        ingr_dict[search] = [temp,item]
                    else:
                        ingr_dict[search].append(item)
    print(ingr_dict)
    ingr_dict = resolve_duplicates(cfg, ingr_dict)
    
    return ingr_dict

def getUnitsAndValues(item,cfg):
    units = ""
    values = ""
    parts = item.split(" ")
    ret = False
    # check for direct units
    for part in parts:
        if part in cfg["units"]:
            for part in cfg 
    
    # if unit is not space separated
    if ret == False:
        for part in parts:
            if containsNumber(part):
                if "/" in part: # double units or fractions
                    first,second = part.split("/")
                    if containsLetter(first) and containsLetter(second): # double unit
                        print(remove_numbers(first))
                        if remove_numbers(first) in cfg["units"]:
                            ret = True
                            break
                        elif remove_numbers(second) in cfg["units"]:
                            ret = True
                            break
                    #fractional case not considered; units would have to be found elsewhere

def hasUnits(item,cfg):
    parts = item.split(" ")
    ret = False
    # check for direct units
    for part in parts:
        if part in cfg["units"]:
            ret = True
    
    # if unit is not space separated
    if ret == False:
        for part in parts:
            if containsNumber(part):
                if "/" in part: # double units or fractions
                    first,second = part.split("/")
                    if containsLetter(first) and containsLetter(second): # double unit
                        print(remove_numbers(first))
                        if remove_numbers(first) in cfg["units"]:
                            ret = True
                            break
                        elif remove_numbers(second) in cfg["units"]:
                            ret = True
                            break
                    #fractional case not considered; units would have to be found elsewhere
    return ret

def resolve_duplicates(cfg,ingredients):
    for ingr in ingredients:
        if type(ingredients[ingr]) == list:
            new_list = []
            for item in ingredients[ingr]:
                if hasUnits(item,cfg):
                    new_list.append(item)
            ingredients[ingr] = new_list
    
    return ingredients
            


def get_data(cfg, link):
    # scrape link
    scraper = scrape_me(link)

    # get ingredients
    ingredients = scraper.ingredients()

    # get relevant ingredients
    ingredients = reduce_ingredients(cfg,ingredients)

    data = convert_to_amounts(ingredients,cfg)
    
    print(data)


def main (): 
    # load config 
    cfg = load_configurations()
    links = []

    # get all links from sites
    for site in cfg["websites"]:
        site_name = site.split("//")[1].split(".")[-2]
        print(site_name)
        links_file = "./" + site_name + "_links.txt"
        #site = "https://www.bbc.co.uk/food/recipes/aclassicspongecakewi_9406"
        #links.append(extract_links(cfg,site,links_file))

    # walk links to get ingredients
    data = []
    links = ["https://www.bbc.co.uk/food/recipes/aclassicspongecakewi_9406"]
    for link in links:
        data.append(get_data(cfg,link))        

if __name__ == '__main__':
    main()
