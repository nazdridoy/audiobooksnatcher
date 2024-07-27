# audiobooksnatcher
> Snatch audiobooks from Tokybook and FreeAudioBooks

## Installation
1. Go to desired clone directory, then run:
```sh
git clone https://github.com/nazdridoy/audiobooksnatcher.git
```
2. Open terminal in audiobooksnatcher directory, then run:
```sh
pip install -r requirements.txt
```

## Usage
Run audiobooksnatcher:
```sh
python main.py
```

### Options
- `-S` or `--source`: Specify the source website (default: "toky")
  - `toky`: Use Tokybook.com
  - `freeaudiobooks`: Use FreeAudioBooks.top

Example:
```sh
python main.py -S freeaudiobooks
```

### Features
1. **Search book**: Search for audiobooks on the selected source.
2. **Download from URL**: Directly download an audiobook using its URL.

## Search Functionality
- Enter your search query when prompted.
- Select the desired book from the search results.
- The program will automatically start downloading the audiobook chapters.

## Direct URL Download
- Enter the URL of the audiobook when prompted.
- Ensure the URL matches the selected source (Tokybook or FreeAudioBooks).

> [!TIP]
> After downloading convert it into a proper m4b ebook with [AudioBookBinder](https://github.com/gonzoua/AudioBookBinder).
