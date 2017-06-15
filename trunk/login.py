import tornado.web
import hashlib
from dbproxy import *
import json

# return whether verify ok.
def doLoginVerifyKey(account,pwd,deviceid,verify):
	salt = '%s3x9g)=;eH4`uzYh%'
	m = hashlib.md5()
	m.update('loginAccount='+account+'&loginPassword='+pwd+'&deviceID='+deviceid+'&'+salt)
	v = m.hexdigest()
	print('v='+v)
	print('verify='+verify)
	if verify == v:
		return True
	else:
		return False

class LoginHandler(tornado.web.RequestHandler):
	def post(self):
		account 	= 	self.get_body_arguments('loginAccount')[0];
		password 	= 	self.get_body_arguments('loginPassword')[0];
		deviceid 	= 	self.get_body_arguments('deviceID')[0];
		verify 		= 	self.get_body_arguments('verifyKey')[0];
		print('\r\n---------- login info ---------------')
		print('loginAccount:' + account)
		print('loginPassword:' + password)
		print('deviceID:' + deviceid)
		print('verifyKey:' + verify)
# check verifyKey salt is
		print('-------------------------------------')
		if doLoginVerifyKey(account,password,deviceid,verify) == False:
			print('LoginVerifyKey fail')
			raise tornado.web.HTTPError(403)
		else:
			rep = None
			db_proxy = LiveDbProxyholder.get_dbproxy()
			db_query_result = db_proxy.login(account,password)
			if db_query_result[0] == False:
				print('login fail')
				rep = {'errcode':-1,'msg':'user name or passwd error'}
			else:
				print('login success')
				print(db_query_result[1])
				rep = {'errcode':0,'msg':json.dumps(db_query_result[1])}
			self.write(json.dumps(rep))