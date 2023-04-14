#Código ejemplo base de flet
#Editor: Abraham Chávez

import flet as ft
import math

def suma(st):
           
            base= ["/","1","0","0",")"]
            propina=[]
            symb= []
            i=0
            for elem in st:
            
                i+= 1
                if elem == "*" or elem =="/" or elem =="%" or elem =="+" or elem =="-":
                    if elem =="+" or elem =="-":
                        st[i-1] = "*" 
                        propina.insert(0,elem)
                        st.insert(i,"(")

                    symb.append(elem)
                    st.insert(i,"(")
                    st.pop()
                    st.append(")")
                    break   
                elif elem != "*" or elem != "/" or elem != "%" or elem != "+" or elem != "-":
                    propina.append(elem)

            for i in range(5):
                st.append(base[i])

            if symb[0] == "+" or symb[0] == "-":
                for i in range(len(propina)):
                    st.append(propina[i])
            return(st)

def mult(st):
    base= ["/","1","0","0"]
    i=0
    for elem in st:
            
            i+= 1
            if elem == "*" or elem =="/" or elem =="%":
                st.insert(i,"(")
                st.pop()
                st.append(")")
                break   
    for i in range(4):
            st.append(base[i])
               

def main(page: ft.Page):
    page.title = "Calculator"
    result = ft.Text(value="0")
    page.window_width = 320
    page.window_height = 370
    page.window_resizable = False
    page.window_frameless=True
    page.bgcolor = "#060606"
    

    widthscreen = page.window_width

    def keyboard(e):
        data = e.control.data
        if data in ["1","2","3","4","5","6","7","8","9","0",".","+","-","*","/","%"]:
            txt.value = str(txt.value) + str(data)
            page.update()   

        if data == "=":
            txt.value = str(eval(txt.value))
            page.update()

        if data == "c":
            txt.value= ""
            page.update()    

        if data == "e":
            st= list(txt.value)
            

            st.pop()
            txt.value= "".join(map(str,st))
            page.update()

        if data =="%":
             st= list(txt.value)
             for elem in st:
                if elem == "*" or elem =="/":
                     mult(st)
                     break
      
                elif elem == "+" or elem =="-":
                    suma(st)
                    break
                else:
                     txt.value = ["Error"]
             txt.value= "".join(map(str,st))
             txt.value = str(eval(txt.value))
             page.update()

    txt = ft.TextField(
        read_only=False,
        
        border_color="#a3a3a3",
        border_width=3.2,
        ##Make border with circular corners
        border_radius= 15,
        text_style=ft.TextStyle(size=20, color="#f6f6f6", font_family="Swiss 7"),
        text_align= ft.TextAlign.RIGHT,
        
    )


    page.add(
            ft.ResponsiveRow([
                ft.WindowDragArea(
                ft.Container(
                    width=widthscreen,
                    padding= 5,
                )
                                )
                ]),    
    txt,
        
        ft.Row(
            controls=[
                ft.ElevatedButton(text="AC", expand= 1, bgcolor="#a3a3a3", color = "#060606",data="c", on_click=keyboard),
                
                ft.ElevatedButton(text="%",expand=1, bgcolor="#a3a3a3", color = "#060606", data="%", on_click=keyboard),
                ft.ElevatedButton(text="/",expand=1, bgcolor="#a3a3a3", color = "#060606", data="/", on_click=keyboard),
                ft.IconButton(icon=ft.icons.ARROW_BACK_IOS_NEW_ROUNDED, expand=1, tooltip="Erase", icon_color="f6f6f6", data="e", on_click=keyboard ),
            ]
        ),
        ft.Row(
            controls=[
                ft.ElevatedButton(text="7",expand=1, color="#f6f6f6", bgcolor="#313131", data="7", on_click=keyboard),
                ft.ElevatedButton(text="8",expand=1, color="#f6f6f6", bgcolor="#313131", data="8", on_click=keyboard),
                ft.ElevatedButton(text="9",expand=1, color="#f6f6f6", bgcolor="#313131", data="9", on_click=keyboard),
                ft.ElevatedButton(text="X",expand=1, bgcolor="#fe9505", color = "#f6f6f6", data="*", on_click=keyboard),
            ]
        ),
        ft.Row(
            controls=[
                ft.ElevatedButton(text="4",expand=1, color="#f6f6f6", bgcolor="#313131", data="4", on_click=keyboard),
                ft.ElevatedButton(text="5",expand=1, color="#f6f6f6", bgcolor="#313131", data="5", on_click=keyboard),
                ft.ElevatedButton(text="6",expand=1, color="#f6f6f6", bgcolor="#313131", data="6", on_click=keyboard),
                ft.ElevatedButton(text="-",expand=1, bgcolor="#fe9505", color = "#f6f6f6", data="-", on_click=keyboard),
            ]
        ),
        ft.Row(
            controls=[
                ft.ElevatedButton(text="1",expand=1, color="#f6f6f6", bgcolor="#313131", data="1", on_click=keyboard),
                ft.ElevatedButton(text="2",expand=1, color="#f6f6f6", bgcolor="#313131", data="2", on_click=keyboard),
                ft.ElevatedButton(text="3",expand=1, color="#f6f6f6", bgcolor="#313131", data="3", on_click=keyboard),
                ft.ElevatedButton(text="+",expand=1, bgcolor="#fe9505", color = "#f6f6f6", data="+", on_click=keyboard),
            ]
        ),
        ft.Row(
             controls=[
                ft.ElevatedButton(text="0",expand=2, color="#f6f6f6", bgcolor="#313131", data="0", on_click=keyboard),
                ft.ElevatedButton(text=".", color="#f6f6f6", bgcolor="#313131", data=".", on_click=keyboard),
                ft.ElevatedButton(text="=", bgcolor="#fe9505", color = "#f6f6f6",data="=", on_click=keyboard ),
            
                
            ]
        ),
    )



ft.app(target=main)
