from library import download_video, read_video_urls, get_video_metadata
import time
from multiprocessing import Pool
import csv


if __name__ == "__main__":

    urls = read_video_urls("data/video_urls.csv")
    # download_video("https://www.youtube.com/watch?v=jNQXAC9IVRw")

    # Serial execution:
    # start_s = time.perf_counter()
    # for url in urls:
    #     download_video(url)
    # end_s = time.perf_counter()
    # elapsed_s = end_s - start_s
    # serial_time = round(elapsed_s, 2)
    # print(f"Serial execution: {serial_time}")

    # Parallel execution:
    # start_p = time.perf_counter()
    # with Pool() as pool:
    #     results = pool.map(download_video, urls)
    # end_p = time.perf_counter()
    # elapsed_p = end_p - start_p
    # parallel_time = round(elapsed_p, 2)
    # print(f"Parallel execution: {parallel_time}")

    # with open("reports/sequential_report.md", "a") as f:
        # f.write(f"# Report\n\n")
        # f.write(f"## Serial execution\n\n")
        # f.write(f"Total time: {serial_time} seconds\n\n")
        # f.write(f"## Complexity\n\n")
        # f.write(f"Time complexity: O(n)\n\n")
        # f.write(f"Space complexity: O(n)\n")
        # f.write(f"## Parallel execution\n\n")
        # f.write(f"Total time: {parallel_time} seconds\n\n")

    # metadata_rows = []

    # for url in urls:
    #     metadata = get_video_metadata(url)
    #     metadata_rows.append(metadata)

    # with open("data/video_metadata.csv", "w", newline="") as file:
    #     fieldnames = ["title", "duration", "uploader", "view_count", "ext", "url"]
    #     writer = csv.DictWriter(file, fieldnames=fieldnames)

    #     writer.writeheader()
    #     writer.writerows(metadata_rows)
    
    results = []

    for url in urls:
        result = download_video(url)
        results.append(result)

    failed_url_count = 0
    for result in results:
        if result["status"] == "failed":
            failed_url_count += 1
            print("Failed:", result["url"])
            print("Error:", result["error"])

    with open("reports/sequential_report.md", "a") as f:
        f.write(f"## Download status\n\n")
        f.write(f"Successful downloads: {len(results) - failed_url_count}\n\n")
        f.write(f"Failed downloads: {failed_url_count}\n\n")
        for result in results:
            if result["status"] == "failed":
                f.write(f"Url thah failed: {result['error']}\n\n")
                f.write(f"Failed downloads: {result['error']}\n\n")
        