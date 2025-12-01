from flask import Flask, send_from_directory
import os

app = Flask(__name__)

# 设置报告所在目录
REPORT_FOLDER = r"D:\report_web\static\reports"
app.config['REPORT_FOLDER'] = REPORT_FOLDER

@app.route('/')
def index():
    return '''
    <html>
        <head>
            <title>报告页面</title>
            <style>
                body {
                    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                    background-color: #f4f4f4;
                    color: #333;
                    margin: 0;
                    padding: 0;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    box-sizing: border-box;
                }
                .container {
                    text-align: center;
                    background-color: #fff;
                    padding: 40px;
                    border-radius: 8px;
                    box-shadow: 0 4px 16px rgba(0, 0, 0, 0.1);
                    max-width: 600px;
                    width: 100%;
                }
                h1 {
                    font-size: 32px;
                    color: #2c3e50;
                    margin-bottom: 20px;
                    font-weight: 600;
                }
                p {
                    font-size: 18px;
                    color: #7f8c8d;
                    margin-bottom: 30px;
                }
                a {
                    display: inline-block;
                    padding: 14px 35px;
                    font-size: 18px;
                    color: #fff;
                    background-color: #3498db;
                    text-decoration: none;
                    border-radius: 30px;
                    transition: background-color 0.3s, transform 0.2s ease-in-out;
                }
                a:hover {
                    background-color: #2980b9;
                    transform: translateY(-3px);
                }
                footer {
                    margin-top: 30px;
                    font-size: 14px;
                    color: #bdc3c7;
                }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>我的报告页面</h1>
                <p>欢迎访问，您可以下载以下报告：</p>
                <p><a href="/download/网易云音乐产品运营策略分析报告.docx">下载网易云音乐产品运营策略分析报告</a></p>
                <p><a href="/download/哔哩哔哩大会员产品分析报告.docx">下载哔哩哔哩大会员产品分析报告</a></p>
                <footer>
                    <p>&copy; 2025 我的报告页面 | 版权所有</p>
                </footer>
            </div>
        </body>
    </html>
    '''

# 设置报告下载路由
@app.route('/download/<filename>')
def download_file(filename):
    return send_from_directory(app.config['REPORT_FOLDER'], filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
