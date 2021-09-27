import webbrowser
import os


def output_formatter():
    """
       Returns the browser output and opens in the default browser of the system
       :return: The browser output in HTML form

    """

    # Formats the final result of word processing from the file
    c = open('results.txt')
    lines = c.read().splitlines()  # List with stripped line-breaks
    c.close()
    return content_formatter(lines)


def content_formatter(lines):
    """
           Returns the browser output and opens in the default browser of the system

           :param lines: The result file contents line by line
           :return: The browser output in HTML form

    """
    # Formats the result in html form
    content = ""
    for line in lines:
        parts = line.split(':', 1)  # Breaks the answer into diff parts for hyperlink
        if parts[0] == 'Answer Link':
            content += parts[0] + ": <a href=" + parts[1] + ">"+parts[1]+"</a><br><hr>"
        else:
            content += line + "<br>"
    return content


def result_display(content, wordcloud_image_name):
    """
    Returns the browser output and opens in the default browser of the system

    :param content: The result file contents in html form
    :param wordcloud_image_name: The name for word cloud image
    :return: The browser output in HTML form

    """

    # Word Cloud image
    src = wordcloud_image_name

    # Default HTML file for rendering
    f = open('result.html', 'w')

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


