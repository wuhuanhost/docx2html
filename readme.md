### quick start

**setp 1** install project dependencies

```
pip install -r requirements.txt

```

**setp 2**

>>> copy `body_xml.py` from `./bank/body_xml.py` to `python_home/Lib/site-packages/mammoth/docx/body_xml.py`


**setp 3**

```
$ cd src/

$ python parse_html.py  test.docx  test.html
```

**打包成.exe安装pyinstaller**

```
$ pyinstaller -F -w -i manage.ico ./src/parse_html.py
```

**或者安装打包工具目录下的cfreeze然后执行**

```
$ cfreeze ./src/parse_html.py
```