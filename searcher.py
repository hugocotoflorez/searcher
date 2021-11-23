#develop in python 3.10
#import modules
try:
    from typing import Literal
    import sys
    import os
except:
    print('[e] Impossible to import python library modules')
    raise('[e] Try to restart.')
try:
    from googlesearch import search
    import requests
    import webbrowser
    import bs4
except:
    print('''[e] External module import error. 
[>] For install all the modules run: 
\t...searcher.py --install modules''')

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
    return('|'.join(search(query=to_search, tld=domain, lang=language, num=int(openNum), start=0, stop=int(openNum), pause=pause)).split('|'))
#make a requests search
def normalSearch():  
    print('Use -u g, this function isnt already writen')
#open files in browser
def openInBrowser(filename,n=False):
    global verbose
    if verbose:print('[>] opening file...'if not n else '[>] opening files...',end='')
    s = 'file:///'
    path = os.getcwd()
    if n:
        filename,filenameext=filename.split('.')
        for l in range(n):
            a = s+(f'{path}/{filename}({l+1}).{filenameext}').replace('\\','/')
            webbrowser.open(a)
    else:
        a = s+(path+'/'+filename).replace('\\','/')
        webbrowser.open(a)
    if verbose:print('success')

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

        Use:
            (searcher dir)...\\ python3(linux)/py(windows) searcher.py [options] [url] [get output]

        options:
            short       large                     use to:

            -h          --help                      get this info:
            -v T/F      --verbose True/False/1/0    decide if prints info in console (it should be in first position)
            _           --project                   open in browser searcher.py github repository and prints the link in consola

        url:
            -u          --url (url)                 especifique url for the search (DISABLED for now...) 
            -u g        --url google                search via google

            -q          --query(s)                  word or words separeted by "," , "+" or "-" [never space!] (default:ask)
            -e          --extension                 extension to search, without "." (".\ searcher.py --extensions" -> see all extensoions) (default .com) 

            -l          --languages (language)      change the search language (".\ searcher.py --languages" -> see all languages) (default english)

        get output: 
            -r h        --return html               returns a html copy of the file
            -r l        --return link               returns the links of pages that contains the searched
            
            -s          --save (filename)           save the returned in a file. You can save it into a .txt (or .html if use -r h)
            -sm        --savemultifile (filename)   save each result in a diferent file, whose name is (miltifile)(1-...).extension.It is useful for html search 
            

            -p          --print (bool)              prints the returned in consola
             
            -n (n)      --numopen (number)          open the specified number of links (default 5 in google link search)
            -b (T/1)    --browser (True/1)          open the links in browser
            -o          --open                      open that is saved into a file with the browser (need -s or -sm)

            
   
        Useful Examples:

            Google link search, open first 10 results in browser and save the links into a file
                python3/py searcher.py -u g --query python-language -n 10 -r link -s searchlinks.txt -b 1

            Copy the HTML who is in the first link page into a file and open it
                python3/py searcher.py -u g --query hugo-coto -n 3 -r html -sm found_htmls.html -o 1
                                            

            

        ~For install all the modules that SEARCHER need you can run .\ python3/py searcher.py --install modules

    ''')
#main isnt loop
def main():
    global verbose
    args = separateArgs(sys.argv[1:] if len(sys.argv)>2 else sys.argv[1:]+[''])# cogemos los parametros introducidos despues de la ruta del script y los separamos 
                                                                        # el ultimo else evita un index error al correr searcher.py con una sola opcion sin argumentos
    verbose = bool(args.get('-v',False) or args.get('--verbose',False))#guardamos el bool de  -v o --verbose en la variable verbose
    if verbose:print('[+] Verbose: All')
    elif args=={}:help();return None #si no hay argumentos corremos help
    if not args.get('--extensions',True):#si corremos -ext... mostramos un link con extensiones
        if verbose:print('[>] visit: https://en.wikipedia.org/wiki/List_of_Internet_top-level_domains')
        webbrowser.open('https://en.wikipedia.org/wiki/List_of_Internet_top-level_domains');return None
    elif not args.get('--languages',True) or not args.get('-l',True):printLanguages();return None#mostramos languages si --languages
    elif args.get('--install',None)=='modules':installModules();return None#corremos la instalacion si --install
    elif not args.get('-h',True) or not args.get('--help',True):help();return None#mostramos ayuda si -h


    #default args
    global domain,to_search,url,returns,printit,save,openNum,language,oib
    domain = 'com'
    to_search = ''
    url = None
    returns = None
    printit = False
    save = None
    openNum = 5
    language = 'en'
    oib = False
    openfile = False
    multifile = False



    for option in args.keys():
        
        if option in ['--verbose','-v']:pass


        elif option in ['-u','--url']:
            url = 'google' if args[option] == 'g' else args[option]
            if verbose:print(f'[+] Domain: {domain}')
            

        elif option in ['-q','--query']:
            to_search = args[option]
            if verbose:print(f'[+] Args: {to_search}')

        
        elif option in ['-e','--extension']:
            domain = args[option]
            if verbose:print(f'[+] Extension: .{url}')


        elif option in ['-r','--return']:
            returns = 'html' if args[option] == 'h' else 'link' if args[option] == 'l' else args[option]
            if verbose:print(f'[+] Returns: {returns}')


        elif option in ['-p','--print']:
            printit = bool(args[option])
            if verbose:print(f'[+] Print: {"All" if printit else "None"}')


        elif option in ['-s','--save']:
            save = args[option]
            if verbose:print(f'[+] Save into: {save}')

        elif option in ['-sm','--savemultifile']:
            save = args[option]
            multifile = True
            if verbose:print(f'[+] Save into: {save} (multifile)')


        elif option in ['-n','--numopen']:
            openNum = int(args[option])
            if verbose:print(f'[+] Links open: {openNum}')


        elif option in ['-l','--language']:
            language = args[option]
            if verbose:print(f'[+] Language: {language}') 


        elif option in ['-b','--browser']:
            oib = bool(args[option])
            if verbose:print(f'[+] Open in browser: {oib}')


        elif option in ['-o','--open']:
            openfile = bool(args[option])
            if verbose:print(f'[+] View file: {openfile}')



        else:#option doesnt match 
            if verbose:print(f'[-] Impossible to resolve {option}')

    if url == 'google':#search via google
        if verbose:print('[>] Searching via google... ',end='')#print status
        urls = googleSearch()# returns \n join(urls)     call a google search

        if printit:txt="\n".join(urls);print(f'[+]urls:\n{txt}')#printit 
        
        if verbose:print('success')#status
        to_return = []#create a list that contains the links or html code

        if returns == 'link':to_return=urls#get the links returned by googleSearch
        elif returns == 'html':
            
            for a in urls:
                if verbose:print(f'[>] getting html ({a})... ',end='')
                to_return.append(requests.get(a).text)#get the html of the links
                if verbose:print('success')
            

        else:print(f'[-] Impossible to resolve {returns}, default "link" ')#status (error)
        if save:#save into a file
            if not multifile:
                try:
                    if verbose:print('[>] Saving in file... ',end='')#status
                    with open(f'{save}','wb') as f:#open the file who wants to create 
                        for a in to_return:
                            f.write(bytearray(a+'\n','utf8'))#write the links or html into the file
                    if verbose:print('success')#status
                except Exception as e:
                    print('Error')
                    print(f'[-] Impossible to save into a file: {e}')#status (error)
            else:
                savename,saveext=save.split('.')
                n=0
                for r in to_return:
                    n+=1
                    try:
                        if verbose:print(f'[>] Saving in file {n}... ',end='')#status
                        with open(f'{savename}({n}).{saveext}','wb') as f:#open the file who wants to create 
                            f.write(bytearray(r+'\n','utf8'))#write the links or html into the file
                        if verbose:print('success')#status
                    except Exception as e:
                        print('error')
                        print(f'[-] Impossible to save into a file: {e}')#status (error)


        if oib:#open in browser option, bool value
            for a in urls:webbrowser.open(a)#open with webbrowser module

        if openfile:openInBrowser(save) if not multifile else openInBrowser(save,openNum) #if use openfile option, call oib function who opens a file in browser


    else: normalSearch()#use directly requests, without a google search

            



if __name__ == '__main__':
    main()#run main module if searcher.py runs locally
