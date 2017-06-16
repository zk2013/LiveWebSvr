import tornado.web
import json
import urllib
import urllib2
import copy

BANLI_HOME_HOT_URL = "https://m-api.banli.com/home/hot"

class LiveListHandler(tornado.web.RequestHandler):
	def post(self):
		rep = None
		banli_stream_cnt = 0
		banli_live_array = []
		banli_live_item = {}

		request = urllib2.Request(BANLI_HOME_HOT_URL, None)
		response = urllib2.urlopen(request)
		httpHead = response.read()
		content = json.loads(httpHead)
		if content["errcode"] == 0:
			data = content["data"]
			for one in data:
				one_data = one["data"]
				one_type = one["type"]
				if one_type == 11:
					continue
				for two in one_data:
					#print "--------------------"
					#print two["videoplay_url"]
					#print two["cover"]
					#print two["nickname"]
					#print two["screen_direction"]
					#print "--------------------\r\n"
					banli_live_item["coverPicUrl"] = two["cover"]
					banli_live_item["title"] = two["nickname"]
					banli_live_item["videoUrl"] = two["videoplay_url"]
					banli_live_item["videoHdUrl"] = two["videoplay_url"]
					banli_live_array.append(copy.deepcopy(banli_live_item))
					banli_stream_cnt = 	banli_stream_cnt + 1
			rep = {'errcode':0,'msg':'success','data':json.dumps(banli_live_array)}
		else:
			rep = {'errcode':content["errcode"],'msg':content["msg"]}
		print "--------------------"
		print "banli_stream_cnt ", banli_stream_cnt
		print "--------------------\r\n"
		print rep
		self.write(json.dumps(rep))
