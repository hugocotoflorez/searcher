#verbose = args.get('-v',False) or args.get('--verbose',False) or True    
#                                                              ^^^^^   we can write this for make verbose allways active
#
#import modules
from typing import Literal
try:
    import sys
    import os
except:
    print('Impossible to import python library modules')
try:
    from googlesearch import search
    import requests
    import webbrowser
    import bs4
except:
    print('External module import error. For install all the modules run: ')


#function that should install all required modules
def installModules():
    moduleList=[
        'google',
        'requests',
        'webbrowser',
        'beautifulsoup4'

    ]
    for module in moduleList:
        try:
            os.system(f'pip install {module}')
        except Exception as e:
            print(f'Impossible to install {module}: {e}')
#returns the args and their values like a dict
def separateArgs(a):
    return({a[d]:('' if a[d+1].startswith('-') else a[d+1]) for d in range(len(a)) if a[d].startswith('-')})
#make a google search with the google module
def googleSearch()->Literal["list of urls"]:
    global to_search,domain,language,openNum
    domain = domain[1:] if domain.startswith('.') else domain
    to_search=to_search.replace(',.-/:&',' ')  
    pause=2.0 if len(to_search.split(' '))<10 else 1.0#only use to optimice 

    return('\n'.join(search(query=to_search, tld=domain, lang=language, num=int(openNum), start=0, stop=int(openNum), pause=pause)))
#make a requests search
def normalSearch():  
    print('Use -u g, this function isnt already writen')
#open files in browser
def openInBrowser(filename):
    s = 'file:///'
    path = os.getcwd()
    print(path)
    a = s+(path+'/'+filename).replace('\\','/')
    print(a)
    webbrowser.open(a)
#prints info (languages)
def printLanguages():
    print(
   '''----Name:----------Code:---
    Amharic	        am
    Arabic	        ar
    Basque	        eu
    Bengali	        bn
    English (UK)    en-GB
    Port.(Brazil)	pt-BR
    Bulgarian	    bg
    Catalan	        ca
    Cherokee	    chr
    Croatian	    hr
    Czech	        cs
    Danish	        da
    Dutch	        nl
    English (US)	en
    Estonian	    et
    Filipino	    fil
    Finnish	        fi
    French	        fr
    German	        de
    Greek	        el
    Gujarati	    gu
    Hebrew	        iw
    Hindi	        hi
    Hungarian	    hu
    Icelandic	    is
    Indonesian	    id
    Italian	        it
    Japanese	    ja
    Kannada	        kn
    Korean	        ko
    Latvian	        lv
    Lithuanian	    lt
    Malay	        ms
    Malayalam	    ml
    Marathi	        mr
    Norwegian	    no
    Polish	        pl
    Port.(Portugal)	pt-PT
    Romanian	    ro
    Russian	        ru
    Serbian	        sr
    Chinese (PRC)	zh-CN
    Slovak	        sk
    Slovenian	    sl
    Spanish	        es
    Swahili	        sw
    Swedish	        sv
    Tamil	        ta
    Telugu	        te
    Thai	        th
    Chinese(Taiwan) zh-TW
    Turkish	        tr
    Urdu	        ur
    Ukrainian	    uk
    Vietnamese	    vi
    Welsh	        cy
        ''')
#prints info (all)
def help():
    print('''                                                                                                                               
         d888888o.   8 8888888888            .8.          8 888888888o.      ,o888888o.    8 8888        8 8 8888888888   8 888888888o.   
       .`8888:' `88. 8 8888                 .888.         8 8888    `88.    8888     `88.  8 8888        8 8 8888         8 8888    `88.  
       8.`8888.   Y8 8 8888                :88888.        8 8888     `88 ,8 8888       `8. 8 8888        8 8 8888         8 8888     `88  
       `8.`8888.     8 8888               . `88888.       8 8888     ,88 88 8888           8 8888        8 8 8888         8 8888     ,88  
        `8.`8888.    8 888888888888      .8. `88888.      8 8888.   ,88' 88 8888           8 8888        8 8 888888888888 8 8888.   ,88'  
         `8.`8888.   8 8888             .8`8. `88888.     8 888888888P'  88 8888           8 8888        8 8 8888         8 888888888P'   
          `8.`8888.  8 8888            .8' `8. `88888.    8 8888`8b      88 8888           8 8888888888888 8 8888         8 8888`8b       
      8b   `8.`8888. 8 8888           .8'   `8. `88888.   8 8888 `8b.    `8 8888       .8' 8 8888        8 8 8888         8 8888 `8b.     
      `8b.  ;8.`8888 8 8888          .888888888. `88888.  8 8888   `8b.     8888     ,88'  8 8888        8 8 8888         8 8888   `8b.   
       `Y8888P ,88P' 8 888888888888 .8'       `8. `88888. 8 8888     `88.    `8888888P'    8 8888        8 8 888888888888 8 8888     `88.   

                                                                                                                        by Hugo Coto Flórez

        Usage:
                (searcher dir)...\\ python3(linux)/py(windows) searcher.py [options]

        options:
            short       large                     use to:

            -h          --help                      get this info:

            -w T/F      --verbose True/False/1/0    decide if prints info in console (it should be in first position)

            -u          --url (url)                 especifique url for the search
            -u g        --url google                search via google

            -q          --query(s)                  word or words separeted by "," , "+" or "-" [never space!] (default:ask)
            -d          --domain                    domain to search (default .com) 

            -r          --return (way)              how to get the information 
            -r h        --return html               returns a html copy of the file
            -r l        --return link               returns the links of pages that contains the searched
            
            -s          --save (filename)           save the returned in a file. You can save it into a .txt or .html if use -r h

            -p          --print                     prints the returned in consola (default True if verbose is True)
             
            -o (n)      --open (number)             open the specified number of links (default 5 in google link search)
            -b (T/1)    --browser (True/1)          open the links in browser
            -v          --view                      open that is saved into a file with the browser (important -o 1 for .html files)(need -s)

            -l          --languages (language)      change the search language (".\ searcher.py --languages" -> see all languages) (default english)

            
        Useful Examples:

            Google normal search, open first 10 results in browser and save the links into a file
                python3/py searcher.py -u g --query python-language --open 10 -r link -s searchlinks.txt -b 1

            Copy the HTML who is in the first link page into a file and open it
                python3/py searcher.py -u g --query python-language --open 1 -r html -s searchlinks.html 
                                            

            

        ~For install all the modules that SEARCHER need you can run .\ python3/py searcher.py --install modules

    ''')
#main isnt loop
def main():
    args = separateArgs(sys.argv[1:] if len(sys.argv)>2 else sys.argv[1:]+[''])# cogemos los parametros introducidos despues de la ruta del script y los separamos 
                                                                               # el ultimo else evita un index error al correr searcher.py con una sola opcion sin argumentos
    if args=={}:help() #si no hay argumentos corremos help
    verbose = args.get('-v',False) or args.get('--verbose',False) 
    if verbose:print('[+] Verbose: All')
    if not args.get('--languages',True) or not args.get('-l',True):printLanguages();return None
    if args.get('--install',None)=='modules':installModules();return None
    elif not args.get('-h',True) or not args.get('--help',True):help();return None


    #default args
    global domain,to_search,url,returns,printit,save,openNum,language,oib
    domain = 'com'
    to_search = ''
    url = None
    returns = None
    printit = False
    save = None
    openNum = None
    language = 'en'
    oib = False
    view = False


    for option in args.keys():
        
        if option in ['-w','--verbose','h','help','--install']:pass


        elif option in ['-u','--url']:
            url = 'google' if args[option] == 'g' else args[option]
            if verbose:print(f'[+] Domain: {domain}')
            

        elif option in ['-q','--query']:
            to_search = args[option]
            if verbose:print(f'[+] Args: {to_search}')

        
        elif option in ['-d','--d']:
            domain = args[option]
            if verbose:print(f'[+] Domain: {url}')


        elif option in ['-r','--return']:
            returns = 'html' if args[option] == 'h' else 'link' if args[option] == 'l' else args[option]
            if verbose:print(f'[+] Returns: {returns}')


        elif option in ['-p','--print']:
            printit = bool(args[option])
            if verbose:print(f'[+] Print: {"All" if printit else "None"}')


        elif option in ['-s','--save']:
            save = args[option]
            if verbose:print(f'[+] Save into: {save}')


        elif option in ['-o','--open']:
            openNum = 5 if args[option] == '' else args[option]
            if verbose:print(f'[+] Links open: {openNum}')


        elif option in ['-l','--language']:
            language = args[option]
            if verbose:print(f'[+] Language: {language}') 


        elif option in ['-b','--browser']:
            oib = bool(args[option])
            if verbose:print(f'[+] Open in browser: {oib}')


        elif option in ['-v','--view']:
            view = args[option]
            if verbose:print(f'[+] View file: {view}')



        else:#option doesnt match 
            if verbose:print(f'[-] Impossible to resolve {option}')

    if url == 'google':
        if verbose:print('[>] Searching via google...')
        urls = googleSearch()# returns \n join(urls)
        if printit:print(f'[+]urls: \n{urls}')
        
        if verbose:print('[+] All links found correctly')
        to_return = []

        if returns == 'link':to_return=urls.split('\n')
        elif returns == 'html':to_return=[requests.get(a).text for a in urls.split('\n')]
        else:print(f'[-] Impossible to resolve {returns}, run with "link" ')
        if verbose:print('[+] Search is over')

        if save:
            if verbose:print('[>] Saving in file...')
            with open(f'{save}','wb') as f:
                for a in to_return:
                    f.write(bytearray(a+'\n','utf8'))
            if verbose:print('[+] Saved correctly')

        if oib:
            for a in urls.split('\n'):webbrowser.open(a)

        if view:openInBrowser(save)


    else: normalSearch()
            



if __name__ == '__main__':
    main()
    print('\n\t\t\t\t\t\t\t\t\t\tThanks for use SEARCHER :)')