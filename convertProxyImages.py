#!/usr/bin/python
# -*- coding: iso-8859-1 -*-

try:
    from Tkinter import *
    import tkFileDialog

except ImportError:
    raise ImportError,"The wxPython module is required to run this program."

try:
    import PIL.Image as mImg #you need python image librery
    import PIL.ImageOps as ImageOps
    from os import listdir, getcwd
    from os.path import isfile, join,splitext,abspath,exists
except ImportError:
    raise ImportError,"Necesitas varias de las librerias mas para poder correr el programa"

def convertImage( fullPathFileExt='', newSize=( 100, 100 ) ):
    '''
    string type fullPathFileExt: Here put the fullpath
    list type newSize : x y of 2D new image ej. (100,100)
    '''
    if isfile(fullPathFileExt):
        try:
            file, ext = splitext(fullPathFileExt)
            newNamefile = fullPathFileExt.replace(ext,'.proxy.png')
            img = mImg.open(fullPathFileExt)
            img = img.convert("RGBA")
            img.thumbnail(newSize)
            img.convert('RGB')
            a=img.save(newNamefile)
            varStatus.set('Se creo el proxy -->' + newNamefile)
        except IOError:
            varStatus.set('cannot convert -->' + fullPathFileExt)
            print("cannot convert", fullPathFileExt)

def convertToJpgProxy(path='O:\EMPRESAS\RIG_FACE2D\PERSONAJES\MILO\FACES',searchExt='png',newSize=(100,100)):
    '''
    string type path : Here put the path folder
    string type searchExt : suf extencion file. ej. 'png' or 'gif'
    list type newSize : x y of 2D new image ej. (100,100)
    '''
    def listFiles(fullPathFile):
        for f in listdir(fullPathFile):
                    fullPathFileExt = fullPathFile+f
                    file, ext = splitext(fullPathFileExt)
                    if ext == '.' + searchExt:
                        if isfile(fullPathFileExt) and (not '.proxy' in file):
                            convertImage(fullPathFileExt,newSize)
                        else:
                            print fullPathFileExt + ' --> ya existe.'

    path = abspath(path)
    if exists(path):
        print 'Comienza la conversion'
        varS.set('Comienza la conversion')
        directorios = {}
        dirs= [f for f in listdir(path) if not isfile(join(path, f))]#only list folders
        if dirs:
            print 'Convertira las imagenes en los subdirectorios.'
            varS.set('Convertira las imagenes en los subdirectorios.')
            for subdir in dirs:
                fullPathFile = path+'\\'+subdir+'\\'
                listFiles(fullPathFile)
        else:
            print 'Convertira las imagenes que estan en este directorio por que no contiene subdirectorios.'
            varS.set('Convertira las imagenes que estan en este directorio por que no contiene subdirectorios.')
            fullPathFile = path+'\\'
            listFiles(fullPathFile)
    else:
        print 'No es un directorio existente.'
        varS.set('No es un directorio existente.')

def askdirectory():
  dirname = tkFileDialog.askdirectory()
  if dirname:
    var.set(dirname)

def UserFileInput(status,name):
  optionFrame = Frame(root)
  optionLabel = Label(optionFrame)
  optionLabel["text"] = name
  optionLabel.pack(fill=BOTH, expand=0)
  text = ''
  var = StringVar(root)
  var.set(text)
  w = Entry(optionFrame, textvariable= var)
  w.pack(fill=BOTH, expand=0)
  optionFrame.pack(fill=BOTH, expand=0)
  return w, var

def Print_entry():

  path = convertToJpgProxy(str(var.get()),'png')
  return path

##def sel():
##   selection = "You selected the option " + str(var.get())


if __name__ == '__main__':
  root = Tk()
  root.title('Convierte a proxys')
##  tkvar = StringVar(root)
##  tkvar.set(1)
##  r1=Radiobutton(root, text="png", variable=tkvar, value=1,command=sel).pack( side = LEFT )
##  r2=Radiobutton(root, text="jpg", variable=tkvar, value=2, command=sel).pack( side = LEFT)
  w, var = UserFileInput("", "Directory")
  varS= StringVar(root)
  Label( root, textvariable=varS ).pack()
  varS.set('Ninguna proceso aun..',)

  varStatus = StringVar(root)
  status = Label( root, textvariable=varStatus ).pack()
  varStatus.set('...')

  dirBut = Button(root, text='Buscar', command = askdirectory).pack(side=LEFT)
  getBut = Button(root, text='Convertir a Proxy',width=50 ,command = Print_entry).pack(side=LEFT)
##  btnExit = Button(root, text='Salir', command=root.destroy).pack(side=LEFT)


  root.mainloop()