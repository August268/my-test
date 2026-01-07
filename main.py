from scraper import get_data

def main():
    url = "https://support.optisigns.com/api/v2/help_center/en-us/articles.json?per_page=50"
    result = get_data(url)

    if type(result) == None:
        print("An error occurred...")
    else:
        for a in result:
            print("----------")
            print("Title: ", a.title)
            print("Slug: ", a.slug)
            print("Source", a.source_url)
            print("Updated at: ", a.updated_at)

if __name__ == "__main__":
    main()