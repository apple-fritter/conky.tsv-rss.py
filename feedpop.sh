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
