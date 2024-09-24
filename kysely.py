import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

pd.set_option('future.no_silent_downcasting', True)

filepath = 'C:/Users/t09jraja/Downloads/12.8. VST Demo Session XR Feedback_Perusraportti.xlsx'

df = pd.read_excel(filepath)

update_df = df.drop(columns=['Language']).drop([0,24,25,26,27,28])

question_1_answers = update_df['1. Question']
question_1_answers_corrected = update_df['1. Question Corrected']
question_2_answers = update_df['2. Question']
question_3_answers = update_df['3. How well do you agree with the following statements regarding system usability?']

# Function to display both the count and the percentage
def func(pct, allvals):
    absolute = int(round(pct/100.*sum(allvals)))  # Calculate the absolute count
    return f"{absolute} ({pct:.1f}%)"  # Format the label as 'count (percentage)'

def pieplot(answer_set, label_set, plt_title):
    value_counts = answer_set.value_counts()
    # Plot the pie chart
    value_counts.plot.pie(
        autopct=lambda pct: func(pct, value_counts),  # Custom autopct to show counts and percentages
        startangle=90,      # Rotate so that the first slice starts at the top
        shadow=True,        # Add a shadow effect for better visibility
        colors= ['lightblue', 'lightcoral', 'lightgreen', 'red', 'green'],  # Optional: Add colors
        labels=label_set  # Add custom labels
    )

    plt.ylabel('')  # Remove y-label for better appearance
    plt.title(plt_title)  # Add a title
    plt.show()
    

pieplot(question_1_answers, ['Researcher', 'Other', 'Shipbuilding Professional'], 'Initial Respondent Professions (unfiltered)')
pieplot(question_1_answers_corrected, ['Researcher', 'Shipbuilding Professional', 'Other'], 'Respondent Professions Filtered')
pieplot(question_2_answers, ['Not very familiar', 'Somewhat familiar', 'I have no prior experience', 'Very familiar'], 'Respondent Familiarity w/ XR')

