import requests
from bs4 import BeautifulSoup


def parser_recipe_card_name(url_data):
    recipes = []

    response = requests.get(url_data)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        recipe_cards_preview = soup.find_all('div', class_='title')
        for _ in recipe_cards_preview:
            recipe_title = soup.find('span', itemprop='name').text.split()
            recipes.append(recipe_title)
    else:
        print(f"Ошибка кода ответа страница не доступна")

    return recipe_title


def parse_recipe_all_pagination(base_url):
    all_recipe_title = []
    curent_page = 1
    while True:
        url_data_get = f"{base_url}&page={curent_page}"
        page_recipes = parser_recipe_card_name(url_data_get)
        if not page_recipes:
            break
        all_recipe_title.extend(page_recipes)
        curent_page += 1

    return all_recipe_title


if __name__ == "__main__":
    url = "https://www.russianfood.com/recipes/bytype/?fid=926"
    all_recipe_theme = parse_recipe_all_pagination(url)

    print(f"Количество рецептов:", len(all_recipe_theme))
    for idx, title in enumerate(all_recipe_theme, start=1):
        print(f"{idx}.{title}")
