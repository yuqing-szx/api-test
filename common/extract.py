#对request.py中的变量提取进行封装
import jsonpath
def extract(resp,attr_name,exp):
    try:
        resp.json = resp.json()
    except Exception:
        resp.json = {}

    attr = getattr(resp,attr_name)#指定提取位置
    res=jsonpath.jsonpath(attr,exp)

    return res[0]