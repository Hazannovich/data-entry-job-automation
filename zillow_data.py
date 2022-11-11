from bs4 import BeautifulSoup
import requests


class ZillowData:
    def __init__(self):
        url = "https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3Anull%2C%22mapBounds%22%3A%7B%22west%22%3A-122.69219435644531%2C%22east%22%3A-122.17446364355469%2C%22south%22%3A37.703343724016136%2C%22north%22%3A37.847169233586946%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A11%7D"
        headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, "
                                 "like Gecko) Chrome/107.0.0.0 Safari/537.36",
                   "Accepted-Language": "en-US,en;q=0.9"}
        self.soup = BeautifulSoup(requests.get(url=url, headers=headers).text, "html.parser")

    def get_addresses(self):

        addresses_list = []
        data = self.soup.find_all(attrs={"data-test": "property-card-addr"})
        for block in data:
            address = block.get_text()
            addresses_list.append(address)
        return addresses_list

    def get_prices(self):
        data = self.soup.find_all(attrs={"data-test": "property-card-price"})
        prices_list = []
        for block in data:
            price_data = block.get_text().split(' ')
            price = price_data[0].strip('+')
            price = price.strip("/mo")
            prices_list.append(price)
        return prices_list

    def get_links(self):
        data = self.soup.find_all(attrs={"data-test": "property-card-link"})
        links_list = []
        for block in data:
            link = block.get("href")
            if not "https" in link:
                link = f"https://www.zillow.com{link}"
            links_list.append(link)
        return links_list
