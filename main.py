# importing Requests library
import requests

# Defining cookies to mimic a session from a browser
cookies = {
    'CookieConsent': '{stamp:%27FJeiFrD8LSzMCWtIYKMo+wqTdjPH7gJvO8piyb3sr+uNBd7nMR370w==%27%2Cnecessary:true%2Cpreferences:true%2Cstatistics:true%2Cmarketing:true%2Cmethod:%27explicit%27%2Cver:1%2Cutc:1728414287009%2Cregion:%27ro%27}',
    '_gcl_au': '1.1.827619676.1728414285',
    '_hjSession_1254138': 'eyJpZCI6ImI1N2RjZDI0LTNkZTQtNGI5ZC05ZmI5LTA2ODI3ZjRiODE2OSIsImMiOjE3Mjg0MTQyODUyNDEsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjoxLCJzcCI6MH0=',
    '_ga': 'GA1.1.1398011057.1728414285',
    '_tt_enable_cookie': '1',
    '_ttp': '5ua8YUsGpKEfBa-FuH0ZQxzorpQ',
    '_pin_unauth': 'dWlkPVlqUXpZVEpqTVdFdE1XSmlaQzAwT0RGa0xUZ3daRGd0TkRGbFkyVmtOR1l6WVdJNA',
    '_fbp': 'fb.1.1728414285412.210127009951878959',
    'imbox': '{"imboxUid":"2nASG5IA9XxVlDTjuVkASvrtwEJ"}',
    'e_sk': '4b037485-c70d-43dc-ab57-c8cf079839f2',
    '_hjSessionUser_1254138': 'eyJpZCI6IjE2Y2ZiZDdlLTY3MmQtNWM3Ni1hZmRmLTBiM2UwYWRkMDcxZiIsImNyZWF0ZWQiOjE3Mjg0MTQyODUyNDEsImV4aXN0aW5nIjp0cnVlfQ==',
    '_uetsid': '2e86254085a811efb214b55d16e81443',
    '_uetvid': '2e86458085a811ef99e89919e2352624',
    '_ga_CT371S5MF9': 'GS1.1.1728417033.2.1.1728419296.60.0.0',
}

# Headers used to make the requests appear as if they are coming from a browser (for products from a category)
headersProducts = {
    'accept': 'application/json',
    'accept-language': 'en-US,en;q=0.9',
    # 'cookie': 'CookieConsent={stamp:%27FJeiFrD8LSzMCWtIYKMo+wqTdjPH7gJvO8piyb3sr+uNBd7nMR370w==%27%2Cnecessary:true%2Cpreferences:true%2Cstatistics:true%2Cmarketing:true%2Cmethod:%27explicit%27%2Cver:1%2Cutc:1728414287009%2Cregion:%27ro%27}; _gcl_au=1.1.827619676.1728414285; _hjSession_1254138=eyJpZCI6ImI1N2RjZDI0LTNkZTQtNGI5ZC05ZmI5LTA2ODI3ZjRiODE2OSIsImMiOjE3Mjg0MTQyODUyNDEsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjoxLCJzcCI6MH0=; _ga=GA1.1.1398011057.1728414285; _tt_enable_cookie=1; _ttp=5ua8YUsGpKEfBa-FuH0ZQxzorpQ; _pin_unauth=dWlkPVlqUXpZVEpqTVdFdE1XSmlaQzAwT0RGa0xUZ3daRGd0TkRGbFkyVmtOR1l6WVdJNA; _fbp=fb.1.1728414285412.210127009951878959; imbox={"imboxUid":"2nASG5IA9XxVlDTjuVkASvrtwEJ"}; e_sk=4b037485-c70d-43dc-ab57-c8cf079839f2; _hjSessionUser_1254138=eyJpZCI6IjE2Y2ZiZDdlLTY3MmQtNWM3Ni1hZmRmLTBiM2UwYWRkMDcxZiIsImNyZWF0ZWQiOjE3Mjg0MTQyODUyNDEsImV4aXN0aW5nIjp0cnVlfQ==; _uetsid=2e86254085a811efb214b55d16e81443; _uetvid=2e86458085a811ef99e89919e2352624; _ga_CT371S5MF9=GS1.1.1728417033.2.1.1728419296.60.0.0',
    'priority': 'u=1, i',
    'referer': 'https://www.citygross.se/matvaror/frukt-och-gront?page=1',
    'sec-ch-ua': '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
}

# Headers used to make the requests appear as if they are coming from a browser (for categories)
headersCategories = {
    'sec-ch-ua-platform': '"Windows"',
    'Referer': 'https://www.citygross.se/matvaror',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
    'Accept': 'application/json',
    'sec-ch-ua': '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
    'sec-ch-ua-mobile': '?0',
}

# Parameters to use when making a request to filter results by category and pagination
params = {
    'categoryId': 0,
    'page': 0,
    'size': 24,
}

# Open/Create (if not created) a file named "produse.txt" in write mode using UTF-8 encoding to avoid encoding issues
with open('produse.txt', 'w', encoding='utf-8') as file:

    # Fetch category information from the website's API
    categories = requests.get('https://www.citygross.se/api/v1/navigation', headers=headersCategories)

    # Extract category IDs from the API response
    ids = categories.json()["data"]["tree"]["children"][0]["children"]

    # Looping through each category ID
    for categoriesId in ids:
        ctgId = categoriesId.get("id")  # Get the category ID
        params['categoryId'] = ctgId  # Set the ID in parameters
        params['page'] = 0  # Reset the page number for each category

        # Loop through all products from each page until no more data is available
        while True:

            # Fetch product information from the website's API
            products = requests.get(f'https://www.citygross.se/api/v1/esales/products', params=params, cookies=cookies, headers=headersProducts)

            # Check for the status code of a category, if the code is not 200 (OK), print an error and move on to the next category ID
            if products.status_code != 200:
                print(f"Eroare la cerere pentru categoria: {ctgId}, status: {products.status_code}")
                break

            # Extract data from the response
            data = products.json().get("data")

            # If there is no data, it means there are no more products and breaks the loop
            if not data:
                break

            # Looping through each product in the current page
            for prod in data:
                name = prod.get("name")
                brand = prod.get("brand")
                price = prod.get("prices")[0]["currentPrice"]["price"]
                gtin = prod.get("gtin")

                # Format the product info and write it into the file
                line = f"{name} --- {brand} --- {price} --- {gtin}\n"
                file.write(line)

            # Increment the page number by 1 to fetch the next set of products in the current category
            params['page'] += 1
