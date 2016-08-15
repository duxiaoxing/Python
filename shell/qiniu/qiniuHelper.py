# encoding:utf-8

from qiniu import Auth,put_file, etag, urlsafe_base64_encode
import qiniu.config
import string
import sys

red_color ='\033[0;31m'
none_color = NC='\033[0m' # No Color

def upload(file_loacl_path):
    qiniu_blogresource_url = 'http://obsc9hxjk.bkt.clouddn.com/'
    #需要填写你的 Access Key 和 Secret Key
    access_key = 'ZOPviEuqiBC-4vyMYDiMAQjfsZkj33DuI-5z9pS8'
    secret_key = 'bMRIoxYZCVxo0o3xP3DH1xibENjoylIM1tM_CEA5'

    #构建鉴权对象
    qiniu_auth = Auth(access_key, secret_key)

    #要上传的空间
    bucket_name = 'blogresource'
    
    #上传到七牛后保存的文件名
    # key = 'architecture_2x.png';
    key = file_loacl_path.split('/')[-1]

    #生成上传 Token，可以指定过期时间等
    token = qiniu_auth.upload_token(bucket_name, key, 3600)
    ret, info = put_file(token, key, file_loacl_path)
    full_url = 'url:' + red_color + qiniu_blogresource_url + key + none_color
    return full_url


#要上传文件的本地路径
# localfile = '/Users/duxiaoxing/Desktop/architecture_2x.png'

if len(sys.argv) > 1:
    localfile = sys.argv[1]

print upload(localfile)


    






