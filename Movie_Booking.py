import tkinter as tk              #This import for the Showing up Windows
import tkinter.ttk                #This import for the styling(designing)

screens = ["Screen 1 ", "Screen 2", "Screen 3", "Screen 4", "Screen 5", "Screen 6"]            
#List

movies = {"Horror"  : ["Annabelle", "Insideous", "Death of Me", "Conjuring","The Invisible Man"],
          "Action"  : ["Avengers End Game", "Spiderman:No Way Home", "Fast and Furious:Tokyo Drift","John Wick", "Venom"],
          "Drama"   : ["Joker", "Spotlight","Little Women", "The IrishMan", "A Star is Born"],
          "Comedy"  : ["The Rush Hour", "Johhny English", "Baby's Day Out", "Bossbaby", "Men in Black"],
          "Fiction" : ["Star Wars", "Annihilation", "Harry Potter", "Interstellar","The Martian"],
          "Romance" : ["The Fault in our Stars", "The Notebook", "The tourist", "Titanic","Crazy Rich Asians"]}
#Movies=Dictionary 

time = ["10:00", "10:45", "11:15", "11;40", "12:20", "13:00", "13:35", "14:10", "14:40","15:05", "15:35","16:00", "16:30", "15:00"]  
#Array

Seat_list = []          #Array
Seat_Selected = []      #Array

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Cinema Booking")
        self.createWidgets()
        
    
    def updateMovies(self, events=None):
        self.movieCombo['values'] = movies[self.genreCombo.get()]
    
    
    def createWidgets(self):
        headingLabel = tk.Label(self,text = "Cinema Seat Bookings", font = "Aries 12 bold")#main heading 
        headingLabel.grid(row=0, column=0, columnspan=5, padx=10, pady=10, stick="w")
        tkinter.ttk.Separator(self, orient="horizontal").grid(row=1, column=0, columnspan= 5, sticky="ew")
        day=tk.Frame(self)
        tk.Label(day, text="_______").pack()
        tk.Label(day, text="Today", font="Aries 10 underline").pack()#writing Today before genre of the movie
        tk.Label(day, text="").pack()
        day.grid(row=2, column=0, padx=10)

        tk.Label(self,text="Genre: ").grid(row=2, column=1, padx=(10,0))              #for selecting the genre of the movie
        self.genreCombo = tkinter.ttk.Combobox(self, width = 15, values = list(movies.keys()),state = "readonly")
        self.genreCombo.set("Select Genre")
        self.genreCombo.bind('<<ComboboxSelected>>', self.updateMovies)
        self.genreCombo.grid(row=2, column=2)
    
        tk.Label(self,text="Movie: ").grid(row=2, column=3, padx=(10,0))             #for selecting the movie in the selected genre
        self.movieCombo = tkinter.ttk.Combobox(width=15, state="readonly")
        self.movieCombo.bind('<<ComboboxSelected>>', self.createTimeButtons)
        self.movieCombo.set("Select Movie")
        self.movieCombo.grid(row=2,column=4, padx=(10,0))
        tkinter.ttk.Separator(self,orient="horizontal").grid(row=3, column=0, columnspan=5, sticky='ew')

    def createTimeButtons(self, event=None):
        tk.Label(self, text="Select Time Slot", font="Aries 11 bold underline").grid(row=4,column=2, columnspan=2 ,pady=5)                                                       #time selection in thos para(and making buttons to click the time slots)
        Time = tk.Frame(self)
        Time.grid(row=5, column=0, columnspan=5)
        for i in range(14):
            tk.Button(Time, text =time[i],command = self.seatSelection).grid(row = 4+i//7, column = i%7)

    def seatSelection(self):
        window = tk.Toplevel()
        window.title("Select your Seat")
        checkoutHeading = tk.Label(window, text = "Seat(s) Selection", font = "Aries 12")
        checkoutHeading.grid(row=0, column=0, columnspan=5, padx=10,pady=(10,0), sticky="w")

        infer = tk.Frame(window)
        infer.grid(row=1, column=0)
        tk.Label(infer, text='BLUE = SELECTED', fg='blue').grid(row=0, column=0, padx=10)
        tk.Label(infer, text='RED = BOOKED', fg='brown').grid(row=0, column=1, padx=10)
        tk.Label(infer, text='GREEN = AVAILABLE', fg='green').grid(row=0, column=2, padx=10)
        tkinter.ttk.Separator(window,orient="horizontal").grid(row=2, column=0, pady=(0,5), sticky='ew')

        w = tk.Canvas(window, width =500, height = 50)
        w.create_rectangle(10, 0 , 490 , 10, fill='black')
        w.grid(row=3, column=0)
        tk.Label(window,text="screens" ).grid(row=4, column=0, pady=(0,10))
        
        seats = tk.Frame(window)
        seats.grid(row=5, column=0)
        Seat_list.clear()
        Seat_Selected.clear()
        for i in range(4):
            temp=[]
            for j in range(15):
                but = tk.Button(seats, bd=2, bg='Green', activebackground='forestGreen',
                command=lambda x=i,y=j: self.selected(x,y))
                temp.append(but)
                but.grid(row=i, column=j, padx=5, pady=5)
            Seat_list.append(temp)
        tk.Button(window, text = "Book Seats", bg = 'black', fg = "white", command=self.bookseat).grid(row=6, column=0, pady=10)


    def selected(self,i,j):
        if  Seat_list[i][j]['bg']=='blue':
            Seat_list[i][j]['bg']=='green'
            Seat_list[i][j]['activebackground'] = "forestGreen"
            Seat_Selected.remove(i,j)
            return
        Seat_list[i][j]['bg'] = 'blue'
        Seat_list[i][j]['activebackground']='blue'
        Seat_Selected.append((i,j))

    def bookseat(self):
        for i in Seat_Selected:
            Seat_list[i[0]][i[1]]['bg'] = 'brown'
            Seat_list[i[0]][i[1]]['activebackground'] = 'brown'
            Seat_list[i[0]][i[1]]['relief'] = 'sunken'


app = Application()
app.mainloop()
