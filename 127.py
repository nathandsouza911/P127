from bs4 import BeautifulSoup as soup
import pandas as pd
import time

scraped_data=[]

def scrape():
    bright_star_table=soup.find("table",attrs={"class","wikitable"})
    table_body = bright_star_table.find('tbody')
    table_rows = table_body.find_all('tr')
    for row in table_rows:
        table_cols = row.find_all('td')
        temp_list=[]

        for col_data in table_cols:
            data=col_data.text.strip()
            temp_list.append(data)
            scraped_data.append(temp_list)

    stars_data=[]
    for i in range(0,len(scraped_data)):
        star_names=scraped_data[i][1]        
        distance=scraped_data[i][3]        
        mass=scraped_data[i][5]        
        radius=scraped_data[i][6]        
        lum=scraped_data[i][7]        

        required_data=[star_names,distance,mass,radius,lum]
        stars_data.append(required_data)

    headers=['star_names','distance','mass','radius','lum']
    star_df_1= pd.DataFrame(stars_data,columns=headers)
    star_df_1.to_csv('scrapped_data.csv',index=True,index_label="id")