from bs4 import BeautifulSoup
import requests
from type.String import *
from type.List import *


class HTMLAnalyzer:
    def __init__(self):
        self.soup = None

        self.text_analyze = []
        self.file_analyze = []
        self.url_page = []

    def addText(self, text: String):
        self.text_analyze.append(text.value)

    def addUrl(self, url: String):
        self.url_page.append(url.value)

    def startAnalyzeText(self):
        self.soup = BeautifulSoup(self.text_analyze[-1], 'html.parser')

        return String(Token(STR, self.soup.prettify()))

    def startAnalyzeUrl(self):
        page = requests.get(self.url_page[-1])
        self.soup = BeautifulSoup(page.text, 'html.parser')

        return String(Token(STR, self.soup.prettify()))

    def getP(self):
        page = requests.get(self.url_page[-1])
        self.soup = BeautifulSoup(page.text, 'html.parser')
        tag_list = []
        for tag in self.soup.find_all(attrs={"class": "text"}):
            tag_list.append(String(Token("STR", str(tag))))
        return List(tag_list)

    def findAll(self, tag_name: String, class_name=None, id_name=None):
        page = requests.get(self.url_page[-1])
        self.soup = BeautifulSoup(page.text, 'html.parser')
        tag_list = []
        if class_name is None and id_name is None:
            for tag in self.soup.find_all(tag_name.value):
                tag_list.append(String(Token("STR", str(tag))))
        elif class_name is None:
            for tag in self.soup.find_all(tag_name.value, {'id': id_name.value}):
                tag_list.append(String(Token("STR", str(tag))))
        elif id_name is None:
            for tag in self.soup.find_all(tag_name.value, {'class': class_name.value}):
                tag_list.append(String(Token("STR", str(tag))))
        else:
            for tag in self.soup.find_all(tag_name.value, {'class': class_name.value, 'id': id_name.value}):
                tag_list.append(String(Token("STR", str(tag))))

        return List(tag_list)

    def findByClass(self, class_name):
        page = requests.get(self.url_page[-1])
        self.soup = BeautifulSoup(page.text, 'html.parser')
        tag_list = []

        for tag in self.soup.find_all(attrs={'class': class_name.value}):
            tag_list.append(String(Token("STR", str(tag))))

        return List(tag_list)

    def findByAttr(self, attr: String, value=None):
        page = requests.get(self.url_page[-1])
        self.soup = BeautifulSoup(page.text, 'html.parser')
        tag_list = []
        if value is None:
            all_tags = self.soup.find_all()

            for tag in all_tags:
                if tag.has_attr(attr.value):
                    tag_list.append(String(Token("STR", str(tag))))
        else:
            for tag in self.soup.find_all(attrs={attr.value: value.value}):
                tag_list.append(String(Token("STR", str(tag))))

        return List(tag_list)


    def findById(self, id_name):
        page = requests.get(self.url_page[-1])
        self.soup = BeautifulSoup(page.text, 'html.parser')
        return String(Token("STR", str(self.soup.find_all(attrs={'id': id_name.value})[0])))

