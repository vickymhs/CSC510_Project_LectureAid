import webbrowser
import os


def showResult(WORDCLOUD_FILE_NAME):
    """
       Returns the browser output and opens in the default browser of the system

       :param WORDCLOUD_FILE_NAME: The name for word cloud image
       :return: The browser output in HTML form

    """
    # Word Cloud image
    src = WORDCLOUD_FILE_NAME

    # Default HTML file for rendering
    f = open('result.html', 'w')

    # Formats the final result of word processing from the file
    c = open('results.txt')
    lines = c.read().splitlines()  # List with stripped line-breaks
    c.close()

    # Formats the result in html form
    content = ""
    for line in lines:
        parts = line.split(':', 1)  # Breaks the answer into diff parts for hyperlink
        if parts[0] == 'Answer Link':
            content += parts[0] + ": <a href=" + parts[1] + ">"+parts[1]+"</a><br><hr>"
        else:
            content += line + "<br>"

    # HTML content
    urls = ""
    message = """<html>
    <head></head>
    <body style="background-color:#000000">
    <h1 style="color:#87D7FA;margin-left:6%;margin-top:4%">LectureAid</h1>
    <div style="text-align: center">
    <div style="background-color:#FFFFFF;width:40%;overflow-wrap: break-word;margin:2%;padding:4%;display: inline-block;
      vertical-align: middle;text-align:left;border-radius:50px">
    <p>{urls}</p>
    </div>
    <div style=" display: inline-block;vertical-align: top;margin:2%">
    <img style="border-radius:50px" src="{src}" alt="Girl in a jacket" width="500" height="600">
    </div>
    </div>
    </body>
    </html>""".format(urls=content, src=src)

    f.write(message)
    f.close()

    # Change path to reflect file location
    filename = 'file:///' + os.getcwd() + '/' + 'result.html'
    webbrowser.open_new_tab(filename)


