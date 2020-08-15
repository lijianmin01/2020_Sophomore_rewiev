"""
1.  编写一段程序，由键盘赋值两个变量a，b，当a和b都是浮点数时输出以a为实部，b为虚部的复数的共轭复数，
如果a和b都是整数，则输出a除以b保留两位小数的结果，如果都不是，则分别输出a和b的类型。
"""

# # 判断数据类型  （假设只有三种数据： 字符  、 整形 、 浮点型）
# def cnt_type(cnt):
#     str_type = ['string','int','float']
#     flag = None
#     # 先除去 . 对字符串的影响
#     strs = cnt.split(".")
#     if len(strs)>2:
#         # 只有浮点数存在一个. ，当存在多个.时，该字符为字符串
#         flag = 0
#     elif len(strs)==1:
#         # 不存在“.”
#         # 判断该字符串是否都是由数字组成
#         # Isdigit()方法
#         # - 检测字符串是否只由数字组成
#         if strs[0].isnumeric():
#             flag=1
#         else:
#             flag=0
#     elif len(strs)==2:
#         if strs[0].isnumeric() and strs[1].isnumeric():
#             flag = 2
#         else:
#             flag = 0
#
#     return str_type[flag]
#
#     pass
#
# while(True):
#     a,b = input().split()
#     if cnt_type(a)=='float' and cnt_type(b)=='float':
#         result = complex(float(a),float(b))
#         print(result)
#     elif cnt_type(a)=='int' and cnt_type(b)=='int':
#         result = int(a)*1.0/int(b)
#         print("{:.2f}".format(result))
#     else:
#         print(cnt_type(a),cnt_type(b))


"""
已知sinfo = 
{'wangwu':{'name':'WangWu','age':28,'score':{'chinese':70,'math':80,'english':60}}}，
请把wangwu的成绩从高到低排列。
"""

# sinfo = {'wangwu':{'name':'WangWu','age':28,'score':{'chinese':70,'math':80,'english':60}}}
#
# sinfo_score = sinfo['wangwu']['score']
#
# wangwu_keys = list(sinfo_score.keys())
# wangwu_values = list(sinfo_score.values())
#
# # 冒泡排序
# for i in range(len(wangwu_keys)-1):
#     for j in range(len(wangwu_keys)-i-1):
#         if wangwu_values[j]>wangwu_values[j+1]:
#             cnt = wangwu_values[j]
#             wangwu_values[j] = wangwu_values[j+1]
#             wangwu_values[j+1] = cnt
#
#             cnt = wangwu_keys[j]
#             wangwu_keys[j] = wangwu_keys[j+1]
#             wangwu_keys[j+1] = cnt
#
# print("wangwu成绩是：")
# for i in range(len(wangwu_keys)):
#     print("{:8}成绩为：{}".format(wangwu_keys[i],wangwu_values[i]))

# 1.  设计一个用来计时装饰器，来实现对2到5000中所有质数打印的计时。

# import math,time
# # 定义一个函数计时器
# def much_time(func):
#     def wrapper(*args,**kw):
#         start_time = time.time()
#         func(*args,**kw)
#         end_time = time.time()
#
#         print("这个函数的执行时间为：{}s".format(end_time-start_time))
#     return wrapper
# # 定义: a，b 输出a~b之间的所有质数
# @much_time
# def find_prime(a,b):
#     # 保存找到的质数
#     nums=[]
#     num = a
#     while (num<=b):
#         # 判断是否为质数
#         flag = 0
#         if num <= 2:
#             # 因为2是最小的质数‘
#             num = 2
#         else:
#             for i in range(2,int(math.sqrt(num)+1)):
#                 if num % i == 0:
#                     flag = 1
#                     break
#
#         if flag==0:
#             nums.append(num)
#         num += 1
#     print(nums)
#     return nums
#
# find_prime(2,5000)

# 2.  用生成器实现杨辉三角。
# def generator_yhs(): # 生成器----杨辉三角
#     print("杨辉三角为：")
#     cnt = 0
#     arrays = [1]
#     while True:
#         if cnt == 1:
#             arrays.append(1)
#         elif cnt>1:
#             arrays_cnt = [1]
#             for index in range(1,cnt):
#                 arrays_cnt.append(arrays[index]+arrays[index-1])
#             arrays_cnt.append(1)
#             arrays = arrays_cnt
#
#         yield arrays
#         cnt += 1
#
# s = generator_yhs()
# print(next(s))
# print(next(s))
# print(next(s))
# print(next(s))
# print(next(s))
# print(next(s))

"""
2. 请用异常处理的方法来编写一个函数，实现减法运算，当被减数小于减数时，抛出“被减数不能小于减数”的异常。

如：jianfa(2,5)

则抛出“被减数2不能小于减数5”。

注：每个题目要求上传代码和截图，以及问题解决过程描述。
"""
#
# # 定义异常
# class NumberError(Exception):
#     # 被减数不能小于减数
#     def __init__(self,num1=0,num2=0):
#         self.num1 = num1
#         self.num2 = num2
#
#     def __str__(self):
#         return "被减数" + str(self.num2) + "不能小于减数" + str(self.num1)
#
# def jianshu(num1,num2):
#     try:
#         if (num1<num2):
#             raise NumberError(num1,num2)
#         print("{}-{}={}".format(num1, num2, num1 - num2))
#     except NumberError:
#         print(NumberError(num1,num2))
#
# jianshu(6,2)
# jianshu(2,6)

"""
实现一个 Python 脚本，可以从 Python 官网首页（https://www.python.org）获取最新的新闻信息（如下图所示），
每一条信息包含“日期”和“标题”两项内容，将获取的新闻信息保存成一个 python-latest-news.csv 文件。
"""

import urllib.request as ur
import re
import csv

def get_html(url):
    # 请求站点获得一个HttpResponse对象
    response = ur.urlopen(url)
    # 使用utf-8格式回去网页文本内容
    html = response.read().decode('utf-8')
    return html

# 使用正则表达式获取所需要的信息
def deal_with(data):
    pattern = re.compile('<li>\s+<time\sdatetime="(\d{4})-(\d{2})-(\d{2}).*?</time>\s+<a\shref="(.*?)">(.*?)</a></li>',re.S)
    #pattern = re.compile('<li>\s+<time\sdatetime="(\d{4})-(\d{2})-(\d{2}).*?</time>\s+<a\shref=".*?>(.*?)</a></li>',re.S)
    items = re.findall(pattern,data)
    return items[:5]

def write_nums(news):
    headers = ['日期', '标题','链接']
    with open('python-lastest-news.cvs','w+',encoding='utf-8',newline='') as f:
        f_csv = csv.writer(f)
        f_csv.writerow(headers)
        rows=[]
        for cnt in news:
            datatime=cnt[0]+"-"+cnt[1]+"-"+cnt[2]
            news1 = cnt[-1]
            url =cnt[-2]
            row=[datatime,news1,url]
            rows.append(row)

        f_csv.writerows(rows)

    f.close()

def main():
    url = 'https://www.python.org'
    # 获取html文件
    # data = get_html(url)

    data="""
    <!doctype html>
<!--[if lt IE 7]>   <html class="no-js ie6 lt-ie7 lt-ie8 lt-ie9">   <![endif]-->
<!--[if IE 7]>      <html class="no-js ie7 lt-ie8 lt-ie9">          <![endif]-->
<!--[if IE 8]>      <html class="no-js ie8 lt-ie9">                 <![endif]-->
<!--[if gt IE 8]><!--><html class="no-js" lang="en" dir="ltr">  <!--<![endif]-->

<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">

    <link rel="prefetch" href="//ajax.googleapis.com/ajax/libs/jquery/1.8.2/jquery.min.js">

    <meta name="application-name" content="Python.org">
    <meta name="msapplication-tooltip" content="The official home of the Python Programming Language">
    <meta name="apple-mobile-web-app-title" content="Python.org">
    <meta name="apple-mobile-web-app-capable" content="yes">
    <meta name="apple-mobile-web-app-status-bar-style" content="black">

    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="HandheldFriendly" content="True">
    <meta name="format-detection" content="telephone=no">
    <meta http-equiv="cleartype" content="on">
    <meta http-equiv="imagetoolbar" content="false">

    <script src="/static/js/libs/modernizr.js"></script>

    <link href="/static/stylesheets/style.30afed881237.css" rel="stylesheet" type="text/css" title="default" />
    <link href="/static/stylesheets/mq.eef77a5d2257.css" rel="stylesheet" type="text/css" media="not print, braille, embossed, speech, tty" />
    

    <!--[if (lte IE 8)&(!IEMobile)]>
    <link href="/static/stylesheets/no-mq.7946159eb289.css" rel="stylesheet" type="text/css" media="screen" />
    
    
    <![endif]-->

    
    <link rel="icon" type="image/x-icon" href="/static/favicon.ico">
    <link rel="apple-touch-icon-precomposed" sizes="144x144" href="/static/apple-touch-icon-144x144-precomposed.png">
    <link rel="apple-touch-icon-precomposed" sizes="114x114" href="/static/apple-touch-icon-114x114-precomposed.png">
    <link rel="apple-touch-icon-precomposed" sizes="72x72" href="/static/apple-touch-icon-72x72-precomposed.png">
    <link rel="apple-touch-icon-precomposed" href="/static/apple-touch-icon-precomposed.png">
    <link rel="apple-touch-icon" href="/static/apple-touch-icon-precomposed.png">

    
    <meta name="msapplication-TileImage" content="/static/metro-icon-144x144-precomposed.png"><!-- white shape -->
    <meta name="msapplication-TileColor" content="#3673a5"><!-- python blue -->
    <meta name="msapplication-navbutton-color" content="#3673a5">

    <title>Welcome to Python.org</title>

    <meta name="description" content="The official home of the Python Programming Language">
    <meta name="keywords" content="Python programming language object oriented web free open source software license documentation download community">

    
    <meta property="og:type" content="website">
    <meta property="og:site_name" content="Python.org">
    <meta property="og:title" content="Welcome to Python.org">
    <meta property="og:description" content="The official home of the Python Programming Language">
    
    <meta property="og:image" content="https://www.python.org/static/opengraph-icon-200x200.png">
    <meta property="og:image:secure_url" content="https://www.python.org/static/opengraph-icon-200x200.png">
    
    <meta property="og:url" content="https://www.python.org/">

    <link rel="author" href="/static/humans.txt">

    <link rel="alternate" type="application/rss+xml" title="Python Enhancement Proposals"
          href="https://www.python.org/dev/peps/peps.rss/">
    <link rel="alternate" type="application/rss+xml" title="Python Job Opportunities"
          href="https://www.python.org/jobs/feed/rss/">
    <link rel="alternate" type="application/rss+xml" title="Python Software Foundation News"
          href="https://feeds.feedburner.com/PythonSoftwareFoundationNews">
    <link rel="alternate" type="application/rss+xml" title="Python Insider"
          href="https://feeds.feedburner.com/PythonInsider">

    

    
    <script type="application/ld+json">
     {
       "@context": "https://schema.org",
       "@type": "WebSite",
       "url": "https://www.python.org/",
       "potentialAction": {
         "@type": "SearchAction",
         "target": "https://www.python.org/search/?q={search_term_string}",
         "query-input": "required name=search_term_string"
       }
     }
    </script>

    
    <script type="text/javascript">
    var _gaq = _gaq || [];
    _gaq.push(['_setAccount', 'UA-39055973-1']);
    _gaq.push(['_trackPageview']);

    (function() {
        var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
        ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
        var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
    })();
    </script>
    
</head>

<body class="python home" id="homepage">

    <div id="touchnav-wrapper">

        <div id="nojs" class="do-not-print">
            <p><strong>Notice:</strong> While Javascript is not essential for this website, your interaction with the content will be limited. Please turn Javascript on for the full experience. </p>
        </div>

        <!--[if lte IE 8]>
        <div id="oldie-warning" class="do-not-print">
            <p>
                <strong>Notice:</strong> Your browser is <em>ancient</em>. Please
                <a href="http://browsehappy.com/">upgrade to a different browser</a> to experience a better web.
            </p>
        </div>
        <![endif]-->

        <!-- Sister Site Links -->
        <div id="top" class="top-bar do-not-print">

            <nav class="meta-navigation container" role="navigation">

                
                <div class="skip-link screen-reader-text">
                    <a href="#content" title="Skip to content">Skip to content</a>
                </div>

                
                <a id="close-python-network" class="jump-link" href="#python-network" aria-hidden="true">
                    <span aria-hidden="true" class="icon-arrow-down"><span>&#9660;</span></span> Close
                </a>

                

<ul class="menu" role="tree">
    
    <li class="python-meta current_item selectedcurrent_branch selected">
        <a href="/" title="The Python Programming Language" class="current_item selectedcurrent_branch selected">Python</a>
    </li>
    
    <li class="psf-meta ">
        <a href="/psf-landing/" title="The Python Software Foundation" >PSF</a>
    </li>
    
    <li class="docs-meta ">
        <a href="https://docs.python.org" title="Python Documentation" >Docs</a>
    </li>
    
    <li class="pypi-meta ">
        <a href="https://pypi.org/" title="Python Package Index" >PyPI</a>
    </li>
    
    <li class="jobs-meta ">
        <a href="/jobs/" title="Python Job Board" >Jobs</a>
    </li>
    
    <li class="shop-meta ">
        <a href="/community-landing/"  >Community</a>
    </li>
    
</ul>


                <a id="python-network" class="jump-link" href="#top" aria-hidden="true">
                    <span aria-hidden="true" class="icon-arrow-up"><span>&#9650;</span></span> The Python Network
                </a>

            </nav>

        </div>

        <!-- Header elements -->
        <header class="main-header" role="banner">
            <div class="container">

                <h1 class="site-headline">
                    <a href="/"><img class="python-logo" src="/static/img/python-logo.png" alt="python&trade;"></a>
                </h1>

                <div class="options-bar-container do-not-print">
                    <a href="https://psfmember.org/civicrm/contribute/transact?reset=1&id=2" class="donate-button">Donate</a>
                    <div class="options-bar">
                        
                        <a id="site-map-link" class="jump-to-menu" href="#site-map"><span class="menu-icon">&equiv;</span> Menu</a><form class="search-the-site" action="/search/" method="get">
                            <fieldset title="Search Python.org">

                                <span aria-hidden="true" class="icon-search"></span>

                                <label class="screen-reader-text" for="id-search-field">Search This Site</label>
                                <input id="id-search-field" name="q" type="search" role="textbox" class="search-field" placeholder="Search" value="" tabindex="1">

                                <button type="submit" name="submit" id="submit" class="search-button" title="Submit this Search" tabindex="3">
                                    GO
                                </button>

                                
                                <!--[if IE]><input type="text" style="display: none;" disabled="disabled" size="1" tabindex="4"><![endif]-->

                            </fieldset>
                        </form><span class="breaker"></span><div class="adjust-font-size" aria-hidden="true">
                            <ul class="navigation menu" aria-label="Adjust Text Size on Page">
                                <li class="tier-1 last" aria-haspopup="true">
                                    <a href="#" class="action-trigger"><strong><small>A</small> A</strong></a>
                                    <ul class="subnav menu">
                                        <li class="tier-2 element-1" role="treeitem"><a class="text-shrink" title="Make Text Smaller" href="javascript:;">Smaller</a></li>
                                        <li class="tier-2 element-2" role="treeitem"><a class="text-grow" title="Make Text Larger" href="javascript:;">Larger</a></li>
                                        <li class="tier-2 element-3" role="treeitem"><a class="text-reset" title="Reset any font size changes I have made" href="javascript:;">Reset</a></li>
                                    </ul>
                                </li>
                            </ul>
                        </div><div class="winkwink-nudgenudge">
                            <ul class="navigation menu" aria-label="Social Media Navigation">
                                <li class="tier-1 last" aria-haspopup="true">
                                    <a href="#" class="action-trigger">Socialize</a>
                                    <ul class="subnav menu">
                                        <li class="tier-2 element-1" role="treeitem"><a href="https://www.facebook.com/pythonlang?fref=ts"><span aria-hidden="true" class="icon-facebook"></span>Facebook</a></li>
                                        <li class="tier-2 element-2" role="treeitem"><a href="https://twitter.com/ThePSF"><span aria-hidden="true" class="icon-twitter"></span>Twitter</a></li>
                                        <li class="tier-2 element-3" role="treeitem"><a href="/community/irc/"><span aria-hidden="true" class="icon-freenode"></span>Chat on IRC</a></li>
                                    </ul>
                                </li>
                            </ul>
                        </div>
                        <span data-html-include="/authenticated"></span>
                    </div><!-- end options-bar -->
                </div>

                <nav id="mainnav" class="python-navigation main-navigation do-not-print" role="navigation">
                    
                        
<ul class="navigation menu" role="menubar" aria-label="Main Navigation">
  
    
    
    <li id="about" class="tier-1 element-1  " aria-haspopup="true">
        <a href="/about/" title="" class="">About</a>
        
            

<ul class="subnav menu" role="menu" aria-hidden="true">
    
        <li class="tier-2 element-1" role="treeitem"><a href="/about/apps/" title="">Applications</a></li>
    
        <li class="tier-2 element-2" role="treeitem"><a href="/about/quotes/" title="">Quotes</a></li>
    
        <li class="tier-2 element-3" role="treeitem"><a href="/about/gettingstarted/" title="">Getting Started</a></li>
    
        <li class="tier-2 element-4" role="treeitem"><a href="/about/help/" title="">Help</a></li>
    
        <li class="tier-2 element-5" role="treeitem"><a href="http://brochure.getpython.info/" title="">Python Brochure</a></li>
    
</ul>

        
    </li>
    
    
    
    <li id="downloads" class="tier-1 element-2  " aria-haspopup="true">
        <a href="/downloads/" title="" class="">Downloads</a>
        
            

<ul class="subnav menu" role="menu" aria-hidden="true">
    
        <li class="tier-2 element-1" role="treeitem"><a href="/downloads/" title="">All releases</a></li>
    
        <li class="tier-2 element-2" role="treeitem"><a href="/downloads/source/" title="">Source code</a></li>
    
        <li class="tier-2 element-3" role="treeitem"><a href="/downloads/windows/" title="">Windows</a></li>
    
        <li class="tier-2 element-4" role="treeitem"><a href="/downloads/mac-osx/" title="">Mac OS X</a></li>
    
        <li class="tier-2 element-5" role="treeitem"><a href="/download/other/" title="">Other Platforms</a></li>
    
        <li class="tier-2 element-6" role="treeitem"><a href="https://docs.python.org/3/license.html" title="">License</a></li>
    
        <li class="tier-2 element-7" role="treeitem"><a href="/download/alternatives" title="">Alternative Implementations</a></li>
    
</ul>

        
    </li>
    
    
    
    <li id="documentation" class="tier-1 element-3  " aria-haspopup="true">
        <a href="/doc/" title="" class="">Documentation</a>
        
            

<ul class="subnav menu" role="menu" aria-hidden="true">
    
        <li class="tier-2 element-1" role="treeitem"><a href="/doc/" title="">Docs</a></li>
    
        <li class="tier-2 element-2" role="treeitem"><a href="/doc/av" title="">Audio/Visual Talks</a></li>
    
        <li class="tier-2 element-3" role="treeitem"><a href="https://wiki.python.org/moin/BeginnersGuide" title="">Beginner&#39;s Guide</a></li>
    
        <li class="tier-2 element-4" role="treeitem"><a href="https://devguide.python.org/" title="">Developer&#39;s Guide</a></li>
    
        <li class="tier-2 element-5" role="treeitem"><a href="https://docs.python.org/faq/" title="">FAQ</a></li>
    
        <li class="tier-2 element-6" role="treeitem"><a href="http://wiki.python.org/moin/Languages" title="">Non-English Docs</a></li>
    
        <li class="tier-2 element-7" role="treeitem"><a href="http://python.org/dev/peps/" title="">PEP Index</a></li>
    
        <li class="tier-2 element-8" role="treeitem"><a href="https://wiki.python.org/moin/PythonBooks" title="">Python Books</a></li>
    
        <li class="tier-2 element-9" role="treeitem"><a href="/doc/essays/" title="">Python Essays</a></li>
    
</ul>

        
    </li>
    
    
    
    <li id="community" class="tier-1 element-4  " aria-haspopup="true">
        <a href="/community/" title="" class="">Community</a>
        
            

<ul class="subnav menu" role="menu" aria-hidden="true">
    
        <li class="tier-2 element-1" role="treeitem"><a href="/community/survey" title="">Community Survey</a></li>
    
        <li class="tier-2 element-2" role="treeitem"><a href="/community/diversity/" title="">Diversity</a></li>
    
        <li class="tier-2 element-3" role="treeitem"><a href="/community/lists/" title="">Mailing Lists</a></li>
    
        <li class="tier-2 element-4" role="treeitem"><a href="/community/irc/" title="">IRC</a></li>
    
        <li class="tier-2 element-5" role="treeitem"><a href="/community/forums/" title="">Forums</a></li>
    
        <li class="tier-2 element-6" role="treeitem"><a href="/psf/annual-report/2020/" title="">PSF Annual Impact Report</a></li>
    
        <li class="tier-2 element-7" role="treeitem"><a href="/community/workshops/" title="">Python Conferences</a></li>
    
        <li class="tier-2 element-8" role="treeitem"><a href="/community/sigs/" title="">Special Interest Groups</a></li>
    
        <li class="tier-2 element-9" role="treeitem"><a href="/community/logos/" title="">Python Logo</a></li>
    
        <li class="tier-2 element-10" role="treeitem"><a href="https://wiki.python.org/moin/" title="">Python Wiki</a></li>
    
        <li class="tier-2 element-11" role="treeitem"><a href="/community/merchandise/" title="">Merchandise</a></li>
    
        <li class="tier-2 element-12" role="treeitem"><a href="/community/awards" title="">Community Awards</a></li>
    
        <li class="tier-2 element-13" role="treeitem"><a href="/psf/conduct/" title="">Code of Conduct</a></li>
    
</ul>

        
    </li>
    
    
    
    <li id="success-stories" class="tier-1 element-5  " aria-haspopup="true">
        <a href="/success-stories/" title="success-stories" class="">Success Stories</a>
        
            

<ul class="subnav menu" role="menu" aria-hidden="true">
    
        <li class="tier-2 element-1" role="treeitem"><a href="/success-stories/category/arts/" title="">Arts</a></li>
    
        <li class="tier-2 element-2" role="treeitem"><a href="/success-stories/category/business/" title="">Business</a></li>
    
        <li class="tier-2 element-3" role="treeitem"><a href="/success-stories/category/education/" title="">Education</a></li>
    
        <li class="tier-2 element-4" role="treeitem"><a href="/success-stories/category/engineering/" title="">Engineering</a></li>
    
        <li class="tier-2 element-5" role="treeitem"><a href="/success-stories/category/government/" title="">Government</a></li>
    
        <li class="tier-2 element-6" role="treeitem"><a href="/success-stories/category/scientific/" title="">Scientific</a></li>
    
        <li class="tier-2 element-7" role="treeitem"><a href="/success-stories/category/software-development/" title="">Software Development</a></li>
    
</ul>

        
    </li>
    
    
    
    <li id="news" class="tier-1 element-6  " aria-haspopup="true">
        <a href="/blogs/" title="News from around the Python world" class="">News</a>
        
            

<ul class="subnav menu" role="menu" aria-hidden="true">
    
        <li class="tier-2 element-1" role="treeitem"><a href="/blogs/" title="Python Insider Blog Posts">Python News</a></li>
    
        <li class="tier-2 element-2" role="treeitem"><a href="/psf/newsletter/" title="Python Software Foundation Newsletter">PSF Newsletter</a></li>
    
        <li class="tier-2 element-3" role="treeitem"><a href="http://planetpython.org/" title="Planet Python">Community News</a></li>
    
        <li class="tier-2 element-4" role="treeitem"><a href="http://pyfound.blogspot.com/" title="PSF Blog">PSF News</a></li>
    
        <li class="tier-2 element-5" role="treeitem"><a href="http://pycon.blogspot.com/" title="PyCon Blog">PyCon News</a></li>
    
</ul>

        
    </li>
    
    
    
    <li id="events" class="tier-1 element-7  " aria-haspopup="true">
        <a href="/events/" title="" class="">Events</a>
        
            

<ul class="subnav menu" role="menu" aria-hidden="true">
    
        <li class="tier-2 element-1" role="treeitem"><a href="/events/python-events" title="">Python Events</a></li>
    
        <li class="tier-2 element-2" role="treeitem"><a href="/events/python-user-group/" title="">User Group Events</a></li>
    
        <li class="tier-2 element-3" role="treeitem"><a href="/events/python-events/past/" title="">Python Events Archive</a></li>
    
        <li class="tier-2 element-4" role="treeitem"><a href="/events/python-user-group/past/" title="">User Group Events Archive</a></li>
    
        <li class="tier-2 element-5" role="treeitem"><a href="https://wiki.python.org/moin/PythonEventsCalendar#Submitting_an_Event" title="">Submit an Event</a></li>
    
</ul>

        
    </li>
    
    
    
    
  
</ul>

                    
                </nav>

                <div class="header-banner "> <!-- for optional "do-not-print" class -->
                    
        <div id="dive-into-python" class="flex-slideshow slideshow">

            <ul class="launch-shell menu" id="launch-shell">
                <li>
                    <a class="button prompt" id="start-shell" data-shell-container="#dive-into-python" href="/shell/">&gt;_
                        <span class="message">Launch Interactive Shell</span>
                    </a>
                </li>
            </ul>

            <ul class="slides menu">
                
                <li>
                    <div class="slide-code"><pre><code><span class="comment"># Python 3: Fibonacci series up to n</span>
>>> def fib(n):
>>>     a, b = 0, 1
>>>     while a &lt; n:
>>>         print(a, end=' ')
>>>         a, b = b, a+b
>>>     print()
>>> fib(1000)
<span class="output">0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987</span></code></pre></div>
                    <div class="slide-copy"><h1>Functions Defined</h1>
<p>The core of extensible programming is defining functions. Python allows mandatory and optional arguments, keyword arguments, and even arbitrary argument lists. <a href="//docs.python.org/3/tutorial/controlflow.html#defining-functions">More about defining functions in Python&nbsp;3</a></p></div>
                </li>
                
                <li>
                    <div class="slide-code"><pre><code><span class="comment"># Python 3: List comprehensions</span>
>>> fruits = ['Banana', 'Apple', 'Lime']
>>> loud_fruits = [fruit.upper() for fruit in fruits]
>>> print(loud_fruits)
<span class="output">['BANANA', 'APPLE', 'LIME']</span>

<span class="comment"># List and the enumerate function</span>
>>> list(enumerate(fruits))
<span class="output">[(0, 'Banana'), (1, 'Apple'), (2, 'Lime')]</span></code></pre></div>
                    <div class="slide-copy"><h1>Compound Data Types</h1>
<p>Lists (known as arrays in other languages) are one of the compound data types that Python understands. Lists can be indexed, sliced and manipulated with other built-in functions. <a href="//docs.python.org/3/tutorial/introduction.html#lists">More about lists in Python&nbsp;3</a></p></div>
                </li>
                
                <li>
                    <div class="slide-code"><pre><code><span class="comment"># Python 3: Simple arithmetic</span>
>>> 1 / 2
<span class="output">0.5</span>
>>> 2 ** 3
<span class="output">8</span>
>>> 17 / 3  <span class="comment"># classic division returns a float</span>
<span class="output">5.666666666666667</span>
>>> 17 // 3  <span class="comment"># floor division</span>
<span class="output">5</span></code></pre></div>
                    <div class="slide-copy"><h1>Intuitive Interpretation</h1>
<p>Calculations are simple with Python, and expression syntax is straightforward: the operators <code>+</code>, <code>-</code>, <code>*</code> and <code>/</code> work as expected; parentheses <code>()</code> can be used for grouping. <a href="http://docs.python.org/3/tutorial/introduction.html#using-python-as-a-calculator">More about simple math functions in Python&nbsp;3</a>.</p></div>
                </li>
                
                <li>
                    <div class="slide-code"><pre><code><span class="comment"># Python 3: Simple output (with Unicode)</span>
>>> print("Hello, I'm Python!")
<span class="output">Hello, I'm Python!</span>

<span class="comment"># Input, assignment</span>
>>> name = input('What is your name?\n')
>>> print('Hi, %s.' % name)
<span class="output">What is your name?
Python
Hi, Python.</span></code></pre></div>
                    <div class="slide-copy"><h1>Quick &amp; Easy to Learn</h1>
<p>Experienced programmers in any other language can pick up Python very quickly, and beginners find the clean syntax and indentation structure easy to learn. <a href="//docs.python.org/3/tutorial/">Whet your appetite</a> with our Python&nbsp;3 overview.</p>
                   </div>
                </li>
                
                <li>
                    <div class="slide-code"><pre><code><span class="comment"># For loop on a list</span>
>>> numbers = [2, 4, 6, 8]
>>> product = 1
>>> for number in numbers:
...    product = product * number
... 
>>> print('The product is:', product)
<span class="output">The product is: 384</span></code></pre></div>
                    <div class="slide-copy"><h1>All the Flow You&rsquo;d Expect</h1>
<p>Python knows the usual control flow statements that other languages speak &mdash; <code>if</code>, <code>for</code>, <code>while</code> and <code>range</code> &mdash; with some of its own twists, of course. <a href="//docs.python.org/3/tutorial/controlflow.html">More control flow tools in Python&nbsp;3</a></p></div>
                </li>
                
            </ul>
        </div>


                </div>

                
        <div class="introduction">
            <p>Python is a programming language that lets you work quickly <span class="breaker"></span>and integrate systems more effectively. <a class="readmore" href="/doc/">Learn More</a></p>
        </div>


             </div><!-- end .container -->
        </header>

        <div id="content" class="content-wrapper">
            <!-- Main Content Column -->
            <div class="container">

                <section class="main-content " role="main">

                    
                    

                    

                    

                

                <div class="row">

                    <div class="small-widget get-started-widget">
                        <h2 class="widget-title"><span aria-hidden="true" class="icon-get-started"></span>Get Started</h2>
<p>Whether you're new to programming or an experienced developer, it's easy to learn and use Python.</p>
<p><a href="/about/gettingstarted/">Start with our Beginner&rsquo;s Guide</a></p>
                    </div>

                    <div class="small-widget download-widget">
                        <h2 class="widget-title"><span aria-hidden="true" class="icon-download"></span>Download</h2>
<p>Python source code and installers are available for download for all versions!</p>
<p>Latest: <a href="/downloads/release/python-385/">Python 3.8.5</a></p>
                    </div>

                    <div class="small-widget documentation-widget">
                        <h2 class="widget-title"><span aria-hidden="true" class="icon-documentation"></span>Docs</h2>
<p>Documentation for Python's standard library, along with tutorials and guides, are available online.</p>
<p><a href="https://docs.python.org">docs.python.org</a></p>
                    </div>

                    <div class="small-widget jobs-widget last">
                        <h2 class="widget-title"><span aria-hidden="true" class="icon-jobs"></span>Jobs</h2>
<p>Looking for work or have a Python related position that you're trying to hire for? Our <strong>relaunched community-run job board</strong> is the place to go.</p>
<p><a href="//jobs.python.org">jobs.python.org</a></p>
                    </div>

                </div>

                <div class="list-widgets row">

                    <div class="medium-widget blog-widget">
                        
                        <div class="shrubbery">
                        
                            <h2 class="widget-title"><span aria-hidden="true" class="icon-news"></span>Latest News</h2>
                            <p class="give-me-more"><a href="https://blog.python.org" title="More News">More</a></p>
                            
                            <ul class="menu">
                                
                                
                                <li>
<time datetime="2020-08-11T21:41:00.000001+00:00"><span class="say-no-more">2020-</span>08-11</time>
 <a href="http://feedproxy.google.com/~r/PythonInsider/~3/VKrYX2pRrD4/python-390rc1-is-now-available.html">Python 3.9.0rc1 is now available</a></li>
                                
                                <li>
<time datetime="2020-07-30T15:14:00.000003+00:00"><span class="say-no-more">2020-</span>07-30</time>
 <a href="http://feedproxy.google.com/~r/PythonInsider/~3/oWRGYtccsHE/upgrade-pip-20-2-changes-20-3.html">Upgrade to pip 20.2, plus, changes coming in 20.3</a></li>
                                
                                <li>
<time datetime="2020-07-27T16:02:00+00:00"><span class="say-no-more">2020-</span>07-27</time>
 <a href="http://feedproxy.google.com/~r/PythonSoftwareFoundationNews/~3/6FahUJasdEc/abigail-dogbe-awarded-psf-community.html">Abigail Dogbe Awarded the PSF Community Service Award for Q1 2020</a></li>
                                
                                <li>
<time datetime="2020-07-24T22:15:00.000004+00:00"><span class="say-no-more">2020-</span>07-24</time>
 <a href="http://feedproxy.google.com/~r/PythonSoftwareFoundationNews/~3/ijGVTo7aKv0/python-software-foundation-fellow.html">Python Software Foundation Fellow Members for Q2 2020</a></li>
                                
                                <li>
<time datetime="2020-07-21T11:16:00.000001+00:00"><span class="say-no-more">2020-</span>07-21</time>
 <a href="http://feedproxy.google.com/~r/PythonInsider/~3/EjSD786Ov68/python-385-released-as-security-hotfix.html">Python 3.8.5 released as a security hotfix. 3.9.0b5, the last beta before 3.9.0, also available</a></li>
                                
                            </ul>
                        </div><!-- end .shrubbery -->

                    </div>

                    <div class="medium-widget event-widget last">
                        
                        <div class="shrubbery">
                        
                            <h2 class="widget-title"><span aria-hidden="true" class="icon-calendar"></span>Upcoming Events</h2>
                            <p class="give-me-more"><a href="/events/calendars/" title="More Events">More</a></p>
                            
                            <ul class="menu">
                                
                                
                                
                                <li>
<time datetime="2020-08-28T00:00:00+00:00"><span class="say-no-more">2020-</span>08-28</time>
 <a href="/events/python-events/951/">PyCon JP 2020</a></li>
                                
                                
                                
                                <li>
<time datetime="2020-09-05T00:00:00+00:00"><span class="say-no-more">2020-</span>09-05</time>
 <a href="/events/python-events/963/">PyCon TW 2020</a></li>
                                
                                
                                
                                <li>
<time datetime="2020-09-11T00:00:00+00:00"><span class="say-no-more">2020-</span>09-11</time>
 <a href="/events/python-events/879/">PyCon SK 2020</a></li>
                                
                                
                                
                                <li>
<time datetime="2020-09-16T00:00:00+00:00"><span class="say-no-more">2020-</span>09-16</time>
 <a href="/events/python-events/891/">DjangoCon Europe 2020</a></li>
                                
                                
                                
                                <li>
<time datetime="2020-09-19T00:00:00+00:00"><span class="say-no-more">2020-</span>09-19</time>
 <a href="/events/python-events/952/">PyCon APAC 2020</a></li>
                                
                                
                            </ul>
                        </div>

                    </div>

                </div>

                <div class="row">

                    <div class="medium-widget success-stories-widget">
                        



                        <div class="shrubbery">
                            

                            <h2 class="widget-title"><span aria-hidden="true" class="icon-success-stories"></span>Success Stories</h2>
                            <p class="give-me-more"><a href="/success-stories/" title="More Success Stories">More</a></p>

                            
                            <div class="success-story-item" id="success-story-838">

                            <blockquote>
                                <a href="/success-stories/saving-the-world-with-open-data-and-python/">When an Open Data standard is created and promoted, it’s important to think why - what change is this trying to drive? What will people do with this data that they couldn’t do before?</a>
                            </blockquote>

                            <table cellpadding="0" cellspacing="0" border="0" width="100%" class="quote-from">
                                <tbody>
                                    <tr>
                                        
                                        <td><p><a href="/success-stories/saving-the-world-with-open-data-and-python/">Saving the world with Open Data and Python</a> <em>by James Baster</em></p></td>
                                    </tr>
                                </tbody>
                            </table>
                            </div>
                            

                        </div><!-- end .shrubbery -->

                    </div>

                    <div class="medium-widget applications-widget last">
                        <div class="shrubbery">
                            <h2 class="widget-title"><span aria-hidden="true" class="icon-python"></span>Use Python for&hellip;</h2>
<p class="give-me-more"><a href="/about/apps" title="More Applications">More</a></p>

<ul class="menu">
    <li><b>Web Development</b>:
        <span class="tag-wrapper"><a class="tag" href="http://www.djangoproject.com/">Django</a>, <a class="tag" href="http://www.pylonsproject.org/">Pyramid</a>, <a class="tag" href="http://bottlepy.org">Bottle</a>, <a class="tag" href="http://tornadoweb.org">Tornado</a>, <a href="http://flask.pocoo.org/" class="tag">Flask</a>, <a class="tag" href="http://www.web2py.com/">web2py</a></span></li>
    <li><b>GUI Development</b>:
        <span class="tag-wrapper"><a class="tag" href="http://wiki.python.org/moin/TkInter">tkInter</a>, <a class="tag" href="https://wiki.gnome.org/Projects/PyGObject">PyGObject</a>, <a class="tag" href="http://www.riverbankcomputing.co.uk/software/pyqt/intro">PyQt</a>, <a class="tag" href="https://wiki.qt.io/PySide">PySide</a>, <a class="tag" href="https://kivy.org/">Kivy</a>, <a class="tag" href="http://www.wxpython.org/">wxPython</a></span></li>
    <li><b>Scientific and Numeric</b>:
        <span class="tag-wrapper">
<a class="tag" href="http://www.scipy.org">SciPy</a>, <a class="tag" href="http://pandas.pydata.org/">Pandas</a>, <a href="http://ipython.org" class="tag">IPython</a></span></li>
    <li><b>Software Development</b>:
        <span class="tag-wrapper"><a class="tag" href="http://buildbot.net/">Buildbot</a>, <a class="tag" href="http://trac.edgewall.org/">Trac</a>, <a class="tag" href="http://roundup.sourceforge.net/">Roundup</a></span></li>
    <li><b>System Administration</b>:
        <span class="tag-wrapper"><a class="tag" href="http://www.ansible.com">Ansible</a>, <a class="tag" href="http://www.saltstack.com">Salt</a>, <a class="tag" href="https://www.openstack.org">OpenStack</a></span></li>
</ul>

                        </div><!-- end .shrubbery -->
                    </div>

                </div>

                
                <div class="pep-widget">

                    <h2 class="widget-title">
                        <span class="prompt">&gt;&gt;&gt;</span> <a href="/dev/peps/">Python Enhancement Proposals<span class="say-no-more"> (PEPs)</span></a>: The future of Python<span class="say-no-more"> is discussed here.</span>
                        <a aria-hidden="true" class="rss-link" href="/dev/peps/peps.rss"><span class="icon-feed"></span> RSS</a>
                    </h2>


                    
                    
                </div>

                                <div class="psf-widget">

                    <div class="python-logo"></div>
                    
                    <h2 class="widget-title">
    <span class="prompt">&gt;&gt;&gt;</span> <a href="/psf/">Python Software Foundation</a>
</h2>
<p>The mission of the Python Software Foundation is to promote, protect, and advance the Python programming language, and to support and facilitate the growth of a diverse and international community of Python programmers. <a class="readmore" href="/psf/">Learn more</a> </p>
<p class="click-these">
    <a class="button" href="/users/membership/">Become a Member</a>
    <a class="button" href="/psf/donations/">Donate to the PSF</a>
</p>
                </div>




                </section>

                
                

                
                


            </div><!-- end .container -->
        </div><!-- end #content .content-wrapper -->

        <!-- Footer and social media list -->
        <footer id="site-map" class="main-footer" role="contentinfo">
            <div class="main-footer-links">
                <div class="container">

                    
                    <a id="back-to-top-1" class="jump-link" href="#python-network"><span aria-hidden="true" class="icon-arrow-up"><span>&#9650;</span></span> Back to Top</a>

                    

<ul class="sitemap navigation menu do-not-print" role="tree" id="container">
    
    <li class="tier-1 element-1">
        <a href="/about/" >About</a>
        
            

<ul class="subnav menu">
    
        <li class="tier-2 element-1" role="treeitem"><a href="/about/apps/" title="">Applications</a></li>
    
        <li class="tier-2 element-2" role="treeitem"><a href="/about/quotes/" title="">Quotes</a></li>
    
        <li class="tier-2 element-3" role="treeitem"><a href="/about/gettingstarted/" title="">Getting Started</a></li>
    
        <li class="tier-2 element-4" role="treeitem"><a href="/about/help/" title="">Help</a></li>
    
        <li class="tier-2 element-5" role="treeitem"><a href="http://brochure.getpython.info/" title="">Python Brochure</a></li>
    
</ul>

        
    </li>
    
    <li class="tier-1 element-2">
        <a href="/downloads/" >Downloads</a>
        
            

<ul class="subnav menu">
    
        <li class="tier-2 element-1" role="treeitem"><a href="/downloads/" title="">All releases</a></li>
    
        <li class="tier-2 element-2" role="treeitem"><a href="/downloads/source/" title="">Source code</a></li>
    
        <li class="tier-2 element-3" role="treeitem"><a href="/downloads/windows/" title="">Windows</a></li>
    
        <li class="tier-2 element-4" role="treeitem"><a href="/downloads/mac-osx/" title="">Mac OS X</a></li>
    
        <li class="tier-2 element-5" role="treeitem"><a href="/download/other/" title="">Other Platforms</a></li>
    
        <li class="tier-2 element-6" role="treeitem"><a href="https://docs.python.org/3/license.html" title="">License</a></li>
    
        <li class="tier-2 element-7" role="treeitem"><a href="/download/alternatives" title="">Alternative Implementations</a></li>
    
</ul>

        
    </li>
    
    <li class="tier-1 element-3">
        <a href="/doc/" >Documentation</a>
        
            

<ul class="subnav menu">
    
        <li class="tier-2 element-1" role="treeitem"><a href="/doc/" title="">Docs</a></li>
    
        <li class="tier-2 element-2" role="treeitem"><a href="/doc/av" title="">Audio/Visual Talks</a></li>
    
        <li class="tier-2 element-3" role="treeitem"><a href="https://wiki.python.org/moin/BeginnersGuide" title="">Beginner&#39;s Guide</a></li>
    
        <li class="tier-2 element-4" role="treeitem"><a href="https://devguide.python.org/" title="">Developer&#39;s Guide</a></li>
    
        <li class="tier-2 element-5" role="treeitem"><a href="https://docs.python.org/faq/" title="">FAQ</a></li>
    
        <li class="tier-2 element-6" role="treeitem"><a href="http://wiki.python.org/moin/Languages" title="">Non-English Docs</a></li>
    
        <li class="tier-2 element-7" role="treeitem"><a href="http://python.org/dev/peps/" title="">PEP Index</a></li>
    
        <li class="tier-2 element-8" role="treeitem"><a href="https://wiki.python.org/moin/PythonBooks" title="">Python Books</a></li>
    
        <li class="tier-2 element-9" role="treeitem"><a href="/doc/essays/" title="">Python Essays</a></li>
    
</ul>

        
    </li>
    
    <li class="tier-1 element-4">
        <a href="/community/" >Community</a>
        
            

<ul class="subnav menu">
    
        <li class="tier-2 element-1" role="treeitem"><a href="/community/survey" title="">Community Survey</a></li>
    
        <li class="tier-2 element-2" role="treeitem"><a href="/community/diversity/" title="">Diversity</a></li>
    
        <li class="tier-2 element-3" role="treeitem"><a href="/community/lists/" title="">Mailing Lists</a></li>
    
        <li class="tier-2 element-4" role="treeitem"><a href="/community/irc/" title="">IRC</a></li>
    
        <li class="tier-2 element-5" role="treeitem"><a href="/community/forums/" title="">Forums</a></li>
    
        <li class="tier-2 element-6" role="treeitem"><a href="/psf/annual-report/2020/" title="">PSF Annual Impact Report</a></li>
    
        <li class="tier-2 element-7" role="treeitem"><a href="/community/workshops/" title="">Python Conferences</a></li>
    
        <li class="tier-2 element-8" role="treeitem"><a href="/community/sigs/" title="">Special Interest Groups</a></li>
    
        <li class="tier-2 element-9" role="treeitem"><a href="/community/logos/" title="">Python Logo</a></li>
    
        <li class="tier-2 element-10" role="treeitem"><a href="https://wiki.python.org/moin/" title="">Python Wiki</a></li>
    
        <li class="tier-2 element-11" role="treeitem"><a href="/community/merchandise/" title="">Merchandise</a></li>
    
        <li class="tier-2 element-12" role="treeitem"><a href="/community/awards" title="">Community Awards</a></li>
    
        <li class="tier-2 element-13" role="treeitem"><a href="/psf/conduct/" title="">Code of Conduct</a></li>
    
</ul>

        
    </li>
    
    <li class="tier-1 element-5">
        <a href="/success-stories/" title="success-stories">Success Stories</a>
        
            

<ul class="subnav menu">
    
        <li class="tier-2 element-1" role="treeitem"><a href="/success-stories/category/arts/" title="">Arts</a></li>
    
        <li class="tier-2 element-2" role="treeitem"><a href="/success-stories/category/business/" title="">Business</a></li>
    
        <li class="tier-2 element-3" role="treeitem"><a href="/success-stories/category/education/" title="">Education</a></li>
    
        <li class="tier-2 element-4" role="treeitem"><a href="/success-stories/category/engineering/" title="">Engineering</a></li>
    
        <li class="tier-2 element-5" role="treeitem"><a href="/success-stories/category/government/" title="">Government</a></li>
    
        <li class="tier-2 element-6" role="treeitem"><a href="/success-stories/category/scientific/" title="">Scientific</a></li>
    
        <li class="tier-2 element-7" role="treeitem"><a href="/success-stories/category/software-development/" title="">Software Development</a></li>
    
</ul>

        
    </li>
    
    <li class="tier-1 element-6">
        <a href="/blogs/" title="News from around the Python world">News</a>
        
            

<ul class="subnav menu">
    
        <li class="tier-2 element-1" role="treeitem"><a href="/blogs/" title="Python Insider Blog Posts">Python News</a></li>
    
        <li class="tier-2 element-2" role="treeitem"><a href="/psf/newsletter/" title="Python Software Foundation Newsletter">PSF Newsletter</a></li>
    
        <li class="tier-2 element-3" role="treeitem"><a href="http://planetpython.org/" title="Planet Python">Community News</a></li>
    
        <li class="tier-2 element-4" role="treeitem"><a href="http://pyfound.blogspot.com/" title="PSF Blog">PSF News</a></li>
    
        <li class="tier-2 element-5" role="treeitem"><a href="http://pycon.blogspot.com/" title="PyCon Blog">PyCon News</a></li>
    
</ul>

        
    </li>
    
    <li class="tier-1 element-7">
        <a href="/events/" >Events</a>
        
            

<ul class="subnav menu">
    
        <li class="tier-2 element-1" role="treeitem"><a href="/events/python-events" title="">Python Events</a></li>
    
        <li class="tier-2 element-2" role="treeitem"><a href="/events/python-user-group/" title="">User Group Events</a></li>
    
        <li class="tier-2 element-3" role="treeitem"><a href="/events/python-events/past/" title="">Python Events Archive</a></li>
    
        <li class="tier-2 element-4" role="treeitem"><a href="/events/python-user-group/past/" title="">User Group Events Archive</a></li>
    
        <li class="tier-2 element-5" role="treeitem"><a href="https://wiki.python.org/moin/PythonEventsCalendar#Submitting_an_Event" title="">Submit an Event</a></li>
    
</ul>

        
    </li>
    
    <li class="tier-1 element-8">
        <a href="/dev/" >Contributing</a>
        
            

<ul class="subnav menu">
    
        <li class="tier-2 element-1" role="treeitem"><a href="https://devguide.python.org/" title="">Developer&#39;s Guide</a></li>
    
        <li class="tier-2 element-2" role="treeitem"><a href="https://bugs.python.org/" title="">Issue Tracker</a></li>
    
        <li class="tier-2 element-3" role="treeitem"><a href="https://mail.python.org/mailman/listinfo/python-dev" title="">python-dev list</a></li>
    
        <li class="tier-2 element-4" role="treeitem"><a href="/dev/core-mentorship/" title="">Core Mentorship</a></li>
    
        <li class="tier-2 element-5" role="treeitem"><a href="/dev/security/" title="">Report a Security Issue</a></li>
    
</ul>

        
    </li>
    
</ul>


                    <a id="back-to-top-2" class="jump-link" href="#python-network"><span aria-hidden="true" class="icon-arrow-up"><span>&#9650;</span></span> Back to Top</a>
                    

                </div><!-- end .container -->
            </div> <!-- end .main-footer-links -->

            <div class="site-base">
                <div class="container">
                    
                    <ul class="footer-links navigation menu do-not-print" role="tree">
                        <li class="tier-1 element-1"><a href="/about/help/">Help &amp; <span class="say-no-more">General</span> Contact</a></li>
                        <li class="tier-1 element-2"><a href="/community/diversity/">Diversity <span class="say-no-more">Initiatives</span></a></li>
                        <li class="tier-1 element-3"><a href="https://github.com/python/pythondotorg/issues">Submit Website Bug</a></li>
                        <li class="tier-1 element-4">
                            <a href="https://status.python.org/">Status <span class="python-status-indicator-default" id="python-status-indicator"></span></a>
                        </li>
                    </ul>

                    <div class="copyright">
                        <p><small>
                            <span class="pre">Copyright &copy;2001-2020.</span>
                            &nbsp;<span class="pre"><a href="/psf-landing/">Python Software Foundation</a></span>
                            &nbsp;<span class="pre"><a href="/about/legal/">Legal Statements</a></span>
                            &nbsp;<span class="pre"><a href="/privacy/">Privacy Policy</a></span>
                            &nbsp;<span class="pre"><a href="/psf/sponsorship/sponsors/#heroku">Powered by Heroku</a></span>
                        </small></p>
                    </div>

                </div><!-- end .container -->
            </div><!-- end .site-base -->

        </footer>

    </div><!-- end #touchnav-wrapper -->

    
    <script src="//ajax.googleapis.com/ajax/libs/jquery/1.8.2/jquery.min.js"></script>
    <script>window.jQuery || document.write('<script src="/static/js/libs/jquery-1.8.2.min.js"><\/script>')</script>

    <script src="/static/js/libs/masonry.pkgd.min.js"></script>
    <script src="/static/js/libs/html-includes.js"></script>

    <script type="text/javascript" src="/static/js/main-min.a3326162e3f0.js" charset="utf-8"></script>
    

    <!--[if lte IE 7]>
    <script type="text/javascript" src="/static/js/plugins/IE8-min.98b6ab00aab8.js" charset="utf-8"></script>
    
    
    <![endif]-->

    <!--[if lte IE 8]>
    <script type="text/javascript" src="/static/js/plugins/getComputedStyle-min.c3860be1d290.js" charset="utf-8"></script>
    
    
    <![endif]-->

    

    
    

</body>
</html>
    """
    news = deal_with(data)
    write_nums(news)
    pass

if __name__ == '__main__':
    main()








