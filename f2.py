import requests

url = 'https://ss0.baidu.com/6ONWsjip0QIZ8tyhnq/it/u=523935819,4249262043&fm=58&bpow=1372&bpoh=864'
r = requests.get(url)
print(r.url)

with open('1.jpg','wb+') as f:
	f.write(r.content)

print('end')