# from flet import TextField,Column,Text,ElevatedButton,Row,app,AppView
# from flet import Page as pg
import flet as ft
def main(page: ft.Page):
    ft.Page.title = 'Program'
    page.window_width = 500    # window's width is 200 px
    page.window_height = 400      # window's height is 200 px
    page.window_resizable = False  # window is not resizable
    page.update()
    cost_per_cloth = ft.TextField(label="قیمت هر لباس", autofocus=True,tooltip='وارد کردن هزینه تولید یک لباس',icon='CREATE')
    desired_profit = ft.TextField(label="سود لازم در هفته",tooltip='در هفته حداقل چقدر باید به سود کنید؟',icon='ATTACH_MONEY')
    selling_price_percent = ft.TextField(label="درصد سود",tooltip='چه مقدار سود قصد افزودن به قیمت لباس دارید؟(قیمت فروش)',icon='PERCENT')
    calc = ft.Column()
    

    def btn_click(e):
        if cost_per_cloth.value != '' and desired_profit.value != '' and selling_price_percent.value != '':
            selling_price = int(cost_per_cloth.value) + (int(cost_per_cloth.value) * int(selling_price_percent.value) / 100)
            if (int(selling_price) - int(cost_per_cloth.value)) == 0:
                calc.controls.append(ft.Text('نمیشه به صفر تقسیم کرد'))
                page.update()
            else:
                minimum_production = int(desired_profit.value) / (int(selling_price) - int(cost_per_cloth.value))
            
                calc.controls.append(ft.Text(f"حداقل مقدار فروش لباس در یک هفته : {minimum_production}"))
                calc.controls.append(ft.Text(f"قیمت فروش هر لباس: {int(cost_per_cloth.value) + (int(cost_per_cloth.value) * int(selling_price_percent.value) / 100)+int(cost_per_cloth.value)}"))
                cost_per_cloth.value = ""
                desired_profit.value = ""
                selling_price_percent.value = ""
                page.update()
                cost_per_cloth.focus()
                
        else:
            calc.controls.append(ft.Text(f"لطفا تمامی اطلاعات را وارد کنید"))
            page.update()
            cost_per_cloth.focus()
    def clss(ee):
        calc.controls.clear()
        page.update()

    page.add(
        cost_per_cloth,
        desired_profit,
        selling_price_percent,
        ft.Row(
            controls=[
                ft.ElevatedButton("محاسبه", on_click=btn_click,icon='CALCULATE'),
                ft.ElevatedButton("پاک کن", on_click=clss,right='right',icon='DELETE_ROUNDED')
            ]
        ),
        calc,
    )

ft.app(target=main, view=ft.AppView.WEB_BROWSER)