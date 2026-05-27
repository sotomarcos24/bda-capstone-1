from library import download_video_semaphore, read_video_urls, get_video_metadata
import threading
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime

download_limit = threading.Semaphore(5)
result_file_guard = threading.Semaphore(1)

urls = read_video_urls("data/video_urls.csv")

file = open("reports/semaphore_results.txt", "w")
file.close()

futures = []
with ThreadPoolExecutor(max_workers=5) as executor:
    for url in urls:
        futures.append(executor.submit(download_video_semaphore, url, download_limit))

for future in futures:
    result = future.result()
    with result_file_guard:
        with open("reports/semaphore_results.txt", "a") as f:
            f.write(f"Url: {result['url']}, status: {result['status']}, error: {result['error']}, timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")