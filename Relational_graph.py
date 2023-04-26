# File: Relational_graph.py
# Date: 2022/8/31 19:42
# Author: HJL
# IDE:  PyCharm
import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Graph

nodes_data = pd.read_excel(r'G:\Grad files\Project2\Graph\node.xlsx', sheet_name="Sheet1")
links_data = pd.read_excel(r'G:\Grad files\Project2\Graph\link.xlsx', sheet_name="Sheet1")
categories_data = pd.read_excel(r'G:\Grad files\Project2\Graph\category.xlsx', sheet_name="Sheet1")

print(f"nodes_df:\n{nodes_data}")
print(f"links_df:\n{links_data}")
print(f"categories_df:\n{categories_data}")

# Prep data: 将nodes,links,categories转化为json格式，列表嵌套字典[{},{},{}]
# Build nodes
nodes = []
for index, row in nodes_data.iterrows():
    row = row.to_dict()
    nodes.append(row)
print(nodes)

# Build links
links = []
for index, row in links_data.iterrows():
    row = row.to_dict()
    links.append(row)
print(f"links_list\n{links}")

# Build categories
categories = []
for index, row in categories_data.iterrows():
    row = row.to_dict()
    categories.append(row)
print(f"categories_list\n{categories}")

g = (
    Graph(init_opts=opts.InitOpts(width="1100px", height="1200px", bg_color="#fff"))
    .add(
        "",
        nodes,
        links,
        categories,
        repulsion=50,
        layout="circular",  # 'none' 普通，'force' 力导向，'circular' 环形
        is_rotate_label=True,  # 'circular' 旋转标签
        linestyle_opts=opts.LineStyleOpts(color="source", curve=0.2),  # mildly curvy = 0.2
        label_opts=opts.LabelOpts(is_show=True, font_size=18),

    )
    .set_global_opts(
        legend_opts=opts.LegendOpts(is_show=True, orient="vertical", pos_left="2%", pos_top="20%"),
        # title_opts=opts.TitleOpts(title="Keyword_Collocations"),

    )
    .set_series_opts(
        tooltip_opts=opts.TooltipOpts(is_always_show_content=True)
    )
    .render("keyword-collocations.html")
)
# g.render_notebook()
