def myxml(tagname, content=' ',**kwargs):
    attr = ' '.join([f' {key} = {value} '
                    for key,value in kwargs.items()])
    print(f' < {tagname} {attr}> {content} <\{tagname}>')

myxml( tagname= 'fp',content='ddjjdjjd', a=1,b=6)