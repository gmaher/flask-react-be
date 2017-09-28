import token as tok
import password as pw
import numpy as np

secret = 'blah'

s = tok.generate_token(secret)
status = tok.token_is_valid(s,secret)
print "Token {} is valid? {}".format(s,status)

status = tok.token_is_valid(s,'monkey')
print "Token {} with secret {} is valid? {}".format(s,'monkey',status)

s = 'exp=nan&digest=11111'
status = tok.token_is_valid(s,secret)
print "Token {} is valid? {}".format(s,status)

s = 'exp=20000000000000000000000000000000000&digest=11111'
status = tok.token_is_valid(s,secret)
print "Token {} is valid? {}".format(s,status)

s = 'apapapapapapa'
status = tok.token_is_valid(s,secret)
print "Token {} is valid? {}".format(s,status)

s = 'exp=111111.111'
status = tok.token_is_valid(s,secret)
print "Token {} is valid? {}".format(s,status)

s = None
status = tok.token_is_valid(s,secret)
print "Token {} is valid? {}".format(s,status)


s = 'maggiesdogsucks!12'
s_h = pw.hash_password(s)
print "{} hashed to {}".format(s,s_h)

status = pw.pw_is_valid(s,s_h)
print "{} valid password for {}? {}".format(s,s_h,status)

s_h_2 = s_h.replace('0','')
status = pw.pw_is_valid(s,s_h_2)
print "{} valid password for {}? {}".format(s,s_h_2,status)

s = 'hurrr'
status = pw.pw_is_valid(s,s_h)
print "{} valid password for {}? {}".format(s,s_h,status)

s = -1
status = pw.pw_is_valid(s,s_h)
print "{} valid password for {}? {}".format(s,s_h,status)

s = '-1'
status = pw.pw_is_valid(s,s_h)
print "{} valid password for {}? {}".format(s,s_h,status)

s = np.nan
status = pw.pw_is_valid(s,s_h)
print "{} valid password for {}? {}".format(s,s_h,status)

s = None
status = pw.pw_is_valid(s,s_h)
print "{} valid password for {}? {}".format(s,s_h,status)
