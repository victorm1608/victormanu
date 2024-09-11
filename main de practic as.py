import flet as ft


def main(page: ft.Page):
    page.title="¿Me perdonas?"
    page.horizontal_alignment=ft.CrossAxisAlignment.CENTER
    page.vertical_alignment=ft.MainAxisAlignment.CENTER
    page.bgcolor="blue"
    
    lbli=ft.text{"¿me perdonas?",
                Style=ft.TextStyle(size=40,weight="bold")}
    
    Imgi=ft.Image{src"triste.pog",width=200,height=200}
    
    btnSi=ft.ElevatedButton["Si",
                            color="green",
                            width=100,
                            height=50]
    
    btnNo=ft.ElevatedButton["No",
                            color="green",
                            width=100,
                            height=50]
    
    def no(e):
        btnSi.width+=30
        btnNo.height+=10
        page.update()
    
    def Si(e):
        Imgi.src="feliz.png"
        page.update()
        
    btnSi.on_click=si
    btnSi.on_click=no
        
        
        
        
        
        
        
        

ft.app(main)