from selenium import webdriver
import time

'''体验selenium'''
# driver = webdriver.Chrome('./chromedriver')
#
# driver.get('http://www.baidu.com')
# print(driver.title)
#
# driver.find_element_by_id('kw').send_keys('天下第一')
# driver.find_element_by_id('su').click()
# time.sleep(3)
# print(driver.title)
# driver.quit()


'''初试增加JS'''
# driver = webdriver.Chrome('./chromedriver')
# driver.get("https://www.baidu.com/")
#
# # 给搜索输入框标红的javascript脚本
# js = "var q=document.getElementById(\"kw\");q.style.border=\"2px solid red\";"
#
# # 调用给搜索输入框标红js脚本
# driver.execute_script(js)
# print('1..')
# time.sleep(3)
# #查看页面快照
# driver.save_screenshot("redbaidu.png")
#
# #js隐藏元素，将获取的图片元素隐藏
# img = driver.find_element_by_xpath("//*[@id='lg']/img")
# driver.execute_script('$(arguments[0]).fadeOut()',img)
# print('2...')
# time.sleep(3)
#
# # 向下滚动到页面底部
# driver.execute_script("$('.scroll_top').click(function(){$('html,body').animate({scrollTop: '0px'}, 800);});")
# print('3....')
# time.sleep(3)
#
# #查看页面快照
# driver.save_screenshot("nullbaidu.png")
#
# driver.quit()



'''滑动JS'''
# driver = webdriver.Chrome('./chromedriver')
# driver.get("https://movie.douban.com/typerank?type_name=剧情&type=11&interval_id=100:90&action=")
#
# # 向下滚动10000像素
# # js = "document.body.scrollTop=10000"
# js="var q=document.documentElement.scrollTop=10000"
# time.sleep(3)
#
# #查看页面快照
# driver.save_screenshot("douban.png")
#
# # 执行JS语句
# driver.execute_script(js)
# time.sleep(10)
#
# #查看页面快照
# driver.save_screenshot("newdouban.png")
#
# driver.quit()


'''滑动JS'''
# driver = webdriver.Chrome('./chromedriver')
# driver.get("https://www.jd.com/?cu=true&utm_source=baidu-pinzhuan&utm_medium=cpc&utm_campaign=t_288551095_baidupinzhuan&utm_term=0f3d30c8dba7459bb52f2eb5eba8ac7d_0_8a261ed6b95641409340dd3ff296cc2c")
#
# # 最大化
# driver.maximize_window()
# # 向下滚动10000像素
# # js = "document.body.scrollTop=10000"
# js="var q=document.documentElement.scrollTop=500"
# time.sleep(3)
#
# # #查看页面快照
# # driver.save_screenshot("douban.png")
#
# # 执行JS语句
# i=1
# while True:
#     js = "var q=document.documentElement.scrollTop=%s"%(500*i)
#     driver.execute_script(js)
#     time.sleep(5)
#     #查看页面快照
#     driver.save_screenshot("images/newdouban%s.png"%i)
#     i+=1
#     if i==20:
#         break
#
#
# driver.quit()



