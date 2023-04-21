# conky-tsv-rss
Python script for integrating `RSS` feeds into a `Conky` window:

1. Reads in a `TSV` file containing feed information, where each row represents a single feed item and each column contains the relevant information such as the `URL`, `title`, and `metadata`.
2. Parses each `RSS` feed using `feedparser` and extracts the relevant information for each feed item.
3. Uses `beautifulsoup4` to extract any embedded links in the feed item's summary.
4. Displays each feed item as a clickable link in the Conky window, including the item title, the URL, and any metadata.
5. The ${goto} coordinates can be adjusted based on the size of your Conky window.

With these features, the script can be used to display multiple RSS feeds in a Conky window, and the feed information can be easily customized by modifying the TSV file.
