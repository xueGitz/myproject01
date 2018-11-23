#-*- encoding=UTF-8 -*

# 导入
from flask import Flask

# 创建一个Flask应用实例
# 需要传入__name__,作用是为了确定资源所在的路径
app = Flask(__name__)

# 定义路由及视图函数
# Falsk中定义路由是通过装饰器实现的
# 路由默认只支持GET，如果需要，可以自行指定
# @app.route('/',methods=['GET','POST'])
@app.route('/')
def hello_world():
    return 'Hello World!'

# 使用同一个视图函数，来显示不同用户的订单信息
@app.route('/orders/<order_id>')
# 对路由的优化，很多时候只需要提供整型（int）或浮点型（float）
# @app.route('orders/<int:order_id>')
# @app.route('orders/<float:order_id>')
def get_order_info(order_id):

    # 参数类型，默认是字符串（unicode）
    print(type(order_id))

    # 需要在视图函数的（）内填入参数名，那么后面的代码才能去使用
    return 'order_is %s' % order_id


if __name__ == '__main__':
    app.run()
