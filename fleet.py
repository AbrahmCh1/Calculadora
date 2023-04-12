import flet as ft
import math


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
            print(txt.value)
            for elem in st: 
                if elem == "*":
                    mult_or_div= 0
                elif elem =="/":
                    mult_or_div= 1
            ns=[]
            if data =="%":
                for elem in st:
                    if elem=="*" or elem =="/":
                        break
                    ns.append(elem)
                for elem in st:
                    if elem == "*" or elem =="/" or elem =="%":
                        break
                    st.pop(0)

                st.pop()


            if st[0]=="*" or st[0]=="/":
                st.pop(0)

            s=len(st)

            if s==1:
                st.insert(0,"0")
                st.insert(0,".")
            elif s==2:
                st.insert(0,".")
            elif s>=3:
                st.insert(s-2,".")


            if mult_or_div==0:
                st.insert(0,"*")
            elif mult_or_div==1:
                st.insert(0,"/")

            s=len(st)
            for i in range(s):
                ns.append(st[i])

            txt.value = ns

    txt = ft.TextField(
        read_only=True,
        border_color="#060606",
        text_style=ft.TextStyle(size=20, color="#f6f6f6"),
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
                ft.ElevatedButton(text="=", bgcolor="#fe9505", color = "#f6f6f6",data="=", on_click=keyboard),
            ]
        ),
    )


ft.app(target=main)
