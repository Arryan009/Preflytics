import collections

import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st
from sklearn.neighbors import KNeighborsClassifier

# Function to collect user preferences
def get_preferences(user):
    st.write(f"Hello {user}, please choose your preference among the following options:")
    preference = st.selectbox(f"Select {user}'s preference:", ['Sports', 'Technology', 'Art'])
    weight = st.slider(f"Rate how strongly {user} prefers {preference} (1 = Low, 5 = High):", 1, 5, step=1)
    return preference, weight

# Function to update user preferences using Streamlit
def update_preferences(preferences):
    st.write("### Update Preferences")
    if st.button('Update preferences'):
        selected_user = st.selectbox("Select a user to update their preference:", list(preferences.keys()))
        if selected_user:
            new_preference, new_weight = get_preferences(selected_user)
            preferences[selected_user] = (new_preference, new_weight)
            st.success(f"{selected_user}'s preference has been updated to {new_preference} with a weight of {new_weight}.")

# Function to visualize preferences
def visualize_preferences(aggregated_preferences):
    st.write("### Preference Distribution")
    prefs, weights = zip(*aggregated_preferences.items())
    fig, ax = plt.subplots()
    ax.bar(prefs, weights, color=['#FF6F61', '#6B5B95', '#88B04B'])
    ax.set_xlabel("Preferences")
    ax.set_ylabel("Total Weight")
    st.pyplot(fig)

# Function to export data as CSV
def export_data(preferences):
    df = pd.DataFrame(preferences.items(), columns=['Preference', 'Weight'])
    st.write(df)
    csv = df.to_csv(index=False)
    st.download_button("Download data as CSV", data=csv, file_name="preferences.csv", mime='text/csv')

# User profiles and history (temporary for now)
def user_profiles(preferences, history):
    st.write("### User Profiles and Preference History")
    for user, (pref, weight) in preferences.items():
        st.write(f"{user}'s current preference: {pref} ({weight})")
        if user in history:
            st.write(f"Previous preferences: {history[user]}")
        st.write("---")

# Function to suggest strategy based on preference distribution
def suggest_strategy(preferences):
    st.write("\n## Strategy Suggestion:")
    top_preference, top_weight = preferences[0]
    if top_weight > sum(weight for _, weight in preferences) * 0.5:
        st.write(f"**Focus heavily on {top_preference}, as it dominates the audience preference.**")
    else:
        st.write(f"**Consider a balanced approach between {preferences[0][0]} and {preferences[1][0]}.**")

# Machine learning prediction using KNN
def predict_preference(preferences, new_user_data):
    # Convert preferences into a training dataset
    pref_mapping = {'Sports': 0, 'Technology': 1, 'Art': 2}
    X_train = []
    y_train = []

    for user, (preference, weight) in preferences.items():
        X_train.append([weight])  # We use weight as a feature
        y_train.append(pref_mapping[preference])  # Map preferences to integers

    # Train the KNN model
    knn = KNeighborsClassifier(n_neighbors=3)
    knn.fit(X_train, y_train)

    # Predict the preference for the new user based on their weight
    predicted_pref = knn.predict([new_user_data])
    inv_pref_mapping = {0: 'Sports', 1: 'Technology', 2: 'Art'}

    return inv_pref_mapping[predicted_pref[0]]

# Core audience analytics function
def audience_analytics(usernames, history):
    # st.write("# Preflytics")
    preferences = {}

    # Collect preferences
    for user in usernames:
        preference, weight = get_preferences(user)
        preferences[user] = (preference, weight)

    update_preferences(preferences)

    # Aggregate preferences
    aggregated_preferences = collections.defaultdict(int)
    for pref, weight in preferences.values():
        aggregated_preferences[pref] += weight

    # Visualize preferences
    visualize_preferences(aggregated_preferences)

    # Analyze and sort the preferences
    sorted_preferences = sorted(aggregated_preferences.items(), key=lambda x: x[1], reverse=True)

    # Display the analysis
    st.write("## Final Preference Analysis:")
    for pref, weight in sorted_preferences:
        st.write(f"{pref}: {weight} points")

    most_common_preference = sorted_preferences[0][0]
    st.write(f"\n**The majority of the audience prefers {most_common_preference}.**")

    # Confidence score calculation
    total_points = sum(aggregated_preferences.values())
    confidence_score = (sorted_preferences[0][1] / total_points) * 100
    st.write(f"**Prediction Confidence:** {confidence_score:.2f}%")

    # Suggest strategy based on analysis
    suggest_strategy(sorted_preferences)

    # Predict a new user's preference
    # st.write("### Predict New User's Preference")
    # new_user_weight = st.slider("Enter new user's preference weight (1-5):", 1, 5, step=1)
    # predicted_preference = predict_preference(preferences, [new_user_weight])
    # st.write(f"**Predicted Preference for the new user: {predicted_preference}**")

    # Export data as CSV
    export_data(aggregated_preferences)

    # Show user profiles and history
    user_profiles(preferences, history)

# Main function to start the app
def main():
    st.title("Welcome to Preflytics")

    # Get the number of users
    num_users = st.number_input("Enter the number of users:", min_value=1, step=1)

    usernames = []
    for i in range(num_users):
        username = st.text_input(f"Enter the name of user {i + 1}:")
        if username:
            usernames.append(username)
    # Temporary history dictionary for preference changes
    history = {}

    if usernames:
        # Run audience analytics
        audience_analytics(usernames, history)

if __name__ == "__main__":
    main()