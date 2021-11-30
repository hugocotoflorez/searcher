#develop in python 3.10
#import modules
try:
    from typing import Literal
    import sys
    import os
    from subprocess import Popen
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

#default global args
 
verbose = False
domain = 'com'
to_search = ''
url = 'google'
returns = 'link'
printit = False
save = None
openNum = 5
language = 'en'
oib = False
openfile = False
multifile = False

def clear():
    
    for file in os.listdir(os.getcwd()):
        try:
            print(f'[+] Delete dir ({file}) ... ',end='')
            if not file in ['README.md','searcher.py']:
                os.remove(f'{os.getcwd()}\\{file}')
                print('success')
            else: print('deny')
        except Exception as e:print('error')

def update():
    clear()
    print('[>] Creating updater ...',end='')
    try:   
        Popen(["git","pull","https://github.com/hugoocf/searcher.git"],shell=False)
    except Exception as e:
        print('error')
        print(f'[-] {e}') 
    else:
        print('success')
    
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
            os.popen(f'pip install {module}',shell=False)
        except Exception as e:
            print(f'[-] Impossible to install {module}: {e}')
#returns the args and their values like a dict
def separateArgs(a):
    a.append('')
    return({a[d]:('' if a[d+1].startswith('-') else a[d+1]) for d in range(len(a)) if a[d].startswith('-')})
#make a google search with the google module
def googleSearch()->Literal["list of urls"]:
    d = domain[1:] if domain.startswith('.') else domain
    t=to_search.replace(',.-/:&',' ')
    if verbose:print()  
    pause=2.0 if len(t.split(' '))<10 else 1.0#only use to optimice 
    return('|'.join(search(query=t, tld=d, lang=language, num=int(openNum), start=0, stop=int(openNum), pause=pause)).split('|'))
#make a requests search
def normalSearch():  
    print('Use -u g, this function isnt already writen')
#open files in browser
def openInBrowser(filename,n=False):
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

def GUI():
    print('success')
    global verbose
    verbose=1
    try:
        if verbose:print('[>] importing tkinter... ',end='')
        import tkinter as tk
        from tkinter import IntVar, StringVar
    except ModuleNotFoundError or ImportError:
        if verbose:print('error')
        print('[e] error at importing tkinter')
    else:
        if verbose:print('success')
        try:
            def dest():w.destroy()
            if verbose:print('[>] run GUI ... ',end='')
            w = tk.Tk()
            e=StringVar();u=StringVar();q=StringVar();n=StringVar();r=StringVar();l=StringVar();fn=StringVar()
            verbose = IntVar();saved = IntVar();multifiles = IntVar();openbrowser = IntVar();opensaved = IntVar()
            frame1 = tk.Frame(master=w, width=100, height=100);frame1.pack(fill=tk.BOTH, expand=True)
            frame2 = tk.Frame(master=w, width=100, height=100);frame2.pack(fill=tk.BOTH, expand=True)
            frame3 = tk.Frame(master=w, width=100, height=100);frame3.pack(fill=tk.BOTH, expand=True)
            frame4 = tk.Frame(master=w, width=100, height=100);frame4.pack(fill=tk.BOTH, expand=True)
            frame5 = tk.Frame(master=w, width=100, height=100);frame5.pack(fill=tk.BOTH, expand=True)
            frame6 = tk.Frame(master=w, width=100, height=100);frame6.pack(fill=tk.BOTH, expand=True)
            frame7 = tk.Frame(master=w, width=100, height=100);frame7.pack(fill=tk.BOTH, expand=True)
            frame8 = tk.Frame(master=w, width=100, height=100);frame8.pack(fill=tk.BOTH, expand=True)
            frame9 = tk.Frame(master=w, width=100, height=100);frame9.pack(fill=tk.BOTH, expand=True)
            frame10= tk.Frame(master=w, width=100, height=100);frame10.pack(fill=tk.BOTH, expand=True)
            frame11= tk.Frame(master=w, width=100, height=100);frame11.pack(fill=tk.BOTH, expand=True)
            frame12= tk.Frame(master=w, width=100, height=100);frame12.pack(fill=tk.BOTH, expand=True)
            tk.Checkbutton(frame1, text = "verbose", variable = verbose, onvalue = 1, offvalue = 0).pack()
            tk.Label(frame2,text='Url').pack();urlentry = tk.Entry(frame2,textvariable=u);urlentry.insert(0,string='google');urlentry.pack()
            tk.Label(frame3,text='query').pack();quentry = tk.Entry(frame3,textvariable=q);quentry.pack()
            tk.Label(frame4,text='extension').pack();extentry = tk.Entry(frame5,textvariable=e);extentry.insert(0,string='.com');extentry.pack()
            tk.Label(frame5,text='language').pack();lngentry = tk.Entry(frame5,textvariable=l);lngentry.insert(0,string='en');lngentry.pack()
            tk.Label(frame6,text='return method').pack();retentry = tk.Entry(frame6,textvariable=r);retentry.insert(0,string='link');retentry.pack()
            tk.Checkbutton(frame7,text='save in file', variable = saved, onvalue = 1, offvalue = 0).pack();
            tk.Checkbutton(frame8,text='save in multifile', variable = multifiles, onvalue = 1, offvalue = 0).pack();sveentry = tk.Entry(frame8,textvariable=fn);sveentry.insert(0,string='filename.txt');sveentry.pack()
            tk.Checkbutton(frame9,text='open in browser', variable = openbrowser, onvalue = 1, offvalue = 0).pack();
            tk.Checkbutton(frame10,text='open saved', variable = opensaved, onvalue = 1, offvalue = 0).pack()
            tk.Label(frame11,text='number to open').pack();numentry = tk.Entry(frame11,textvariable=n);numentry.insert(0,string='5');numentry.pack()
            tk.Button(frame12,text='Done',command=dest).pack()
            w.mainloop()
            verbose = verbose.get()
            varv={
                'url':u.get(),
                'query':q.get(),
                'extension':e.get(),
                'language':l.get(),
                'returns':'html' if r.get()=='html' else 'links',
                'save':fn.get() if saved.get() else None,
                'multifile':bool(multifiles.get()),
                'browser':bool(openbrowser.get()),
                'opensaved':bool(opensaved.get()),
                'numopen':n.get()}
            global domain,to_search,url,returns,save,openNum,language,oib,openfile,multifile
            domain = varv['extension'].replace('. ','')
            to_search = varv['query'].replace(' ','-')
            url = varv['url']
            returns = varv['returns']
            save = varv['save']
            openNum = varv['numopen']
            language = varv['language']
            oib = varv['browser']
            openfile = varv['opensaved']
            multifile = varv['multifile']
            p='\n'.join(f"[+] {a}: {varv[a]}" for a in varv.keys() if varv[a])
            if verbose:w=tk.Tk();tk.Label(text=p).pack();tk.Button(w,text='Done',command=dest).pack();w.mainloop()
        except Exception as e:
            if verbose:print('error')
            print('[e] unexpected error:',e)
        else:
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
    
                                 _               
         ___  ___  __ _ _ __ ___| |__   ___ _ __ 
        / __|/ _ \/ _` | '__/ __| '_ \ / _ \ '__|
        \__ \  __/ (_| | | | (__| | | |  __/ |          v.1.1 (only tested in windows)
        |___/\___|\__,_|_|  \___|_| |_|\___|_|   
                                                by Hugo Coto Flórez

        Use:
            (searcher dir)...\\ python3(linux)/py(windows) searcher.py [options] [url] [get output]

        options:
            short       large                     use to:

            -h          --help                      get this info
            __          --gui                       open the gui (need tkinter)
            -v          --verbose                   decide if prints info in console (it should be in first position)
            __          --project                   open in browser searcher.py github repository and prints the link in consola

        url:
            -u          --url (url)                 especifique url for the search (DISABLED for now...) 
            -u g        --url google                search via google

            -q          --query                     word or words separeted by "," , "+" or "-" [never space!] (default:ask)
            -e          --extension                 extension to search, without "." (".\ searcher.py --extensions" -> see all extensoions) (default .com) 

            -l          --language (language)       change the search language (".\ searcher.py --languages" -> see all languages) (default english)

        get output: 
            -r h        --return html               returns a html copy of the file (default:link)
            -r l        --return link               returns the links of pages that contains the searched
            
            -s          --save (filename)           save the returned in a file. You can save it into a .txt (or .html if use -r h)
            -sm        --savemultifile (filename)   save each result in a diferent file, whose name is (miltifile)(1-...).extension.It is useful for html search 
            

            -p          --print                     prints the returned in consola
             
            -n (n)      --numopen (number)          open the specified number of links (default 5 in google link search)
            -b (T/1)    --browser                   open the links in browser
            -o          --open                      open that is saved into a file with the browser (need -s or -sm)
           


        Useful Examples:

        -open 3 links that contains the query
            ...searcher.py -v -u g -q to-search -n 3 -b
        -save 3 links that contains the query into a file and open it
            ...searcher.py -v -u g -q to-search -n 3 -s filename.txt -o
        -get the html of 3 pages that contains the query, save in diferent files and open it.
            ...searcher.py -v -u g -q to-search -n 3 -r h -sm htmls.html -o
                                            

            
        ~For clear all the folder you can run ... searcher.py --clear
        ~For install all the modules that SEARCHER need you can run ... searcher.py --install modules

    ''')

def main():
    global domain,to_search,url,returns,save,openNum,language,oib,openfile,multifile,printit
    args = separateArgs(sys.argv[1:])# cogemos los parametros introducidos despues de la ruta del script y los separamos 
    if not args.get('--gui',True):
        try:print('[>] Open GUI...',end='');GUI()
        except Exception as e:print('error')
    verbose = not all([args.get('-v',True),args.get('--verbose',True)])#guardamos el bool de  -v o --verbose en la variable verbose
    global osystem;osystem = sys.platform
    if verbose:print(f'[+] Run on: {osystem}')
    if verbose:print('[+] Verbose: All')
    elif args=={}:help();return None #si no hay argumentos corremos help
    if not args.get('--extensions',True):#si corremos -ext... mostramos un link con extensiones
        if verbose:print('[>] visit: https://en.wikipedia.org/wiki/List_of_Internet_top-level_domains')
        webbrowser.open('https://en.wikipedia.org/wiki/List_of_Internet_top-level_domains');return None
    elif not args.get('--languages',True) or not args.get('-l',True):printLanguages();return None#mostramos languages si --languages
    elif args.get('--install',None)=='modules':installModules();return None#corremos la instalacion si --install
    elif not args.get('--update',True):update()
    elif not args.get('-h',True) or not args.get('--help',True):help();return None#mostramos ayuda si -h
    if not args.get('--clear',True):clear()#limpiamos dir
        


   



    for option in args.keys():#set args 
        
        if option in ['--verbose','-v','gui']:pass

        elif option in ['-u','--url']:
            url = 'google' if args[option] == 'g' else args[option]
            if verbose:print(f'[+] Domain: {url}')
            
        elif option in ['-q','--query']:
            to_search = args[option]
            if verbose:print(f'[+] Args: {to_search}')

        elif option in ['-e','--extension']:
            domain = args[option]
            if verbose:print(f'[+] Extension: .{domain}')

        elif option in ['-r','--return']:
            returns = 'html' if args[option] == 'h' else 'link' if args[option] == 'l' else args[option]
            if verbose:print(f'[+] Returns: {returns}')

        elif option in ['-p','--print']:
            printit = True
            if verbose:print('[+] Print: All')

        elif option in ['-s','--save']:
            save = args[option]
            if verbose:print(f'[+] Save into: {save}')
            if not save:print('[e] Filename is empty, impossible to write in it')

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
            oib = True
            if verbose:print('[+] Open in browser: All')

        elif option in ['-o','--open']:
            openfile = True
            if verbose:print('[+] View file: True')

        else:#option doesnt match 
            if verbose:print(f'[-] Impossible to resolve {option}')

   
    if url == 'google':#search via google
        if verbose:print('[>] Searching via google... ',end='')#print status
        urls = googleSearch()# returns \n join(urls)     call a google search
        to_return = []#create a list that contains the links or html code
        if printit:txt="\n".join(urls);print(f'[+]urls:\n{txt}')#printit 
        if verbose:print('success')#status
        if returns == 'link' or returns=='links':to_return=urls#get the links returned by googleSearch
        elif returns == 'html':
            for a in urls:
                if verbose:print(f'[>] getting html ({a})... ',end='')
                try:
                    to_return.append(requests.get(a).text)#get the html of the links
                    if verbose:print('success')
                except Exception as e:
                    print('error')
                    print(f'[e] >> {e}')
                
            

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
    
