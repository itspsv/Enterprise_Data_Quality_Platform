import os

import matplotlib.pyplot as plt
import polars as pl
import streamlit as st

st.set_page_config(
    page_title="Enterprise Data Reliability Platform",
    layout="wide",
)

st.title("Enterprise Data Reliability Platform")

st.divider()

metadata_file = "metadata/pipeline_runs.parquet"

if not os.path.exists(metadata_file):
    st.warning("No pipeline metadata found.")
    st.stop()

df = pl.read_parquet(metadata_file)

latest = df.tail(1)

quality = latest["quality_score"][0]
total = latest["total_rows"][0]
valid = latest["valid_rows"][0]
invalid = latest["invalid_rows"][0]

col1, col2, col3, col4 = st.columns(4)

col1.metric("Quality Score", f"{quality:.2f}%")
col2.metric("Total Rows", total)
col3.metric("Valid Rows", valid)
col4.metric("Invalid Rows", invalid)

st.divider()

left, right = st.columns(2)

with left:

    st.subheader("Quality Score Trend")

    fig = plt.figure(figsize=(6, 3))

    plt.plot(
        df["quality_score"].to_list(),
        marker="o",
    )

    plt.xlabel("Pipeline Run")
    plt.ylabel("Quality Score (%)")
    plt.grid(True)

    st.pyplot(fig)

with right:

    st.subheader("Execution Time")

    fig = plt.figure(figsize=(6, 3))

    plt.plot(
        df["execution_time_seconds"].to_list(),
        marker="o",
    )

    plt.xlabel("Pipeline Run")
    plt.ylabel("Seconds")
    plt.grid(True)

    st.pyplot(fig)

st.divider()

st.subheader("Latest Rule Failures")

rule_failures = latest["rule_failures"][0]

rule_names = list(rule_failures.keys())
rule_counts = list(rule_failures.values())

fig = plt.figure(figsize=(8, 4))

plt.bar(rule_names, rule_counts)

plt.xlabel("Validation Rule")
plt.ylabel("Failed Records")

plt.xticks(rotation=20)

st.pyplot(fig)

st.divider()

st.subheader("Pipeline History")

st.dataframe(
    df.to_pandas(),
    use_container_width=True,
)