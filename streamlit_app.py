from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st

"""
# Welcome to ZeroGPT.CC
# How Does the AI ZeroGPT.cc Work?
Our AI content detector, ZeroGPT.cc, uses massive amounts of data from different sources to precisely predict the origin of a text or a phrase. It has been tested and trained to use combinations of machine learning algorithms alongside natural language processing techniques to present the most accurate results. These algorithms are designed and developed by the expert and professional team of ZeroGPT. The accuracy of these algorithms is backed by several in-house experiments and published highly reputable papers.

Our AI text detector works effectively for all versions of GPT models, including GPT-4. You can easily detect whether your text is human-written or AI/GPT Generated. Our AI text detector accurately displays the percentage of AI/GPT plagiarized text for an in-depth analysis of your content.

Check out website for more details: https://zerogpt.cc

"""


with st.echo(code_location='below'):
    total_points = st.slider("Number of points in spiral", 1, 5000, 2000)
    num_turns = st.slider("Number of turns in spiral", 1, 100, 9)

    Point = namedtuple('Point', 'x y')
    data = []

    points_per_turn = total_points / num_turns

    for curr_point_num in range(total_points):
        curr_turn, i = divmod(curr_point_num, points_per_turn)
        angle = (curr_turn + 1) * 2 * math.pi * i / points_per_turn
        radius = curr_point_num / total_points
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        data.append(Point(x, y))

    st.altair_chart(alt.Chart(pd.DataFrame(data), height=500, width=500)
        .mark_circle(color='#0068c9', opacity=0.5)
        .encode(x='x:Q', y='y:Q'))
