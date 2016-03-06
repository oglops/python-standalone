pyinstaller 版本
===================

lz由于不能确定x64的python 2.7.11会不会比原作者的module列表要来得多，所以按照作者的方法用help('modules')和help('modules .')得到了所有modules的列表，贴进了py.py里,在去掉明显不需要的一些以后还是[多好多](https://www.diffchecker.com/1b8bymmo)

此外，启动时间比原作者慢很多，可能是由于pyinstaller启动解压过慢(你换成--onedir mode就会秒开)，lz试着去掉更多module，改善不明显，可以试试就用原作者的比较少的module列表，但是lz这里用的是pypiwin32和原作者用的pywin32似乎有点不同，所以lz没有继续试

现在的moudules列表出来的py.exe约14mb,比原作者的9mb大很多，所以如果有不需要的module可以继续去掉以减小体积

Usage
------------------
  pyinstaller --onefile  py.py

  # 上面的命令会生成py.spec 如果需要进一步自定义，可以修改他之后
  pyinstaller --onefile  py.spec
