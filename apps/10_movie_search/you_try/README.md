# App 10: Movie Search App

![image](app-10-screenshot.png)
 
If you want to try this yourself, try to build the interactive app above. 

This application use the OMDb API to search live movie data for movies matching the title in your search text. It focuses on being reliable even when the network fails or the user enters bad information.

Key concepts introduced
=================

**The API**

You can find the details of the JSON HTTP API at [www.omdbapi.com](http://www.omdbapi.com).

**Try/Except Error Handling**

    try:        method1()        method2()        method3()    except ConnectionError as ce:        # handle network error    except Exception as x:        # handle general error

**Raising your own errors and exceptions**

    class MovieClient:
        def __init__(self, search_text):

            if not search_text or not search_text.strip():
                raise ValueError('Must specify a search string.')

