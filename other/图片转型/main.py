import os
import re



if __name__ == '__main__':
    root = r'D:\desktop_new____________________________________________\python脚本\python-crawler-practice\other' \
           r'\图片转型\2023届专业毕业生获得技能证书一览表（终审）'
    for i in os.listdir(root):
        if os.path.isdir(root + '/' + i):
            for j in os.listdir(root + '/' + i):
                print(j)
                file_name_ = os.path.join(root, i, j)
                if os.path.splitext(root + '/' + i + '/' + j)[1] == '.png':
                    if not os.path.splitext(root + '/' + i + '/' + j)[0] + '.jpg' in os.listdir(root + '/' + i):
                        file_name_ = os.path.join(root, i, os.path.splitext(root + '/' + i + '/' + j)[0] + '.jpg')
                        os.rename(os.path.join(root, i, j),
                                  os.path.join(root, i, os.path.splitext(root + '/' + i + '/' + j)[0] + '.jpg'))
                # print(re.findall(r'^(?P<link>\d{10}.*?)[信息|web|技术|界面]',
                #               file_name[0]),file_name[0])
                milt = r'^(?P<link>\d{10}.+?)(信息|软件|软考|嘻嘻|微信|，|-|web|Web|中级|系统|\+|广告|工业|移动|web|技术|技能|界面|5G|\d|广东省|计算机|第|ncda|初级|网络|程序员|蓝桥)'
                if re.findall(milt,
                              j):
                    print(re.search(milt, j).group('link'))
                    file_name = re.search(milt, j).group('link')
                    os.rename(file_name_,
                              os.path.join(root, i, file_name + os.path.splitext(root + '/' + i + '/' + j)[1]))
                    file_name_ = os.path.join(root, i, file_name + os.path.splitext(root + '/' + i + '/' + j)[1])
                # print(file_name_)


# def pdf_to_jpg(pdf_path):
#     jpg_path = pdf_path[:-3] + 'jpg'
#     os.system(f'convert -density 150 {pdf_path} -quality 90 {jpg_path}')
#
#
# pdf_folder = '/path/to/pdf/folder/'
# for pdf_file in os.listdir(pdf_folder):
#     if pdf_file.endswith('.pdf'):
#         pdf_path = os.path.join(pdf_folder, pdf_file)
#         pdf_to_jpg(pdf_path)
# def pdf_to_jpg(pdf_path, jpg_save_path, one_page=False):
#     """
#         将PDF文件转换为JPG图片
#     :param pdf_path: PDF文件路径
#     :param jpg_save_path: JPG图片保存路径， 若one_page为False，输入一个文件夹路径保存所有JPG图片
#     :param one_page: True：返回 PDF首页的JPG；False：返回 PDF所有页的JPG
#     :return:
#     """
#     pages = convert_from_path(pdf_path, 200)  # 若pdf有多页，则返回一个列表
#     if one_page:
#         pages[0].save(jpg_save_path, 'JPEG')
#     else:
#         if not os.path.exists(jpg_save_path):
#             os.mkdir(jpg_save_path)     # 创建文件夹
#         for i, page in enumerate(pages):
#             page.save(jpg_save_path + str(i+1) + '.jpg', 'JPEG')
#
#
# if __name__ == "__main__":
#     pdf_path = "../data/pdfdemo.pdf"
#
#     # 保存第一张图片
#     jpg_save_path = "../data/pdfimg.jpg"
#     one_page = True
#     pdf_to_jpg(pdf_path, jpg_save_path, one_page)
#
#     # 将每页图片都保存
#     # jpg_save_path = "../data/pdfimg/"
#     # one_page = False
#     # pdf_to_jpg(pdf_path, jpg_save_path, one_page)
