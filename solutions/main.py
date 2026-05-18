from library import download_video, read_video_urls
import time
from multiprocessing import Pool

if __name__ == "__main__":
    # download_video("https://www.youtube.com/watch?v=jNQXAC9IVRw")

    # Serial execution:
    # start_s = time.perf_counter()
    # urls = read_video_urls("data/video_urls.csv")
    # for url in urls:
    #     download_video(url)
    # end_s = time.perf_counter()
    # elapsed_s = end_s - start_s
    # serial_time = round(elapsed_s, 2)
    # print(f"Serial execution: {serial_time}")


    # Parallel execution:
    start_p = time.perf_counter()

    urls = read_video_urls("data/video_urls.csv")

    with Pool() as pool:
        results = pool.map(download_video, urls)
    
    end_p = time.perf_counter()
    elapsed_p = end_p - start_p
    parallel_time = round(elapsed_p, 2)
    print(f"Parallel execution: {parallel_time}")



    with open("reports/sequential_report.md", "a") as f:
        # f.write(f"# Report\n\n")
        # f.write(f"## Serial execution\n\n")
        # f.write(f"Total time: {serial_time} seconds\n\n")
        # f.write(f"## Complexity\n\n")
        # f.write(f"Time complexity: O(n)\n\n")
        # f.write(f"Space complexity: O(n)\n")
        f.write(f"## Parallel execution\n\n")
        f.write(f"Total time: {parallel_time} seconds\n\n")

