import requests
import os
import base64


def create_task(url, file_path, file_url):
    """
    Args:
        url: string, 服务请求链接
        file_path: 本地文件路径
        file_url: 文件链接
    Returns: 响应
    """
    # 文件请求
    with open(file_path, "rb") as f:
        file_data = base64.b64encode(f.read())
    data = {
        "file_data": file_data,
        "file_url": file_url,
        "file_name": os.path.basename(file_path)
    }
    
    # 文档切分参数，非必传
    # return_doc_chunks = json.dumps({"switch": True, "chunk_size": -1})
    # data["return_doc_chunks"] = return_doc_chunks
    
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}

    response = requests.post(url, headers=headers, data=data)
    return response

def query_task(url, task_id):
    """
    Args:
        url: string, 请求链接
        task_id: string, task id
    Returns: 响应
    """
    data = {
        "task_id": task_id
    }
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    response = requests.post(url, headers=headers, data=data)
    return response




if __name__ == '__main__':
    request_host = "https://aip.baidubce.com/rest/2.0/brain/online/v2/parser/task?" \
                   "access_token=Bearer bce-v3/ALTAK-PpSxPERxwO3FSb9mZlj5O/a652e38c73199648164d5cfbcc126c6470e02948"
    file_path = "./test.pdf"
    response = create_task(request_host, file_path, "")
    print(response.json())