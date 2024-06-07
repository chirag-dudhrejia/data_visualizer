import streamlit as st
from plotly import express as px
from data_processing import Process_data


def print_dataframe():
    st.text("Hover over Top right corner of dataframe and click on Fullscreen to open whole dataset.")
    st.text("Click on any column name to sort data.")
    st.dataframe(data_obj.get_df(), height=400)


def plot_bar_graph(x_label, y_label, barmode):
    res_data = data_obj.get_bar_data()
    col1 = st.container(border=True)
    col1.plotly_chart(px.bar(res_data, x=res_data[x_label], y=res_data[y_label], barmode=barmode))


def plot_scatter_graph(x_label, y_label, color_col):
    res_data = data_obj.get_bar_data()
    col1 = st.container(border=True)
    col1.plotly_chart(px.scatter(res_data, x=res_data[x_label], y=res_data[y_label], color=color_col))


def plot_hist_graph(x_label, color_col):
    res_data = data_obj.get_bar_data()
    col1 = st.container(border=True)
    col1.plotly_chart(px.histogram(res_data, x=res_data[x_label], color=color_col))


st.set_page_config(page_title="Data Visualizer", page_icon=":bar_chart:", layout="wide")
st.title(":bar_chart: Data Visualizer")

# st.sidebar.subheader("Upload CSV file")
file = st.sidebar.file_uploader("Upload CSV file", type="csv")

if file:
    data_obj = Process_data(file)
    chosen_graph = st.sidebar.selectbox(label="Choose Task", options=["Dataframe", "Histogram", "Bar graph", "Scatter", "Line chart"])

    if chosen_graph == "Dataframe":
        print_dataframe()

    elif chosen_graph == "Histogram":
        columns = data_obj.get_columns()
        x_label = st.sidebar.selectbox("Select X-axis (Numeric column only)", options=columns)
        columns.insert(0, None)
        color_col = st.sidebar.selectbox("Color differentiation based on column:", options=columns)
        btn_clicked = st.sidebar.button("Generate Graph")

        if btn_clicked:
            plot_hist_graph(x_label, color_col)

    elif chosen_graph == "Bar graph":
        columns = data_obj.get_columns()
        x_label = st.sidebar.selectbox("Select X-axis (Categorical column Preferred)", options=columns)
        columns.remove(x_label)
        y_label = st.sidebar.selectbox("Select Y-axis (Numeric Column Preferred)", options=columns)
        barmode = st.sidebar.selectbox("Bar Type:", options=["overlay", "group", "relative"])
        btn_clicked = st.sidebar.button("Generate Graph")

        if btn_clicked:
            plot_bar_graph(x_label, y_label, barmode)

    elif chosen_graph == "Scatter":
        columns = data_obj.get_columns()
        x_label = st.sidebar.selectbox("Select X-axis (Numeric column only)", options=columns)
        columns.remove(x_label)
        y_label = st.sidebar.selectbox("Select Y-axis (Numeric Column only)", options=columns)
        color_options = data_obj.get_columns()
        color_options.insert(0, None)
        color_col = st.sidebar.selectbox("Color differentiation based on column:", options=color_options)
        btn_clicked = st.sidebar.button("Generate Graph")

        if btn_clicked:
            plot_scatter_graph(x_label, y_label, color_col)

    elif chosen_graph == "Line chart":
        pass
