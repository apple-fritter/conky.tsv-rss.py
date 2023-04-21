import feedparser
from bs4 import BeautifulSoup

# Set the path to the TSV file containing the feed information
tsv_file = '/path/to/feeds.tsv'

# Read in the TSV file and split each row into columns
with open(tsv_file, 'r') as f:
    lines = f.readlines()

rows = [line.strip().split('\t') for line in lines if not line.startswith('#')]

# Loop through each row and parse the corresponding RSS feed
for row in rows:
    url = row[0]
    title = row[1] if len(row) > 1 else ''
    metadata = row[2] if len(row) > 2 else ''

    # Parse the RSS feed using feedparser
    feed = feedparser.parse(url)

    # Loop through the feed items and extract the relevant information
    for item in feed.entries:
        item_title = item.title if not title else title
        item_metadata = item.get(metadata, '') if metadata in item else ''

        # Use BeautifulSoup to extract any embedded links in the summary
        soup = BeautifulSoup(item.summary, 'html.parser')
        links = soup.find_all('a')

        # Print the feed item as a clickable link in Conky format
        print('${goto 10}' + item_title + ': ' + '${goto 150}' + links[0]['href'] + ' ' + item_metadata)
