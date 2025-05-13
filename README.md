# Bright Data Web Unlocker Python project

[Edit in CodeSandbox editor](https://codesandbox.io/s/github/luminati-io/bright-data-web-unlocker-python-project?file=index.py)

## Bright Data Web Unlocker API Example

This project demonstrates how to use Bright Data's Web Unlocker API to access websites through Bright Data Web Unlocker API.

## Overview

This script helps you access websites with anti-bot protection or CAPTCHAs by using Bright Data's Web Unlocker to automatically bypass these obstacles.

### Direct configuration

1. Replace `BRIGHT_DATA_API_TOKEN` with your actual API token
2. Replace `web_unlocker1` with your zone
3. Replace `https://geo.brdtest.com/welcome.txt` with your target URL

## Running the example

1. Make sure you've configured your `API token` and `zone`
2. Run `python index.py` in the terminal
3. Check the console output for the results

## How it works?

1. The script makes a POST request to Bright Data's Unlocker API endpoint
2. It includes your authentication token and target URL
3. Bright Data's Web Unlocker accesses the target URL
4. The response is returned to your script and displayed in the console

## Troubleshooting

If you encounter errors:

- Verify your API token is correct
- Check that your zone name is valid
- Ensure your target URL is properly formatted

## Modifying the example

To request a different URL:
1. Update the `targetUrl` in the CONFIG object
2. Run the script again

## Additional resources

- [Bright Data Web Unlocker API](https://docs.brightdata.com/scraping-automation/web-unlocker/introduction)
- [Get an API Token](https://docs.brightdata.com/general/account/api-token)
- [Manage Zones](https://brightdata.com/cp/zones)

**Note:** This is an example implementation for educational purposes. For production use, consider adding additional error handling, logging, and security measures.
