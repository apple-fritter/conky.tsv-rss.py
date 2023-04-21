# conky-rss-tsv
## What it is
Python script for integrating `RSS` feeds into a `Conky` window:

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

## License

These files released under the [MIT License](LICENSE).
