import streamlit as st

from apputil import *

# Load Titanic dataset
df = pd.read_csv('https://raw.githubusercontent.com/leontoddjohnson/datasets/main/data/titanic.csv')

st.write(
'''
# Titanic Visualization 1

'''
"Did women in first class have a higher survival rate than men in other classes?"
)
# Generate and display the figure
summary_df = survival_demographics(df)
fig1 = visualize_demographic(summary_df)
st.plotly_chart(fig1, use_container_width=True)

st.write(
'''
# Titanic Visualization 2
'''
)
# Generate and display the figure
fig2 = visualize_families()
st.plotly_chart(fig2, use_container_width=True)

st.write(
'''
# Titanic Visualization Bonus
'''
)
# Generate and display the figure
fig3 = visualize_family_size()
st.plotly_chart(fig3, use_container_width=True)