import requests

def get_url():
	url = 'http://www.baidu.com'
	r = requests.get(url)
	return r

def file_put():
	g = get_url()
	t = 'a.txt'
	with open(t, 'w', encoding=g.encoding, errors='ignore') as f:
		f.write(g.text)
		return g.url


if __name__ == "__main__":
	print(file_put())