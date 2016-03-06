cx_freeze 版本
===================

由于cx_freeze[没有打包单个文件的功能](https://cx-freeze.readthedocs.org/en/latest/faq.html#single-file-executables),所以只能借助官方说明里举例的IExpress或者7-zip的sfx module,但是lz试过之后前者无法传递参数，后者会弹出一个新窗口

Usage
------------------
```bash
    python setup.py build
```
