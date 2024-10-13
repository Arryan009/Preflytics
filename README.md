# Preflytics

Preflytics is an interactive web app built with Streamlit, allowing users to collect, analyze, and visualize audience preferences for various categories such as Sports, Technology, and Art. This tool is designed to help predict audience preferences and provide strategic insights based on the distribution of these preferences. The app also leverages machine learning to predict preferences for new users.

Key Features
Collect User Preferences: The app allows users to input their preferences for categories like Sports, Technology, or Art, along with a weight representing how strongly they favor that preference.
Update Preferences: Users can update their previously provided preferences.
Visualize Preferences: The app generates a bar chart to visualize the aggregated preferences and their corresponding weights.
Export Preferences to CSV: Users can export the preference data into a CSV file for further analysis.
User Profiles & History: The app displays current and historical preferences for each user.
Preference Prediction Using Machine Learning: Using the K-Nearest Neighbors (KNN) algorithm, the app predicts a new user's preference based on their weighted input.
Strategy Suggestion: The app suggests strategies based on the most dominant preference category among the audience.
Code Explanation
1. Importing Libraries
The app uses several external libraries for different purposes:

collections: Used for creating a default dictionary to aggregate user preferences.
matplotlib.pyplot: For plotting graphs.
pandas: Used to convert preference data into a DataFrame and export it as a CSV file.
streamlit: The core library for building the web app interface.
sklearn.neighbors.KNeighborsClassifier: For implementing K-Nearest Neighbors (KNN) machine learning to predict new user preferences.
2. Core Functions
a. get_preferences(user)
This function prompts the user to input their preference and assign a weight to it. It uses Streamlit’s selectbox and slider components to capture the input.

Parameters: user – The name of the user providing their preference.
Returns: A tuple containing the selected preference and its weight.
b. update_preferences(preferences)
This function allows users to update their existing preferences. It lists all users whose preferences can be updated and allows changes to be made.

Parameters: preferences – A dictionary containing user preferences.
Returns: None; updates the preferences dictionary in place.
c. visualize_preferences(aggregated_preferences)
This function generates a bar chart to visualize the distribution of aggregated preferences using matplotlib.

Parameters: aggregated_preferences – A dictionary containing the aggregated preference data.
Returns: None; displays the chart on the Streamlit app.
d. export_data(preferences)
This function converts the user preference data into a Pandas DataFrame and provides a CSV download option through Streamlit.

Parameters: preferences – A dictionary containing user preferences.
Returns: None; allows users to download the preference data as a CSV file.
e. user_profiles(preferences, history)
Displays each user's current preferences and their historical preferences (if any). This helps track changes in user preferences over time.

Parameters:
preferences – A dictionary containing user preferences.
history – A dictionary that stores historical preference data for each user.
Returns: None; displays user profiles and preference history in the Streamlit interface.
f. suggest_strategy(preferences)
Provides strategic suggestions based on the most dominant preferences among users. If one preference strongly outweighs others, it recommends focusing on that; otherwise, it suggests a balanced approach.

Parameters: preferences – A sorted list of aggregated preferences and their weights.
Returns: None; displays strategy recommendations.
g. predict_preference(preferences, new_user_data)
Uses a KNN machine learning model to predict a new user's preference based on their weight. The function maps categorical preferences (Sports, Technology, Art) to numerical values for model training and prediction.

Parameters:
preferences – A dictionary of existing user preferences.
new_user_data – Weight data for the new user.
Returns: The predicted preference for the new user.
3. Audience Analytics Workflow
a. audience_analytics(usernames, history)
This is the main function that orchestrates the audience analytics process. It first collects user preferences, updates them, visualizes the preference distribution, and provides strategy recommendations. It also predicts new user preferences and allows for data export.

Steps:
Collects user preferences using get_preferences().
Updates preferences using update_preferences().
Aggregates preferences into a dictionary.
Visualizes the aggregated data using visualize_preferences().
Displays the analysis and most common preference.
Suggests a strategy based on the analysis using suggest_strategy().
Exports preference data to CSV using export_data().
Displays user profiles and historical preferences using user_profiles().
b. main()
This function starts the app. It captures the number of users and their names, and then runs the audience analytics workflow.

Steps:
Captures the number of users and their names.
Calls audience_analytics() with the collected usernames and a history dictionary.

Run the app:-
streamlit run main.py

This will launch the app in your web browser.

Future Enhancements
User Authentication: Adding login functionality for users to save preferences over sessions.
Advanced Visualization: More detailed charts such as pie charts or stacked bar graphs.
Prediction Improvements: Use more features (e.g., demographics) to improve preference prediction.
Real-Time Data Storage: Store user preferences in a database instead of memory for better persistence.
