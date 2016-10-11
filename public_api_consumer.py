import urllib3

request_handle = urllib3.PoolManager()
data_handle = request_handle.request('GET', 'http://api.fixer.io/latest')
#JSON API for foreign exchange rates and currency conversion

print data_handle.status

if data_handle.status == 200:
	print data_handle.data
else:
	print 'request error!'