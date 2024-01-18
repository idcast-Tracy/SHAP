# ----------- Python streamlit可视化Web ----------
# pip install -i https://pypi.tuna.tsinghua.edu.cn/simple streamlit
# 打开网页，在cmd命令界面运行下面一段
# streamlit run C:\Users\Tracy\Desktop\2024寒假\科研\01.18Python-streamlit\app.py [ARGUMENTS]
# 打开网页，在cmd命令界面运行下面一段{有皮肤}  【purple、light、dark、serif】
# streamlit run --theme.base light C:\Users\Tracy\Desktop\2024寒假\科研\01.18Python-streamlit\app.py [ARGUMENTS]
# 部署Web网页，运行下面一段
# streamlit deploy C:\Users\Tracy\Desktop\2024寒假\科研\01.18Python-streamlit\app.py [ARGUMENTS]
# -----------  加载包 ---------- #
import streamlit as st
# from streamlit_option_menu import option_menu
from PIL import Image
import pandas as pd
# import matplotlib.pyplot as plt
# import plotly.express as px
import numpy as np
import os
# os.chdir(r'C:\Users\Tracy\Desktop\2024寒假\科研\01.18Python-streamlit') # 设定文件路径



# 多页面应用程序
def main():
    # st.set_page_config(page_title="知秋的网站", page_icon="⭐", layout="wide") # 网页的名称和图标
    st.set_page_config(
        page_title="七里香还是稻香",  # 页面标题
        page_icon=":rainbow:",  # icon
        layout="wide",  # 页面布局
        initial_sidebar_state="auto"  # 侧边栏
    )
    st.title("多页面应用程序示例")
    page = st.sidebar.selectbox("选择一个页面", ["主页", "关于我们"])
    if page == "主页":
        # 设置页面 配置
        st.write("欢迎来到主页！")
        ## ========================= 基本元素与布局 ========================== ##
        # 文本与布局
        st.title("这是一个标题")
        st.header("这是一个头部")
        st.subheader("这是一个子标题")
        st.text("这是一段文本")
        # 图片与媒体
        # image = Image.open("任务分配.png")
        # st.image(image, caption="这是一张图片", use_column_width=True)
        # 表格
        data = pd.DataFrame({"列1": [1, 2, 3], "列2": [4, 5, 6]})
        st.dataframe(data)

        ## ========================== 交互组件 ========================== ##
        # 按钮与触发事件
        if st.button("点击我"):
            st.write("按钮被点击了！")
        # 输入框与表单
        name = st.text_input("请输入你的名字")
        st.write("你输入的名字是：", name)
        # 下拉框与选择器
        option = st.selectbox("选择一个选项", ["选项1", "选项2", "选项3"])
        st.write("你选择的是：", option)

        ## ========================== 数据可视化 ========================== ##
        # 绘图与图表
        x = np.linspace(0, 10, 100)
        y = np.sin(x)
        st.line_chart(list(zip(x, y)))
        # 与Matplotlib、Plotly等集成
        # Matplotlib
        # fig, ax = plt.subplots()
        # ax.plot(x, y)
        # st.pyplot(fig)
        # Plotly
        # fig = px.scatter(x=x, y=y, title="Scatter Plot")
        # st.plotly_chart(fig)

        ## ========================== 高级主题 ========================== ##
        # 自定义主题与样式
        # 创建一个自定义主题
        # custom_theme = {
        #     "primaryColor": "#ff6347",
        #     "backgroundColor": "#f0f0f0",
        #     "secondaryBackgroundColor": "#d3d3d3",
        #     "textColor": "#121212",
        #     "font": "sans serif"
        # }
        # st.set_page_config(page_title="Custom Theme Example", page_icon="🚀", layout="wide", initial_sidebar_state="collapsed")
        # st.set_theme(custom_theme)
        # 使用Markdown增强文本展示
        st.markdown("## 这是Markdown标题")
        st.markdown("这是 **加粗** 的文本")
    elif page == "关于我们":
        st.write("这是关于我们页面。")
        ## ========================== 构建数据仪表盘 ========================== ##
        # 生成示例数据
        data = pd.DataFrame({
            '日期': pd.date_range('2023-01-01', periods=10, freq='D'),
            '销售额': np.random.randint(100, 1000, size=10)
        })
        # 创建仪表盘
        st.title("销售数据仪表盘")
        st.line_chart(data.set_index('日期'))
        # ## ========================== 创建一个交互式数据分析工具 ========================== ##
        # # 导入数据集
        # data = pd.read_csv('一阶特征.csv')
        # # 选择变量
        # selected_variable = st.selectbox("选择一个变量", data.columns)
        # # 绘制箱线图
        # st.title("箱线图 - {}".format(selected_variable))
        # st.box_plot(data[selected_variable])
if __name__ == "__main__":
    main()
