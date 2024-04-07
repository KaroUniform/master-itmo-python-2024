# Питоновский скрипт, которому можно указать количество отличных друг от друга файлов, которые нужно загрузить в нужную папку. (С использованием aiohttp)
# Не получилось использовать https://picsum.photos/ , потому что доступ к сайту из России ограничен, и это затрудняет тестирование.
import asyncio
import os
import click
import aiohttp
import aiofiles
import logging
from aiohttp import ClientError
import time


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

async def download_image(session: aiohttp.ClientSession, url: str, filename: str):
    """
    Asynchronously downloads an image from a given URL and saves it to a specified filename.
    
    Args:
    - session: aiohttp.ClientSession for HTTP requests.
    - url: URL of the image to download.
    - filename: Filename to save the downloaded image.
    """
    try:
        async with session.get(url) as response:
            response.raise_for_status()  # Raises exception for 4XX/5XX responses
            async with aiofiles.open(filename, 'wb') as f:
                await f.write(await response.content.read())
            logging.info(f"Downloaded {filename}")
    except ClientError as e:
        logging.error(f"Failed to download {filename}: {e}")
    except Exception as e:
        logging.error(f"Unexpected error downloading {filename}: {e}")

async def download_images(num_images: int, output_dir: str):
    """
    Asynchronously downloads a specified number of images to a given directory.
    
    Args:
    - num_images: Number of images to download.
    - output_dir: Directory to save the downloaded images.
    """
    async with aiohttp.ClientSession() as session:
        tasks = [
            download_image(session, "https://thispersondoesnotexist.com/", os.path.join(output_dir, f"image_{i}.jpg"))
            for i in range(num_images)
        ]
        await asyncio.gather(*tasks)

@click.command()
@click.option('--num-images', type=int, default=10, help='Number of images to download.')
@click.option('--output-dir', type=click.Path(), default='images', help='Output directory to save images.')
def main(num_images: int, output_dir: str):
    """
    Main function to handle command-line arguments and initiate the download process.
    """
    start_time = time.time()
    os.makedirs(output_dir, exist_ok=True)
    asyncio.run(download_images(num_images, output_dir))
    logging.info(f"Downloads completed in {time.time() - start_time:.2f} seconds")

if __name__ == "__main__":
    main()
