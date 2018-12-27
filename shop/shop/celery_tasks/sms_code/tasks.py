from celery import Celery


broker_url = "redis://127.0.0.1:6379/14"
result_backend = "redis://127.0.0.1:6379/15"
app = Celery('tasks', broker=broker_url, backend=result_backend)


from yunpian_python_sdk.model import constant as YC
from yunpian_python_sdk.ypclient import YunpianClient
apikey = '3c28c4a767ac41fbd622a9194fb2b765'


@app.task(name='send_sms_code')  # 给任务取一个名字，一般就是函数名字
def send_sms_code(mobile, sms_code):
    clnt = YunpianClient(apikey)
    param = {YC.MOBILE: mobile, YC.TEXT: '【云片网】您的验证码是%s' % sms_code}
    r = clnt.sms().single_send(param)
