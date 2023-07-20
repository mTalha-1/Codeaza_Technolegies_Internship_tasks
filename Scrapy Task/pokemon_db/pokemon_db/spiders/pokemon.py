import scrapy
from pathlib import Path
import pandas as pd


class PokemonSpider(scrapy.Spider):
    
    name = "pokemon"
    allowed_domains = ["pokemondb.net"]
    start_urls = ["https://pokemondb.net"]

    def start_requests(self):
        url = 'https://pokemondb.net/pokedex/all'
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        id = []
        name = []
        Icon_link = []
        type_ = []
        total = []
        hp = []
        attack = []
        defence = []
        Sp_atk = []
        Sp_def = []
        speed = []
 
        rows = response.xpath('//*[@id="pokedex"]/tbody/tr')
        for row in rows:

            icon_link = row.css('.cell-num.cell-fixed > span.infocard-cell-img > img')
            Icon_link.append(icon_link.attrib["src"])

            Id = row.css('.cell-num.cell-fixed > span.infocard-cell-data::text').get(default="NA")
            id.append(Id)

            Name = row.css('.cell-name > a::text').get(default="NA")
            name.append(Name)

            Type = row.css('.cell-icon > a.type-icon::text').getall()
            type_.append(Type)

            Total = row.css('.cell-num.cell-total::text').get(default="NA")
            total.append(Total)

            HP = row.css('.cell-num:nth-child(5)::text').get(default="NA")
            hp.append(HP)

            Attack = row.css('.cell-num:nth-child(6)::text').get(default="NA")
            attack.append(Attack)

            Defence = row.css('.cell-num:nth-child(7)::text').get(default="NA")
            defence.append(Defence)

            Sp_Atk = row.css('.cell-num:nth-child(8)::text').get(default="NA")
            Sp_atk.append(Sp_Atk)

            Sp_Def = row.css('.cell-num:nth-child(9)::text').get(default="NA")
            Sp_def.append(Sp_Def)

            Speed = row.css('.cell-num:nth-child(10)::text').get(default="NA")
            speed.append(Speed)

        df = pd.DataFrame ({
            'Id': id,
            'Name': name,
            'Icon_Link': Icon_link, 
            'Type': type_, 
            'Total': total, 
            'HP': hp, 
            'Attack': attack, 
            'Defence': defence, 
            'Sp.Atk': Sp_atk, 
            'Sp.Def': Sp_def, 
            'Speed': speed
        })

        df.to_excel('Pokemon_Database.xlsx',index=False)
            
        
