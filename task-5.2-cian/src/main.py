from bs4 import BeautifulSoup
import httpx
import asyncio
from data import FlatData
import json

content = None
headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36"
}

async def download_page(client: httpx.AsyncClient, url: str, data:list):
    response = await client.get(url, headers=headers)
    if response.status_code == 200:
        data.append(response.text)
    else:
        print(f"Ошибка получения страницы: {response.status_code}")
    return content

async def download_pages(links, data):
    """
    Asynchronously downloads a specified number of images to a given directory.
    
    Args:
    - num_images: Number of images to download.
    - output_dir: Directory to save the downloaded images.
    """
    async with httpx.AsyncClient() as session:
        tasks = [
            download_page(session, link, data)
            for link in links
        ]
        await asyncio.gather(*tasks)

def get_flat_info(soup: BeautifulSoup):
    offer_summary_info_group = soup.find('div', {'data-name': 'OfferSummaryInfoGroup'})
    apartment_info = {}
    items = offer_summary_info_group.find_all('div', {'data-name': 'OfferSummaryInfoItem'})
    for item in items:
        key = item.find('p', class_='a10a3f92e9--color_gray60_100--mYFjS').text.strip()
        value = item.find('p', class_='a10a3f92e9--color_black_100--Ephi7').text.strip()
        apartment_info[key] = value

    return apartment_info

def get_building_info(soup: BeautifulSoup):
    house_info_group = soup.find('div', {'class': 'a10a3f92e9--group--K5ZqN', 'class': 'a10a3f92e9--right--_9uBM'})
    house_info = {}
    items = house_info_group.find_all('div', {'data-name': 'OfferSummaryInfoItem'})
    for item in items:
        key_element = item.find('p', class_='a10a3f92e9--color_gray60_100--mYFjS')
        value_element = item.find('p', class_='a10a3f92e9--color_black_100--Ephi7')
        if key_element and value_element:
            key = key_element.text.strip()
            value = value_element.text.strip()
            house_info[key] = value
    
    return house_info

def get_goods(soup: BeautifulSoup):
    features_layout = soup.find('div', {'data-name': 'FeaturesLayout'})
    amenities_list = []
    items = features_layout.find_all('div', {'data-name': 'FeaturesItem'})
    for item in items:
        amenity = item.text.strip()
        amenities_list.append(amenity)

    return(amenities_list)

async def main():
    url = "https://www.cian.ru/cat.php?deal_type=rent&engine_version=2&offer_type=flat&p=2&region=1&room1=1&room2=1&room3=1&room4=1&room5=1&room6=1&room7=1&room9=1&type=4"
    async def fetch_page(url):
        global content
        async with httpx.AsyncClient() as client:
            response = await client.get(url, headers=headers)
            if response.status_code == 200:
                content = response.text
            else:
                print(f"Ошибка получения страницы: {response.status_code}")
    
    soup = BeautifulSoup(content, 'html')
    links = soup.find_all(class_= '_93444fe79c--link--eoxce')
    links = list(set([link['href'] for link in links]))
    asyncio.run(fetch_page(url))
    
    data = []
    for pair in zip(links[::2], links[1::2]):
        await download_pages(pair, data)
        await asyncio.sleep(3)
        
    ready_data = []
    for link, d in zip(links[:9], data[:9]):
        soup = BeautifulSoup(d, 'html.parser')
        title = soup.find('h1', class_='a10a3f92e9--title--vlZwT').text
        price = soup.find('div', class_='a10a3f92e9--amount--ON6i1').find('span').text
        attributes = {}
        fact_items = soup.find_all('div', class_='a10a3f92e9--item--iWTsg')
        for item in fact_items:
            attribute_span = item.find('span', class_='a10a3f92e9--color_black_100--Ephi7')
            if attribute_span:
                attribute = attribute_span.text.strip()
                value_span = attribute_span.find_next_sibling('span')
                if value_span:
                    value = value_span.text.strip()
                else:
                    value = ''
                attributes[attribute] = value
        description = soup.find('div', class_='a10a3f92e9--layout--BaqYw').text.strip()
        flat_ifno = get_flat_info(soup)
        building_info = get_building_info(soup)
        goods = get_goods(soup)
        ready_data.append(FlatData(link=link, name=title, price=price, description=description, other_description=attributes, about_flat=flat_ifno, about_building=building_info, goods=goods))
    
    json_data = [flat.dict() for flat in ready_data]
    # Записываем JSON на диск
    with open('flats_data.json', 'w', encoding="utf-8") as json_file:
        json.dump(json_data, json_file, indent=4, ensure_ascii=False)
    print("Data has been written to flats_data.json")

if __name__ == "__main__":
    asyncio.run(main())