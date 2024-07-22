import flet as ft

filtro = ft.InputFilter(allow=True, regex_string=r"[0-9.]", replacement_string="")

def main(page: ft.Page):
    page.title = "Calculadora de Juros"
    page.theme_mode = ft.ThemeMode.SYSTEM

    caixaj = ft.TextField(label="Juros", expand=True, keyboard_type='NUMBER', input_filter=filtro)
    caixac = ft.TextField(label="Capital", expand=True, keyboard_type='NUMBER', input_filter=filtro)
    caixai = ft.TextField(label="Taxa de Juros", expand=True, keyboard_type='NUMBER', input_filter=filtro)
    caixat = ft.TextField(label="Tempo", expand=True, keyboard_type='NUMBER', input_filter=filtro)
    txt_agradecimento = ft.Text(value=f"Obrigado a todos que baixaram e usaram a {page.title} de Tiago Apps! Estou muito grato pelo seu apoio.", expand=True, size=20)
    txt_agradecimento2 = ft.Text(value=f"Tem alguma ideia de como tornar a {page.title} ainda melhor? Deixe-me saber enviando um feedback!", expand=True, size=20)
    versao = ft.Text(value="Versão: 1.0.0", expand=True, size=20)
    imesano = ft.Dropdown(width=110, options=[
        ft.dropdown.Option("% ao Mês"),
        ft.dropdown.Option("% ao Ano")
        ], expand=False)
    tmesano = ft.Dropdown(width=110, options=[
        ft.dropdown.Option("Mês(es)"),
        ft.dropdown.Option("Ano(s)"),
        ], expand=False)

    def limpar(e):
        caixaj.value = ""
        caixac.value = ""
        caixai.value = ""
        caixat.value = ""
        imesano.value = None
        tmesano.value = None
        resultado.value = "0"
        page.update()
        pass

    def calcular(e):
        if page.route == "/juros":
            c = caixac.value
            i = caixai.value
            t = caixat.value
            c = float(c)
            i = float(i)
            t = float(t)
            if imesano.value == "% ao Ano":
                if tmesano.value == "Mês(es)":
                    resultado.value = (c * (i / 12) * t) / 100
                elif tmesano.value == "Ano(s)":
                    resultado.value = (c * i * t) / 100
            elif imesano.value == "% ao Mês":
                if tmesano.value == "Mês(es)":
                    resultado.value = (c * i * t) / 100
                elif tmesano.value == "Ano(s)":
                    resultado.value = (c * (i * 12) * t) / 100
            resultado.value = f"Juros: R${resultado.value:.2f}\nMontante: R${resultado.value + c}"
        elif page.route == "/capital":
            j = caixaj.value
            i = caixai.value
            t = caixat.value
            j = float(j)
            i = float(i)
            t = float(t)
            if imesano.value == "% ao Ano":
                if tmesano.value == "Mês(es)":
                    resultado.value = f"R${(j * 100) / ((i / 12) * t):.2f}"
                elif tmesano.value == "Ano(s)":
                    resultado.value = f"R${(j * 100) / (i * t):.2f}"
            if imesano.value == "% ao Mês":
                if tmesano.value == "Mês(es)":
                    resultado.value = f"R${(j * 100) / (i * t):.2f}"
                elif tmesano.value == "Ano(s)":
                    resultado.value = f"R${(j * 100) / ((i * 12) * t):.2f}"
        elif page.route == "/tax_juros":
            c = caixac.value
            j = caixaj.value
            t = caixat.value
            c = float(c)
            j = float(j)
            t = float(t)
            resultado.value = f"{(j * 100) / (c * t):.2f}"
            resultado.value = float(resultado.value)
            if tmesano.value == "Ano(s)":
                if resultado.value < 1:
                    resultado.value = f"{resultado.value * 12:.2f}% ao Mês"
                else:
                    resultado.value = f"{resultado.value:.2f}% ao Ano"
            if tmesano.value == "Mês(es)":
                if resultado.value >= 12:
                    resultado.value = f"{resultado.value / 12:.2f}% ao Ano"
                else:
                    resultado.value = f"{resultado.value:.2f}% ao Mês"
        elif page.route == "/tempo":
            c = caixac.value
            i = caixai.value
            j = caixaj.value
            c = float(c)
            i = float(i)
            j = float(j)
            resultado.value = f"{(j * 100) / (c * i):.2f}"
            resultado.value = float(resultado.value)
            if imesano.value == "% ao Ano":
                if resultado.value < 1:
                    resultado.value = f"{resultado.value * 12:.2f} Mês(es)"
                else:
                    resultado.value = f"{resultado.value:.2f} Ano(s)"
            if imesano.value == "% ao Mês":
                if resultado.value >= 12:
                    resultado.value = f"{resultado.value / 12:.2f} Ano(s)"
                else:
                    resultado.value = f"{resultado.value:.2f} Mês(es)"
        pass
        page.update()
    pass

    resultado = ft.Text(value="0", size=20, text_align=ft.TextAlign.CENTER)
    btn_calcular = ft.ElevatedButton(text="Calcular", on_click=calcular, expand=True)
    btn_limpar = ft.ElevatedButton(text="Limpar", on_click=limpar, expand=True)
    doe = ft.Text(value="tiagogomesdasilva283@gmail.com", expand=True, size=20)
    btn_votar = ft.IconButton(icon=ft.icons.ARROW_BACK, on_click=lambda _: page.go('/'))
    
    def rota(e: ft.RouteChangeEvent):

        page.views.clear()

        page.views.append(
            ft.View(
                route='/',
                controls=[
                    ft.ElevatedButton(text="Juros", icon=ft.icons.ATTACH_MONEY, height=50, width=300, on_click=lambda _: page.go('/juros')),
                    ft.ElevatedButton(text="Capital", icon=ft.icons.LOCAL_ATM, height=50, width=300, on_click=lambda _: page.go('/capital')),
                    ft.ElevatedButton(text="Taxa de Juros", icon=ft.icons.PERCENT, height=50, width=300, on_click=lambda _: page.go('/tax_juros')),
                    ft.ElevatedButton(text="Tempo", icon=ft.icons.ACCESS_TIME,height=50, width=300, on_click=lambda _: page.go('/tempo')),
                    ft.ElevatedButton(text="Mais", icon=ft.icons.MORE_OUTLINED,height=50, width=300, on_click=lambda _: page.go('/mais')),
                    ft.ElevatedButton(text="Noidades", icon=ft.icons.NEWSPAPER,height=50, width=300, on_click=lambda _: page.go('/noidades'))
                ],
                vertical_alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            )
        )

        if page.route == '/juros':
            page.views.append(
            ft.View(
                route='/juros',
                controls=[
                    ft.Text(value="", size=10),
                    ft.Row([btn_votar, caixac]),
                    ft.Row([caixai, imesano]),
                    ft.Row([caixat, tmesano]),
                    ft.Row([btn_calcular, btn_limpar]),
                    ft.Row([resultado], ft.MainAxisAlignment.CENTER)
                ],
                vertical_alignment=ft.MainAxisAlignment.START,
                horizontal_alignment=ft.MainAxisAlignment.CENTER
            )
        )
            
        elif page.route == '/capital':
            page.views.append(
            ft.View(
                route='/capital',
                controls=[
                    ft.Text(value="", size=10),
                    ft.Row([btn_votar, caixaj]),
                    ft.Row([caixai, imesano]),
                    ft.Row([caixat, tmesano]),
                    ft.Row([btn_calcular, btn_limpar]),
                    ft.Row([resultado], ft.MainAxisAlignment.CENTER)
                ],
                vertical_alignment=ft.MainAxisAlignment.START,
                horizontal_alignment=ft.MainAxisAlignment.CENTER
            )
        )
            
        elif page.route == '/tax_juros':
            page.views.append(
            ft.View(
                route='/tax_juros',
                controls=[
                    ft.Text(value="", size=10),
                    ft.Row([btn_votar, caixaj]),
                    ft.Row([caixac]),
                    ft.Row([caixat, tmesano]),
                    ft.Row([btn_calcular, btn_limpar]),
                    ft.Row([resultado], ft.MainAxisAlignment.CENTER)
                ],
                vertical_alignment=ft.MainAxisAlignment.START,
                horizontal_alignment=ft.MainAxisAlignment.CENTER
            )
        )
            
        elif page.route == '/tempo':
            page.views.append(
            ft.View(
                route='/tempo',
                controls=[
                    ft.Text(value="", size=10),
                    ft.Row([btn_votar, caixaj]),
                    ft.Row([caixac]),
                    ft.Row([caixai, imesano]),
                    ft.Row([btn_calcular, btn_limpar]),
                    ft.Row([resultado], ft.MainAxisAlignment.CENTER)
                ],
                vertical_alignment=ft.MainAxisAlignment.START,
                horizontal_alignment=ft.MainAxisAlignment.CENTER
            )
        )

        elif page.route == '/mais':
            page.views.append(
            ft.View(
                route='/mais',
                controls=[
                    ft.Text(value="", size=10),
                    ft.Row([btn_votar, ft.Text(value="Agradecimentos:", expand=True, size=20)]),
                    ft.Divider(thickness=3),
                    ft.Row([txt_agradecimento]),
                    ft.Row([txt_agradecimento2]),
                    ft.Divider(thickness=3),
                    ft.Row([versao]),
                    ft.Divider(thickness=3),
                    ft.Row([ft.Text("Por Favor apoie o trabalho da Tiago Apps com uma doação(via Pix)!", expand=True, size=20)]),
                    ft.Row([ft.SelectionArea(content=doe)])
                ],
                vertical_alignment=ft.MainAxisAlignment.START,
                horizontal_alignment=ft.MainAxisAlignment.START
            )
        )
            
        elif page.route == '/noidades':
            page.views.append(
            ft.View(
                route='/noidades',
                controls=[
                    ft.Text(value="", size=10),
                    ft.Row([btn_votar, ft.Text("Noidades:", size=20)]),
                    ft.Divider(thickness=3),
                    ft.Row([ft.Text(" •Criação do aplicativo", expand=True, size=20)]),
                    ft.Row([ft.Text("Mais embreve...", expand=True, size=20)]),
                ],
                vertical_alignment=ft.MainAxisAlignment.START,
                horizontal_alignment=ft.MainAxisAlignment.START,
            )
        )
            
        page.update()

    def view_pop(e: ft.ViewPopEvent):
        page.views.pop()
        top_view: ft.view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = rota
    page.on_view_pop = view_pop
    page.go(page.route)

ft.app(target=main)
