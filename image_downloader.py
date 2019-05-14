import urllib.request as req
from collections import defaultdict

link_count = 0
name_count_dict = defaultdict(int)
with open("image_links.txt","r") as links_file:
	for link in links_file:
		print(link)
		name_start = len('https://www.wga.hu/detail/g/')
		name_end = name_start + link[name_start:].find('/')
		artist_name = link[name_start:name_end]
		name_count_dict[artist_name] += 1
		img_name = artist_name + '_' + str(name_count_dict[artist_name])
		print(img_name)
		req.urlretrieve(link, img_name + '.jpg')
		link_count += 1
		if (link_count == 2):
			break