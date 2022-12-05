import tkinter as tk
import eazychart as ec
import hcacheclient as hc

def drawindex(app, canvas):
    width = 1500
    height = 750
    xoffset = 30
    yoffset = 40
    x = xoffset + 980
    y = yoffset + 50
    yscale = 39
    font="Calibri 11"
    mark = 14.07
    pricescale = 0.01
    markstr = format(mark,".2f")
    canvas.create_text(x,y,fill="darkblue",font=font, text=markstr)
    y += yscale
    mark -= pricescale
    markstr = format(mark,".2f")
    canvas.create_text(x,y,fill="darkblue",font=font, text=markstr)  
    y += yscale
    mark -= pricescale
    markstr = format(mark,".2f")    
    canvas.create_text(x,y,fill="darkblue",font=font, text=markstr)  
    y += yscale
    mark -= pricescale
    markstr = format(mark,".2f")    
    canvas.create_text(x,y,fill="darkblue",font=font, text=markstr)
    y += yscale
    mark -= pricescale    
    markstr = format(mark,".2f")    
    canvas.create_text(x,y,fill="darkblue",font=font, text=markstr)
    y += yscale
    mark -= pricescale    
    markstr = format(mark,".2f")  
    canvas.create_text(x,y,fill="darkblue",font=font, text=markstr)
    y += yscale
    mark -= pricescale    
    markstr = format(mark,".2f") 
    canvas.create_text(x,y,fill="darkblue",font=font, text=markstr)
    y += yscale
    mark -= pricescale    
    markstr = format(mark,".2f") 
    canvas.create_text(x,y,fill="darkblue",font=font, text=markstr)
    y += yscale
    mark -= pricescale    
    markstr = format(mark,".2f")  
    canvas.create_text(x,y,fill="darkblue",font=font, text=markstr)
    y += yscale
    mark -= pricescale    
    markstr = format(mark,".2f") 
    canvas.create_text(x,y,fill="darkblue",font=font, text=markstr)
    y += yscale
    mark -= pricescale    
    markstr = format(mark,".2f")  
    canvas.create_text(x,y,fill="darkblue",font=font, text=markstr)
    y += yscale
    mark -= pricescale    
    markstr = format(mark,".2f") 
    canvas.create_text(x,y,fill="darkblue",font=font, text=markstr)
    y += yscale
    mark -= pricescale    
    markstr = format(mark,".2f")  
    canvas.create_text(x,y,fill="darkblue",font=font, text=markstr)
    y += yscale
    mark -= pricescale    
    markstr = format(mark,".2f")  
    canvas.create_text(x,y,fill="darkblue",font=font, text=markstr)
    y += yscale
    mark -= pricescale    
    markstr = format(mark,".2f")  
    canvas.create_text(x,y,fill="darkblue",font=font, text=markstr)    
    y += yscale
    mark -= pricescale    
    markstr = format(mark,".2f")  
    canvas.create_text(x,y,fill="darkblue",font=font, text=markstr)  
    
def drawstatus(canvas):
    xoffset = 30
    yoffset = 40
    x = xoffset + 60
    y = yoffset + 13
    canvas.create_text(x,y,fill="black",font="Calibri 10", text="American Airlines", justify=tk.LEFT)  

def drawbars(canvas,df):
    xoffset = 30
    yoffset = 40
    x1 = xoffset
    x2 = xoffset+11
    y1 = yoffset+50
    y2 = yoffset+60
    
    count = 330
    max = 14.07
    while (count < 330+55):
        time = df.iat[count,0]
        #print(df.iat[count,3])
        #print(df.iat[count,4])      
        open = df.iat[count,3]
        close = df.iat[count,4]        
        x1 = xoffset + ((count-330) * 16)
        x2 = x1+11
        y1 = yoffset+(((open-max)*100)*37)
        y2 = yoffset+(((close-max)*100)*37)
        print(time, open,close)
        #print(y1,y2)
        #y1 = 80
        #y2 = 100
        canvas.create_rectangle(x1, y1, x2, y2, fill="green", width=0)  
        count += 1        
    

def drawapp(app):
    width = 1500
    height = 750
    canvas = tk.Canvas(app.window, width=width, height=height,bg="white") 
    drawtoolbar(app,canvas)
    xoffset = 30
    yoffset = 40
    x1 = xoffset
    x2 = xoffset+1000
    y1 = yoffset+0
    y2 = yoffset+650
    canvas.create_rectangle(x1, y1, x2, y2, outline="#05f", fill="white")    
    df = hc.get_df("AAL","2022-10-24")
    drawindex(app,canvas) 
    drawbars(canvas,df)    
    drawstatus(canvas)    
    canvas.pack()

def drawchart(ssp):
    canvas.create_line(55, 85, 155, 85, 105, 180, 55, 85)
    canvas.pack()

def drawtoolbar(app,canvas):
    xoffset = 0
    yoffset = 40
    x1 = xoffset
    x2 = xoffset+29
    y1 = yoffset+0
    y2 = yoffset+650
    canvas.create_rectangle(x1, y1, x2, y2, fill="grey", width=0)  

# --------- ---------
        
app = ec.App()
app.window.geometry('1500x750+25+25')
app.window.title('eazychart')
drawapp(app)
app.window.mainloop()