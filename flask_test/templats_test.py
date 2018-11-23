#-*- encoding=UTF-8 -*

# 导入
from flask import Flask,render_template

# 创建一个Flask应用实例
# 需要传入__name__,作用是为了确定资源所在的路径
app = Flask(__name__)

# 定义路由及视图函数
# Falsk中定义路由是通过装饰器实现的
# 路由默认只支持GET，如果需要，可以自行指定
# @app.route('/',methods=['GET','POST'])
@app.route('/')
def hello_world():
    name_str = '快乐'
    return render_template('index.html',name_str=name_str)



if __name__ == '__main__':
    app.run()
