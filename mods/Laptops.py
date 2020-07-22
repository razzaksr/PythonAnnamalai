# access and manipulate resource members

'''import mods.Resource

mods.Resource.models['hp15y01']=36900'''

'''import mods.Resource as res

res.models['hp15y01']=40000
res.models['toshiba']=43000
res.models['vostro']={'brand':'dell','price':32700,'ram':2,'hdd':250}
res.report()
print(res.models['vostro']['brand'])'''


from mods.Resource import *
models['vostro']=34500
models['pavilion']=43500
models['imac']=98700
models['alian']=28700
models['probook']=29100
models['satellite']=39800
report()
filter(30000,40000)


