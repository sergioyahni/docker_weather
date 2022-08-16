from datetime import date


class Html:
    content: str
    today = date.today().strftime("%B %d, %Y")

    def __init__(self):
        self.head = """<html lang="en"><head><meta charset="UTF-8"><meta http-equiv="X-UA-Compatible" 
        content="IE=edge"><meta name="viewport" content="width=device-width, initial-scale=1.0"><style>html body div 
        h1 h2 h3 p {font-family: Arial, Helvetica, sans-serif;}p{color: rgb(30, 53, 6);}h2{color: blueviolet;}th,
        td{padding: 15px;}.bold {font-weight: 900;}.page {position: relative; left: 
        80px;}</style><title>Document</title></head><body><div class="page"> """
        self.footer = """</div></body></html>"""
        self.content = str()

    def body(self, data, **kwargs):
        self.content = f"""<h2>Forecast for &nbsp;<spam>{self.today}</spam></h2><p><spam 
        class="bold">Minimum</spam>&nbsp;<spam>{kwargs['min']}C</spam></spam><p><spam 
        class="bold">Maximum</spam>&nbsp;<spam>{kwargs['max']} C</spam></spam><p><spam class="bold">Sun 
        rises:</spam>&nbsp;<spam>{kwargs['sunrise'][11:]}</spam></p><p><spam class="bold">Sun Sets: 
        </spam>&nbsp;<spam>{kwargs['sunset'][11:]}</spam></p><hr><h2>What can you expect?</h2><table 
        style="width:33%"><tr><th>Date</th><th>Min</th><th>Max</th><th>Sunrise</th><th>Sunset</th></tr>"""

        for index, item in data.iterrows():
            self.content += f"""<tr><td>{item['time']}</td><td>{item['temperature_min']} C</td>
            <td>{item['temperature_max']} C</td><td>{item['sunrise'][11:]}</td><td>{item['sunset'][11:]}</td></tr>"""

        return self._conclude()

    def _conclude(self):
        return self.head + self.content + self.footer


if __name__ == "__main__":
    doc = Html()
    s = doc.body(min='23', max='33', sunrise='6:30', sunset='18:30')
    print(s)
