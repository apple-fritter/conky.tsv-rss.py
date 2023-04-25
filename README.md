## What it is
Python script for integrating `RSS` feeds into a `Conky` window.

## What it does
1. Reads in a `TSV` file containing feed information, where each row represents a single feed item and each column contains the relevant information such as the `URL`, `title`, and `metadata`.
2. Parses each `RSS` feed using `feedparser` and extracts the relevant information for each feed item.
3. Uses `beautifulsoup4` to extract any embedded links in the feed item's summary.
4. Displays each feed item as a clickable link in the Conky window, including the item title, the URL, and any metadata.
5. The `${goto}` coordinates can be adjusted based on the size of your Conky window.

With these features, the script can be used to display multiple RSS feeds in a Conky window, and the feed information can be easily customized by modifying the TSV file.

## Considerations:

The script assumes that the RSS feed's summary contains embedded links that can be extracted using `beautifulsoup4`. If the summary does not contain any links or the links are embedded in a different format, the script may not function as intended.

The script may encounter errors if the feed information in the TSV file is not properly formatted or contains invalid URLs.

Depending on the number of feeds and feed items being displayed, the script may consume significant system resources, such as CPU and memory. This could impact the performance of other applications running on the same machine.

The `${goto}` coordinates used to display the feed items as clickable links in Conky format may need to be adjusted based on the size of your Conky window. This could be time-consuming if you need to fine-tune the layout of the feed items.

The script may not be suitable for users who require a more advanced or flexible RSS feed reader. In this case, a dedicated feed reader application may be a better option.

>Finally, as with any script, it's important to be mindful of security considerations. Ensure that the TSV file and any external resources, **such as the RSS feeds themselves**, are trustworthy and do not pose a security risk.

## Usage
### Prerequisites
Before using the script, ensure that the following packages are installed:
```
feedparser
beautifulsoup4
```
You can install these packages using the following command:
```
pip install feedparser beautifulsoup4
```

### Configuration
Create a TSV file containing the feed information. The TSV file should have the following format:
```
URL<TAB>Title<TAB>Metadata
```

For example:
```
https://rss.nytimes.com/services/xml/rss/nyt/World.xml  New York Times World News
https://www.npr.org/rss/rss.php?id=1001  NPR Top Stories
https://www.reddit.com/r/worldnews/.rss  Reddit World News
```

Note that each row represents a single feed item, and each column contains the relevant information. The Title and Metadata columns are optional.

In the conky-rss-tsv.py script, modify the following variables to match your configuration:
```
TSV_FILE = 'feeds.tsv'
NUM_FEEDS = 3
NUM_ITEMS_PER_FEED = 5
FEED_REFRESH_TIME = 300
CONKY_WIDTH = 600
CONKY_HEIGHT = 300
FEED_FONT = 'DejaVu Sans:size=8'
```

## TSV List population script
A small bash script to populate the TSV file with the required information using curl or any other mechanism to retrieve the RSS feed information from the provided URL, that uses `curl` and `sed` to extract the relevant information from the RSS feed and append it to the TSV file:
```
#!/bin/bash

# Check if URL is provided
if [ -z "$1" ]; then
  echo "Please provide a valid URL"
  exit 1
fi

# Retrieve RSS feed using curl and extract relevant information
RSS_FEED=$(curl -s "$1")
TITLE=$(echo "$RSS_FEED" | sed -n 's/.*<title>\(.*\)<\/title>.*/\1/ip;T;q')
DESCRIPTION=$(echo "$RSS_FEED" | sed -n 's/.*<description>\(.*\)<\/description>.*/\1/ip;T;q')

# Append information to TSV file
echo -e "${1}\t${TITLE}\t${DESCRIPTION}" >> feeds.tsv

# Print success message
echo "RSS feed information for ${1} has been added to feeds.tsv"
```

> This script has been provided in this repository and I am considering integrating its mechanism into the python script itself. Stay tuned!

## [Disclaimer](DISCLAIMER)
**This software is provided "as is" and without warranty of any kind**, express or implied, including but not limited to the warranties of merchantability, fitness for a particular purpose and noninfringement. In no event shall the authors or copyright holders be liable for any claim, damages or other liability, whether in an action of contract, tort or otherwise, arising from, out of or in connection with the software or the use or other dealings in the software.

**The authors do not endorse or support any harmful or malicious activities** that may be carried out with the software. It is the user's responsibility to ensure that their use of the software complies with all applicable laws and regulations.

## License

These files released under the [MIT License](LICENSE).
