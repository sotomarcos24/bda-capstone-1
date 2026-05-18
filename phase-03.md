# Phase 03: Refactor to improve (10 minutes)

## Goal

Improve the code structure by moving the download logic out of `solutions/main.py` and into a reusable function in `solutions/library.py`.

## Steps

1. Delete the video file from the `videos/` folder if it already exists.
2. Create a new file called `solutions/library.py`.
3. Inside `solutions/library.py`, create a function called `download_video`.
4. Move the `yt-dlp` download logic from `solutions/main.py` into that function.
5. Update `solutions/main.py` so it imports and calls the function.

## Function shape

```python
def download_video(url):
    # download one video
    ...
```

## Update `solutions/main.py`

Your `solutions/main.py` should call the function from `solutions/library.py`.

Make sure `solutions/main.py` uses the standard `__main__` check:

```python
from ...

if __name__ == "__main__":
    ...
```

## Checkpoint

Run:

```bash
python solutions/main.py
```

The app should still download the same video, but the download logic should now live in `solutions/library.py`.

After running the script, a fresh video file should appear in the `videos/` folder.
