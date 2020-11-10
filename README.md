# text-based_browser  
Simplified text-based browser that ignores JS and CSS, doesn't have cookies, and shows a limited set of tags. It gives an option to read online documentation or find something on the Internet from the command line/terminal. The links are displayed in blue color(using library Colorama).
  
**Learning outcomes**   
In this project, I've learned how HTTP works, how to parse HTML and how to work with it in Python(library requests and BeautifulSoup4). I've become familiar with Python input and output, how to read/write files, learned the basics of Colorama library.

**How it works - possible inputs**
-  *python browser.py dir-for-files* (start browser through command line or terminal, "dir-for-files" represents directory where the internet pages will be saved)
-  *google.com* (input web address you want to display with or without "https://")
-  *back* (this command will show previous page)
-  *google* (If web page was displayed before, it was also saved into a text file. You can display the saved web page from file by calling it without the prefix "https://" and postfix ".com", e.g. "google")  
-  *exit* (to quit the app)
