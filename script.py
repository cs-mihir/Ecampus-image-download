import urllib2
for i in range(1,50):
	url = 'https://ecampus.daiict.ac.in/webapp/intranet/StudentPhotos/'
	ext = '2015010'+str(i)+'.jpg'
	if i < 10:
		ext = '20150100'+str(i)+'.jpg'
	url += ext
	#Here you can specify your url also from where you want to download jpg file
	file = open(str(i)+'.jpg','wb')
	file.write(urllib2.urlopen(url).read())
	file.close()
	print 'Image of '+str(i)+' downloaded'
print 'Success'
