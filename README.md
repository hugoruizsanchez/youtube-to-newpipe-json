# youtube-to-newpipe-json
A system that converts the YouTube subscriptions feed (CTRL+A) into a formatted JSON for Newpipe or Freetube.
> [!NOTE]  
> Although the resulting file is correct, its format is obsolete. This file may be useful if modified for other purposes related to youtube subscriptions, but it is no longer valid for NewPipe or Freetube.
## Instructions
- Go to the subscriptions feed and copy all the text contained in the page (CTRL+A).
- Paste the text in `subscriptions.txt`
- Depending on your language, modify the keyword array so that the filtering is correct.
- Execute the script, the resulting file will contain a JSON with all youtube subscriptions with their links and names.
