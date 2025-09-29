import plotly.express as px
import pandas as pd

# update/add code below ...

def survival_demographics(df):
    # 1. Create a new column in the Titanic dataset that classifies passengers into age categories
    age_bins = [0, 12, 19, 59, float('inf')]
    age_catagory = ['Child', 'Teen', 'Adult', 'Senior']
    df['age_group'] = pd.cut(df['Age'], bins=age_bins, labels=age_catagory, right=True)
    df['age_group'] = df['age_group'].astype('category')

    # 2. Group the passengers by class, sex, and age group
    grouped = df.groupby(['Pclass', 'Sex', 'age_group'], observed=True)

    # 3. For each group, calculate n_passengers,n_survivors, and survival_rate
    #4. Return a table that includes the results for all combinations of class, sex, and age group.
    data_summary = grouped.agg(
        n_passengers=('PassengerId', 'count'),
        n_survivors=('Survived', 'sum')
    ).reset_index()

    data_summary['survival_rate'] = data_summary['n_survivors'] / data_summary['n_passengers']

    # 5. Order the results so they are easy to interpret
    data_summary = data_summary.sort_values(by=['Pclass', 'Sex', 'age_group'])

    return data_summary


def visualize_demographic(summary_df):
    # Filter to highlight adult women in first class
    highlight = (
        (summary_df['Pclass'] == 1) &
        (summary_df['Sex'] == 'female') &
        (summary_df['age_group'] == 'Adult')
    )

    # Add a highlight column for color emphasis
    summary_df['highlight'] = highlight.map({True: 'Highlighted', False: 'Other'})

    # Create bar chart
    fig = px.bar(
        summary_df,
        x='survival_rate',
        y='age_group',
        color='highlight',
        facet_row='Sex',
        facet_col='Pclass',
        orientation='h',
        title='Survival Rate by Class, Sex, and Age Group',
        labels={'survival_rate': 'Survival Rate', 'age_group': 'Age Group'},
        color_discrete_map={'Highlighted': 'crimson', 'Other': 'lightgray'}
    )

    fig.update_layout(showlegend=False)
    return fig

