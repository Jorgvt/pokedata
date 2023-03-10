# AUTOGENERATED! DO NOT EDIT! File to edit: ../../Notebooks/00_Webscrapping/00_01_getting_images.ipynb.

# %% auto 0
__all__ = ['download_img']

# %% ../../Notebooks/00_Webscrapping/00_01_getting_images.ipynb 3
import re
import requests
from bs4 import BeautifulSoup

import pandas as pd
from fastcore.foundation import L
from fastcore.xtras import Path
from fastcore.parallel import parallel
from fastprogress.fastprogress import progress_bar

# %% ../../Notebooks/00_Webscrapping/00_01_getting_images.ipynb 18
def download_img(link):
    route = f"{home}/{link}"
    r_ = requests.get(route)
    soup_ = BeautifulSoup(r_.text, "html.parser")
    try:
        img_link = soup_.find("a", attrs={"rel": "lightbox"})["href"]
    except:
        return False
    file_name = img_link.split("/")[-1]
    with open(path_data / file_name, "wb") as f: 
        f.write(requests.get(img_link).content)
    return True
