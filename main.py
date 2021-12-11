import copy
import json
import process as app

import PySimpleGUI as sg
from PIL import Image as PILImage
from PIL import ImageTk
from tkinter import *
import io
from urllib import request
import requests
layout=[
    [sg.Text("MOVIE RECOMMENDATION",font='Arial 30')],
    [sg.HorizontalSeparator()]
]
response=requests.get('http://www.omdbapi.com/?apikey=6887c6&t=Toy+Story&y=1995')
#response2=request.get(response.)
jsonObject=response.json()

#movieInfo=jsonObject.load()


def getMovieTittle():
    result=[]
    f=open("u.item","rb")
    text="buffeeValue"
    while text!=None:
        text = f.readline()

        newText = text.decode('latin-1')
        if newText == "": break
        arr = newText.split('|')
        if(', The' in arr[1]):
            arr[1]='The '+arr[1].replace(", The",'')
        result.append(arr[1])

    return result

movieTittles=getMovieTittle()





def scrapeImage(tittle,year):
    #if(tittle[len(tittle)-5:len(tittle)-1]=='The'):


    titleParts=tittle.split()
    buffer=""
    pos=-1
    for i in titleParts:
        pos+=1
        buffer+=i
        if (pos!=len(titleParts)-1):
            buffer+="+"
    #return buffer


    response=requests.get('http://www.omdbapi.com/?apikey=6887c6&t='+buffer)
    movieInfo=response.json()
    #print(movieInfo)

    if("Error" in movieInfo or movieInfo["Poster"]=='N/A'):
        im=PILImage.open("img.png")
        #movieInfo=json.loads('{"Poster": "https://www.theprintworks.com/wp-content/themes/psBella/assets/img/film-poster-placeholder.png"}')
    else:
        response2=requests.get(movieInfo["Poster"])
        #print(response2.content)
        im=PILImage.open(io.BytesIO(response2.content))
    return im

buttonList=[]
#response2=requests.get(jsonObject["Poster"])
#img=PILImage.open(io.BytesIO(response2.content))
#movieTabe=sg.Table()*
def set_size(element, size):
    # Only work for sg.Column when `scrollable=True` or `size not (None, None)`
    options = {'width':size[0], 'height':size[1]}
    if element.Scrollable or element.Size!=(None, None):
        element.Widget.canvas.configure(**options)
    else:
        element.Widget.pack_propagate(0)
        element.set_size(size)

def getImageData(tittleRaw,first):                          # Need a tittle to work
    length=len(tittleRaw)
    title=tittleRaw[:length-7]
    year=tittleRaw[length-5:length-1]
    im=scrapeImage(title,year)
    im=im.resize((200,300),resample=PILImage.BICUBIC)
    if first:                     # tkinter is inactive the first time
        bio = io.BytesIO()
        im.save(bio, format="PNG")
        del im
        return bio.getvalue()
    image=ImageTk.PhotoImage(image=im)

    return image


def loadingMovie(movieId):                      # using ID instead of tittle
    movieName=movieId
    fileName=movieTittles[movieId]
    moviePoster=sg.Image(size=(200,300),data=getImageData(fileName,True))
    rateButton=sg.Button("Rate",key=movieId)
    buttonList.append(movieName)
    if len(fileName)>32:
        fileName=fileName[:32]
    movieCard=sg.Frame("",[
        [sg.Text(fileName)],
        [moviePoster],
        [rateButton]
    ])
    #moviePoster.update(data=image)
    return movieCard

def popMovieIn(layout,movie):                           # push movie cards in layout
    if(len(layout[len(layout)-1])<4):
        layout[len(layout)-1].append(movie)
    elif(len(layout[len(layout)-1])==4):
        layout.append([movie])



#movieListLayout.append([loadingMovie(2)])
#movieListLayout.append([loadingMovie(3)])


def CreateUserLayout():
    UserInfoLayout=[]
    personalInfoLayout=[
        [sg.Text("name"),sg.Input("your name")],
        [sg.Text('age'),sg.Input("eg 18")],
        [sg.Text("gender"),sg.Radio("Male","GENDER",True),sg.Radio("Female","GENDER",False)],
        [sg.Text("Ocupation"),sg.Combo(["other","academic/educator","artist",
	        "clerical/admin","college/grad student","customer service",
	        "doctor/health care","executive/managerial","farmer",
            "homemaker","K-12 student","lawyer",
	        "programmer","retired","sales/marketing",
	        "scientist","self-employed","technician/engineer",
	        "tradesman/craftsman","unemployed", "writer"],"programmer",key="Ocupation",readonly=True)],
        [sg.Text("ZIP Code"),sg.In("12345")],
        [sg.Button("Enter UserID")]
    ]
    personalInfo=sg.Frame("User Infomation",personalInfoLayout)
    geareLayout=[
        [sg.Checkbox("Action",False,key="1"),sg.Checkbox("Adventure",False,key="2")],
        [sg.Checkbox("Animation",False,key="3"),sg.Checkbox("Children's",False,key="4")],
        [sg.Checkbox("Comedy",False,key="5"),sg.Checkbox("Crime",False,key="6"),sg.Checkbox("Drama",False,key="8")],
        [sg.Checkbox("Fantasy",False,key="9"),sg.Checkbox("Film-Noir",False,key="10")],
        [sg.Checkbox("Documentary",False,key="7"),sg.Checkbox("Musical",False,key="12")],
        [sg.Checkbox("Mystery",False,key="13"),sg.Checkbox("Sci-fi",False,key="15")],
        [sg.Checkbox("Romance",False,key="14"),sg.Checkbox("Horror",False,key="11")],
        [sg.Checkbox("Thriller",False,key="16"),sg.Checkbox("War",False,key="17"),sg.Checkbox("Western",False,key="18")],
        [sg.Button("comfirm")]
    ]
    geara=sg.Frame("Geare",geareLayout)
    UserInfoLayout.append([personalInfo])
    UserInfoLayout.append([geara])
    userInfomation=sg.Frame("",UserInfoLayout,size=(300,600))

    return userInfomation

def makeMovieDisplay(movies):                               # a list of movie id
    global buttonList
    buttonList.clear()
    movieListLayout=[[]]
    #movieListLayout.append([loadingMovie(1),loadingMovie(2),loadingMovie(3),loadingMovie(4)])
    for e in movies:
        popMovieIn(movieListLayout,loadingMovie(e))
    #popMovieIn(movieListLayout,loadingMovie("made in abyss"))
    #popMovieIn(movieListLayout,loadingMovie("margaret thatcher"))
    #popMovieIn(movieListLayout,loadingMovie("clean bois"))
    #popMovieIn(movieListLayout,loadingMovie("Chicken"))
    #popMovieIn(movieListLayout,loadingMovie("Fuck"))

    bodyRecommend=sg.Column(movieListLayout,scrollable=True,size=(900,600))

    #load movies here
    return bodyRecommend




#set_size(bodyRecommend,(1000,600))
#bodyRecommend.set_size((1000,None))
layout.append([makeMovieDisplay([]),CreateUserLayout()])
def updateMovieDisplay(movies):
    layout=[
        [sg.Text("MOVIE RECOMMENDATION",font='Arial 30')],
        [sg.HorizontalSeparator()]
    ]
    #userinfo=copy.deepcopy(userInfomation)
    layout.append([makeMovieDisplay(movies),CreateUserLayout()])
    #window.close()
    window=sg.Window(title="hello world",layout=layout,margins=(10,20),finalize=True,size=(1200,700))
    return window


window = sg.Window(title="hello world",layout=layout,margins=(10,20),finalize=True,size=(1200,700))
model=app.process()
moviesSample=[1,2,3,4,5]
userID='0';
flag=False
while True:
    if(flag):
        window.close()
        moviesSample=model.recommend(int(userID))
        print(moviesSample)
        window=updateMovieDisplay(moviesSample)
    event,values=window.read()
    if(event==sg.WIN_CLOSED):
        window.close()
        break
    for b in buttonList:
        if(event==b):
            sg.popup(title=b)
    if(event=="Enter UserID"):
        userID = sg.popup_get_text("Enter User ID: ","UserId Input")
        flag=True


window.close()

