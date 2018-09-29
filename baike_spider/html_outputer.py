

class HtmlOutputer(object):
    def __init__(self):
        self.datas = []


    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    def output_html(self):
        fout = open('output.html','w')
        fout.write("<html>")
        fout.write("<body>")
        fout.write("<table>")
        for data in self.datas:
            fout.write("<tr>")
            fout.write("<td>%s</td>" % data['url'])
           #  print(data['url'])
            fout.write("<td>%s</td>" % data['title'])
          #   print(data['title'])
            fout.write("<td>%s</td>" % data['summary'].encode('gbk', 'ignore').decode("gbk"))    # 使用utf-8的话会因为一些特殊字符无法解码报错 头疼。。。
          #   print(data['summary'])
            fout.write("<tr>")
            fout.write("</tr>")
        fout.write("</table>")
        fout.write("</body>")
        fout.write("</html>")
        fout.close()
