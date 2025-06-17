import os
from icrawler.builtin import GoogleImageCrawler

def download_images(query, num_images=50, save_dir='Original'):
    person_dir = os.path.join(save_dir, query.replace(' ', '_'))
    os.makedirs(person_dir, exist_ok=True)
    crawler = GoogleImageCrawler(storage={'root_dir': person_dir})
    crawler.crawl(keyword=query, max_num=num_images)
    print(f"Downloaded {num_images} images for '{query}' to '{person_dir}'")

if __name__ == "__main__":
    query = input("Enter the search query (person's name): ")
    num_images = int(input("Enter the number of images to download: "))
    download_images(query, num_images)